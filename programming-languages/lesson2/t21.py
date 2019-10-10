from threading import Thread, Condition
import random
import time
import signal


class MyCondition(Condition):
    useful_meta = None


class SimpleThread(Thread):
    def __init__(self, name, condition: MyCondition):
        Thread.__init__(self, name=name, target=self._target)
        self.condition = condition

    def run(self):
        try:
            self._target()
        finally:
            with self.condition:
                print(f'Thread {self.getName()} exit')
                self.condition.useful_meta = -1
                self.condition.notify_all()
                del self._target

    def _target(self):
        while True:
            with self.condition:
                while self.condition.useful_meta != self.getName():
                    if self.condition.useful_meta == -1:
                        return
                    self.condition.wait()
                print(f'Thread {self.getName()}')
                self.condition.useful_meta = None


class MainThread(Thread):
    def __init__(self, count: int, condition: MyCondition):
        Thread.__init__(self, target=self._target)
        self.condition = condition
        self.count = count

    def _target(self):
        while True:
            with self.condition:
                cur = 1 + random.randrange(self.count)
                self.condition.useful_meta = str(cur)
                self.condition.notify_all()
            time.sleep(2)

    def close(self):
        with self.condition:
            self.condition.useful_meta = -1
            self.condition.notify_all()
        time.sleep(2)


def main():
    n = int(input('Input count of threads: '))
    cond = MyCondition()

    main_thread = MainThread(count=n, condition=cond)
    threads = list()

    for name in map(str, range(1, n + 1)):
        threads.append(SimpleThread(name=name, condition=cond))
        threads[-1].daemon = True
        threads[-1].start()
    try:
        main_thread.run()
        signal.pause()
    except (KeyboardInterrupt, SystemExit):
        main_thread.close()


if __name__ == '__main__':
    main()
