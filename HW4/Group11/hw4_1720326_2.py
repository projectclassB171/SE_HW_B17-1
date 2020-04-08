#coding=utf-8
#鸡兔同笼问题。假设共有鸡、兔30只,脚90只,求鸡、兔各有多少只?

for chi in range(0,30):
    rab=30-chi
    chiLeg=2*chi
    rabLeg=4*rab
 
    if(chiLeg+rabLeg==90):
        print("鸡{0} 兔{1}".format(str(chi),str(rab)))