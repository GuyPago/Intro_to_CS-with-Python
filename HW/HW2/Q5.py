# The chosen function is the built-in "insert" list method.
import time
import random
import matplotlib.pyplot as plt


def insert_sort(lst):
    for i in range(1, len(lst)):
        if lst[i] < lst[i - 1]:
            j = i
            while lst[i] < lst[j-1] and j != 0:
                j -= 1
            lst.insert(j, lst.pop(i))


# nums = [49, 4, 1, 2, 23, 5, 86, 17, 7, 24, 10, 55]
# insert_sort(nums)
# print(nums)

def expir(t):
    data = []
    for i in range(t):
        lst = [random.randint(1, 1000) for i in range(random.randint(1, 30000))]
        stamp = time.time()
        insert_sort(lst)
        t = time.time() - stamp
        data.append((len(lst), t * 10))
    return data


# times = 300
# result = expir(times)
# print(result)
# x, y = zip(*result)
# print(sum(y) / 60)
#
# plt.scatter(x=x, y=y)
# plt.suptitle('Running time as a function of input size', fontsize=15)
# plt.title(f'{times} experiments')
# plt.xlabel('Input size (n)')
# plt.ylabel('Time (milli-sec)')
# plt.show()
