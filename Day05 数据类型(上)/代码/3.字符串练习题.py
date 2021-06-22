# 1. 写代码实现判断用户输入的值否以 "al"开头,如果是则输出 "是的" 否则 输出 "不是的"
# data = input("请输入:")
# result = data.startswith("al")
# if result is True:
#     print("是的")
# else:
#     print("不是的")
"""
data = input("请输入内容：")
if data.startswith("al"):
    print("是的")
else:
    print("不是的")
"""

# 2. 写代码实现判断用户输入的值否以"Nb"结尾,如果是则输出 "是的" 否则 输出 "不是的"
# data = input("请输入:")
# result = data.endswith("Nb")
# if result is True:
#     print("是的")
# else:
#     print("不是的")
"""
data = input("请输入内容：")
if data.endswith("al"):
    print("是的")
else:
    print("不是的")
"""

# 3. 将 name 变量对应的值中的 所有的"l"替换为 "p",并输出结果
# data = input("请输入:")
# v1 = data.replace("l","p")
# print(v1)
"""
name = "alex"
result = name.replace("l",'p')
print(result)
"""

# 4. 写代码实现对用户输入的值判断，是否为整数，如果是则转换为整型并输出，否则直接输出"请输入数字"
# data = input("请输入:")
# v1 = data.isdecimal()
# if v1 is True:
#     print(v1)
# else:
#     print("请输入数字")
"""
data = input("请输入内容：")
if data.isdecimal():
    data = int(data)
    print(data)
else:
    print("请输入数字")
"""

# 5. 对用户输入的数据使用"+"切割，判断输入的值是否都是数字？
#    提示：用户输入的格式必须是以下+连接的格式，如 5+9 、alex+999
# data = input("请输入数据:")
# data_list = data.split("+")
# print(data_list)
# result1 = data_list[0].isdecimal()
# result2 = data_list[1].isdecimal()
# print(result1)
# print(result2)
"""
data = input("请输入内容：")
num_list = data.split("+", 1)  # ["5","9"]
if num_list[0].isdecimal() and num_list[1].isdecimal():
    print("都是整数")
else:
    print("不全是整数")
"""

# 6. 写代码实现一个整数加法计算器(两个数相加)
#    需求：提示用户输入：5+9或5+9或5+9，计算出两个值的和（提示：先分割再转换为整型，再相加）
# data = input("请输入两个数,输入类型为5+9或5+9或5+9:")
# data_list = data.split("+")
# result = int(data_list[0]) + int(data_list[1])
# print(result)
"""
data = input("请输入内容：")
num_list = data.split("+", 1)  # ["5","9"]
if num_list[0].isdecimal() and num_list[1].isdecimal():
    v1 = int(num_list[0])
    v2 = int(num_list[1])
    result = v1 + v2
    print(result)
else:
    print("用户输入有问题")
"""

# 7. 写代码实现一个整数加法计算器(两个数相加)
#    需求：提示用户输入：5 +9或5+ 9或5 + 9，计算出两个值的和（提示：先分割再去除空白、再转换为整型，再相加）
# data = input("请输入两个数,输入类型为5 +9或5+ 9或5 + 9:")
# data1 = data.strip()
# data_list = data1.split("+")
# result = int(data_list[0]) + int(data_list[1])
# print(result)
"""
data = input("请输入内容：")
num_list = data.split("+", 1)  # ["5","9"]
v1 = int(num_list[0].strip())  # "5"  "5 "  " 5 "
v2 = int(num_list[1].strip())
result = v1 + v2
print(result)
"""
# 8. 补充代码实现用户认证。
#    需求：提示用户输入手机号、验证码，全都验证通过之后才算登录成功（验证码大小写不敏感）
'''
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
'''


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




# 9.补充代码实现数据拼接
'''
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
'''

"""
data_list = []
while True:
    hobby = input("请输入你的爱好（Q/q退出）：")
    if hobby.upper() == 'Q':
        break
    # 把输入的值添加到 data_list 中，如：data_list = ["小姨子","哥们的女朋友"]
    data_list.append(hobby)

result = "、".join(data_list)
print(result)
"""