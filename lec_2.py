from random import random


# x = -3
#
# if x < 0:
#     x = abs(x)
# print(x ** 0.5)
#
# if int(x) != x:
#     x = int(x)
# print(x % 7)

# x = -5
# if x < 0:
#     print('You can not square root a negative value')
# elif x > 0:
#     print(x ** 0.5)
#
# x = 8
# if x % 6 == 0:
#     print('group by 6')
# if x % 3 == 0 and x % 2 != 0:
#     print('group by 3')
# x = 4324456666666666662
# if x % 6 == 0:
#     print('group by 6')
# elif x % 2 == 0:
#     print('group by 2')
# elif x % 3 == 0:
#     print('group by 3')
# else:
#     print('other')

# x = random()
# iter_num = 1
# while x > 0.2:
#     x = random()
#     iter_num += 1
#
# print(x, iter_num, 'iterations')

# x = 608560087
# print(len(str(x)))

# s = 1
# for i in range(6):
#     s *= (i+1)
# print(sum)

# for i in range(5):
#     if i == 3:
#         continue
#     print(i)
# s = 0
# for i in range(5, 51):
#     if i % 2 == 0:
#         s += i
# print(s)

# def is_prime(n):
#     for i in range(2, n):
#         if n % i == 0:
#             return

# def choose(n,k):
#     return fact(n) / (fact(k) * fact(n-k))

# def fibonacci(n):
#     n1, n2 = 0
#     for i in range(n):
#         print(n1)
#         tmp = n1 + n2
#         n2 = n1
#         n1 = tmp

# s = 'betanir'
# print(s.replace('b', 'n'))

def word_len(sentence):
    for i in range(len(sentence)):
        if sentence[i] == ' ':
            return len(sentence[:i])


print(word_len('be eer'))


