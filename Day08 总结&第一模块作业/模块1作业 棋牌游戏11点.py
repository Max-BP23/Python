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
