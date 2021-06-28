## 作业

1. 请定义一个函数，用于计算一个字符串中字符`a`出现的次数并通过return返回。

   - 参数，字符串。

   - 返回值，字符串中 a 出现的次数。

     ```python
     def count():
         info = ""
         count = 0
         for items in info:
             if items == "a":
                 count += 1
         return()
     
     答案
     def char_count(text):
         count = 0
         for char in text:
             if char == 'a':
                 count += 1
         return count # 可以省略一个else:
     
     
     result = char_count("89alskdjf;auqkaaafasdfiojqln")
     print(result)
     ```

     

2. 写函数，判断用户传入的一个值（字符串或列表或元组任意）长度是否大于5，并返回真假。

   ```python
   def judge_lenth(data):
       if len(data) > 5:
           return True
       return False
   result = judge_lenth("123456max")
   print(result)
   
   答案
   def judge_length(data):
       if len(data) > 5:
           return True
       return False
   
   
   result = judge_length("武沛齐武沛齐")
   print(result)
   ```

   

3. 写函数，接收两个数字参数，返回比较大的那个数字（等于时返回两个中的任意一个都可以）。

   ```python
   def get_bigger(num1,num2):
       if num1 > num2:
           return num1
       return num2
   result = get_bigger(1,2)
   print(result)
   
   答案
   def get_bigger(num1, num2):
       if num1 > num2:
           return num1
       return num2
   
   
   result = get_bigger(11, 22)
   ```

   

4. 写函数，函数接收四个参数分别是：姓名，性别，年龄，学历，然后将这四个值通过"*"拼接起来并追加到一个student_msg.txt文件中。

   ```python
   def write_file(name, gender, age, degree):
       data_list = [name, gender, age, degree]
       data = "*".join(data_list)
       with open("student_msg.txt", mode="a", encoding="utf-8") as file_object:
           file_object.write(data)
   write_file("武沛齐", "男", "18", "博士")
   ```

   

5. 补充代码，实现如下功能：

   - 【位置1】读取文件中的每一行数据，将包含特定关键的数据筛选出来，并以列表的形式返回。
   - 【位置1】文件不存在，则返回None
   - 【位置2】文件不存在，输出 "文件不存在"，否则循环输出匹配成功的每一行数据。

   ```python
   import os
   
   def select_content(file_path,key):
       # 补充代码【位置1】
       if not os.path.exists(file_path):
           return
       data_list = []
       with open(file_path, mode="r", encoding="utf-8") as file_object:
           for line in file_object:
               if key in line:
                   data_list.append(line)
       return data_list
   result = select_content("files/xxx.txt", "股票")
   # 补充代码【位置2】 
   if result == None:
       print("文件不存在")
   else:
       print(result)
   ```

6. 补充代码，实现敏感词替换的功能。

   ```python
   def change_string(origin):
       # 补充代码，将字符串origin中中的敏感词替换为 **，最后将替换好的值返回。
       data_list = ["苍老师","波多老师","大桥"]
       for items in  data_list:
           origin = origin.replace(items,"**")
       return origin
   text = input("请输入内容：")
   result = change_string(text)
   print(result)
   ```

7. 基于函数实现用户认证，要求：

   - 写函数，读取的用户信息并构造为字典（用户信息存放在`files/user.xlsx`文件中）

     <img src="assets/image-20201220144654241.png" alt="image-20201220144654241" style="zoom:50%;" />

     ```python
     # 构造的字典格式如下
     user_dict = {
         "用户名":"密码"
         ...
     }
     ```

   - 用户输入用户名和密码，进行校验。（且密码都是密文，所以，需要将用户输入的密码进行加密，然后再与Excel中的密文密码进行比较）

     ```python
     import hashlib
     
     def encrypt(origin):
         origin_bytes = origin.encode('utf-8')
         md5_object = hashlib.md5()
         md5_object.update(origin_bytes)
         return md5_object.hexdigest()
     
     
     p1 = encrypt('admin')
     print(p1) # "21232f297a57a5a743894a0e4a801fc3"
     
     p2 = encrypt('123123')
     print(p2) # "4297f44b13955235245b2497399d7a93"
     
     p3 = encrypt('123456')
     print(p3) # "e10adc3949ba59abbe56e057f20f883e"
     ```


扩展：密码都不是明文。

- 注册京东，京东存储：用户名和密码（密文）

- 登录京东：用户名& 密码。

  ```python
  import hashlib
  from openpyxl import load_workbook
  
  
  def get_user_dict():
      user_dict = {}
      wb = load_workbook("files/user.xlsx")
      sheet = wb.worksheets[0]
      for row in sheet.rows:
          user_dict[row[1].value] = row[2].value
      return user_dict
  
  
  def encrypt(origin):
      origin_bytes = origin.encode('utf-8')
      md5_object = hashlib.md5()
      md5_object.update(origin_bytes)
      return md5_object.hexdigest()
  
  
  user = input("请输入用户名：")
  pwd = input("请输入密码：")
  
  encrypt_password = encrypt(pwd)
  
  user_dict = get_user_dict()
  
  db_password = user_dict.get(user)
  
  if encrypt_password == db_password:
      print("登录成功")
  else:
      print("登录失败")
  ```

  