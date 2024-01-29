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
    "*** YOUR CODE HERE ***"
    ans = 0
    while y:
        ans += y % 10
        # 小数点部分直接省略了。
        print(ans)
        y //= 10
        print(y)
    return ans


sum_digits(10)
sum_digits(145)