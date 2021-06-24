# 1.集合作业

1.写代码实现

循环提示用户输入，如果输入值在v1中存在，则追加到v2中，如果v1中不存在，则添加到v1中。（如果输入N或n则停止循环）

```python
v1 = {'alex','武sir','肖大'}
v2 = []

# 循环提示用户输入，如果输入值在v1中存在，则追加到v2中，如果v1中不存在，则添加到v1中。（如果输入N或n则停止循环）
while True:
    name = input("请输入姓名(N/n退出)：")
    if name.upper() == "Q":
        break
    if name in v1:
        v2.append(name)
	else:
        v1.add(name)
        print(v1)
    print(v2)
```

2.下面那些值不能做集合的元素

```python
""
0
[11,22,33]   # 不能
[]           # 不能
(123)
{1,2,3}      # 不能
```

3.模拟用户信息录入程序，已录入则不再创建。

```python
user_info_set = set()

while True:
    name = input("请输入姓名：")
    age = input("请输入年龄：")
    item = (name,age,)
    if item in user_info_set:
        print("该用户已录入")
    else:
        user_info_set.add(item)
        print(user_info_set)
```

4.给列表去重

```python
v = [11,22,11,22,44455]
data = set(v) # {11,22,44455}
result = list(data) # [11,22,44455]
print(result)
```

# 2.字典作业

```python
# 练习题
""" 
结合下面的两个变量 header 和 stock_dict实现注意输出股票信息，格式如下：
	SH601778，股票名称:中国晶科、当前价:6.29、涨跌额:+1.92。
    SH688566，股票名称:吉贝尔、当前价:...               。
	...
"""
header = ['股票名称', '当前价', '涨跌额']

stock_dict = {
    'SH601778': ['中国晶科', '6.29', '+1.92'], 
    'SH688566': ['吉贝尔', '52.66', '+6.96'], 
    'SH688268': ['华特气体', '88.80', '+11.72'], 
    'SH600734': ['实达集团', '2.60', '+0.24']
}
```

```python
header = ['股票名称', '当前价', '涨跌额']

stock_dict = {
    'SH601778': ['中国晶科', '6.29', '+1.92'],
    'SH688566': ['吉贝尔', '52.66', '+6.96'],
    'SH688268': ['华特气体', '88.80', '+11.72'],
    'SH600734': ['实达集团', '2.60', '+0.24']
}
for key, value in stock_dict.items():
    # print(key, value)  # 'SH601778': ['中国晶科', '6.29', '+1.92'],
    text_list = []
    for index in range(len(value)):
        text = "{}:{}".format(header[index],value[index]) #先实现后面股票名称当前价等的一一对应
        text_list.append(text)
    data = "、".join(text_list) #股票名称:中国晶科、当前价:6.29、涨跌额:+1.92
    result = "{},{}。".format(key,data)
    print(result)
```

# 3.今日作业

1. 根据需求写代码

   ```python
   dic = {'k1': "v1", "k2": "v2", "k3": [11,22,33]}
   
   # 请在字典中添加一个键值对，"k4": "v4"，输出添加后的字典
   # 请在修改字典中 "k1" 对应的值为 "alex"，输出修改后的字典
   # 请在k3对应的值中追加一个元素 44，输出修改后的字典
   # 请在k3对应的值的第 1 个位置插入个元素 18，输出修改后的字典
   ```

   ```python
   dic.update({"k4":"v4"})
   print(dic)
   
   dic.update({"k1":"alex"})
   print(dic)
   
   dic["k3"].append(44)
   print(dic)
   
   dic["k3"].insert(1,18)
   print(dic)
   
   #注意：不要用Python内置的一些变量或者函数int/float/bool/str/list/tuple/set/dict
   ```

   

2. 根据需求写代码

   ```python
   dic1 = {
    'name':['alex',2,3,5],
    'job':'teacher',
    'oldboy':{'alex':['python1','python2',100]}
   }
   
   # 1，将name对应的列表追加⼀个元素’wusir’。
   # 2，将name对应的列表中的alex全变成大写。
   # 3，oldboy对应的字典加⼀个键值对’⽼男孩’:’linux’。
   # 4，将oldboy对应的字典中的alex对应的列表中的python2删除
   ```

   ```python
   dic1["name"].append("wusir")
   print(dic1)
   
   new_name = dic1["name"][0].upper()
   dic1["name"][0] = new_name
   print(dic1)
   
   dic1["oldboy"]["老男孩"] = "linux"
   print(dic1)
   
   dic1["oldboy"]["alex"].remove("python2")
   print(dic1)
   
   ```

   

3. 循环提示用户输入，并将输入内容添加到字典中（如果输入N或n则停止循环）

   ```python
   例如：用户输入 x1|wupeiqi ,则需要再字典中添加键值对 {'x1':"wupeiqi"}
   ```

   ```python
   info = {}
   while True:
    text = input("请输入内容(Q/q退出):")  #x1|wupeiqi
    if text.upper() == "Q":
     break
    data_list = text.split("|") #["x1","wupeiqi"]
    info[data_list[0]] = data_list[1]
   #print(data_list[0]) 为了知道上面的俩相等为啥可以成为字典
   #print(data_list[1]) 为了知道上面的俩相等为啥可以成为字典
   print(info)
   ```

   

4. 判断以下值那个能做字典的key ？那个能做集合的元素？

   - 1 

   - -1

   - ""

   - None

   - [1,2]

   - (1,)

   - {11,22,33,4}

   - {'name':'wupeiq','age':18}

     ```python
     #字典的键必须可哈希,以下不可以
     [1,2]
     {11,22,33,4}
     {'name':'wupeiq','age':18}
     ```
     
     
   
