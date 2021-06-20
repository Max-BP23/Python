# name = "武沛齐"
# # 占位符
# # text = "我叫%s，今年18岁" %"武沛齐"
# text = "我叫%s，今年18岁" %name
# print(text)

# name = "武沛齐"
# age = 18
# # text = "我叫%s，今年%s岁" %("武沛齐",18)
# # text = "我叫%s，今年%s岁" %(name,age)
# text = "我叫%s，今年%d岁" %(name,age)
# print(text)

# message = "%(name)s你什么时候过来呀？%(user)s今天不在呀。" % {"name": "死鬼", "user": "李杰"}
# print(message)

# 当文本那里面有占位符和百分比,百分比部分应该显示两个%,告知计算机此处不是占位符
text = "%s，这个片我已经下载了90%%了，居然特么的断网了" %"兄弟"
print(text)

text = "我叫%s，今年%d岁"
data1 = text %("武沛齐",20)
data2 = text %("alex",84)