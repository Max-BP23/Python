# 1.列表阶段作业

1. 写代码，有如下列表，按照要求实现每一个功能。

   ```python
   li = ["alex", "WuSir", "ritian", "barry", "武沛齐"]
   ```

   - 计算列表的长度并输出

   - 列表中追加元素"seven",并输出添加后的列表

   - 请在列表的第1个索引位置插入元素"Tony",并输出添加后的列表

   - 请修改列表第2个索引位置的元素为"Kelly",并输出修改后的列表

   - 请将列表的第3个位置的值改成 "妖怪"，并输出修改后的列表

   - 请将列表 `data=[1,"a",3,4,"heart"]` 的每一个元素追加到列表 `li` 中，并输出添加后的列表

   - 请将字符串 `s = "qwert"`的每一个元素到列表 `li` 中。

   - 请删除列表中的元素"barry",并输出添加后的列表

   - 请删除列表中的第2个元素，并输出删除元素后的列表

   - 请删除列表中的第2至第4个元素，并输出删除元素后的列表

     ```python
     print(len(li))
     
     li.append("seven")
     print(li)
     
     li.insert(1,"Tony")
     print(li)
     
     li[2] = "Kelly"
     print(li)
     
     li[3] = "妖怪"
     print(li)
     
     data=[1,"a",3,4,"heart"]
     li.extend(data)
     print(li)
     
     #方法一
     s = "qwert"
     for item in s:
         li.append(item)
     print(li)
     #方法二
     s = "qwert"
     li.extend(s)
     print(li)
     
     #方法一
     del li[-2]
     print(li)
     #方法二
     ele = li.pop(1)
     print(li)
     
     del li[2]
     print(li)
     
     del li[2:4]
     print(li)
     ```
     
     

2. 写代码，有如下列表，利用切片实现每一个功能

   ```python
   li = [1, 3, 2, "a", 4, "b", 5,"c"]
   ```

   - 通过对li列表的切片形成新的列表 [1,3,2]

   - 通过对li列表的切片形成新的列表 ["a",4,"b"] 

   - 通过对li列表的切片形成新的列表  [1,2,4,5]

   - 通过对li列表的切片形成新的列表 [3,"a","b"]

   - 通过对li列表的切片形成新的列表 [3,"a","b","c"]

   - 通过对li列表的切片形成新的列表  ["c"]

   - 通过对li列表的切片形成新的列表 ["b","a",3]

     ```python
     print(li[:3])
     
     print(li[3:6])
     
     print(li[::2])
     
     print(li[1:6:2])
     
     print(li[1::2])
     
     print(li[-1])
     
     print(li[-3:0:-2])
     ```

     

3. 写代码，有如下列表，按照要求实现每一个功能。

   ```python
   lis = [2, 3, "k", ["qwe", 20, ["k1", ["tt", 3, "1"]], 89], "ab", "adv"]
   ```

   - 将列表lis中的第2个索引位置的值变成大写，并打印列表。

   - 将列表中的数字3变成字符串"100"

   - 将列表中的字符串"tt"变成数字 101

   - 在 "qwe"前面插入字符串："火车头"

     ```python
     #方法一
     data = lis[2].upper()
     lis[2] = data
     print(lis)
     #方法二
     lis[2] = lis[2].upper()
     print(lis)
     
     lis[1] = "100"
     lis[3][2][1][1] = "100"
     print(lis)
     
     lis[3][2][1][0] = 101 #是数字不是字符串
     print(lis)
     
     lis[3].insert(0,"火车头")
     print(lis)
     ```

     

4. 请用代码实现循环输出元素和值：users = ["武沛齐","景女神","肖大侠"] ，如：

   ```python
   0 武沛齐
   1 景女神
   2 肖大侠
   ```

   ```python
   #方法一
   users = ["武沛齐","景女神","肖大侠"]
   for index in range(len(users)):
       print(index,users[index])
       
   #方法二
   users = ["武沛齐","景女神","肖大侠"]
   count = 0
   for item in users:
       print(count,item)
       count += 1
   ```

   

5. 请用代码实现循环输出元素和值：users = ["武沛齐","景女神","肖大侠"] ，如：

   ```python
   1 武沛齐
   2 景女神
   3 肖大侠
   ```

   ```python
   users = ["武沛齐","景女神","肖大侠"]
   for index in range(len(users)):
       print(index+1,users[index])
   ```

   

6. 写代码实现以下功能

   - 如有变量 goods = ['汽车','飞机','火箭'] 提示用户可供选择的商品：

     ```python
     0,汽车
     1,飞机
     2,火箭
     ```

   - 用户输入索引后，将指定商品的内容拼接打印，如：用户输入0，则打印 您选择的商品是汽车。

     ```python
     goods = ['汽车','飞机','火箭']
     for index in range(len(goods)):
         print(index,goods[index])
     index = int(input("请输入序号:"))
     text = goods[index]
     message = "您选择的商品是{}".format(text)
     print(message)
     ```

     

