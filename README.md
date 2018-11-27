# tutor code

<!-- MarkdownTOC autolink="true" style="ordered" -->

1. [Base](#base)
    1. [Syntax](#syntax)
    1. [Variables](#variables)
        1. [get variable type](#get-variable-type)
        1. [convert type](#convert-type)
        1. [enum](#enum)
    1. [Operators](#operators)
        1. [三元運算](#%E4%B8%89%E5%85%83%E9%81%8B%E7%AE%97)
        1. [if](#if)
        1. [else if](#else-if)
        1. [else](#else)
        1. [==](#)
        1. [True / False](#true--false)
        1. [while ... else](#while--else)
        1. [break / continue](#break--continue)
        1. [for ... else](#for--else)
        1. [range\(\)](#range)
    1. [Number](#number)
    1. [Strings](#strings)
    1. [Iterate](#iterate)
        1. [List](#list)
        1. [Set](#set)
        1. [Dict](#dict)
    1. [Iterate Advanced](#iterate-advanced)
        1. [filter](#filter)
        1. [map](#map)
        1. [reduce](#reduce)
    1. [Lambda](#lambda)
    1. [Functions](#functions)
    1. [Closure](#closure)
    1. [Modules](#modules)
    1. [Classes and Objects](#classes-and-objects)
        1. [類別方法](#%E9%A1%9E%E5%88%A5%E6%96%B9%E6%B3%95)
    1. [DateTime](#datetime)
    1. [JSON](#json)
    1. [System](#system)
    1. [Try...Except](#tryexcept)

<!-- /MarkdownTOC -->


## Base

### Syntax
每行不用`;` , 使用縮進2格或4格

Comments: `#`
Docstrings: """  or '''

keywords: https://www.programiz.com/python-programming/keyword-list


### Variables
內建資料類型:
- boolean : True / False
- int : e.g. 42, 100000
- float : e.g. 3.14159, 1.0e8
- string : 'abc'
- enum

#### get variable type
type()

#### convert type
int({str})

#### enum


*******************
### Operators
#### 三元運算
```python
condition_is_true if condition else condition_is_false
```

#### if
```python
if condition:
	pass
```

#### else if
```python
if condition:
	pass
elif condition:
```

#### else
```python
if condition:
	pass
else:
	pass
```

#### ==

#### True / False
True
`True, 'abc', 1, -1, [1,2]`

False 
`False, None, 0, 0.0, '', [], (), {}, set()`

#### while ... else

#### break / continue

#### for ... else

#### range()



*******************
### Number


*******************
### Strings


*******************
### Iterate

#### List

#### Set

#### Dict


*******************
### Iterate Advanced

#### filter
```python
f = filter(fn, array)
```

#### map
```python
m = map(fn, array)
```

#### reduce
```python
d = reduce(fn, array)
```


*******************
### Lambda
```python
f = lambda arg1, arg2, ....: expression
```


*******************
### Functions


*******************
### Closure


*******************
### Modules


*******************
### Classes and Objects

#### 類別方法
```python
class Some:
    def __init__(self, x):
        self.x = x

    @classmethod
    def service(clz, y):
        print('do service...', clz, y)

Some.service(30)
```

*******************
### DateTime


*******************
### JSON


*******************
### System


*******************
### Try...Except
