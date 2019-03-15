def selection_sort(lst):
    for i in range(len(lst)):
        ind_min = i
        for j in range(i+1, len(lst)):
            if lst[j] < lst[ind_min]:
                ind_min = j
        lst[i], lst[ind_min] = lst[ind_min], lst[i]


if __name__ == '__main__':
    import myTest
    print(myTest.check(selection_sort))
