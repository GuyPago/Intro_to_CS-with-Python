
def no_dup(lst):
    lst = lst[:]
    return list(set(lst))


def intersection(l1, l2):
    return list(set(l1) & set(l2))


def bubble_sort(lst):
    for i in range(len(lst)):
        for j in range(len(lst) - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst
                

def factorial(n):
    if n in (0, 1):
        return 1
    return n * factorial(n-1)


def fibonacci(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    
    return fibonacci(n-2) + fibonacci(n-1)


# print(no_dup([1,2,3,4,4,4,2,1]))
# print(intersection([1,2,3,4], [2,3,4,6,7,8]))
# print(bubble_sort([1,6,4,5,2,10,3]))
print(factorial(3))
print(fibonacci(12))
