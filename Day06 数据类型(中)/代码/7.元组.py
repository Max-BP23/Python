# 1.将字符串`text = "wupeiqi|alex|eric"`根据 `|` 分割为列表，然后列表转换为元组类型。
'''
text = "wupeiqi|alex|eric"
data = text.split("|")
result = tuple(data)
print(result)
'''

# 2.根据如下规则创建一副扑克牌（排除大小王）。
# 请根据以上的花色和牌值创建一副扑克牌（排除大小王）
# 最终result的结果格式为： [ ("红桃",1), ("红桃",2) ... ]
# 花色列表
color_list = ["红桃", "黑桃", "方片", "梅花"]

# 牌值
num_list = []
result = []
for num in range(1, 14):
    num_list.append(num)
    for color in color_list:
        poker = (color, num)
        result.append(poker)
print(result)

