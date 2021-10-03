
def merge_sort(lst):
    n = len(lst)
    if n == 1:
        return lst

    l1_sorted = merge_sort(lst[: n // 2])
    l2_sorted = merge_sort(lst[n // 2:])
    return merge(l1_sorted, l2_sorted)


def merge(l1, l2):
    lst = []
    i, j = 0, 0
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            lst.append(l1[i])
            i += 1
        else:
            lst.append(l2[j])
            j += 1
    if i >= len(l1):
        lst.extend(l2[j:])
    else:
        lst.extend(l1[i:])

    return lst

l1 = [1,2,3,5,10]
l2 = [1,10,8,1,5,6,7]

print(merge(l1, l2))
print(merge_sort(l2))
