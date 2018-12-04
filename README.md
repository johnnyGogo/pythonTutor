# tutor code

<!-- MarkdownTOC autolink="true" style="ordered" -->

1. [Base](#base)
    1. [Syntax](#syntax)
    1. [Variables](#variables)
        1. [get variable type](#get-variable-type)
        1. [convert type](#convert-type)
        1. [enum](#enum)
        1. [作用域](#%E4%BD%9C%E7%94%A8%E5%9F%9F)
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
        1. [switch / case](#switch--case)
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
        1. [時區](#%E6%99%82%E5%8D%80)
        1. [時間加減](#%E6%99%82%E9%96%93%E5%8A%A0%E6%B8%9B)
        1. [格式化](#%E6%A0%BC%E5%BC%8F%E5%8C%96)
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

#### 作用域
LEGB

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

#### switch / case
python 沒有
替代方式 dictionary
```python
def numbers_to_strings(argument):
    switcher = {
        0: "zero",
        1: "one",
        2: "two",
    }
    return switcher.get(argument, "nothing")
```

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
```python
import datetime
import time

# datetime
now = datetime.datetime.now()
now = datetime.datetime.utcnow()

# timestamp
time.time()

# time tuple
time.localtime()

# date
now.date()

```

#### 時區
import pytz
```python
now = datetime.datetime.utcnow()

# 從國家取得時區
pytz.country_timezones(‘cn’)

# 取得時區時間
tz = pytz.timezone('Asia/Tokyo')
datetime.datetime.now(tz)
```


#### 時間加減
datetime.timedelta
```python
datetime.datetime.now() - datetime.timedelta(days=3)

# 時間差
(datetime.datetime(2015,1,13,12,0,0) - datetime.datetime.now()).total_seconds()
```

#### 格式化
time.strftime("%Y-%m-%d %H:%M:%S")

datetime.datetime.strptime("2014-12-31 18:20:10", "%Y-%m-%d %H:%M:%S")

*******************
### JSON
- json.dumps: dict to json
- json.loads: json to dict


*******************
### System


*******************
### Try...Except
