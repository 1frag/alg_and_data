def insert_sort(lst):
    for i in range(1, len(lst)):
        j = i
        while j > 0 and lst[j] < lst[j-1]:
            lst[j], lst[j-1] = lst[j-1], lst[j]
            j -= 1


if __name__ == '__main__':
    import myTest
    print(myTest.check(insert_sort))