# 1.匿名函数 练习题

根据函数写写出其匿名函数的表达方式

```python
def func(a1,a2):
    return a1 + a2

func = lambda a1,a2: a1+a2
```

```python
def func(data):
    return data.replace("苍老师","***")

func= lambda data: data.replace("苍老师","***")
```

```python
def func(data):
    name_list = data.replace(".")
    return name_list[-1]

func = lambda data: data.replace(".")[-1]
```

在编写匿名函数时，由于受限 函数体只能写一行，所以匿名函数只能处理非常简单的功能



# 2.推导式

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
   
   result = []
   for item in data_list:
       result.append(item.rsplit('.',1)[0])
       
   result = [ item.rsplit('.',1)[0] for item in data_list]
   ```

2. 将字典中的元素按照 `键-值`格式化，并最终使用 `;`连接起来。

   ```python
   info = {
       "name":"武沛齐",
       "email":"xxx@live.com",
       "gender":"男",
   }
   
   data_list [] 
   for k,v in info.items():
       temp = "{}-{}".format(k,v)
       temp.append(data_list)
   resutl = ";".join(data)
   
   result = ";".join( [ "{}-{}".format(k,v) for k,v in info.items()] )
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
   ```

5. 看代码写结果

   ```python
   def func(num):
       return num + 100
   
   
   data_list = [func(i) for i in range(10)]
   
   print(data_list)
   ```

6. 看代码写结果（执行出错，通过他可以让你更好的理解执行过程）

   ```python
   def func(x):
       return x + i
   
   data_list = [func for i in range(10)]
   
   val = data_list[0](100)
   print(val)
   ```

7. 看代码写结果（新浪微博面试题）

   ```python
   data_list = [lambda x: x + i for i in range(10)]  # [函数,函数,函数]   i=9
   
   v1 = data_list[0](100)
   v2 = data_list[3](100)
   print(v1, v2)  # 109 109
   ```

   # 3.推导式补充

   

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

   # 4.今日作业

   1. 看代码写结果

      ```python
      v = [ lambda :x  for x in range(10)] 
      print(v)  # [0,1,2,...,9] 错了,这个是10个函数[函数,函数,...,函数]
      print(v[0]) # 9  第一个函数
      print(v[0]()) # 9
      ```

   2. 看代码写结果

      ```python
      v = [i for i in range(10,0,-1) if i > 5]
      print(v) # 9,8,7,6 错误,是列表且从10开始 [10, 9, 8, 7, 6]
      ```

   3. 看代码写结果

      ```python
      data = [lambda x:x*i for i in range(10)]
      print(data) # 10个函数
      print(data[0](2)) # 18
      print(data[0](2) == data[8](2)) # True
      ```

   4. 请用列表推导式实现，踢出列表中的字符串，最终生成一个新的列表保存。

      ```python
      data_list = [11,22,33,"alex",455,'eirc']
      
      new_data_list = [ ... ] # 请在[]中补充代码实现。
      
      # 提示：可以用type判断类型
      
      
      # 我的想法
      '''
      data_list = [11, 22, 33, "alex", 455, 'eirc']
      
      new_data_list = [data_list.pop(str(item) == True) for item in data_list]  # 请在[]中补充代码实现。
      print(new_data_list) # [11, 22, 33] 不太对
      # 提示：可以用type判断类型
      '''
      
      #正确答案
      data_list = [11, 22, 33, "alex", 455, 'eirc']
      
      new_data_list = [item for item in data_list if type(item) == int]  # 请在[]中补充代码实现。
      print(new_data_list) # [11, 22, 33, 455]
      ```

   5. 请用列表推导式实现，对data_list中的每个元素判断，如果是字符串类型，则计算长度作为元素放在新列表的元素中；如果是整型，则让其值+100 作为元素放在新的列表的元素中。

      ```python
      data_list = [11,22,33,"alex",455,'eirc']
      
      new_data_list = [ ... ] # 请在[]中补充代码实现。
      
      # 提示：可以基于三元运算实现
      
      ##参考了下答案, 我用了append和str(item) == True,错误
      data_list = [11, 22, 33, "alex", 455, 'eirc']
      
      new_data_list = [len(item) if type(item) == str else item + 100 for item in
          data_list]  # 请在[]中补充代码实现。
      # 提示：可以基于三元运算实现
      print(new_data_list)
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
      
      # 我的想法
      info_dict = {i + 1: items  for i in range(3) for items in data_list}
      print(info_dict)
      
      # 正确答案
      info_dict = {item[0]: item for item in data_list}
      print(info_dict)
      ```

   7. 有4个人玩扑克牌比大小，请对比字典中每个人的牌的大小，并输入优胜者的姓名（值大的胜利，不必考虑A）。

      ```python
      player = {
          "武沛齐":["红桃",10],
          "alex":["红桃",8],
          'eric':["黑桃",3],
          'killy':["梅花",12],
      }
      
      # 
      winner = sorted(player.items(),key=lambda x:x[1][-1],reverse=True)[0]
      print(winner)
      data = sorted(player.items(),key=lambda x:x[1][-1])[-1][0]
      print(data)
      ```

   8. 尽量多的列举你记得的内置函数？【能记住多少就写多少，不强制去背，在此尽权利写即可，这种公共后续用的多了就自然而然就记住了】

      ```python
      bin oct hex
      max min any all
      sum abs round 
      input print len range type open
      str int float tuple set dict list bool
      ```

      

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

        