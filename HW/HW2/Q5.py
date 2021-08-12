# The chosen function is the built-in "insert" list method.

def insert_sort(lst):
    for i in range(1, len(lst)):
        if lst[i] < lst[i - 1]:
            j = i
            while lst[i] < lst[j - 1]:
                j -= 1
            lst.insert(j, lst.pop(i))


nums = [4, 2, 23, 5, 86, 17, 7, 24, 10, 55]
insert_sort(nums)
print(nums)