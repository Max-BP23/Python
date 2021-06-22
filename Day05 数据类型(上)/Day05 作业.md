# 1.GitHub静态博客

教程:https://segmentfault.com/a/1190000020210216

网址:https://github.com/Max-BP23/max-bp23.github.io.git

位置:C:\Users\Administrator\.ssh

里面信息:ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQC2ryV/3nTzuwajr0B5roqdnjKtk4Eza7ZRdnZHuq8pvOGMeQqUCWrzX8TCEyGjygOoXsNGgwh6do3H3nW/5pLRwyYOWlAeELqpG2qqmygPhoVLJEb9/A/+8IP+FZzGaGC1o9g2DE+qP703SCcDbFEt7NyGDLsqUbmGwUdzGLlt36zIikIxS2f9LOHNpOIeukOSYv0ckjZ6n/zbIJ1dHeR+hQfgbJEg466Ok1ordwFh/Q1s7LmieuC/yJToa+Rcts236hm7ztwNj+U6NzokNOU/OfjW499+n+jwkeahCXrVtC6RIh4fQdo+CsHWzuyqrO8V74XgSnD5QT2d0jCckqIh+ZPJlfnxw1QJnq1hu+kghvW8kXoxjsFAM9VvlhGuELoMtWn/Drvotm4wl95ku8SKCUTYdfV2dF1nDACZ8a1dA3Zyptjp7JqpuegdG4VtNcSoMKlX7Sg3T6TWhG5iaCkHeyspFww+KNr3f7zngcwqHBL+cYjTRLb0dF8U7U4KRRE= email@email.com

# 2.字符串练习题

1. 写代码实现判断用户输入的值否以 "al"开头,如果是则输出 "是的" 否则 输出 "不是的"

   ```python
   data = input("请输入:")
   result = data.startswith("al")
   if result is True:
       print("是的")
   else:
       print("不是的")
       
       
   #标准答案
   data = input("请输入内容：")
   if data.startswith("al"):
       print("是的")
   else:
       print("不是的")
   ```

   

2. 写代码实现判断用户输入的值否以"Nb"结尾,如果是则输出 "是的" 否则 输出 "不是的"

   ```python
   data = input("请输入:")
   result = data.endswith("Nb")
   if result is True:
       print("是的")
   else:
       print("不是的")
       
   #标准答案
   data = input("请输入内容：")
   if data.endswith("al"):
       print("是的")
   else:
       print("不是的")
   ```

   

3. 将 name 变量对应的值中的 所有的"l"替换为 "p",并输出结果

   ```python
   data = input("请输入:")
   v1 = data.replace("l","p")
   print(v1)
   
   #标准答案
   name = "alex"
   result = name.replace("l",'p')
   print(result)
   ```

   

4. 写代码实现对用户输入的值判断，是否为整数，如果是则转换为整型并输出，否则直接输出"请输入数字"

   ```python
   data = input("请输入:")
   v1 = data.isdecimal()
   if v1 is True:
       print(v1)
   else:
       print("请输入数字")
   
   #标准答案
   data = input("请输入内容：")
   if data.isdecimal():
       data = int(data)
       print(data)
   else:
       print("请输入数字")
   ```

   

5. 对用户输入的数据使用"+"切割，判断输入的值是否都是数字？
   提示：用户输入的格式必须是以下+连接的格式，如 5+9 、alex+999

   ```python
   data = input("请输入数据:")
   data_list = data.split("+")
   print(data_list)
   result1 = data_list[0].isdecimal()
   result2 = data_list[1].isdecimal()
   print(result1)
   print(result2)
   
   #正确答案
   data = input("请输入内容：")
   num_list = data.split("+", 1)  # ["5","9"]
   if num_list[0].isdecimal() and num_list[1].isdecimal():
       print("都是整数")
   else:
       print("不全是整数")
   ```

   

6. 写代码实现一个整数加法计算器(两个数相加)
   需求：提示用户输入：5+9或5+9或5+9，计算出两个值的和（提示：先分割再转换为整型，再相加）

   ```python
   data = input("请输入两个数,输入类型为：5+9或5+9或5+9:")
   data_list = data.split("+")
   result = int(data_list[0]) + int(data_list[1])
   print(result)
   
   #正确答案
   data = input("请输入内容：")
   num_list = data.split("+", 1)  # ["5","9"]
   if num_list[0].isdecimal() and num_list[1].isdecimal():
       v1 = int(num_list[0])
       v2 = int(num_list[1])
       result = v1 + v2
       print(result)
   else:
       print("用户输入有问题")
   ```

   

