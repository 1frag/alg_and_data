def merge_sort(lst):
    if len(lst) == 1:
        return lst
    elif len(lst) == 2:
        if lst[0] > lst[1]:
            lst[0], lst[1] = lst[1], lst[0]
        return lst
    left = merge_sort(lst[:len(lst)//2])
    right = merge_sort(lst[len(lst)//2:])
    i, j = 0, 0
    while len(left) > i and len(right) > j:
        if left[i] < right[j]:
            lst[i+j] = left[i]
            i += 1
        else:
            lst[i+j] = right[j]
            j += 1
    while len(left) > i:
        lst[i + j] = left[i]
        i += 1
    while len(right) > j:
        lst[i + j] = right[j]
        j += 1
    return lst


if __name__ == '__main__':
    import myTest
    print(myTest.check(merge_sort))
