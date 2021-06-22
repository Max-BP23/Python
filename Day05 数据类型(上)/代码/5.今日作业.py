# 1.请用代码实现如下进制的转换。
'''
v1 = 675          # 请将v1转换为二进制（字符串类型）。
v2 = "0b11000101" # 请将二进制v2转换为十进制（整型）
v3 = "11000101"   # 请将二进制v3转换为十进制（整型）
print(bin(v1))
print(int("0b11000101",base=2))
print(int("11000101",base=2))
'''

# 2.按要求实现
# 现有 `v1=123` 和 `v2=456`，请将这两个值转换为二进制，并将其二进制中的前缀 0b 去掉，然后将两个二进制拼接起来，最终再转换为整型（十进制）。
# 例如：
# 123  对应二进制为  "0b1111011" ，去除前缀0b之后的二进制为 "1111011"
# 456  对应二进制为  "0b111001000" ，去除前缀0b之后的二进制为 "111001000"
# 将两个二进制拼接起来的值为："1111011111001000"，再将此值转换为整型为：63432
'''
v1 = 123
v2 = 456
data1 = bin(v1)[2:]
data2 = bin(v2)[2:]
print(data1)
print(data2)
s1 = data1 + data2
print(s1)
print(int("1111011111001000",base=2))
'''

# 按要求实现
# 现有 `v1=123` 和 `v2=456`，请将这两个值转换为二进制，并将其二进制中的前缀 0b 去掉，再补足为2个字节（16位），然后将两个二进制拼接起来，最终再转换为整型（十进制）。
# 例如：
# 123  对应二进制为  "0b1111011" ，去除前缀0b之后的二进制为 "1111011" ，补足16位为  "00000000 01111011"
# 456  对应二进制为  "0b111001000" ，去除前缀0b之后的二进制为 "111001000"，，补足16位为  "00000001 11001000"
# 将两个二进制拼接起来的值为："00000000 0111101100000001 11001000"，再将此值转换为整型为：8061384
'''
v1 = 123
v2 = 456
data1 = bin(v1)[2:].zfill(16)
data2 = bin(v2)[2:].zfill(16)
print(data1)
print(data2)
s1 = data1 + data2
print(int(s1,base=2))
'''

# 4.列举你了解的那些数据类型的值转换为布尔值为False
'''
v1 = bool(0)
v2 = bool("")
print(v1)
print(v2)
'''

# 5.看代码写结果:
'''
if "":
    print(123)
else:
    print(456)  #456

if 0:
    print(999)
else:
    print(666) #666

if "武沛齐":
    print(345)  #345
else:
    print(110)
'''

# 6.让用户输入一段文本，请实现将文本中的敏感词 `苍老师`、`波波老师`替换为 `***`，最后并输入替换后的文本
'''
data = input("请输入内容:")
data1 = data.replace("苍老师","***")
data2 = data1.replace("波波老师","***")
print(data2)
'''

# 7.有变量name = "aleX leNb " 完成如下操作：
# - 移除 name 变量对应的值两边的空格,并输出处理结果
'''
name = "aleX leNb "
data1 = name.strip()
print(data1)
'''
# - 判断 name 变量是否以 "al" 开头,并输出结果（用切片 或 startswith实现）
'''
name = "aleX leNb "
data2 = name.startswith("al")
print(data2)
'''
# - 判断name变量是否以"Nb"结尾,并输出结果（用切片 或 endswith实现）
'''
name = "aleX leNb "
data3 = name.endswith("Nb")
print(data3)
'''
# - 将 name 变量对应的值中的 所有的"l" 替换为 "p",并输出结果
'''
name = "aleX leNb "
data4 = name.replace("l","p")
print(data4)
'''
# - 将 name 变量对应的值根据 所有的"l" 分割,并输出结果
'''
name = "aleX leNb "
data5 = name.split("l")
print(data5)
'''
# - 将name变量对应的值根据第一个"l"分割,并输出结果
'''
name = "aleX leNb "
data6 = name.split("l",1)
print(data6)
'''
# - 将 name 变量对应的值变大写,并输出结果
'''
name = "aleX leNb "
data7 = name.upper()
print(data7)
'''
# - 将 name 变量对应的值变小写,并输出结果
'''
name = "aleX leNb "
data8 = name.lower()
print(data8)
'''

