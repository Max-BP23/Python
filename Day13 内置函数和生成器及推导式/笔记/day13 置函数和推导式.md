# day13 内置函数和推导式

![image-20201230125816095](assets/image-20201230125816095.png) 

今日概要：

- 匿名函数
- 生成器
- 内置函数
- <span style='color:red;'>**附加**</span>：推导式，属于数据类型的知识，内部的高级的用法会涉及到【生成器】和【函数】的知识。



## 1. 匿名函数

传统的函数的定义包括了：函数名 + 函数体。

```python
def send_email():
    pass

# 1. 执行
send_email()
# 2. 当做列表元素
data_list = [send_email, send_email, send_email ]
# 3. 当做参数传递
other_function(send_email)
```



匿名函数，则是基于lambda表达式实现定义一个可以没有名字的函数，例如：

```python
data_list = [ lambda x:x+100,  lambda x:x+110, lambda x:x+120 ]

print( data_list[0] )
```

```python
f1 = lambda x:x+100

res = f1(100)
print(res)
```



基于Lambda定义的函数格式为：`lambda 参数:函数体` (lambda后面有空格)

- 参数，支持任意参数。

  ```python
  lambda x: 函数体
  lambda x1,x2: 函数体
  lambda *args, **kwargs: 函数体
  ```

- 函数体，只能支持单行的代码。

  ```python
  def xxx(x):
      return x + 100
      
  lambda x: x + 100 (和上面def的意思一样)
  ```

- 返回值，默认将函数体单行代码执行的结果返回给函数的执行这。

  ```python
  func = lambda x: x + 100
  
  v1 = func(10)
  print(v1) # 110
  ```



```python
def func(a1,a2):
    return a1 + a2 + 100

foo = lambda a1,a2: a1 + a2 + 100 (和上面的def表达的意思一样,lambda只能一行)
```

匿名函数适用于简单的业务处理，可以快速并简单的创建函数。

### 练习题

根据函数写写出其匿名函数的表达方式

```python
def func(a1,a2):
    return a1 + a2

# func = lambda a1,a2: a1+a2
```

```python
def func(data):
    return data.replace("苍老师","***")

# func= lambda data: data.replace("苍老师","***")
```

```python
def func(data):
    name_list = data.replace(".")
    return name_list[-1]

# func = lambda data: data.replace(".")[-1]
```

在编写匿名函数时，由于受限 函数体只能写一行，所以匿名函数只能处理非常简单的功能。



### 扩展：三元运算

简单的函数，可以基于lambda表达式实现。

简单的条件语句( if else)，可以基于三元运算实现，例如：

```python
num = input("请写入内容")

if "苍老师" in num:
    data = "臭不要脸"
else:
    data = "正经人"
    
print(data)
```

```python
num = input("请写入内容")
data = "臭不要脸" if "苍老师" in num else "正经人"
print(data)

# 结果 =  条件成立时    if   条件   else   不成立
```

lambda表达式和三元运算没有任何关系，属于两个独立的知识点。



掌握三元运算之后，以后再编写匿名函数时，就可以处理再稍微复杂点的情况了，例如：

```python
func = lambda x: "大了" if x > 66 else "小了"

v1 = func(1)
print(v1) # "小了"

v2 = func(100)
print(v2) # "大了"
```





## 2. 生成器

生成器是由函数+yield关键字创造出来的写法，在特定情况下，用他可以帮助我们节省内存。

- 生成器函数，但函数中有yield存在时，这个函数就是生产生成器函数。

  ```python
  def func():
      print(111)
      yield 1 # yield后面可以加任何类型
  ```

  ```python
  def func():
      print(111)
      yield 1
  
      print(222)
      yield 2
  
      print(333)
      yield 3
  
      print(444)
  ```

- 生成器对象，执行生成器函数时，会返回一个生成器对象。

  ```python
  def func():
      print(111)
      yield 1
  
      print(222)
      yield 2
  
      print(333)
      yield 3
  
      print(444)
      
  data = func()
  
  # 执行生成器函数func，返回的生成器对象。
  # 注意：执行生成器函数时，函数内部代码不会执行。
  ```

  ```python
  def func():
      print(111)
      yield 1
  
      print(222)
      yield 2
  
      print(333)
      yield 3
  
      print(444)
      
  data = func()
  
  v1 = next(data)
  print(v1)
  
  v2 = next(data)
  print(v2)
  
  v3 = next(data)
  print(v3)
  
  v4 = next(data)
  print(v4)  # 结束或中途遇到return，程序爆：StopIteration 错误
  #这个是本质
  ```
  
  ```python
  data = func()
  
  for item in data:
      print(item) # 且循环完毕之后,即使最后一个没有return或者yield,也不会报错
  # 这个常用,将上面的v1-v4用for循环表示
  ```


