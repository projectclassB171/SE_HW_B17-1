'''编写程序，计算百钱买百鸡问题。
假设公鸡5元一只，母鸡3元一只，小鸡1元三只，
现在有100块钱，想买100只鸡，问有多少种买法？'''

sum = 0;
for i in range(0, 21):
    for j in range(0, 34):
        for k in range(3, 98, 3):
            if i + j + k == 100 and 5 * i + 3 * j + k //3 == 100:
                sum+=1;
                print("方法：",sum,"公鸡：", i, "母鸡：", j, "小鸡：", k)




