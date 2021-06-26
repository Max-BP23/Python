### 第一模块：Python基础（V2.0版）·第7章day7--数据类型（下）

**作业题目：**棋牌游戏11点

```
作业需求：
1、生成一副扑克牌（自己设计扑克牌的结构，小王和大王可以分别用14、15表示 ）

2、3个玩家(玩家也可以自己定义)
user_list = ["alex","武沛齐","李路飞"]

3、发牌规则
默认先给用户发一张牌，其中 J、Q、K、小王、大王代表的值为0.5，其他就是则就是当前的牌面值。
用户根据自己的情况判断是否继续要牌。
    要，则再给他发一张。（可以一直要牌，但是如果自己手中的牌总和超过11点，你的牌就爆掉了(牌面变成0)）
    不要，则开始给下个玩家发牌。（没有牌则则牌面默认是0）
如果用户手中的所有牌相加大于11，则表示爆了，此人的分数为0，并且自动开始给下个人发牌。

4、最终计算并获得每个玩家的分值，例如：
result = {
    "alex":8,
    "武沛齐":9,
    "李路飞":0
}

必备技术点：随机抽排
import random

total_poke_list = [("红桃", 1), ("黑桃", 2), ......,("大王", 15), ("小王", 14)]

# 随机生成一个数，当做索引。
index = random.randint(0, len(total_poke_list) - 1)
# 获取牌
print("抽到的牌为：", total_poke_list[index])
# 踢除这张牌
total_poke_list.pop(index)

print("抽完之后，剩下的牌为：", total_poke_list)

踩分点:
请补充完善你的代码
result = {}    # 存储最终各位玩家的得分
user_list = ["alex","武沛齐","李路飞"]
# 补充代码


print(result)
```

```python
result = {}    # 存储最终各位玩家的得分
user_list = ["alex","武沛齐","李路飞"]

poker = ["红桃","方块","黑桃","梅花"]
special_poker_list = [("小王", 14),("大王", 15)]
total_poker_list = []
for index in poker:
        for num in range(1,14):
                total_poker_list.append((index,num))
total_poker_list.extend(special_poker_list)  #生成一副牌
#print(total_poker_list) #生成一副牌

for user in user_list:
    score = 0
    import random
    # 随机生成一个数，当做索引。
    items = random.randint(0, (len(total_poker_list) - 1))
    #print(items) #抽到第几个
    #print("抽到的牌为：", [total_poker_list[items]]) #抽到的牌面
    # 踢除这张牌
    poker = total_poker_list.pop(items)
    #print("抽完之后，剩下的牌为：", poker)
    poker_value = poker[1]
    if poker_value > 10:
        score += 0.5
    else:
        score += poker_value
    print("{}得到牌{},目前牌面值总和为{}".format(user,poker,score))  #开始时三人分别分了一张牌

    while True:
        choice = input("是否要牌?(Y:要/N:不要):")
        if choice.upper() not in {"Y","N"}:
            print("输入有误,请重新选择:")
            continue
        if choice.upper() == "N":
            break

        items = random.randint(0, (len(total_poker_list) - 1))
        poker = total_poker_list.pop(items)
        poker_value = poker[1]
        if poker_value > 10:
            score += 0.5
        else:
            score += poker_value
        print("{}得到牌{},目前牌面值总和为{}".format(user,poker,score))  #开始时三人分别分了一张牌
        if score > 11:
            print("{}爆了".format(user))
            score = 0
            break
    result[user] = score
print(result)

```

