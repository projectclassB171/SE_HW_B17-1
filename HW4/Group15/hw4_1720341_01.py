#问题：计算百钱买百鸡问题。假设公鸡5元一只，母鸡3元一只，小鸡1元三只，现在有100块钱，想买100只鸡，问有多少种买法？

#总金额:totalAmount
#买法种类:num
#x代表公鸡的数量；y代表母鸡的数量；z代表小鸡的数量
#x,y,z只取整数，用// 进行整数除法；format进行格式化


totalAmount = 100
num = 0
for x in range(0,totalAmount//5):
    for y in range(0,totalAmount//3):
        for z in range(0,101,3):
            if x+y+z == 100 and (5*x+3*y+(1/3)*z) == totalAmount:
                print("公鸡的数量：{}\t母鸡的数量：{}\t小鸡的数量：{}".format(x,y,z))
                num += 1
            
print("综上，买法一共有{}种".format(num))
