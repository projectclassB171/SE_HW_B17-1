#coding=utf-8
#计算百钱买百鸡问题。假设公鸡5元一只，母鸡3元一只，小鸡1元三只，现在有100块钱，想买100只鸡，问有多少种买法？?
for cock in range(0,101):   # 公鸡
    for hen in range(0,101):  #母鸡
        for chick in range(0,101): #小鸡
            if cock * 5 + hen * 3 + chick == 100:
                if cock + hen + chick * 3 == 100:
                    print("公鸡%d\t母鸡%d\t小鸡%d"%(cock,hen,chick * 3))