生成器的特点是，记录在函数中的执行位置，下次执行next时，会从上一次的位置基础上再继续向下执行。



### 应用场景

- 假设要让你生成 300w个随机的4位数，并打印出来。

  - 在内存中一次性创建300w个
  - 动态创建，用一个创建一个。

  ```python
  import random
  
  val = random.randint(1000, 9999)
  print(val)
  ```

  ```python
  import random
  
  data_list = []
  for i in range(300000000):
      val = random.randint(1000, 9999)
  	data_list.append(val)
      
  # 再使用时，去 data_list 中获取即可。
  # ...传统思路,一下子全部生成
  ```

  ```python
  import random
  
  
  def gen_random_num(max_count):
      counter = 0
      while counter < max_count:
          yield random.randint(1000, 9999)
          counter += 1
  
  
  data_list = gen_random_num(3000000)
  # 再使用时，去 data_list 中获取即可。
  ```

- 假设让你从某个数据源中获取300w条数据（后期学习操作MySQL 或 Redis等数据源再操作，了解思想即可）。

<img src="assets/image-20201230174253215.png" alt="image-20201230174253215" style="zoom: 33%;" />

所以，当以后需要我们在内存中创建很多数据时，可以想着用基于生成器来实现一点一点生成（用一点生产一点），以节省内存的开销。



### 扩展(了解)

```python
def func():
    print(111)
    v1 = yield 1 # 会把v2传入的666返回输出,然后再进行print(222)及下面的运行
    print(v1) # 111,1

    print(222)
    v2 = yield 2
    print(v2) # 111,1,666,222,2

    print(333)
    v3 = yield 3
    print(v3)

    print(444)


data = func()

n1 = data.send(None)
print(n1)

n2 = data.send(666)
print(n2)

n3 = data.send(777)
print(n3)

n4 = data.send(888)
print(n4)
```



## 3.内置函数

<img src="assets/image-20201230201618164.png" alt="image-20201230201618164" style="zoom:50%;" />

Python内部为我们提供了很多方便的内置函数，在此整理出来36个给大家来讲解。

- 第1组 数学运算（5个）

  - abs，绝对值

    ```python
    v = abs(-10)
    ```

  - pow，指数

    ```python
    v1 = pow(2,5) # 2的5次方  2**5
    print(v1)
    ```

  - sum，求和

    ```python
    v1 = sum([-11, 22, 33, 44, 55]) # 可以被迭代-即for循环,列表,元组,字典均可
    print(v1)
    ```

  - divmod，求商和余数

    ```
    v1, v2 = divmod(9, 2)
    print(v1, v2)
    ```

  - round，小数点后n位（四舍五入）

    ```python
    v1 = round(4.11786, 2)
    print(v1) # 4.12
    ```

- 第2组 循环用并对数据进行处理（4个）

  - min，最小值

    ```python
    v1 = min(11, 2, 3, 4, 5, 56) # 直接传参
    print(v1) # 2
    ```

    ```Python
    v2 = min([11, 22, 33, 44, 55]) # 迭代的类型（for循环） 字符串也行,将字符串里面的数字元素一一比较 ("12347265")
    print(v2) # 11
    ```

    ```python
    v3 = min([-11, 2, 33, 44, 55], key=lambda x: abs(x)) # 在内部进行绝对值计算,然后取min,min是加工之前的值
    print(v3) # 2
    ```

  - max，最大值

    ```python
    v1 = max(11, 2, 3, 4, 5, 56)
    print(v1)
    
    v2 = max([11, 22, 33, 44, 55])
    print(v2)
    ```

    ```python
    v3 = max([-11, 22, 33, 44, 55], key=lambda x: x * 10) # 输出加工前的值
    print(v3) # 55
    ```

  - all，是否全部为True (有False,结果就是False)

    ```python
    v1 = all(   [11,22,44,""]   ) # False 里面数据没有保证全部为True
    ```

  - any，是否存在True(有True,结果就是True)

    ```python
    v2 = any([11,22,44,""]) # True 
    ```

    