7. 写代码实现一个整数加法计算器(两个数相加)
   需求：提示用户输入：5 +9或5+ 9或5 + 9，计算出两个值的和（提示：先分割再去除空白、再转换为整型，再相加）

   ```python
   data = input("请输入两个数,输入类型为5 +9或5+ 9或5 + 9:")
   data1 = data.strip()
   data_list = data1.split("+")
   result = int(data_list[0]) + int(data_list[1])
   print(result)
   
   #标准答案
   data = input("请输入内容：")
   num_list = data.split("+", 1)  # ["5","9"]
   v1 = int(num_list[0].strip())  # "5"  "5 "  " 5 "
   v2 = int(num_list[1].strip())
   result = v1 + v2
   print(result)
   ```

   

8. 补充代码实现用户认证。
   需求：提示用户输入手机号、验证码，全都验证通过之后才算登录成功（验证码大小写不敏感）

```python
import random
code = random.randrange(1000,9999) # 生成动态验证码
msg = "欢迎登录PythonAV系统，您的验证码为：{},手机号为：{}".format(code,"15131266666")
print(msg)
# 请补充代码

```

```python
#错误---
phone = input("请输入您的手机号:")
import random
code = random.randrange(1000,9999) # 生成动态验证码
print("你的验证码为".join(code))
data = input("请输入手机号+验证码:")
data1 = data.strip("+")
if data1[0] == "15131266666" and data1[1] == code1:
    msg = "欢迎登录PythonAV系统，您的验证码为：{},手机号为：{}".format(code1,"15131266666")
    print(msg)
else:
    print("输入有误")
    
#正确答案
import random

code = random.randrange(1000, 9999)  # 生成动态验证码，整型
code = str(code)  # 字符串类型
msg = "欢迎登录PythonAV系统，您的验证码为：{},手机号为：{}".format(code, "15131266666")

phone = input("请输入手机号：")
data = input("请输入验证码：")  # 字符串类型
if code.upper() == data.upper() and phone == "15131266666":
    print("登录成功")
else:
    print("登录失败")
```



9.补充代码实现数据拼接

```python
data_list = []
while True:
    hobby = input("请输入你的爱好（Q/q退出）：")
    if hobby.upper() == 'Q':
        break
    # 把输入的值添加到 data_list 中，如：data_list = ["小姨子","哥们的女朋友"]
    data_list.append(hobby) 
    # 将所有的爱好通过符号 "、"拼接起来并输出
```

```python
#错误
data_list = []
while True:
    hobby = input("请输入你的爱好（Q/q退出）：")
    if hobby.upper() == 'Q':
        break
    # 把输入的值添加到 data_list 中，如：data_list = ["小姨子","哥们的女朋友"]
        list = data_list.append(hobby)
        result = "、".join(list)
    # 将所有的爱好通过符号 "、"拼接起来并输出
print(result)

#正确答案
data_list = []
while True:
    hobby = input("请输入你的爱好（Q/q退出）：")
    if hobby.upper() == 'Q':
        break
    # 把输入的值添加到 data_list 中，如：data_list = ["小姨子","哥们的女朋友"]
    data_list.append(hobby)

result = "、".join(data_list)
print(result)


```

# 3.今日作业

1. 请用代码实现如下进制的转换。

   ```python
   v1 = 675          # 请将v1转换为二进制（字符串类型）。 #0b1010100011
   
   v2 = "0b11000101" # 请将二进制v2转换为十进制（整型） #197
   
   v3 = "11000101"   # 请将二进制v3转换为十进制（整型） #197
   ```

   ```python
   print(bin(v1))
   print(int("0b11000101",base=2))
   print(int("11000101",base=2))
   ```

   

2. 按要求实现

   > 现有 `v1=123` 和 `v2=456`，请将这两个值转换为二进制，并将其二进制中的前缀 0b 去掉，然后将两个二进制拼接起来，最终再转换为整型（十进制）。
   >
   > 例如：
   >
   > ​		123  对应二进制为  "0b1111011" ，去除前缀0b之后的二进制为 "1111011"
   >
   > ​		456  对应二进制为  "0b111001000" ，去除前缀0b之后的二进制为 "111001000"
   >
   > ​		将两个二进制拼接起来的值为："1111011111001000"，再将此值转换为整型为：63432
   >
   > ```python
   > v1 = 123
   > v2 = 456
   > data1 = bin(v1)[2:]
   > data2 = bin(v2)[2:]
   > print(data1)
   > print(data2)
   > s1 = data1 + data2
   > print(s1)
   > print(int("1111011111001000",base=2))
   > ```
   >
   > 

