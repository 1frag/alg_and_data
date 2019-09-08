def bubble_sort(lst):
    n = 1
    while n < len(lst):
        for i in range(len(lst) - n):
            if lst[i] < lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
        n += 1


if __name__ == '__main__':
    import myTest
    print(myTest.check(bubble_sort, True))
