def hanoi(n, src, des, aux):
    if n == 1:
        print(f'Move disk {n} from {src} to {aux}')
    else:
        hanoi(n - 1, src=src, des=aux, aux=des)
        print(f'Move disk {n} from {src} to {des}')
        hanoi(n - 1, src=aux, des=des, aux=src)


x = 5


def ret():
    global x
    x += 5
    print(x)


# print(x)
# ret()
# print(x)


def intersect(l1, l2):
    return [i for i in l2 if i in l1]


# print(intersect([1,2,3,5,4,8], [4,2,7,8,6]))

def choose_rec(n, k):
    if k == 0 or n == k:
        return 1
    return choose_rec(n-1, k) + choose_rec(n-1, k-1)


print(choose_rec(52, 5))
