
def int_to_str(num):
    iter = 0
    digits = '0123456789'
    if num == 0:
        return '0'
    result = ''
    while num > 0:
        result = digits[num % 10] + result
        num //= 10
        iter += 1
    return result, iter


print(int_to_str(485484600))