7. 利用for循环和range 找出 0 ~ 50 以内能被3整除的数，并追加到一个列表。

   ```python
   # 自己未考虑0
   list = []
   for index in range(0,51): #左取右不取,所有右边应该是51
       if index%3 == 0:
           list.append(index)
   print(list)
   
   # 修改后
   list = []
   for index in range(0,51):
       if index == 0:
           continue
       if index%3 == 0:
           list.append(index)
   print(list)
   
   #标准答案:
   data_list = []
   for num in range(0,51):
       if num == 0:
           continue
       # 是否能被3整除呢？
       data = num % 3
       if data == 0:
           data_list.append(num)
   print(data_list) 
   ```

   

8. 利用for循环和range 找出 0 ~ 50 以内能被3整除的数，并插入到列表的第0个索引位置，最终结果如下：

   ```python
   [48,45,42...] #理解了,只是结果的例子,不是让把数据插在这个表的0位置
   ```

   ```python
   list = [48,45,42]
   list1 = []
   for index in range(0,50):
       if index == 0:
           continue
       if index%3 == 0:
           list1.append(index)
   list.insert(0,list1)
   print(list) #结果[[3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48], 48, 45, 42]
   
   #答案的意思是每个元素每次都添加到0,倒着
   data_list = []
   for num in range(0,51):
       if num == 0:
           continue
       data = num % 3
       if data == 0:
           data_list.insert(0,num)
   print(data_list) #结果[48, 45, 42, 39, 36, 33, 30, 27, 24, 21, 18, 15, 12, 9, 6, 3]
   
   ```

   

9. 查找列表li中的元素，移除每个元素的空格，并找出以"a"开头，并添加到一个新列表中,最后循环打印这个新列表。

   ```python
   li = ["alexC", "AbC ", "egon", " riTiAn", "WuSir", "  aqc"]
   ```

   ```python
   li = ["alexC", "AbC ", "egon", " riTiAn", "WuSir", "  aqc"]
   list = []
   for index in li:
       item = index.strip()
       if item.startswith("a"):
           list.append(item)
   print(list)
   
   
   #方法二
   data_list = []
   li = ["alexC", "AbC ", "egon", " riTiAn", "WuSir", "  aqc"]
   for item in li:
       data = item.strip()
       if not data.startswith("a"):
           continue
       data_list.append(data)  #注意这个添加的缩进
   print(data_list)
   ```

   

10. 将以下车牌中所有 `京 `的车牌搞到一个列表中，并输出京牌车辆的数量。

    ```python
    data = ["京1231", "冀8899", "京166631", "晋989"]
    ```

    ```python
    data = ["京1231", "冀8899", "京166631", "晋989"]
    list = []
    for index in data:
        if index.startswith("京"):
            list.append(index)
    text = "一共有{}辆京牌车,车号为{}".format(len(list),list)
    print(text)
    
    #得到京牌数据,可以按照如下
    for item in data:
        if not item.startswith("京"):
            continue
        result.append(item)
    ```

# 2.元组作业

1. 以下哪些数据类型转换为布尔值为False

   ```python
   0  # False
   1  #True
   "" #False
   -19 #True
   [] #False
   [11,22] #True
   (1) #True
   (1,2,3) #True
   () #False
   ```

   

2. 运算符操作

   ```python
   v1 = [] or "alex" # ([],"alex")  --- 写错了,忽略了and or的计算 正确答案 "alex"
   v2 = [11,22] and (1,2,) #([11,22],(1,2,))
   #正确答案 (1,2,)
   ```

   

3. 比较：` a = [1,2,3] `和 `b = [(1),(2),(3) ]` 以及 `c = [(1,),(2,),(3,) ]` 的区别？

   ```python
   # a是列表,里面是整型
   # b是列表,里面是整型
   # C是列表,里面是元组
   a = [1, 2, 3]
   b = [(1), (2), (3)]
   c = [(1,), (2,), (3,)]
   ```

   

4. 将字符串`text = "wupeiqi|alex|eric"`根据 `|` 分割为列表，然后列表转换为元组类型。

   ```python
   text = "wupeiqi|alex|eric"
   data = text.split("|")
   result = tuple(data)
   print(result) # ('wupeiqi', 'alex', 'eric')
   
   
   ```

   

5. 根据如下规则创建一副扑克牌（排除大小王）。

```python
# 花色列表
color_list = ["红桃","黑桃","方片","梅花"]

# 牌值
num_list = []
for num in range(1,14):
    num_list.append(num)
    
result = []
# 请根据以上的花色和牌值创建一副扑克牌（排除大小王）
# 最终result的结果格式为： [ ("红桃",1), ("红桃",2) ... ]
```

```python
# 花色列表
color_list = ["红桃", "黑桃", "方片", "梅花"]

# 牌值
num_list = []
result = []
for num in range(1, 14):
    num_list.append(num)
    for color in color_list:
        poker = (color, num)
        result.append(poker)
print(result)


#答案
num_list = []  # 1 2 3 4 5...11、12、13
for num in range(1, 14):
    num_list.append(num)

result = []
# 请根据以上的花色和牌值创建一副扑克牌（排除大小王）
# 最终result的结果格式为： [ ("红桃",1), ("红桃",2) ... ]
for color in color_list:
    # print(color) # 红桃
    for num in num_list:  #l
        item = (color, num,)
        result.append(item)
print(result)

```



