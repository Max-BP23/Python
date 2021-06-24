# 案例1：
'''
user_list = {
    "wupeiqi": "123",
    "alex": "uk87",
}

username = input("请输入用户名：")
password = input("请输入密码：")
# None，用户名不存在
# 密码，接下来比较密码
pwd = user_list.get(username)

if pwd == None:
    print("用户名不存在")
else:
    if password == pwd:
        print("登录成功")
    else:
        print("密码错误")
'''
'''
user_list = {
    "wupeiqi": "123",
    "alex": "uk87",
}

username = input("请输入用户名：")
password = input("请输入密码：")
# None，用户名不存在
# 密码，接下来比较密码
pwd = user_list.get(username)

if pwd:
    if password == pwd:
        print("登录成功")
    else:
        print("密码错误")
else:
    print("用户名不存在")
'''

# 字典练习题
""" 
结合下面的两个变量 header 和 stock_dict实现注意输出股票信息，格式如下：
	SH601778，股票名称:中国晶科、当前价:6.29、涨跌额:+1.92。
    SH688566，股票名称:吉贝尔、当前价:...               。
	...
"""
'''
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
'''
'''
info = {"age": 12, "status": True, "name": "武沛齐"}
# 输出info.items()获取到的 dict_items([ ('age', 12),  ('status', True),  ('name', 'wupeiqi'),  ('email', 'xx@live.com')  ])
v1 = ("age", 12) in info.items()
print(v1)
'''
'''
info = {"age": 12, "status": True, "name": "武沛齐"}
if "age" in info:

    # del info["age"]
    data = info.pop("age")
    print(info)
    print(data)
else:
    print("键不存在")
'''
dic = {
    'name': '汪峰',
    'age': 48,
    'wife': [{'name': '国际章', 'age': 38}, {'name': '李杰', 'age': 48}],
    'children': ['第一个娃', '第二个娃']
}

# 1. 获取汪峰的妻子名字
d1 = dic['wife'][0]['name']
print(d1)
# 2. 获取汪峰的孩子们
d2 = dic['children']
print(d2)
# 3. 获取汪峰的第一个孩子
d3 = dic['children'][0]
print(d3)
# 4. 汪峰的媳妇姓名变更为 章子怡
dic['wife'][0]['name'] = "章子怡"
print(dic)
# 5. 汪峰再娶一任妻子
dic['wife'].append( {"name":"铁锤","age":19} )
print(dic)

# 6. 给汪峰添加一个爱好：吹牛逼
dic['hobby'] = "吹牛逼"
print(dic)
# 7. 删除汪峰的年龄
del dic['age']
	# 或
	# dic.pop('age')
	# print(dic)