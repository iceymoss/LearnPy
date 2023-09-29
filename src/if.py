# 猜数字游戏
number = 23
while True:
    guess = int(input("请输入数字："))
    if number == guess:
        print('恭喜你！猜对了，number为{0}'.format(number))
        break
    elif number < guess:
        print('您猜大了！')
    else:
        print('您猜小了！')