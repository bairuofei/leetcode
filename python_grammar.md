# str
python中str是不可变对象，因此不支持对str本身进行元素替换，元组也不可以

```py
str2=str1.replace('a','b') #替换str中的a为b，并返回一个新的str2

str.join(sequence) #将sequence中的str元素通过str连接，并返回一个新的字符串
```

# divide
1. 普通除法"/": 整数与小数都适用，返回带有小数部分
2. 整数地板除"//": 整数与小数都适用，返回地板除结果
   
math模块提供类似功能的函数：
```py
import math
math.floor(num) #地板除
math.ceiling(num) #天花板除
```

# set

## 创建set
s=set() or {...}  
> 创建空集合只能用set()，因为{}会创建一个空字典

## 添加元素
```py
s.add(x) # 添加单个元素，若元素已存在，则不进行操作
s.update(x) # 参数可以是列表，元组，字典等；x也可以有多个，用逗号隔开
```
## 移除元素
```py
s.remove(x) # 若x不存在，则会发生错误
s.discard(x) # 若x不存在，不会发生错误
s.pop() # 随机删除集合中的一个元素
# set 集合的 pop 方法会对集合进行无序的排列，然后将这个无序排列集合的左面第一个元素进行删除
```

## 计算元素个数
```py
len(s)
```
## 清空集合
```py
s.clear()
```
## 集合运算
```py
intersection() # 返回集合交集
union() # 返回集合并集
```

```bash
>>> a = set('abracadabra')
>>> b = set('alacazam')
>>> a                                  # unique letters in a
{'a', 'r', 'b', 'c', 'd'}
>>> a - b                              # letters in a but not in b
{'r', 'd', 'b'}
>>> a | b                              # letters in a or b or both
{'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
>>> a & b                              # letters in both a and b
{'a', 'c'}
>>> a ^ b                              # letters in a or b but not both
{'r', 'd', 'b', 'm', 'z', 'l'}
```

## set comprehensions
`a={x for x in "abcdesge" if x not in "abc"}`
> similar to list comprehensions

# collections.defaultdict()
> https://docs.python.org/zh-cn/3/library/collections.html#defaultdict-objects

```py
from collections import defaultdict
d1=defaultdict(int)  # dict中的value类型为int，初始调用每一个key时设置int类型的默认值0
# d2=defaultdict(list) # 与上同理 d2["a"].append
d["a"]+=1
```

# sorted() and list.sort()
> https://docs.python.org/zh-cn/3/howto/sorting.html

默认升序;
- list.sort(key=func)仅为list设计，在原list上进行修改。 *list.sort()没有返回值*，直接在原list上进行修改
- sorted(iterable,key=func,Reverse=True)可以接收任何可迭代对象，并*返回一个修改后的列表*
```py
# key指定根据哪个字段对列表元素进行排序
key=lambda 元素： 元素[字段索引]

# list排序同时保留下标信息
a=[1,2,3,4,5]
b=sorted(enumerate(a),key=lambda x: x[1])
```
key=func表示在每一个对象使用func处理之后进行排序

# list
```py
list.append(x)
list.extend(iterable)
list.insert(i,x)
list.remove(x)
list.pop([i])
list.count(x)
list.clear()
list.reverse()
list.copy(), same to a[:]
del list(slices_index)
```
stack: 使用pop和append可以将list作为stack
queue:

list.index(item): 返回item在list中第一次出现时的小标，若不存在则抛出ValueError

## tuple: 
immutable, usually contain heterogeneous elements
tuple元素不可变，但是元素本身可以为可变元素，比如tuple的元素为list

element can be accessed by unpacking or indexing

> one element tuple need a comma after the element
a=1,
b=(2,)

- packing: t=123,344,'string'
- unpacking: num1, num2, str1=t

## list: 
mutable, usually contain homogeneous elements

accessed by iterated over the list