- 第3组 进制转换相关（3个）

  - bin，十进制转二进制
  - oct，十进制转八进制
  - hex，十进制转十六进制

- 第4组 unicode和数字的对应关系（2个）

  - ord，获取字符对应的unicode码点（十进制）

    ```
    v1 = ord("武")
    print(v1, hex(v1)) # 转换为16进制
    ```

  - chr，根据码点（十进制）获取对应unicode字符

    ```python
    v1 = chr(27494)
    print(v1)
    ```

- 第5组 数据类型（9个）

  - int

  - foat

  - str，unicode编码

  - bytes(一般和str联合使用)，utf-8、gbk编码 

    ```python
    v1 = "武沛齐"  # str类型
    
    v2 = v1.encode('utf-8')  # bytes类型 
    
    v3 = bytes(v1,encoding="utf-8") # bytes类型
    ```

  - bool

  - list

  - dict

  - tuple

  - set

- 第6组（13个）

  - len

  - print

  - input

  - open

  - type，获取数据类型

    ```python
    v1 = "123"
    
    if type(v1) == str:
        pass
    else:
        pass
    ```

  - range 

    ```python
    range(10)
    ```

  - enumerate 列举

    ```python
    # 例1
    v1 = ["武沛齐", "alex", 'root']
    
    for num in enumerate(v1): 
        print(num)
    # 结果
    (0, '武沛齐')
    (1, 'alex')
    (2, 'root')
    
    # 例1
    v1 = ["武沛齐", "alex", 'root']
    
    for num in enumerate(v1,1): # v1后面加1,从1开始
        print(num)
    # 结果
    (1, '武沛齐')
    (2, 'alex')
    (3, 'root')
    ```

    
  
    ```python
    v1 = ["武沛齐", "alex", 'root']
    
    for num, value in enumerate(v1, 1): # v1不加信息,默认从0开始,后面加1,从1开始,且直接解包,去掉()
        print(num, value)
    #结果
    1 武沛齐
    2 alex
    3 root
    ```
  
  - id
  
  - hash 哈希
  
    ```python
    v1 = hash("武沛齐") # 转换完数字
    ```
  
  - help，帮助信息
  
    - pycharm，不用 ,因为可以直接输入函数,Ctrl+点击函数即可
  
    - 终端，使用
  
      ```python
      help(str) # 功能等各种全部显示出来
      ```
  
      
  
  - zip 拉链
  
    ```python
    v1 = [11, 22, 33, 44, 55, 66]
    v2 = [55, 66, 77, 88]
    v3 = [10, 20, 30, 40, 50]
    
    # [11,55,10] [11,66,20] [33,77,30] [44,88,40] 后面v2没值,就不在取值了
    # 正常应该是列表套列表
    [
        [11,55,10],
     	[11,66,20],
     	[33,77,30],
     	[44,88,40]
    ]
    result = zip(v1, v2, v3) # 通过zip处理,一行一行输出
    # print(result)  # <zip object at 0x000000000246EF88>
    for item in result:
        print(item)
    # 一行一行输出
    (11, 55, 10)
    (22, 66, 20)
    (33, 77, 30)
    (44, 88, 40)
    ```
  
  - callable，是否可执行，后面是否可以加括号(其实就是函数)。
  
    ```python
    v1 = "武沛齐"
    v2 = lambda x: x
    def v3():
        pass
    
    
    print( callable(v1) ) # False
    print(callable(v2)) # True
    print(callable(v3)) # True
    ```
  
  - sorted，排序(此为内置函数 列表,元组,字典(Python3.6后)均可用)
  
    ```python
    v1 = sorted([11,22,33,44,55]) # 从小到大
    v1 = sorted([11,22,33,44,55], reverse=True)  #从大到小
    
    # 列表内部专用功能
    v1 = [11,22,33,44,55]
    v1.sort() # 从小到大
    v1.sort(reverse=True) #从大到小
    
    ```
    
    
    
    ```python
    # 字典
    info = {
        "wupeiqi": {
            'id': 10,
            'age': 119
        },
        "root": {
            'id': 20,
            'age': 29
        },
        "seven": {
            'id': 9,
            'age': 9
        },
        "admin": {
            'id': 11,
            'age': 139
        },
    }
    
    result = sorted(info.items(), key=lambda x: x[1]['id']) # key后面以值[1]中的id排序
    #[('seven', {'id': 9, 'age': 9}), ('wupeiqi', {'id': 10, 'age': 119}), ('admin', {'id': 11, 'age': 139}), ('root', {'id': 20, 'age': 29})]
    print(result)
    
    result = sorted(info) # 只按照key进行排序 # ['admin', 'root', 'seven', 'wupeiqi']
    result = sorted(info, reverse=True) # ['wupeiqi', 'seven', 'root', 'admin']
    ```
    
    ```python
    data_list = [
        '1-5 编译器和解释器.mp4',
        '1-17 今日作业.mp4',
        '1-9 Python解释器种类.mp4',
        '1-16 今日总结.mp4',
        '1-2 课堂笔记的创建.mp4',
        '1-15 Pycharm使用和破解（win系统）.mp4',
        '1-12 python解释器的安装（mac系统）.mp4',
        '1-13 python解释器的安装（win系统）.mp4',
        '1-8 Python介绍.mp4', '1-7 编程语言的分类.mp4',
        '1-3 常见计算机基本概念.mp4',
        '1-14 Pycharm使用和破解（mac系统）.mp4',
        '1-10 CPython解释器版本.mp4',
        '1-1 今日概要.mp4',
        '1-6 学习编程本质上的三件事.mp4',
        '1-18 作业答案和讲解.mp4',
        '1-4 编程语言.mp4',
        '1-11 环境搭建说明.mp4'
    ]
    result = sorted(data_list, key=lambda x: int(x.split(' ')[0].split("-")[-1]) )
    print(result)
    ```





