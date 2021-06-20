# 1.输出练习题

1. 使用print输出自己的姓名

```python
Print("马梦利")
```

2. 使用print输出
   春眠不觉晓，
   出处闻啼鸟，
   夜来风雨声，
   花落知多少。

```python
print("""春眠不觉晓,
出处闻啼鸟,
夜来风雨声,
花落知多少.""")


```

3. 是用print输出
   春眠不觉晓，出处闻啼鸟，夜来风雨声，花落知多少。

```python
print("春眠不觉晓,出处闻啼鸟,夜来风雨声,花落知多少.")
```

# 2.数据类型转换练习题

1. 计算整型50乘以10再除以5的商并使用print输出。

   ```python
   print(50 * 10 / 5) 结果100
   ```

   

2. 判断整型8是否大于10的结果并使用print输出。

   ```python
   print(8 > 10) 结果 FALSE
   ```

   

3. 计算整型30除以2得到的余数并使用print输出。

   ```python
   print(30 % 2) 结果 0
   ```

   

4. 使用字符串乘法实现 把字符串”我爱我的祖国”创建三遍并拼接起来最终使用print输出。

   ```python
   print(3 * "我爱我的祖国") 结果我爱我的祖国我爱我的祖国我爱我的祖国
   ```

   

5. 判断 字符串”wupeiqi”和”alex”是否相等的结果并使用print输出。

   ```python
   print("wupeiqi" == "alex") 结果 FALSE
   ```

   

6. 判断 整型666和整型666是否相等的结果并使用print输出。

   ```python
   print(666 == 666) 结果 TRUE
   ```

   

7. 判断 字符串”666”和整型666是否相等的结果并使用print输出。

   ```python
   print(str(666) == 666) 结果 FALSE
   ```

   

8. 看代码写结果（禁止运行代码）：

   ```python
   print( int("100")*3 ) -- 300
   print( int("123") + int("88") ) -- 211
   print( str(111) + str(222) ) -- 111222
   print( str(111)*3 ) -- 111111111
   print( int("8") > 7 ) -- TRUE
   print( str(111) == 111 ) -- FALSE
   print( bool(-1) ) -- TRUE
   print( bool(0) ) -- FALSE
   print( bool("") ) -- FALSE 
   print( bool("你好") ) -- TRUE
   print( True == True)  -- TRUE
   print( True == False)  -- FALSE
   print( bool("") == bool(0) ) -- TRUE
   
   输出结果:
   300
   211
   111222
   111111111
   True
   False
   True
   False
   False
   True
   True
   False
   True
   
   
   ```

注意：类型转换不是改变原来值，实际在底层是新创建了一个值。例如有整数 6 ，然后使用 str(6) 转化了一下得到 “6”,实际上这个字符串”6”是依据整数6新创建的。

# 3.变量命名练习题

name = "吉诺比利"
name0 = "帕克"
name_1 = "邓肯"
_coach = "波波维奇"
_ = "卡哇伊"
1_year = "1990" **# 错误**
year_1_ = "1990"
_1_year = "1990"
nba-team = "马刺" **# 错误**
new*name = "伦纳德" **# 错误**

# 4.基础条件语句练习题

1. 提示用户输入用户名和密码，用户名等于"wupeiqi"且密码等于"uuu"就输出登录成功；否则输出登录失败。

   ```python
   username = input("请输入用户名:")
   password = input("请输入密码:")
   if username == "wupeiqi" and password == "uuu":
   	print("登录成功")
   else:
       print("登陆失败")
   ```

   

2. 猜数字，提示用户输入一个数字，判断数字如果大于10，就输出猜错了；否则输出猜对了。

   ```python
   guess_number = input("请输入一个数字:")
   if int(guess_number) > 10:
       print("猜错了")
   else:
       print("猜对了")
       
   ```

   

3. 提示用户输入一个数字，判断是否为偶数，是偶数则输出 偶偶偶数，否则输出 奇奇奇数。

   ```python
   guess_number = input("请输入一个数字:")
   if int(guess_number) % 2 == 0:
       print("偶偶偶数")
   else:
       print("奇奇奇数")
       
   ```

   

