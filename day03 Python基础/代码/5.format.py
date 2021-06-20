#1
text = "我叫{0}，今年18岁".format("武沛齐")

text = "我叫{0}，今年{1}岁".format("武沛齐",18)

text = "我叫{0}，今年{1}岁，真实的姓名是{0}。".format("武沛齐",18)

#2
text = "我叫{}，今年18岁".format("武沛齐")

text = "我叫{}，今年{}岁".format("武沛齐",18)

text = "我叫{}，今年{}岁，真实的姓名是{}。".format("武沛齐",18,"武沛齐")

#3
text = "我叫{n1}，今年18岁".format(n1="武沛齐")

text = "我叫{n1}，今年{age}岁".format(n1="武沛齐",age=18)

text = "我叫{n1}，今年{age}岁，真实的姓名是{n1}。".format(n1="武沛齐",age=18)

#4
text = "我叫{0}，今年{1}岁"
data1 = text.format("武沛齐",666)
data2 = text.format("alex",73)

