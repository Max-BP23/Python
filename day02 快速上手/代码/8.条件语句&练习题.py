# name = input("请输入用户名:")
# if name == "alex":
#   print("sb")
# else:
#   print("db")

# 1.提示用户输入用户名和密码，用户名等于"wupeiqi"且密码等于"uuu"就输出登录成功；否则输出登录失败。
# username = input("请输入用户名:")
# password = input("请输入用户名:")
# if username == "wupeiqi" and password == "uuu":
#   print("登录成功")
# else:
#   print("登陆失败")

# 2.猜数字，提示用户输入一个数字，判断数字如果大于10，就输出猜错了；否则输出猜对了。
# guess_number = input("请输入一个数字:")
# if int(guess_number) > 10:
#   print("猜错了")
# else:
#   print("猜对了")

#3.提示用户输入一个数字，判断是否为偶数，是偶数则输出 偶偶偶数，否则输出 奇奇奇数。
guess_number = input("请输入一个数字:")
if int(guess_number) % 2 == 0:
  print("偶偶偶数")
else:
  print("奇奇奇数")