# 5.day02 整体作业

1. 谈谈你了解的编码以及为什么会出现乱码的现象？

   ```
   文件保存时的编码和打开的编码不一致,导致无法读取
   
   编码种类有: utf-8, gbk
   
   标准答案:
   编码相当于是一个`密码本`，其中存储着文字和01010的对应关系。
   乱码的出现时因为文件的存储方式和打开方式不一致导致。另外，如何数据丢失也可能会造成乱码。
   假如：
   	武，对应存储的是：100100001000000111。如果文件中的内容丢失只剩下100100001000000，则读取时候就可能出现乱码。
   ```

   

2. Python解释器默认编码是什么？如何修改？

   ```
   utf-8
   
   修改的话: # -*- coding:gbk -*-
   
   标准答案
   Python解释器默认编码：utf-8
   在文件的顶部通过设置： # -*- coding:编码 -*- 实现修改。
   ```

   

3. 用print打印出下面内容：

   ```
   ⽂能提笔安天下,
   武能上⻢定乾坤.
   ⼼存谋略何⼈胜,
   古今英雄唯是君。
   
   答:
   print("""
   ⽂能提笔安天下,
   武能上⻢定乾坤.
   ⼼存谋略何⼈胜,
   古今英雄唯是君。
   """)
   
   标准答案:
   答案1:
   print("⽂能提笔安天下,")
   print("武能上⻢定乾坤.")
   print("⼼存谋略何⼈胜,")
   print("古今英雄唯是君。")
   
   答案2:
   text = """
   ⽂能提笔安天下,
   武能上⻢定乾坤.
   ⼼存谋略何⼈胜,
   古今英雄唯是君。
   """
   print(text)
   ```

4. 变量名的命名规范和建议？

   ```
   三个要求:
   1.只能是字母,数字,下划线
   2.开头不能是数字
   3.不能是python的内置关键字
   
   建议:
   见名知意
   下划线连接命名(小写)
   ```

   

5. 如下那个变量名是正确的？

   ```pythonn
   name = '武沛齐' #正确
   _ = 'alex'  #正确
   _9 = "老男孩"  #正确
   9name = "宝浪"  #错误
   oldboy(edu = 666  #错误
   ```

6. 设定一个理想数字比如：66，让用户输入数字，如果比66大，则显示猜测的结果大了；如果比66小，则显示猜测的结果小了;只有等于66，显示猜测结果正确。

   ```python
   number = 66
   guess_number = input("请输入数字:")
   if int(guess_number) > number:
       print("猜大了")
   elif int(guess_number) < number:
       print("猜小了")
   else:
       print("结果正确")    
   
   ```

   

7. 提示⽤户输入 "爸爸" ，判断⽤户输入的对不对。如果对, 提示真聪明, 如果不对, 提示你是傻逼么。

   ```python
   content = input("请输入内容")
   if content == "爸爸":
       print("真聪明")
   else:
       print("你是傻逼么")
   ```

   

8. 写程序，成绩有ABCDE5个等级，与分数的对应关系如下.

   ```python
   A    90-100
   B    80-89
   C    60-79
   D    40-59
   E    0-39
   ```

   要求用户输入0-100的数字后，你能正确打印他的对应成绩等级.

   ```python
   score = int(input("请输入你的成绩:"))
   if 90 <= score <= 100:
       print("A")
   elif 80 <= score <= 89:
       print("B")
   elif 60 <= score <= 79:
       print("C")
   elif 40 <= score <= 59:
       print("D")
   elif 0 <= score <= 39:
       print("E")
   else:
       print("输入有误")
       
   另外一种形式:
   score = input("请输入分数")
   data = int(score)
   
   if data >= 90 and data <= 100:
     print("A")
   elif data >= 80 and data <90:
     print("B")
   elif data >= 60 and data <80:
     print("C")
   elif data >= 40 and data <60:
     print("D")
   elif data >= 0 and data <40:
     print("E")
   else:
     print("输入错误")
   ```

   