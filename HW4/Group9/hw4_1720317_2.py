result1=0 #鸡
result2=0 #兔
result=0  #多少种答案
for i in range(0,30):
    if 2*i+4*(30-i)==90:
        result1=i
        result2=30-i
        break
print("鸡：",result1,"\n兔：",result2)