## 4.推导式

推导式是Python中提供了一个非常方便的功能，可以让我们通过一行代码实现创建list、dict、tuple、set 的同时初始化一些值。

请创建一个列表，并在列表中初始化：0、1、2、3、4、5、6、7、8、9...299 整数元素。

```python
data = []
for i in range(300):
    data.append(i)

data_list = [i for i in range(300)]
```

- 列表

  ```python
  num_list = [ i for i in range(10)] # [0,1,2,3,...,9]
  
  num_list = [ [i,i] for i in range(10)] #[[0,0],[1,1],...,[9,9]]
  
  num_list = [ [i,i] for i in range(10) if i > 6 ] # [[7,7],[8,8],[9,9]]
  
  num_list = [ i+100 for i in range(10) if i > 6 ] # [107,108,109]
  
  num_list = ["武沛齐-{}".format(i) for i in range(10) if i > 6] # ['武沛齐-7', '武沛齐-8', '武沛齐-9']
  ```

- 集合 (不可是列表,列表不可哈希, 元组,字符串,整型可以)

  ```python
  num_set = { i for i in range(10)}
  
  num_set = { (i,i,i) for i in range(10)}
  
  num_set = { (i,i,i) for i in range(10) if i>3}
  ```

- 字典

  ```python
  num_dict = { i:i for i in range(10)}  # {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9}
  
  num_dict = { i:100 for i in range(10)} # {0: 100, 1: 100, 2: 100, 3: 100, 4: 100, 5: 100, 6: 100, 7: 100, 8: 100, 9: 100}
  
  num_dict = { i:"root-{}".format(i) for i in range(10)} # {0: 'root-0', 1: 'root-1', 2: 'root-2', 3: 'root-3', 4: 'root-4', 5: 'root-5', 6: 'root-6', 7: 'root-7', 8: 'root-8', 9: 'root-9'}
  
  num_dict = { i:(i,11) for i in range(10)} # {0: (0, 11), 1: (1, 11), 2: (2, 11), 3: (3, 11), 4: (4, 11), 5: (5, 11), 6: (6, 11), 7: (7, 11), 8: (8, 11), 9: (9, 11)}
  
  num_dict = { i:(i,11) for i in range(10) if i>7} # {8: (8, 11), 9: (9, 11)}
  ```

- 元组，<span style="color:red">不同于其他类型。</span>

  ```python
  # 不会立即执行内部循环去生成数据，而是得到一个生成器。
  data = (i for i in range(10))
  print(data) # <generator object <genexpr> at 0x000000000215B318>
  for item in data:
      print(item)
  #
  0
  1
  2
  3
  4
  5
  6
  7
  8
  9
  
  ```