3. 按要求实现

   > 现有 `v1=123` 和 `v2=456`，请将这两个值转换为二进制，并将其二进制中的前缀 0b 去掉，再补足为2个字节（16位），然后将两个二进制拼接起来，最终再转换为整型（十进制）。
   >
   > 例如：
   >
   > ​		123  对应二进制为  "0b1111011" ，去除前缀0b之后的二进制为 "1111011" ，补足16位为  "00000000 01111011"
   >
   > ​		456  对应二进制为  "0b111001000" ，去除前缀0b之后的二进制为 "111001000"，，补足16位为  "00000001 11001000"
   >
   > ​		将两个二进制拼接起来的值为："00000000 0111101100000001 11001000"，再将此值转换为整型为：8061384
   >
   > ```python
   > v1 = 123
   > v2 = 456
   > data1 = bin(v1)[2:].zfill(16)
   > data2 = bin(v2)[2:].zfill(16)
   > print(data1)
   > print(data2)
   > s1 = data1 + data2
   > print(int(s1,base=2))
   > ```
   >
   > 

4. 列举你了解的那些数据类型的值转换为布尔值为False。

   ```python
   v1 = bool(0)
   v2 = bool("")
   print(v1)
   print(v2)
   
   # 正确答案
   空、0转换布尔值都是False
   ```

   

5. 看代码写结果：

   ```python
   if "":
       print(123)
   else:
       print(456)  #456
   ```

   ```python
   if 0:
       print(999)
   else:
       print(666) #666
   ```

   ```python
   if "武沛齐":
       print(345)  #345
   else:
       print(110)
   ```

6. 让用户输入一段文本，请实现将文本中的敏感词 `苍老师`、`波波老师`替换为 `***`，最后并输入替换后的文本。

   ```python
   data = input("请输入内容:")
   data1 = data.replace("苍老师","***")
   data2 = data1.replace("波波老师","***")
   print(data2)
   ```

   

7. 有变量name = "aleX leNb " 完成如下操作： 

   - 1)移除 name 变量对应的值两边的空格,并输出处理结果

   - 2)判断 name 变量是否以 "al" 开头,并输出结果（用切片 或 startswith实现）

   - 3)判断name变量是否以"Nb"结尾,并输出结果（用切片 或 endswith实现）

   - 4)将 name 变量对应的值中的 所有的"l" 替换为 "p",并输出结果 

   - 5)将 name 变量对应的值根据 所有的"l" 分割,并输出结果

   - 6)将name变量对应的值根据第一个"l"分割,并输出结果

   - 7)将 name 变量对应的值变大写,并输出结果

   - 8)将 name 变量对应的值变小写,并输出结果

     ```python
     # 1)
     name = "aleX leNb "
     data1 = name.strip()
     print(data1)
     # 2)
     name = "aleX leNb "
     data2 = name.startswith("al")
     print(data2)
     # 3)
     name = "aleX leNb "
     data3 = name.endswith("Nb")
     print(data3)
     # 4)
     name = "aleX leNb "
     data4 = name.replace("l","p")
     print(data4)
     # 5)
     name = "aleX leNb "
     data5 = name.split("l")
     print(data5)
     # 6)
     name = "aleX leNb "
     data6 = name.split("l",1)
     print(data6)
     # 7)
     name = "aleX leNb "
     data7 = name.upper()
     print(data7)
     # 8)
     name = "aleX leNb "
     data8 = name.lower()
     print(data8)
     
     ```

     ```python
     
     # 答案
     name = "aleX leNb "
     print(name.strip())
     
     print(name.startswith("al"))
     print(name[0:2] == "al")
     
     print(name.endswith("Nb"))
     print(name[-2:] == "Nb")
     
     v1 = name.replace("l", "p")
     print(v1)
     
     v2 = name.split("l")
     print(v2)  # ['a', 'eX ', 'eNb ']
     
     v3 = name.split("l", 1)
     print(v3)  # ['a', 'eX leNb ']
     
     print(name.upper())
     print(name.lower())
     ```

     

