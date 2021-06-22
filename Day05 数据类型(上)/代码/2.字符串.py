#替换
data = "你是个好人，但是好人不合适我"
v1 = data.replace("好人","贱人")
print(v1)

#字符串切割
data = "武沛齐|root|wupeiqi@qq.com"
v1 = data.split("|")
print(v1)
v2 = data.split("|",1) #从做到右切几个
print(v2)

#字符串转化为字节
data = "墨"
v1 = data.encode("utf-8")
v2 = data.encode("gbk")
print(v1)
print(v2)

s1 = v1.decode("utf-8")
s2 = v2.decode("gbk")
print(s1)
print(s2)

#居中,居左,居右
v1 = "墨"
data1 = v1.center(21,"_")
print(data1)
data2 = v1.ljust(21,"_")
print(data2)
data3 = v1.rjust(21,"_")
print(data3)

#填充0
data = "墨"
v1 = data.zfill(5)
print(v1)
# 填充的应用场景：处理二进制数据
data = "101" # "00000101"
v1 = data.zfill(8)
print(v1) # "00000101"

str


