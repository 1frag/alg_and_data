def say1():
    print('h_say1')


def say2():
    print('h_say2')


def say3():
    print('h_say3')


d = {x[0]: x for x in list(locals().items())}

for i in list(locals().items()):
    print(i[1])

print(say1.__class__)

print(d)
