
def pwr_set(lst):
    if len(lst) > 0:
        p = pwr_set(lst[1:])
        return p + [i + lst[:1] for i in p]
    return [[]]


def test_pwr_set():
    assert len(pwr_set([1,6,81,21,4])) == 2 ** 5 and len(pwr_set([1,3,5])) == 2 ** 3


tst_lst = [1, 2, 6]

test_pwr_set()
# print(pwr_set(tst_lst), len(pwr_set(tst_lst)), sep='\n')
print(pwr_set(tst_lst))
