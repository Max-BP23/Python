name = "我喜欢BLACKPINK"
date = name.encode("utf-8")

# 打开一个文件
file_object = open("log.txt",mode="wb")

# 在文件中写入内容
file_object.write(date)

# 关闭文件

file_object.close()