for x in range(21):                                                         # 公鸡定义变量为X,且最多有二十只
    for y in range(34):                                                     # 母鸡定义变量为Y,且最多有三十三只
        z = 100 - x - y                                                     # 通过XY,算出小鸡的数量
        if x * 5 + y * 3 + z / 3 == 100:                                    # 买鸡共花费100元
            print("公鸡：%d 只，母鸡：%d 只，小鸡：%d 只"%(x,y,z))
