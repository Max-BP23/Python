# or，看第一个值，如果第一个值为真，结果就应该是第一个值，否则就结果就是第二个值
# and，看第一个值，如果第一个值真，结果就应该是第二个值，否则结果就是第一个值
# 如果多个and 和or的情况，先计算and再计算or
# 先计算not，在计算and，最后计算or

# v2 = "wupeiqi" and "alex"
# print(v2)
# # 第一步：将and前后的只转换为布尔值 True and True
# # 第二步：判断本次操作取悦于谁？由于前面的是True，所以本次逻辑判断取决于后面的值。
# # 所以，后面的只等于多少最终结果就是多少。 v2 = "alex"
#
#
# v3 = "" and "alex"
# print(v3)
# # 第一步：将and前后的只转换为布尔值 False and True
# # 第二步：判断本次操作取悦于谁？由于前面的是False，所以本次逻辑判断取决于前面的值。
# # 所以，前面的只等于多少最终结果就是多少。 v2 = ""
#
# v4 = 1 or 8
# print(v4)
# # 第一步：将and前后的只转换为布尔值 True or True
# # 第二步：判断本次操作取悦于谁？由于前面的是True，所以本次逻辑判断取决于前面的值。
# # v4 = 1
#
# v5 = 0 or 8
# print(v5)
# # 第一步：将and前后的只转换为布尔值 False or True
# # 第二步：判断本次操作取悦于谁？由于前面的是False，所以本次逻辑判断取决于后面的值。
# # v5 = 8



#练习题
v1 = 1 or 2
v2 = -1 or 3
v3 = 0 or -1
v4 = 0 or 100
v5 = "" or 10
v6 = "wupeiqi" or ""
v7 = 0 or ""
print(v1,v2,v3,v4,v5,v6,v7)

v1 = 4 and 8
v2 = 0 and 6
v3 = -1 and 88
v4 = "" and 7
v5 = "武沛齐" and ""
v6 = "" and 0
v7 = 0 and "中国"
print(v1,v2,v3,v4,v5,v6,v7)

v4 = not 8 or 3 and 4 or 2
print(v4)

