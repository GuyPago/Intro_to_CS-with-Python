def is_int_list(lst):
    for i in lst:
        if not isinstance(i, int):
            return False
    return True


def pure_int_list(lst):
    if is_int_list(lst):
        return max(lst)
    return None


def sym_diff(lst1, lst2):
    lst = []
    for i in lst1:
        if i not in lst2:
            lst.append(i)
    for j in lst2:
        if j not in lst1:
            lst.append(j)
    return lst


def dedup(lst1):
    lst = []
    for i in lst1:
        if i not in lst:
            lst.append(i)
    return lst


def intersect(lst1, lst2):
    lst = []
    for i in lst1:
        if i in lst2:
            lst.append(i)
    return dedup(lst)
            

def match(tup, num):
    if tup[0] == num:
        return tup[2]
    return False


def dict_from_lists(lst1, lst2):
    dic = {}
    for i in range(len(lst1)):
        dic[lst1[i]] = lst2[i]
    return dic
        

l1 = [2, 3, 6, 4, 6, 4, 1]
l2 = ['4', 'k', 'Betanir', 3, 6, 'g']
details = ('206260762', 'Guy Taggar', '0525797331')
id_num = '206260762'
f_id_num = '201402572'

list_1 = ['a', 'b', 'c']
list_2 = [1, 2, 3]

# print(is_int_list(l1))
# print(pure_int_list(l1))
# print(sym_diff(l1, l2))
# print(dedup(l1))
# print(intersect(l1, l2))

print(match(details, id_num))
print(match(details, f_id_num))
print(dict_from_lists(list_1, list_2))