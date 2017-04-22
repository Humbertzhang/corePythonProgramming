#Python核心编程Chapter8笔记
### 三元表达式

如用三元表达式求较小值

    In [3]: x = 1
    
    In [4]: y = 2
    
  >  In [5]: a = x if x < y else y
    
    In [6]: a
    Out[6]: 1

***
### enumerate()函数

可以用来一次性输出index与列表的值

    In [8]: list1 = ['one','two','three','four']

    In [9]: for i,each in enumerate(list1):
        ...:     print i,each
        ...:     
    0 one
    1 two
    2 three
    3 four

***
### 序列的一些内建函数
sorted(),zip() 返回列表 enumerate() , reversed() 返回可迭代对象
> reversed() ：列表反向

.
> sorted()

按照排序规则排序元素,如对于字符串是字典序


    In [10]: list = ['a','b','aaaaa','d','c']
    
    In [11]: list
    Out[11]: ['a', 'b', 'aaaaa', 'd', 'c']
    
    In[12]: list2 = sorted(list)   #<there
    
    In [13]: list2
    Out[13]: ['a', 'aaaaa', 'b', 'c', 'd']
.
> zip() :生成元组的一个列表，较常用于dict()工厂函数

    In [15]: a = [1,2,3,4]
    
    In [16]: b = ['one','two','three','four']
    
    In [17]: c = dict(zip(a,b))
    
    In [18]: c
    Out[18]: {1: 'one', 2: 'two', 3: 'three', 4: 'four'}


    In [19]: d = zip(a,b)

    In [20]: d
    Out[20]: [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]

***
### 循环中的else 语句
用于在循环完成之后进行一些操作
注意break语句也会使其不进行

    In [32]: s = ["a111", "b222", "c333", "d444", "e555"]
    
    In [33]: for c in s:
       ....:         if c.startswith("c"):
       ....:                 print u"发现以字母c开头的项"
       ....:                 break
       ....: else:   
       ....:         print u"没有发现以字母c开头的项"
       ....:     
    发现以字母c开头的项


    In [35]: s = ['qqqq','wwww','eeee','rrrr']
    
    In [36]: for c in s:
       ....:         if c.startswith("c"):
       ....:                 print u"发现以字母c开头的项"
       ....:                 break
       ....: else:    
       ....:         print u"没有发现以字母c开头的项"
       ....:     
    没有发现以字母c开头的项


***
### 元组用于格式化输出的一个特性

    In [37]: t = ('a','b',11,33)
    
    In [38]: print "%s--%s--%d--%d"  %t
             
    a--b--11--33

***
### startswith()函数
检测字符串的开头

    In [39]: str = "abcdefg"
    
    In [40]: str.startswith('abcd')
    Out[40]: True

***
### 列表解析
（1） [expr for iter_var in iterable]

    In [41]: [x*2 for x in range(6)]
    Out[41]: [0, 2, 4, 6, 8, 10]
(2) [expr for iter_var in iterable if cond_expr]

    In [42]: [x*2 for x in range(6) if (x%2 == 1)]
    Out[42]: [2, 6, 10]
    
    1、3、5 × 2 = 2、6、10
### 生成器
(expr for iter_var in iterable)
(expr for iter_var in iterable if cond_expr)
但生成器只在调用时才会生成出来
而列表解析会在一开始就生成完
所以生成器更加“环保”

***
### Tips
xrange()函数比range()函数更加高效，故在数值较大时应使用xrange








