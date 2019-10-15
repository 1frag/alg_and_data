import threading
from collections import namedtuple
from random import randrange
from time import sleep
import signal
# from queue import Queue  # my sample

Task = namedtuple('Task', ['group_no', 'priority'])
threads = []
creator = None


class StopThread(Exception):
    pass


class MyCondition(threading.Condition):
    _useful_meta = None
    fail = False

    @property
    def useful_meta(self):
        return self._useful_meta

    @useful_meta.getter
    def useful_meta(self):
        if self.fail:
            raise StopThread
        return self._useful_meta

    @useful_meta.setter
    def useful_meta(self, value):
        if self.fail:
            raise StopThread
        self._useful_meta = value

    def set_fail(self):
        self.fail = True


class CustomQueue:
    def __init__(self, maxsize, groups):
        self.group_no = None
        self.count = 0
        self.maxsize = maxsize
        self.collection = dict()

        self.e_empty = []

        self.changed_count = MyCondition()
        self.changed_count.useful_meta = True

        for _ in range(groups):
            evt = MyCondition()
            with evt:
                evt.useful_meta = True
            self.e_empty.append(evt)

    def get(self, group_no):
        # print(f'зашел в get {threading.current_thread().getName()}')
        with self.e_empty[group_no]:
            # print(f'до вайла {threading.current_thread().getName()}')
            while self.e_empty[group_no].useful_meta:
                # print(f'скоро будет wait у {threading.current_thread().getName()}')
                self.e_empty[group_no].wait()
                # print(f'вышел из ожидания {threading.current_thread().getName()}')
            # print(f'после вайла {threading.current_thread().getName()}')

            obj = self.unpack(group_no)
            return obj

    def deep_unpack(self, what_is_it):
        if isinstance(what_is_it, (list, tuple)):
            return len(what_is_it)
        if isinstance(what_is_it, dict):
            return sum(map(self.deep_unpack, what_is_it.values()))
        raise NotImplementedError

    def unpack(self, group_no):
        """ priority unpack and pick"""
        is_last = self.deep_unpack(self.collection[group_no]) == 1

        if is_last:
            self.e_empty[group_no].useful_meta = True
        self.count -= 1
        with self.changed_count:
            self.changed_count.notify_all()

        for _ in [3, 2, 1]:
            if self.collection[group_no][_]:
                return self.collection[group_no][_].pop()

        raise Exception(f'fatal fail group#{group_no}, {is_last}')

    def put(self, task: Task):
        with self.changed_count:
            while self.count == self.maxsize:
                self.changed_count.wait()

            self.collection.setdefault(task.group_no, {})
            self.collection[task.group_no].setdefault(1, [])
            self.collection[task.group_no].setdefault(2, [])
            self.collection[task.group_no].setdefault(3, [])
            self.collection[task.group_no][task.priority].append(task)
            self.count += 1

            with self.e_empty[task.group_no]:
                self.e_empty[task.group_no].useful_meta = False
                self.e_empty[task.group_no].notify_all()

    def join(self):
        """ Дождаться """
        print('come in join')
        for evt in self.e_empty:
            with evt:
                evt.set_fail()
                evt.notify_all()

        with self.changed_count:
            self.changed_count.set_fail()
            self.changed_count.notify_all()

        for thr in threads:
            thr.join()
        creator.join()


def worker(queue: CustomQueue, group_no, *, smtp):
    try:
        while True:
            print(f'Worker #{smtp} wait for tasks of GROUP#{group_no}')
            task = queue.get(group_no=group_no)
            print(f'Worker #{smtp} got {task}')
            sleep(randrange(9, 27))
            print(f'Worker #{smtp} done task successfully')

    except StopThread:
        return
    finally:
        print(f'Thread {smtp} complete')
        return


def generator(queue: CustomQueue):
    try:
        while True:
            task = Task(
                group_no=randrange(NUMBER_OF_GROUPS),
                priority=1 + randrange(3),
            )
            queue.put(task)
            print(f'generator created new task: {task}')
            print(f'queue: {queue.count}/{queue.maxsize} taken')
            sleep(randrange(1, 3))
            # sleep(5)

    except StopThread:
        return
    finally:
        print('generator complete his task')
        return


def io_actions():
    for group_no in range(NUMBER_OF_GROUPS):
        yield group_no, int(input(f'What count of workers in GROUP#{group_no}: '))


if __name__ == '__main__':
    NUMBER_OF_GROUPS = int(input('Input number of groups: '))
    q = CustomQueue(
        maxsize=int(input('Input ёmkost\': ')),
        groups=NUMBER_OF_GROUPS,
    )
    smtp = 1

    for gno, cnt in io_actions():
        data = {'target': worker, 'args': (q, gno,)}
        for _ in range(cnt):
            threads.append(threading.Thread(**data, kwargs={'smtp': smtp}))
            threads[-1].start()
            smtp += 1

    creator = threading.Thread(target=generator, args=(q,))
    try:
        creator.start()
        signal.pause()
    except (KeyboardInterrupt, SystemExit):
        q.join()
        print('\nBye!')
