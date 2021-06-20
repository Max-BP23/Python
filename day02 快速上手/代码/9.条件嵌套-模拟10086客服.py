print("欢迎致电10086，我们提供了如下服务： 1.话费相关；2.业务办理；3.人工服务")
choice = input("请输入服务序号:")

if choice == "1":
    print("话费相关业务")
    cost = input("查询话费请按1,交话费请按2")
    if cost == "1":
        print("您查询话费余额为100元")
    elif cost == "2":
        print("交话费")
    else:
        print("你输入有误,请重新输入")
elif choice == "2":
    print("业务办理")
elif choice == "3":
    print("人工服务")
else:
    print("您输入有误,请重新输入")
