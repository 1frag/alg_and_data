import asyncio
from timeit import timeit
from random import randint
from pprint import pprint


def get_array():
    constraint = (-2147483648, 2147483647)
    count = int(input('Input size of array: '))
    return [randint(*constraint) for _ in range(count)]


class Collector:
    response = None
    results = {
        'minimum': None,
        'maximum': None,
    }

    def callback(self, response: asyncio.Future):
        self.response = response.result()
        self.resolve('minimum')
        self.resolve('maximum')

    def resolve(self, name):
        if not self.results[name]:
            self.results[name] = self.response[name]
        if self.results[name][0] > self.response[name][0]:
            self.results[name] = self.response[name]


class Executor:
    loop = None
    collector = Collector()

    def __init__(self, array):
        self.array = array

    def search(self, tasks: int):
        self.loop = asyncio.get_event_loop()
        datas = [self.data(code, tasks) for code in range(tasks)]
        futures = []

        for future, params in datas:
            self.loop.create_task(self.task(future, *params))
            futures.append(future)

        self.loop.run_until_complete(asyncio.wait(futures))

    def callback(self, args):
        print([fut.result() for fut in args])

    def data(self, code, tasks):
        fut = self.loop.create_future()
        fut.add_done_callback(self.collector.callback)
        return fut, self.borders(code, tasks)

    def borders(self, code, tasks):
        size = len(self.array) // tasks
        return code * size, (
            (code + 1) * size,
            len(self.array),
        )[code + 1 == tasks]

    async def task(self, fut: asyncio.Future, left, right):
        setup = lambda pos: (self.array[pos], pos)
        minimum = maximum = setup(left)

        for num in range(left, right):
            if minimum[0] > self.array[num]:
                minimum = setup(num)
            if maximum[0] < self.array[num]:
                maximum = setup(num)

        return fut.set_result({
            'minimum': minimum,
            'maximum': maximum,
        })


if __name__ == '__main__':
    results = []
    exe = Executor(get_array())
    for times in [2, 4, 8, 16]:
        print(timeit(
            f'exe.search({times})',
            'from __main__ import exe',
            number=100,
        ), f'with {times} tasks')
        results.append(exe.collector.results)
    pprint(results)
