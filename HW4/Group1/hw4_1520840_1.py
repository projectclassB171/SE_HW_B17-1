i=0
j=0
for i in range (1,20):
    for j in range (1,33):
        k=100-i-j
        if(k%3==0)&(5*i+3*j+k/3==100):
         print("公鸡",i,"母鸡",j,"小鸡",k,"\n")


