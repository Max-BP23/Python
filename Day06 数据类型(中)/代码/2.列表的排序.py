# num_list = [11, 22, 4, 5, 11, 99, 88]
# print(num_list)
# num_list.sort() #让num_list从小到大排序
# print(num_list)
# num_list.sort(reverse=True) #让num_list从大到小排序
# print(num_list)

user_list = ["王宝强", "Ab陈羽凡", "Alex", "贾乃亮", "贾乃", "1"]
print(user_list)
'''
sort 排序原理
按照对应的Unicode编码的大小,位置一一对比


'''
user_list.sort()
print(user_list)

user_list = ["范德彪", "刘华强", '尼古拉斯赵四']
user_list[-10000:1] = [11, 22, 33, 44]
print(user_list) # 输出 [11, 22, 33, 44, '刘华强', '尼古拉斯赵四']

