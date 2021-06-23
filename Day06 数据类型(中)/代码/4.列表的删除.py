# 千万不要再循环的过程中,边循环获取列表数据,变删除列表的数据
'''
#错误的
user_list = ["刘的话", "范德彪", "刘华强", '刘尼古拉斯赵四', "宋小宝", "刘能"]
for item in user_list:
    if item.startswith("刘"):
        user_list.remove(item)

print(user_list)
'''

# 正确方式，倒着删除。
user_list = ["刘的话", "范德彪", "刘华强", '刘尼古拉斯赵四', "宋小宝", "刘能"]
for index in range(len(user_list) - 1, -1, -1):
    item = user_list[index]
    if item.startswith("刘"):
        user_list.remove(item)
print(user_list)