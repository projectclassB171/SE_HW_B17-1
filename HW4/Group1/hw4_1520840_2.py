i=0
j=30-i
for i in range(1,30):
    for j in range(1,30):
        if(2*i+4*j==90)&(i+j==30):
            print("鸡有:",i,"兔有:",j)

