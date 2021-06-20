# 1.while循环练习题

1. 补充代码实现
   猜数字，设定一个理想数字比如：66，一直提示让用户输入数字，如果比66大，则显示猜测的结果大了；如果比66小，则显示猜测的结果小了;只有输入等于66，显示猜测结果正确，然后退出循环。

   ```python
   num = 66
   flag = True
   print("开始")
   while flag:
       guess_num = int(input("请输入数字:"))
       if guess_num > num:
           print("猜大了")
       elif guess_num < num:
           print("猜小了")
       else:
           print("猜测正确")
           flag = False
   print("结束")
   ```

2. 使用循环输出1~100所有整数。

   ```python
   方法一
   num = 1
   print("开始")
   while num < 101:
       print(num)
       num = num+1
   print("结束")
   
   方法二:
   num = 1
   print("开始")
   while num:
       if num < 101:
           print(num)
           num = num+1
       else:
           num = False
           print("over")
   print("结束")
   ```

   

3. 使用循环输出 1 2 3 4 5 6   8 9 10，即：10以内除7以外的整数。

   ```python
   方法一
   num = 1
   print("开始")
   while num < 11:
       if num == 7:
           pass
       else:
           print(num)
       num = num + 1
      
   方法二
   num = 1
   print("开始")
   while num < 11:
       if num != 7:
           print(num)
       num = num + 1 #和if缩进一样
   ```

   

4. 输出 1~100 内的所有奇数。

   ```python
   num = 1
   print("开始")
   while num < 101:
       if num%2 == 1:
           print(num)
       num = num+1
   print("结束")
   ```

   

5. 输出 1~100 内的所有偶数。

   ```python
   num = 1
   print("开始")
   while num < 101:
       if num%2 == 0:
           print(num)
       num = num+1
   print("结束")
   ```

   

6. 求 1~100 的所有整数的和。

   ```python
   total = 0 #0+1/0+1+2/0+1+2+3
   num = 1
   print("开始")
   while num < 101:
       total = total + num
       num = num+1
   print(total)
   print("结束")
   ```

   

7. 输出10 ~ 1 所有整数。

   ```python
   num = 10
   while num > 0:
       print(num)
       num = num - 1
   ```

8. 思考题 求100以内整数这样的结果:1-2+3-4+5-6...=?

   ```python
   total = 0
   num = 1
   print("开始")
   while num < 101:
       if num%2 == 1:
           total = total + num
       else:
           total = total - num
       num = num+1
   print(total)
   print("结束")
   ```

   

# 2.and or面试题

```python
v1 = 1 or 2 #1
v2 = -1 or 3 #-1
v3 = 0 or -1 # -1
v4 = 0 or 100 #100
v5 = "" or 10 # 10
v6 = "wupeiqi" or "" #wupeiqi
v7 = 0 or "" #""

print(v1,v2,v3,v4,v5,v6,v7)

# or，看第一个值，如果第一个值为真，结果就应该是第一个值，否则就结果就是第二个值。
```

```python
v1 = 4 and 8 #8
v2 = 0 and 6 # 0
v3 = -1 and 88 #88
v4 = "" and 7 #""
v5 = "武沛齐" and "" #""
v6 = "" and 0 #""
v7 = 0 and "中国" #0

print(v1,v2,v3,v4,v5,v6,v7)

# and，看第一个值，如果第一个值真，结果就应该是第二个值，否则结果就是第一个值。
```

```python
# 如果多个and 和or的情况，先计算and再计算or.
v1 = 0 or 4 and 3 or 7 or 9 and 6
     #0 or 3 or 7 or 9 and 6
     #0 or 3 or 7 or 6
     #3 or 7 or 6
     #3 or 6
     #3
v2 = 8 or 3 and 4 or 2 and 0 or 9 and 7
		 #8
  
  
v3 = 0 or 2 and 3 and 4 or 6 and 0 or 3
		 #4
 
```

```python
# 先计算not，在计算and，最后计算or
v4 = not 8 or 3 and 4 or 2
		 #4
```

# 3.今日作业

1. 判断下列逻辑语句的True,False

   ```python
   1 > 1 or 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6
   # F or T or F or F --- F  正确答案 T 理解
   not 2 > 1 and 3 < 4 or 4 > 5 and 2 > 1 and 9 > 8 or 7 < 6
   # not T and F or F and T and T or F  --- F
   ```

2. 求出下列逻辑语句的值。

   ```python
   8 or 3 and 4 or 2 and 0 or 9 and 7
   # 8
   0 or 2 and 3 and 4 or 6 and 0 or 3
   # 4
   ```

3. 下列结果是什么？

   ```python
   6 or 2 > 1 #6
   3 or 2 > 1 #3
   0 or 5 < 4 #F
   5 < 4 or 3 #3
   2 > 1 or 6 #T
   3 and 2 > 1 #T
   0 and 3 > 1 #0
   2 > 1 and 3 #3
   3 > 1 and 0 #0
   3 > 1 and 2 or 2 < 3 and 3 and 4 or 3 > 2 
   #2 or 4 or T -- 4  正确答案2 理解
   ```

4. 实现用户登录系统，并且要支持连续三次输错之后直接退出，并且在每次输错误时显示剩余错误次数（提示：使⽤字符串格式化）。

   ```python
   方法一
   print("开始")
   i = 1 #或者i=0 下面i<3, format是4-i
   while i < 4:
       i += 1
       user = input("请输入用户名:")
       pwd = input("请输入密码:")
       if user == "wupeiqi" and pwd == "luffy":
           print("成功")
           break
       else:
           message = "用户名或者密码错误,剩余错误次数为{}次".format(4 - i)
           print(message)
   
   方法二
   i=3
   while i>0: #这边需要设置大于了
       i -= 1
       user = input("请输入用户名:")
       pwd = input("请输入密码:")
       if user == "wupeiqi" and pwd == "luffy":
           print("成功")
           break
       else:
           message = "用户名或者密码错误,剩余错误次数为{}次".format(i)
       print(message)
   ```

   

5. 猜年龄游戏 
   要求：允许用户最多尝试3次，3次都没猜对的话，就直接退出，如果猜对了，打印恭喜信息并退出。

   ```python
   i = 0
   while i < 3:
       i += 1
       age = int(input("请输入年龄:"))
       if age == 73:
           print("恭喜你猜对了")
           break
       else:
           print("猜错了")
   print("程序结束")
   ```

   

6. 猜年龄游戏升级版
   要求：允许用户最多尝试3次，每尝试3次后，如果还没猜对，就问用户是否还想继续玩，如果回答Y，就继续让其猜3次，以此往复，如果回答N，就退出程序，如何猜对了，就直接退出。

   ```python
   i = 0
   while i < 3:
       i += 1
       age = input("请输入年龄:")
       if age == 73:
           print("猜对了")
           break
       else:
           print("猜错了")
   
       if i == 3:
           choice = input("请问会否还想继续玩?请输入Y or N:")
           if choice == "N":
               break
           elif choice == "Y":
               i = 0
               continue
           else:
               print("输入有误")
   
   print("程序结束")
   ```

   