### 练习题

1. 去除列表中每个元素的 `.mp4`后缀。

   ```python
   data_list = [
       '1-5 编译器和解释器.mp4',
       '1-17 今日作业.mp4',
       '1-9 Python解释器种类.mp4',
       '1-16 今日总结.mp4',
       '1-2 课堂笔记的创建.mp4',
       '1-15 Pycharm使用和破解（win系统）.mp4',
       '1-12 python解释器的安装（mac系统）.mp4',
       '1-13 python解释器的安装（win系统）.mp4',
       '1-8 Python介绍.mp4', '1-7 编程语言的分类.mp4',
       '1-3 常见计算机基本概念.mp4',
       '1-14 Pycharm使用和破解（mac系统）.mp4',
       '1-10 CPython解释器版本.mp4',
       '1-1 今日概要.mp4',
       '1-6 学习编程本质上的三件事.mp4',
       '1-18 作业答案和讲解.mp4',
       '1-4 编程语言.mp4',
       '1-11 环境搭建说明.mp4'
   ]
   
   # 原来办法
   result = []
   for item in data_list:
       result.append(item.rsplit('.',1)[0])
   
   # 推导式
   result = [ item.rsplit('.',1)[0] for item in data_list]
   ```

2. 将字典中的元素按照 `键-值`格式化，并最终使用 `;`连接起来。

   ```python
   info = {
       "name":"武沛齐",
       "email":"xxx@live.com",
       "gender":"男",
   }
   
   # 原来办法
   data_list [] 
   for k,v in info.items():
       temp = "{}-{}".format(k,v)
       temp.append(data_list)
   resutl = ";".join(data)
   
   # 推导式
   result = ";".join( [ "{}-{}".format(k,v) for k,v in info.items()] )
   # k v分开写是为了分别用, 如果用item是生成元组
   ```

3. 将字典按照键从小到大排序，然后在按照如下格式拼接起来。（微信支付API内部处理需求）

   ```python
   info = {
       'sign_type': "MD5",
       'out_refund_no': "12323",
       'appid': 'wx55cca0b94f723dc7',
       'mch_id': '1526049051',
       'out_trade_no': "ffff",
       'nonce_str': "sdfdffd",
       'total_fee': 9901,
       'refund_fee': 10000
   }
   
   data = "&".join(["{}={}".format(key, value) for key, value in sorted(info.items(), key=lambda x: x[0])])
   print(data)
   ```

4. 看代码写结果

   ```python
   def func():
       print(123)
   
   
   data_list = [func for i in range(10)]
   
   print(data_list)
   
   # 未调用func函数,根本就不会执行
   
   data_list = [ lambda: 100 for i in range(10) ]
   print(data_list)
   # 未调用函数,依旧不执行
   ```

5. 看代码写结果

   ```python
   def func(num):
       return num + 100
   
   
   data_list = [func(i) for i in range(10)]
   
   print(data_list)
   
   # [100,101,...,109]
   ```

6. 看代码写结果（执行出错，通过他可以让你更好的理解执行过程）

   ```python
   def func(x):
       return x + i # 这个i读不到推导式(里面是一个作用域)里面的i
   
   data_list = [func for i in range(10)] # 列表推导式里面的i是这个作用域里面的i, 如果能读到,循环都已经完毕了,读data_list[任何值]都应该是9
   
   val = data_list[0](100)
   print(val)
   ```

7. 看代码写结果（新浪微博面试题）

   ```python
   data_list = [lambda x: x + i for i in range(10)]  # [函数,函数,函数]   循环完毕了i=9
   
   v1 = data_list[0](100)
   v2 = data_list[3](100)
   print(v1, v2)  # 109 109
   ```

   

### 小高级(开发不常见,面试常见)

1. 推导式支持嵌套

   ```python
   # 推导式
   data = [ i for i in range(10)]
   
   # 原始
   data = []
   for i in range(10):
       data.append(i)
   print(data)
   ```

   ```python
   data = [ (i,j) for j in range(5) for i in range(10)]
   
   data = []
   for i in range(10):
       for j in range(5):
           data.append( (i,j) )
   
   data = [ [i, j] for j in range(5) for i in range(10)]
   ```

   ```python
   # 一副扑克牌
   
   poker_list = [ (color,num) for num in range(1,14) for color in ["红桃", "黑桃", "方片", "梅花"]]
   
   poker_list = [ [color, num] for num in range(1, 14) for color in ["红桃", "黑桃", "方片", "梅花"]]
   
   print(poker_list)	
   ```