## mod
python模除使用向下取整原则
若$-10\%2$，则首先计算$-10//2$，得到$-2.5->-3$，因此相应计算余数为$+2$.
```py
-10 % 4 = 2
10 % -4 = -2
-10 % -4 = -2
# 可以看到模除的结果始终与除数同号 
```
规律总结：
- 模除的结果始终与除数同号
- 若模除的结果不为零，且除数为正数，则存在关系$a\%b+(-a)\%b=b$

## reversed
reversed(seq):反转迭代器，seq可以是tuple,string,list,range

## 值类型和引用类型
list,字典属于引用类型
数字，tuple,string属于值类型。

## dict
dict的key可以用num和str,tuple也可以，但是tuple中的元素只能是num,str或tuple。
否则含有可变元素的tuple不可以作为dict的key。
```py
del dict[key]  # 删除元素
list(dict) # 以插入顺序将dict中的key作为list
sorted(dict) # 返回排序之后的list(dict)

# dict comprehensions
{x: x**2 for x in (2, 4, 6)}

#  builds dictionaries directly from sequences of key-value pairs
dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
# using key word arguement
dict(sape=4139, guido=4127, jack=4098)
{'sape': 4139, 'guido': 4127, 'jack': 4098}
```

```py
# 遍历字典的key
for key in d:

for key in d.keys():
# 遍历字典的value
for value in d.values():
```
> d.keys()和d.values()都属于迭代器，因此不能用下标访问。可以用list(d.values())转换为list。

## loop techniques
```py
# using items() method to looping through the key-value pairs of a dict at the same time
for key, value in dict.items():

# loop over two or more sequences at the same time, the entries can be paired with zip() function.
for q,a in zip(questions,answers):
```

## collections.Counter([iterable-or-mapping])
```py
import collections
c=collections.Counter([iterable])
# c: type Counter, is a sub-class of dict, with no restrictions on value type.
```
```py
sum(c.values())                 # total of all counts
c.clear()                       # reset all counts
list(c)                         # list unique elements
set(c)                          # convert to a set
dict(c)                         # convert to a regular dictionary
c.items()                       # convert to a list of (elem, cnt) pairs
Counter(dict(list_of_pairs))    # convert from a list of (elem, cnt) pairs
c.most_common()[:-n-1:-1]       # n least common elements
+c                              # remove zero and negative counts
```

```py
c = Counter(a=3, b=1)
d = Counter(a=1, b=2)
c + d                       # add two counters together:  c[x] + d[x]
Counter({'a': 4, 'b': 3})
c - d                       # subtract (keeping only positive counts)
Counter({'a': 2})
c & d                       # intersection:  min(c[x], d[x]) 
Counter({'a': 1, 'b': 1})
c | d                       # union:  max(c[x], d[x])
Counter({'a': 3, 'b': 2})
```
```py
# 单目加和减（一元操作符）意思是从空计数器加或者减去
c = Counter(a=2, b=-4)
+c
Counter({'a': 2})
-c
Counter({'b': 4})
```

> Counter对象有一个字典接口，如果引用的键没有任何记录，就返回一个0，而不是弹出一个 KeyError



## 判断字符是否为字母或数字
```py
str.isdigit() # reutrn boolean
str.isalpha() 

str.isalnum() # 是否仅为数字和字母的组合
```

## python中的真值

> https://juejin.im/post/5da18984e51d4577fa2b01b7

Python3中判断为假的值有：
- False
- 所有数值类型的零值。int,float,double
- 空序列空集合空映射
- 定义了__bool__或__len__并返回False或0的用户自定义类的实例
- None


## lambda expression
```py
lambda args1[,args2,...]: expression
# example
sum=lambda x,y: x+y
res=sum(5,6)
```
lambda expression返回值为一个函数，可以作为函数使用，也可以作为某些函数的参数使用。

## map function
```py
# Return an iterator that applies function to every item of iterable, yielding the results
# with many iterables, the iterator stops when the shortest iterable is exhausted.
map(fun,iter,...)
```