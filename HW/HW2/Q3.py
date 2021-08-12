
def choose_rec(n, k):  # From recitation. This is a recursive function.
    if k == 0 or n == k:
        return 1
    return choose_rec(n-1, k) + choose_rec(n-1, k-1)


def pascal(n):
    return [choose_rec(n, i) for i in range(n+1)]


def test_pascal():
    assert pascal(0) == [1] and pascal(4) == [1, 4, 6, 4, 1]


test_pascal()
print(pascal(10))
