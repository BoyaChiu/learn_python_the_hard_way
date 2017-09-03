"""
"""Keywords
and #+
del #delete
from #in
not
while #loop
as
elif
global
or
with
eassert
if
pass
yield
break
except
import
print
class
exec
in
raise
continue
finally
is
return
def
for
lambda
try
"""
"""
assert
1、assert语句用来声明某个条件是真的。
2、如果你非常确信某个你使用的列表中至少有一个元素，而你想要检验这一点，并且在它非真的时候引发一个错误，那么assert语句是应用在这种情形下的理想语句。
3、当assert语句失败的时候，会引发一AssertionError。

测试程序：
mylist = ['item']
assert len(mylist) >= 1
mylist.pop()
'item'


assert len(mylist) >= 1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AssertionError
"""
"""
判断:if    elif    else        for    while    break    continue    and    or       is       not          in
if
if  condition1:
    do something
elif  condition2:
    do another thing
else:
    also do something

while condition：
    do something
else：
    do something

for  i in range（1，10，2）：
    do something
    if  condition:
        break
    else:
        do something
for items in list:
    print items


a ? b : c !=a and b or c

is 和 is not 是Python下判断同一性的关键字，通常用来判断 是 True 、False或者None（Python下的NULL）！
2.函数、模块、类
对于Python的函数及模块主要包括这些关键字：

from import as def pass lambda return class
那么你还能记得它们么？下面简单介绍一下：


2.1 模块
Python的编程通常大量使用标准库中的模块，使用方法就是使用import 、from以及as 关键字。

比如： import sys # 导入sys模块

from sys import argv # 从sys模块中导入argv ，这个在前面介绍脚本传参数时使用到

import cPickle as p # 将cPickle模块导入并在此将它简单命名为p，此后直接可以使用p替代cPickle模块原名，这个在介绍文件输入输出时的存储器中使用到


2.2 函数
Python中定义函数时使用到def关键字，如果你当前不想写入真实的函数操作，可以使用pass关键字指代不做任何操作：

def JustAFunction：

pass

当然，在需要给函数返回值时就用到了return关键字，这里简单提一下Python下的函数返回值可以是多个（接收返回值时用相应数量的变量接收！）！

此外Python下有个神奇的Lambda函数，它允许你定义单行的最小函数，这是从Lisp中借用来的，可以用在任何需要函数的地方。比如：

g = lambda x : x*2 # 定义一个Lambda函数用来计算参数的2倍并返回！

print g(2) # 使用时使用lambda函数返回的变量作为这个函数的函数名，括号中带入相应参数即可！

3.异常
对于Python的异常主要包括这些关键字：

try except finally raise
异常这一节还是比较简单的，将可能出现的异常放在 try： 后面的语句块中，使用except关键字捕获一定的异常并在接下来的语句块中做相应操作，而finally中接的是无论出现什么异常总在执行最后做finally： 后面的语句块（比如关闭文件等必要的操作！）

raise关键字是在一定的情况下引发异常，通常结合自定义的异常类型使用。


4.其他
上面的三类过后，还剩下这些关键字：

print del global with assert yield exec

首先print 在前面的笔记或者任何地方你都能见到，所以还是比较熟悉的，此处就不多介绍了！
del 关键字在前面的笔记中已有所涉及，比如删除列表中的某项，我们使用 “ del mylist[0] ”

可能这些剩下来的关键字你比较陌生，所以下面来介绍一下：


4.1.global 关键字
当你在函数定义内声明变量的时候，它们与函数外具有相同名称的其他变量没有任何关系，即变量名称对于函数来说是 局部 的。这称为变量的 作用域 。所有变量的作用域是它们被定义的块，从它们的名称被定义的那点开始。
全局变量
4.2.with 关键字
with语句的执行逻辑如下：紧跟with后面的语句被求值后，返回对象的__enter__()方法被调用，这个方法的返回值将被赋值给as后面的变量。当with后面的代码块全部被执行完之后，将调用前面返回对象的__exit__()方法。
4.3.assert 关键字
assert语句是一种插入调试断点到程序的一种便捷的方式。assert语句用来声明某个条件是真的,当assert语句失败的时候，会引发一AssertionError，所以结合try...except我们就可以处理这样的异常。
eg.
>>> mylist # 此时mylist是有三个元素的列表
['a', 'b', 'c']
>>> assert len(mylist) is not None # 用assert判断列表不为空，正确无返回
>>> assert len(mylist) is None # 用assert判断列表为空
Traceback (most recent call last):
File "", line 1, in
AssertionError # 引发AssertionError异常

4.4.yield 关键字
yield 的作用就是把一个函数变成一个 generator（生成器），带有 yield 的函数不再是一个普通函数，Python 解释器会将其视为一个 generator，调用 fab(5) 不会执行 fab 函数，而是返回一个 iterable（可迭代的）对象！在 for 循环执行时，每次循环都会执行 fab 函数内部的代码，执行到 yield b 时，fab 函数就返回一个迭代值，下次迭代时，代码从 yield b 的下一条语句继续执行，而函数的本地变量看起来和上次中断执行前是完全一样的，于是函数继续执行，直到再次遇到 yield。
4.5.exec 关键字
官方文档对于exec的解释: "This statement supports dynamic execution of Python code."也就是说使用exec可以动态执行Python代码（也可以是文件）。
"""
