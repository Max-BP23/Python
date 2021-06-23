# 创建用户列表
#    用户列表应该长： [ ["alex","123"],["eric","666"] ]
# user_list = [["alex","123"],["eric","666"],]
# user_list.append(["alex","123"])
# user_list.append(["eric","666"])

# 方法一
'''
user_list = []
while True:
    user = input("请输入用户名(Q退出)：")
    if user == "Q":
        break
    pwd = input("请输入密码:")
    data = []
    data.append(user)
    data.append(pwd)
    user_list.append(data)
print(user_list)
'''
# 方法二 简便
user_list = []
while True:
    user = input("请输入用户名(Q退出):")
    if user == "Q":
        break
    pwd = input("请输入密码:")
    data = [user,pwd]  #直接创建列表
    user_list.append(data)
print(user_list)