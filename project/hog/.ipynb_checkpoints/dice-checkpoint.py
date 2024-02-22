"""模拟掷骰子的函数。

骰子函数不带参数，返回一个从 1 到 n 的数字
（含），其中 n 是骰子上的边数。

骰子的种类:

- 骰子可以是公平的，这意味着它们会产生相等的每个可能的结果
    概率。示例：four_sided、six_sided

 -  于使用骰子的测试函数，确定性测试骰子始终循环 通过作为参数传递给make_test_dice功能。
"""

from random import randint

def make_fair_dice(sides):
    # 此函数的作用函数一个函数
    """Return a die that returns 1 to SIDES with equal chance."""
    assert type(sides) == int and sides >= 1, 'Illegal value for sides'
    # 判断此参数是否大于1
    def dice():
        return randint(1,sides)
        # 返回一个随机值
    return dice
    # 为什么要这样写呢，返回函数。而不是返回值一个值。利于复用吗？
    # 如何学习这种学法呢

four_sided = make_fair_dice(4)
six_sided = make_fair_dice(6)
six_sided
four_sided

def make_test_dice(*outcomes):
    """Return a die that cycles deterministically through OUTCOMES.

    >>> dice = make_test_dice(1, 2, 3)
    >>> dice()
    1
    >>> dice()
    2
    >>> dice()
    3
    >>> dice()
    1
    >>> dice()
    2

    This function uses Python syntax/techniques not yet covered in this course.
    The best way to understand it is by reading the documentation and examples.
    """
    assert len(outcomes) > 0, 'You must supply outcomes to make_test_dice'
    # 判断参数是否大于0
    for o in outcomes:
        # 参数迭代
        assert type(o) == int and o >= 1, 'Outcome is not a positive integer'
        # 确保每一个参数都是正整数
    index = len(outcomes) - 1
    # 为什么索引值要减去一，因为索引值是从零开始
    def dice():
        # 又定义一个函数
        nonlocal index
        index = (index + 1) % len(outcomes)
        return outcomes[index]
    return dice

test_dice = make_test_dice(5, 1, 1,10,35)


print(test_dice())