2. 烧脑面试题

   ```python
   def num():
       return [lambda x: i * x for i in range(4)] # 列表格式,是匿名函数
   
   
   # 1. num()并获取返回值  [函数,函数,函数,函数] i=3 函数体i * 3是不执行的
   # 2. for循环返回值
   # 3. 返回值的每个元素(2)
   result = [m(2) for m in num()]  # [6,6,6,6] m就代表num()上面的四个函数, 即四个函数的返回值 x是参数,传进来2,2* i-=2* 3 = 6  
   print(result)
   
   ```

   ```python
   def num():
       return (lambda x: i * x for i in range(4)) # 元组,生成器
   
   
   # 1. num()并获取返回值  生成器对象 (lambda x: i * x for i in range(4)) 循环一次生成一个函数
   # 2. for循环返回值 两个循环同时进行
   # 3. 返回值的每个元素(2)
   result = [m(2) for m in num()]  # [0,2,4,6 ]
   print(result)
   ```

   

## 总结

1. 匿名函数，基于lambda表达式实现一行创建一个函数。一般用于编写简单的函数。
2. 三元运算，用一行代码实现处理简单的条件判断和赋值。
3. 生成器，函数中如果yield关键字
   - 生成器函数
   - 生成器对象
   - 执行生成器函数中的代码
     - next
     - for（常用）
     - send
4. 内置函数（36个）
5. 推导式
   - 常规操作
   - 小高级操作

## 作业

1. 看代码写结果

   ```
   v = [ lambda :x  for x in range(10)] 
   print(v)
   print(v[0])
   print(v[0]())
   ```

2. 看代码写结果

   ```
   v = [i for i in range(10,0,-1) if i > 5]
   print(v)
   ```

3. 看代码写结果

   ```python
   data = [lambda x:x*i for i in range(10)]
   print(data)
   print(data[0](2))
   print(data[0](2) == data[8](2))
   ```

4. 请用列表推导式实现，踢出列表中的字符串，最终生成一个新的列表保存。

   ```python
   data_list = [11,22,33,"alex",455,'eirc']
   
   new_data_list = [ ... ] # 请在[]中补充代码实现。
   
   # 提示：可以用type判断类型
   ```

5. 请用列表推导式实现，对data_list中的每个元素判断，如果是字符串类型，则计算长度作为元素放在新列表的元素中；如果是整型，则让其值+100 作为元素放在新的列表的元素中。

   ```python
   data_list = [11,22,33,"alex",455,'eirc']
   
   new_data_list = [ ... ] # 请在[]中补充代码实现。
   
   # 提示：可以基于三元运算实现
   ```

6. 请使用字典推导式实现，将如果列表构造成指定格式字典.

   ```python
   data_list = [
       (1,'alex',19),
       (2,'老男',84),
       (3,'老女',73)
   ]
   
   # 请使用推导式将data_list构造生如下格式：
   """
   info_dict = {
       1:(1,'alex',19),
       2:(2,'老男',84),
       3:(3,'老女',73)
   }
   """
   ```

7. 有4个人玩扑克牌比大小，请对比字典中每个人的牌的大小，并输入优胜者的姓名（值大的胜利，不必考虑A）。

   ```python
   player = {
       "武沛齐":["红桃",10],
       "alex":["红桃",8],
       'eric':["黑桃",3],
       'killy':["梅花",12],
   }
   ```

8. 尽量多的列举你记得的内置函数？【能记住多少就写多少，不强制去背，在此尽权利写即可，这种公共后续用的多了就自然而然就记住了】

9. 请编写一个生成器函数实现生成n个斐波那契数列的值。

   - 什么是斐波那契数列？

     ```
     前两个数相加的结果，就是下一个数。
     1 1 2 3 5 8 13 21 34 55 ...
     ```

   - 代码结构示例，请在此基础上补充代码实现。

     ```python
     def fib(max_count):
         pass
     
     
     count = input("请输入要生成斐波那契数列的个数：")
     count = int(count)
     fib_generator = fib(count)
     for num in fib_generator:
         print(num) 
     ```

     

   



























































