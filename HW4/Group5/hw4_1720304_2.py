#鸡兔同笼问题。假设共有鸡、兔30只，脚90只，求鸡、兔各有多少只?

for chicken in range(0,30):                                 #鸡定义变量为chicken，最多为30只
    rabbit=30-chicken                                 #兔定义变量为rabbit
    chickLeg=2*chicken                                 #定义鸡脚的数量
    rabLeg=4*rabbit

    if(chickLeg+rabLeg==90):                                 #若鸡腿和兔腿相加满足90的条件则输出
        print("鸡:"+str(chicken)+" 兔:"+str(rabbit))

#输出结果为：
鸡15 兔15
