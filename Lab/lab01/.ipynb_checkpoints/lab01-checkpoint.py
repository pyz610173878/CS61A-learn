def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    # result = 1
    # for i in range(k):
    #     result *= n
    #     n -= 1
    # return result
    if k == 0:
        return 1
    elif k == 1:
        return n
    else:
        return n * falling(n-1, k-1)

print(falling(6, 3))
print(falling(4, 3))
print(falling(4, 1))
print(falling(4, 0))

    # 输入空间
    # 两个参数都是正整数。
    # 参数1为正整数，参数2为阶乘的数量。
    # 输出空间

    # 简化一下，给定数字，算出她的阶乘。
    # 1. 了解阶乘的概念
    # 2. 了解用迭代解决
    # 3. 了解用递归解决
    # 4. 增加一个参数。


def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    total = 0
    while y > 0:
        total += y % 10
        print(y % 10)
        y //= 10
    return total

# print(sum_digits(10))
# print(sum_digits(4224))
# print(sum_digits(1234567890))
# a = sum_digits(123)
# print(a)

def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
    
    string_n = str(n)
    for i in range(len(string_n)- 1):
        if string_n[i:i+1] == "88":
            return True
        else:
            return False





print(double_eights(8))
print(double_eights(88))
print(double_eights(2882))
print(double_eights(880088))
print(double_eights(12345))
print(double_eights(80808080))