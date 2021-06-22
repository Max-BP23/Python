"""
message = "来做点py交易呀"
index = 0
while index < len(message):
    value = message[index]
    print(value)
    index += 1
"""
# message = "来做点py交易呀"
# index = len(message) - 1
# while index >=0:
#     value = message[index]
#     print(value)
#     index -= 1

# message = "来做点py交易呀"
# value = message[:3] + "Python" + message[5:]
# print(value)

name = "生活不是电影，生活比电影苦"
print( name[ 0:5:2 ] )   # 输出：生不电 【前两个值表示区间范围，最有一个值表示步长】
print( name[ :8:2 ] )    # 输出：生不电，  【区间范围的前面不写则表示起始范围为0开始】
print( name[ 2::3 ] )    # 输出：不影活影 【区间范围的后面不写则表示结束范围为最后】
print( name[ ::2 ] )     # 输出：生不电，活电苦 【区间范围不写表示整个字符串】
print( name[ 8:1:-1 ] )  # 输出：活生，影电是不 【倒序】

print(name[8:1:-1])  # 输出：活生，影电是不 【倒序】
print(name[-1:1:-1])  # 输出：苦影电比活生，影电是不 【倒序】
# 面试题：给你一个字符串，请将这个字符串翻转。
value = name[-1::-1]
print(value)  # 苦影电比活生，影电是不活生

#循环
# for i in range(5):
#     print(i)# 0 1 2 3 4
#     for j in range(3):
#         print(j) # 0 1 2  # 0 1 2  # 0 1 2  # 0 1 2  # 0 1 2

for i in range(5):
    print(i)# 0 1 2 3 4
    for j in range(3):
        break #下面的数据本来要打印,如果加了break,永远无法执行第二个循环,下面数据也就不打印
        print(j) # 0 1 2  # 0 1 2  # 0 1 2  # 0 1 2  # 0 1 2

data_list = ["alex","eric",999]
data = str(data_list) #数据本身就是一个字符串
print(data) # '["alex","eric",999]'