8. 如何实现字符串的翻转？

   ```python 
   data = "我喜欢墨"
   print(data[-1::-1])
   ```

   

9. 有字符串s = "123a4b5c"

   - 通过对s切片形成新的字符串 "123"

   - 通过对s切片形成新的字符串 "a4b"

   - 通过对s切片形成字符串 "c"

   - 通过对s切片形成字符串 "ba2"

     ```python 
     s = "123a4b5c"
     print(s[0:3])
     print(s[3:6])
     print(s[7:])  #print(len(s)-1)
     print(s[-3::-2])
     ```

     

10. 使用while循环实现对字符串 message = "伤情最是晚凉天，憔悴厮人不堪言" 中每个字符进行输出。

    ```python 
    message = "伤情最是晚凉天，憔悴厮人不堪言"
    s = 0
    while s < len(message):
        print(message[s])
        s += 1
    ```

    

11. 使用for循环实现对字符串 message = "伤情最是晚凉天，憔悴厮人不堪言" 中每个字符进行输出。

    ```python
    message = "伤情最是晚凉天，憔悴厮人不堪言"
    for i in message:
        print(i)
    ```

    

12. 使用for循环和range实现对字符串 message = "伤情最是晚凉天，憔悴厮人不堪言" 中每个字符进行倒叙输出。

    ```python
    message = "伤情最是晚凉天，憔悴厮人不堪言"
    s = message[-1::-1]
    for i in s:
        print(i)
        
    # 方法二
    message = "伤情最是晚凉天，憔悴厮人不堪言"
    for index in range(len(message)-1,-1,-1):
        print(message[index])
    #range(start, stop(娶不到)), step])
    ```

    

13. 使用for循环实现输出倒计时效果，例如：输出内容依次是："倒计时3秒"，"倒计时2秒"，"倒计时1秒"。

    ```python
    s = "321"
    for i in s:
        print("倒计时" + i + "秒")
    #方法二
    for num in range(3, 0, -1):  # [3,2,1]
        text = "倒计时{}秒".format(num)
        print(text)
    ```

    

14. 让用户输入一段文本，请计算文本中 "浪" 出现的次数，并输入结果。

    ```python 
    # 可能是错的,只输出,没计数
    text = input("请输入:")
    for i in text:
        if i == "浪":
            print(i)
            
    # 答案:
    text = input("请输入一段文本：") # 阿士大夫埃里克森打发斯蒂芬
    count = 0
    for item in text:
        if item == "浪":
            count += 1
    print(count)
    ```

    

15. 获取用户两次输入的内容，并提取其中的数字，然后实现数字的相加（转换为整型再相加）：

    ```python
    """
    要求：
    	将num1中的的所有数字找到并拼接起来：1232312
    	将num1中的的所有数字找到并拼接起来：1218323
    	然后将两个数字进行相加。
    """
    num1 = input("请输入：") # asdfd123sf2312
    num2 = input("请输入：") # a12dfd183sf23
    # 请补充代码
    ```

    ```python
    # 无共通性
    num1 = input("请输入：") # asdfd123sf2312
    num2 = input("请输入：") # a12dfd183sf23
    s1 = num1[5:8] + num1[10:]
    print(s1)
    s2 = num2[1:3] + num2[6:9] + num2[11:]
    print(s2)
    s = int(s1) + int(s2)
    print(s)
    ```

    ```python
    # 方法一
    num1 = input("请输入：") # asdfd123sf2312
    num1_list = []
    for i1 in num1:
        if i1.isdecimal():
            num1_list.append(i1)
    data1 = "".join(num1_list)
    print(data1)
    
    num2 = input("请输入：") # a12dfd183sf23
    num2_list = []
    for i2 in num2:
        if i2.isdecimal():
            num2_list.append(i2)
    data2 = "".join(num2_list)
    print(data2)
    
    print(int(data1) + int(data2))
    
    
    # 方法二
    num1 = input("请输入：") # asdfd123sf2312
    item1 = ""
    for i1 in num1:
        if i1.isdecimal():
            item1 += i1
    print(item1)
    
    num2 = input("请输入：") # a12dfd183sf23
    item2 = ""
    for i2 in num2:
        if i2.isdecimal():
            item2 += i2
    print(item2)
    
    print(int(item1) + int(item2))
    ```

    

