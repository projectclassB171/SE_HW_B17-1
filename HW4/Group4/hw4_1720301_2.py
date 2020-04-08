'''鸡兔同笼问题。
假设共有鸡、兔30只，脚90只，求鸡、兔各有多少只?'''

for chicken in range(0,30):
    rabbit=30-chicken
    chickLeg=2*chicken
    rabLeg=4*rabbit
 
    if(chickLeg+rabLeg==90):
        print("鸡:"+str(chicken)+"只， 兔:"+str(rabbit)+"只")