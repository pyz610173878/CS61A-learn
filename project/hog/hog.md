# 

# hog 项目
根据 [CS61A第一次大作业要求](https://inst.eecs.berkeley.edu/~cs61a/fa20/proj/hog/#problem-1-hint-video)每个函数按照顺序进行排序。为了照顾英语不好的同学，或者想着用中文阅读起来快一点。我根据gpt和翻译软件。把每个函数的参数与作用都进行了翻译。


```python
"""CS 61A Presents The Game of Hog."""

from dice import six_sided, four_sided, make_test_dice
from ucb import main, trace, interact

GOAL_SCORE = 100  # The goal of Hog is to score 100 points.
FIRST_101_DIGITS_OF_PI = 31415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679
# 圆周率的值

######################
# Phase 1: Simulator #
######################
```

    5
    

# roll_dice函数
此函数有两个参数, 一个名为 num_rolls 的正整数，表示要掷的骰子数量；另一个是dice函数，用于模拟掷骰子的行为。

roll_dice 函数的返回值是根据掷骰子的结果计算出的本回合得分：要么是所有骰子点数之和，要么是1分（如果出现了“Pig Out”情况）。 

“Pig Out”是指如果任何一次掷骰的结果是1，那么当前玩家的本回合得分就是1分。

例如：
1. 当前玩家掷了7次骰子（num_rolls = 7），其中5次的结果是1。由于出现了“Pig Out”，他们本回合的得分是1分。
2. 当前玩家掷了4次骰子，结果都是3。因为没有出现“Pig Out”，他们本回合的得分是12分（3+3+3+3）。


```python
def roll_dice(num_rolls, dice=six_sided):
    """模拟将骰子精确滚动 NUM_ROLLS > 0 次。返回结果的总和，除非任何结果为 1。在这种情况下 返回 1.

    
    num_rolls: 将要进行的掷骰子的次数
    dice:      一个模拟单次掷骰子结果的函数 也就是几面
    """
    # 下列 assert语句 表示 num_rolls 必须为正整数.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls > 0, 'Must roll at least once.'
    # BEGIN PROBLEM 1
    "*** YOUR CODE HERE ***"

    Pig_out = False
    sum_of_rolls = 0
    
    for _ in range(num_rolls):
        roll = dice()  # 掷骰子
        if roll == 1:  # 如果结果为1
            Pig_out = True  # 设置“Pig Out”标志为True
        sum_of_rolls += roll  # 累加点数
        print(roll)
    if Pig_out:  # 如果出现了“Pig Out”
        return 1  # 返回1分
    
    else:
        return sum_of_rolls  # 返回点数总和



roll_dice(5)
roll_dice(4, four_sided) # 4面的骰子
```

# free_bacon 

题目要求实现一个名为free_bacon的函数，该函数接受对手的当前分数作为参数，并返回玩家在掷0个骰子时获得的分数。假设对手的分数小于100。

规则如下：
圆周率： 31415926535...

玩家如果选择不掷骰子，将获得k+3分，其中k是圆周率π小数点后第n位的数字，而n是玩家对手的总分。作为一个特殊情况，如果对手的分数是n=0，那么k=3（圆周率π小数点前的数字）。

比如：
1. 对手的分数为0：
    - 预期结果：`k`是圆周率π小数点前的数字，即3。因此，当前玩家应获得`3+3=6`分。
    - 测试调用：`free_bacon(0)`
    - 预期输出：6
2. 对手的分数为1：
    - 预期结果：`k`是圆周率π小数点后的第一位数字，即1。因此，当前玩家应获得`1+3=4`分。
    - 测试调用：`free_bacon(1)`
    - 预期输出：4
3. 对手的分数为2：
    - 预期结果：`k`是圆周率π小数点后的第二位数字，即4。因此，当前玩家应获得`4+3=7`分。
    - 测试调用：`free_bacon(2)`
    - 预期输出：7
4. 对手的分数为42：
    - 预期结果：`k`是圆周率π小数点后的第四十二位数字，即9。因此，当前玩家应获得`9+3=12`分。
    - 测试调用：`free_bacon(42)`
    - 预期输出：12

提供的代码中包括了FIRST_101_DIGITS_OF_PI作为一个整数，它在本地存储为pi。解决这个问题的一种方法是将pi截断，直到它只有score+1位数字，然后返回pi的最后一位数字加3。

提示：如果一个整数n有k+1位数字，那么n小于pow(10, k+1)但大于或等于pow(10, k)。

限制条件：不能使用**for循环**或**方括号[ ]**。




```python
def free_bacon(score):
    """Return the points scored from rolling 0 dice (Free Bacon).

    score:  The opponent's current score.
    """
    assert score < 100, 'The game should be over.'
    pi = FIRST_101_DIGITS_OF_PI

    # Trim pi to only (score + 1) digit(s)
    # BEGIN PROBLEM 2
    "*** YOUR CODE HERE ***"
    # END PROBLEM 2

    return pi % 10 + 3



def test_free_bacon():
    assert free_bacon(0) == 6
    assert free_bacon(1) == 4
    assert free_bacon(2) == 7
    assert free_bacon(42) == 12
test_free_bacon()
```