# 8.如何实现字符串的翻转？
'''
data = "我喜欢墨"
print(data[-1::-1])
'''

# 9.有字符串s = "123a4b5c"
# - 通过对s切片形成新的字符串 "123"
# - 通过对s切片形成新的字符串 "a4b"
# - 通过对s切片形成字符串 "c" # print(len(s)-1)
# - 通过对s切片形成字符串 "ba2"
'''
s = "123a4b5c"
print(s[0:3])
print(s[3:6])
print(s[7:])
print(s[-3::-2])
'''

# 10. 使用while循环实现对字符串 message = "伤情最是晚凉天，憔悴厮人不堪言" 中每个字符进行输出。
'''
message = "伤情最是晚凉天，憔悴厮人不堪言"
s = 0
while s < len(message):
    print(message[s])
    s += 1
'''

# 11. 使用for循环实现对字符串 message = "伤情最是晚凉天，憔悴厮人不堪言" 中每个字符进行输出。
'''
message = "伤情最是晚凉天，憔悴厮人不堪言"
for i in message:
    print(i)
'''

# 12. 使用for循环和range实现对字符串 message = "伤情最是晚凉天，憔悴厮人不堪言" 中每个字符进行倒叙输出。
'''
message = "伤情最是晚凉天，憔悴厮人不堪言"
s = message[-1::-1]
for i in s:
    print(i)
'''
"""
# 方法二
message = "伤情最是晚凉天，憔悴厮人不堪言"
for index in range(len(message)-1,-1,-1):
    print(message[index])
"""
# 13. 使用for循环实现输出倒计时效果，例如：输出内容依次是："倒计时3秒"，"倒计时2秒"，"倒计时1秒"。
'''
s = "321"
for i in s:
    print("倒计时" + i + "秒")
'''
'''
# 方法二
for num in range(3, 0, -1):  # [3,2,1]
    text = "倒计时{}秒".format(num)
    print(text)
'''
# 14. 让用户输入一段文本，请计算文本中 "浪" 出现的次数，并输入结果。
'''
text = input("请输入:")
for i in text:
    if i == "浪":
        print(i)
'''
'''
text = input("请输入:")
i = 0
for index in text:
    if index == "浪":
        i += 1
print(i)
'''

# 15. 获取用户两次输入的内容，并提取其中的数字，然后实现数字的相加（转换为整型再相加）：
# 要求：
# 	将num1中的的所有数字找到并拼接起来：1232312
# 	将num1中的的所有数字找到并拼接起来：1218323
# 	然后将两个数字进行相加。
'''
#本来想做个通用的,但是列表怎么显示忘记了,没掌握
num1 = input("请输入：") # asdfd123sf2312
num2 = input("请输入：") # a12dfd183sf23
s1 = num1[5:8] + num1[10:]
print(s1)
s2 = num2[1:3] + num2[6:9] + num2[11:]
print(s2)
s = int(s1) + int(s2)
print(s)
'''
'''
# 方法一
num1 = input("请输入：") # asdfd123sf2312
num1_list = []
for i1 in num1:
    if i1.isdecimal():
        num1_list.append(i1)
data1 = "".join(num1_list)
print(data1)

num2 = input("请输入：") # a12dfd183sf23
num2_list = []
for i2 in num2:
    if i2.isdecimal():
        num2_list.append(i2)
data2 = "".join(num2_list)
print(data2)

print(int(data1) + int(data2))
'''

'''
# 方法二
num1 = input("请输入：") # asdfd123sf2312
item1 = ""
for i1 in num1:
    if i1.isdecimal():
        item1 += i1
print(item1)

num2 = input("请输入：") # a12dfd183sf23
item2 = ""
for i2 in num2:
    if i2.isdecimal():
        item2 += i2
print(item2)

print(int(item1) + int(item2))
'''