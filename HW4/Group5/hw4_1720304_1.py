1. 编写程序，计算百钱买百鸡问题。
假设公鸡5元一只，母鸡3元一只，小鸡1元三只，现在有100块钱，想买100只鸡，问有多少种买法？

使用for循环

for x in range(21):                                                         # 公鸡定义变量为x 
 for y in range(34):                                                        # 母鸡定义变量为y
         z = 100-x-y
 if (z%3==0 and
             5*x + 3*y + z/3 == 100):                                    # 总共100元
 print(x,y,z)

运行结果为：
0 25 75
4 18 78
8 11 81
12 4 84
