
def start():
    print("游戏开始了，请做好准备")
    print("你前面有三个小屋，分别是红色、绿色、白色,请问你想进入那个房间")
    house = input("请输入红色、绿色或者白色：")
    if house == "红色":
        redhouse()
    elif house == "绿色":
        greenhouse()
    elif house == "白色":
        whitehouse()
    else:
        print("请输入正确的房间类型：")
        print("假如你想退出，请输入0，继续请输入1")
        choice = input()
        if choice == "0":
            exit(0)
        elif choice == "1":
            start()
        else:
            print("下次请输入正确数字")

def redhouse():
    print("欢迎来到红房子，这里是爱情的")

def greenhouse():
    print("欢迎来到绿房子，这里有最新的环保知识")
def whitehouse():
    print("你想去美国吗？")
    choice = input("请输入是或者否:")
    if choice == "是":
        choice = input("请选择一种交通工具、飞机、轮船、火车:")
        if choice == "飞机":
            print("恭喜你，你可以从上海直达美国")
        elif choice == "轮船":
            print("好长的旅程")
            print("上海-横滨，横滨-火奴鲁鲁，火奴鲁鲁-洛杉矶（或西雅图）") 
        elif choice == "火车":
            print("北京坐火车到莫斯科，从莫斯科坐火车到巴黎，再经过海底隧道到英国，从英国利物浦乘船到美国纽约")
        else:
            print("没有其他工具了，只能等xsapce的火箭了")
    else:
        print("推出游戏")
        exit(0)
start()