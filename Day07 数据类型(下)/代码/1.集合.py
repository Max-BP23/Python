# 1.写代码实现
v1 = {'alex','武sir','肖大'}
v2 = []
# 循环提示用户输入，如果输入值在v1中存在，则追加到v2中，如果v1中不存在，则添加到v1中。（如果输入N或n则停止循环）
'''
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
'''

#2.模拟用户信息录入程序，已录入则不再创建。
'''
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
'''
#3.给列表去重
v = [11,22,11,22,44455]
data= set(v)
result = list(data)
print(result)