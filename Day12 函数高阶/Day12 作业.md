# Day12 作业

1. 请为以下所有函数编写一个装饰器，添加上装饰器后可以实现：执行func时，先执行func函数内部代码，再输出 "after"

   ```python
   import functools
   
   def outer(function):
       @functools.wraps(function)
       def inner(*args, **kwargs):
           res = function(*args, **kwargs)
           print("after")
           return res
       return inner
       
   @outer
   def func(a1):
       return a1 + "傻叉"
   @outer
   def base(a1,a2):
       return a1 + a2 + '傻缺'
   
   @outer
   def foo(a1,a2,a3,a4):
       return a1 + a2 + a3 + a4 + '傻蛋'
   ```

2. 请为以下所有函数编写一个装饰器，添加上装饰器后可以实现：将被装饰的函数执行5次，讲每次执行函数的结果按照顺序放到列表中，最终返回列表。

   ```python
   import functools
   import random 
   
   def five_times(function):
       @functools.wraps(function)
       def inner (*args,**kwargs):
           data_list = []
           for i in range(5):
               res = function(*args,**kwargs)
               data_list.append(res)
           return data_list
       return inner
   @five_times
   def func():
       return random.randint(1,4)
   
   result = func() # 内部自动执行5次，并将每次执行的结果追加到列表最终返回给result
   print(result) 
   ```

3. 请为以下函数编写一个装饰器，添加上装饰器后可以实现： 检查文件所在路径（文件件）是否存在，如果不存在自动创建文件夹（保证写入文件不报错）。(不会)

   ```python
   import os
   import functools
   
   def gard(function):
       @function.wraps(function)
       def inner(path):
           # 获取路径上的上级目录
           folder_path = os.path.dirname(path)
           
           # 不存在就创建
           if not os.path.exist(folder_path):
               os.makedirs(folder_path)
           res = function(path)
       	return res
       return inner
   @gard
   def write_user_info(path):
       file_obj = open(path, mode='w', encoding='utf-8')
       file_obj.write("武沛齐")
       file_obj.close()
   
   write_user_info('/usr/bin/xxx/xxx.png')
   ```

4. 分析代码写结果：

   ```python
   def get_data():
       scores = []
   
       def inner(val):
           scores.append(val)
           print(scores)
   
       return inner
   
   
   func = get_data()
   
   func(10) # [10]
   func(20) # [10,20]
   func(30) # [10,20,30]
   ```

5. 看代码写结果

   ```python
   name = "武沛齐"
   
   
   def foo():
       print(name)
   
   
   def func():
       name = "root"
       foo()
   
   
   func() # 武沛齐
   ```

6. 看代码写结果

   ```python
   name = "武沛齐"
   
   
   def func():
       name = "root"
   
       def foo():
           print(name)
   
       foo()
   
   
   func() # root
   ```

7. 看代码写结果

   ```python
   def func(val):
       def inner(a1, a2):
           return a1 + a2 + val
   
       return inner
   
   
   data_list = []
   
   for i in range(10):
       data_list.append(  func(i)   )
   
   print(data_list) # 10个inner函数
   ```

8. 看代码写结果

```python
def func(val):
    def inner(a1, a2):
        return a1 + a2 + val

    return inner


data_list = []

for i in range(10):
    data_list.append(func(i))

# data_list是inner函数列表
v1 = data_list[0](11,22) # 11+22+0
v2 = data_list[2](33,11) # 33+11+2

print(v1) # 33
print(v2) 
```