5. 将字典的键和值分别追加到 key_list 和 value_list 两个列表中，如：

   ```python
   key_list = []
   value_list = []
   info = {'k1':'v1','k2':'v2','k3':'v3'}
   ```

   ```python
   key_list = []
   value_list = []
   info = {'k1':'v1','k2':'v2','k3':'v3'}
   for key,value in info.items():
    key_list.append(key)
    value_list.append(value)
   print(key_list)
   print(value_list)
   ```

   

6. 字典dic = {'k1': "v1", "k2": "v2", "k3": [11,22,33]}

   ```python
   a. 请循环输出所有的key
   b. 请循环输出所有的value
   c. 请循环输出所有的key和value
   ```

   ```python
   dic = {'k1': "v1", "k2": "v2", "k3": [11,22,33]}
   for key in dic.keys():
    print(key)
   
   for value in dic.values():
    print(value)
   
   for key,value in dic.items():
    print(key,value)
   ```

   

7. 请循环打印k2对应的值中的每个元素。

   ```python
   info = {
       'k1':'v1',
       'k2':[('alex'),('wupeiqi'),('oldboy')],
   }
   ```

   ```python
   info = {
       'k1':'v1',
       'k2':[('alex'),('wupeiqi'),('oldboy')],
   }
   for items in info['k2']:
    print(items)
   ```

   

8. 有字符串"k: 1|k1:2|k2:3  |k3 :4" 处理成字典 {'k':1,'k1':2....} 

   ```python
   #方法一
   '''
   result = {}
   text = "k: 1|k1:2|k2:3  |k3 :4"
   data_list = text.split("|")  #["k: 1","k1:2","k2:3  ","k3 :4"]
   for item in data_list:
    # item "k: 1"
    small_list = item.split(":") #["k"," 1"]
    result[ small_list[0] ] = int(small_list[1].strip())
   print(result)
   '''
   
   #小知识
   v = "k1:3"
   v1, v2 = v.split(":")  # ["k1","3"] 确定是2个值的话,可以直接定义两个变量分别等于分出来的值
   print(v1, v2) #k1 3
   #
   
   #方法二
   result = {}
   text = "k: 1|k1:2|k2:3  |k3 :4"
   data_list = text.split("|")  #["k: 1","k1:2","k2:3  ","k3 :4"]
   for item in data_list:
    key,value = item.split(":") #["k"," 1"]
    result[ key ] = int(value.strip())
   print(result)
   
   ```

   

9. 写代码

   ```python
   """
   有如下值 li= [11,22,33,44,55,66,77,88,99,90] ,将所有大于 66 的值保存至字典的第一个key对应的列表中，将小于 66 的值保存至第二个key对应的列表中。
   
      result = {'k1':[],'k2':[]}
   """
   ```

   ```python
   li= [11,22,33,44,55,66,77,88,99,90]
   result = {'k1':[],'k2':[]}
   for index in li:
    if index == 66:
     pass
    elif index > 66:
     result["k1"].append(index)
    else:
     result["k2"].append(index)
   print(result)
   
   #扩展 如果result里面不知道有没有k2这个键
   result = {}
   li = [11, 22, 33, 44, 55, 66, 77, 88, 99, 90]
   
   for item in li:
       if item > 66:
           if "k1" in result:
               result['k1'].append(item)
           else:
               result['k1'] = [item]
       elif item == 66:
           pass
       else:
           if "k2" in result:
               result['k2'].append(item)
           else:
               result['k2'] = [item]
   print(result)
   ```

   

10. 输出商品列表，用户输入序号，显示用户选中的商品

    ```python
    """
    商品列表：
      goods = [
    		{"name": "电脑", "price": 1999},
    		{"name": "鼠标", "price": 10},
    		{"name": "游艇", "price": 20},
    		{"name": "美女", "price": 998}
    	]
    要求:
    1：页面显示 序号 + 商品名称 + 商品价格，如：
          1 电脑 1999 
          2 鼠标 10
    	  ...
    2：用户输入选择的商品序号，然后打印商品名称及商品价格
    3：如果用户输入的商品序号有误，则提示输入有误，并重新输入。
    4：用户输入Q或者q，退出程序。
    """
    ```

    ```python
    #方法一
    for index in range(len(goods)):
     items = goods[index]
     print(index+1,items["name"],items["price"])
    
    while True:
     num = input("请输入您选的商品编号(Q/q退出)")
     if num.upper() == "Q":
      break
     if num.isdecimal():
      num = int(num)
      if 0 < num < 5:
       target_index = num - 1
       choice_item = goods[target_index]
       print(choice_item["name"], choice_item['price'])
      else:
       print("序号范围选择错误")
     else:
       print("用户输入的序号格式错误")
    
    #这是初级程序员会写且选择写的方式,非野生资深程序猿一般不这样写,嵌套太多了
    #准则：尽可能少if嵌套, 简单的逻辑先处理
    
    #方法二
    goods = [
        {"name": "电脑", "price": 1999},
        {"name": "鼠标", "price": 10},
        {"name": "游艇", "price": 20},
        {"name": "美女", "price": 998}
    ]
    for index in range(len(goods)):
        item = goods[index]
        print(index + 1, item['name'], item['price'])
    
    while True:
        num = input("请输入要选择的商品序号(Q/q)：")  # "1"
        if num.upper() == "Q":
            break
        if not num.isdecimal():
            print("用输入的格式错误")
            break
        num = int(num)
    
        if num > 4 or num < 0:
            print("范围选择错误")
            break
        target_index = num - 1
        choice_item = goods[target_index]
        print(choice_item["name"], choice_item['price'])
    ```
    
    
