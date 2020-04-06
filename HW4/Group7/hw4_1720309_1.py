money = 100
cock = 5
hen = 3
check = 1/3
num = 0

for x in range(0, money//cock):
    for y in range(0, money//hen):
        for z in range(0, 101, 3):
            if x+y+z == 100 and (cock*x+hen*y+check*z) == money:
                print("{},{},{}".format(x, y, z))
                num += 1
                print("一共有{}种方法".format(num))
