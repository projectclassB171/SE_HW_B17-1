2.鸡兔同笼问题。假设共有鸡、兔30只，脚90只，求鸡、兔各有多少只?
for x in range(0,30):
    for y in range(0,30):
        if x + y ==30 and 2*x + 4*y == 90:
            print("鸡有：",x,"兔有：",y)