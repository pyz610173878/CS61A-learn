# lambda的调用


```python
>>> a = lambda x: x  # Assigning the lambda function to the name a
>>> a(5)
>>> (lambda: 3)()

# Example


```




    3



因为lambda没有函数名，所以调用的时候，只需要输入框()即可。


```python
>>> b = lambda x: lambda: x  # Lambdas表达式能够返回其他lambdas。
>>> c = b(88)
>>> print(c)
# 88

>>> c()
# 函数名
```

    <function <lambda>.<locals>.<lambda> at 0x000002A2A95F8360>
    




    88



# 用lambda编写高阶函数


```python
>>> d = lambda f: f(4)  # They can have functions as arguments as well.
>>> def square(x):
...     return x * x
>>> d(square)
# 16

# Example

def c(f):
    return f(4)

g = lambda x: pow(x,3)

c(g)

```




    64



特征：一个函数返回另外一个函数。

用lambda编写高阶函数。这个函数接受一个函数参数，返回xx。



```python
>>> z = 3
>>> e = lambda x: lambda y: lambda: x + y + z
>>> e(0)(1)()
```




    4




```python
>>> f = lambda z: x + z
>>> f(3)

# 你需要做的是，把两个函数的结果想加起来是这样吗？我也不确定。
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    Cell In[24], line 2
          1 f = lambda z: x + z
    ----> 2 f(3)
          4 # 你需要做的是，把两个函数的结果想加起来是这样吗？我也不确定。
    

    Cell In[24], line 1, in <lambda>(z)
    ----> 1 f = lambda z: x + z
          2 f(3)
          4 # 你需要做的是，把两个函数的结果想加起来是这样吗？我也不确定。
    

    TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'


# 高阶函数（lambda）


```python
>>> higher_order_lambda = lambda f: lambda x: f(x)
>>> g = lambda x: x * x
>>> higher_order_lambda(2)(g)  # Which argument belongs to which function call?

```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    Cell In[27], line 3
          1 higher_order_lambda = lambda f: lambda x: f(x)
          2 g = lambda x: x * x
    ----> 3 higher_order_lambda(2)(g)  # Which argument belongs to which function call?
          4 higher_order_lambda(g)(2)
    

    Cell In[27], line 1, in <lambda>(x)
    ----> 1 higher_order_lambda = lambda f: lambda x: f(x)
          2 g = lambda x: x * x
          3 higher_order_lambda(2)(g)  # Which argument belongs to which function call?
    

    TypeError: 'int' object is not callable



```python
>>> higher_order_lambda(g)(2)
```




    4




# 嵌套函数（lambda表达式）


```python
>>> call_thrice = lambda f: lambda x: f(f(f(x)))
>>> call_thrice(lambda y: y + 1)(0)

# 函数一共重复调用了三次。0 + 1  1 + 1 2 + 1 = 3
```




    3




```python
>>> print_lambda = lambda z: print(z)  # When is the return expression of a lambda expression executed?
>>> print_lambda

one_thousand = print_lambda(1000)

one_thousand
```

    1000
    

## 高阶函数


```python
>>> def even(f):
...     def odd(x):
...         if x < 0:
...             return f(-x)     # steven(4)
...         return f(x)
...     return odd
>>> steven = lambda x: x
>>> stewart = even(steven)
>>> print(stewart)

>>> print(stewart(61))
# 返回61然后返回odd的内存地址。

>>> stewart(-4)
# 4
```

    <function even.<locals>.odd at 0x000002A2A9D505E0>
    61
    




    4



1. 定义了一个函数参数为f
2. 在函数体内部又定义了一个函数参数为x
3. odd函数的函数体：如果 x 小于 0: 返回 f函数(-x). 参数为odd的参数但是为负值。
否则 就返回f(x)。
然后在返回 odd函数。 注意这里是返回odd函数，并没有调用odd函数。

编写了一个steven函数，就返回参数x。


定义一个cake函数。输出 beats。内部定义pie没有参数，输出 sweats并且 返回 cake。最后cake函数返回 pie函数。



```python
>>> def cake():
...    print('beets')
...    def pie():
...        print('sweets')
...        return 'cake'
...    return pie
>>> chocolate = cake()
chocolate
chocolate()
# beets
```

    beets
    <function cake.<locals>.pie at 0x000002A2AA45C5E0>
    

cake是一个很神奇的函数。他既可以输出值，也可以当做函数调用。


```python
>>> chocolate()
>>> more_chocolate, more_cake = chocolate(), cake


```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    Cell In[44], line 1
    ----> 1 chocolate()
          3 # sweets cake
    

    TypeError: 'NoneType' object is not callable



```python


```


```python
______

>>> more_chocolate
```
