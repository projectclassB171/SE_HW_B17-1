
'''1. 编写程序，计算百钱买百鸡问题。
假设公鸡5元一只，
母鸡3元一只，
小鸡1元三只，
现在有100块钱，想买100只鸡，
问有多少种买法？'''


money = 100
cock = 5
hen = 3
check = 1/3
num = 0


for x in range(0, money//cock):
    for y in range(0, money//hen):
        for z in range(0, 101, 3):
            if x+y+z == 100 and (cock*x+hen*y+check*z) == money:
                print("{},{},{}".format(x,y,z))
                num+=1
print("一共有{}种方法".format(num))
