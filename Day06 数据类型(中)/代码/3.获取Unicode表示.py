# data = "王宝强"
# data_list = []
# for char in data:
#     v1 = ord(char)  # 求对应Unicode代码表示
#     data_list.append(v1)
# print(data)
# print(data_list) #[29579, 23453, 24378]

user_list = ["范德彪","刘华强",'尼古拉斯赵四',"宋小宝","刘能"]
for index in range( len(user_list) ):#长度为5,index为0,1,2,3,4
    print(index)
    item = user_list[index] #获取索引的值
    print(item)