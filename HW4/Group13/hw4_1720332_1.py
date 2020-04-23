# coding=gbk
result=0
for a in range(0,20):
   for b in range(0,33):
       for c in range(0,100):
           if a+b+3*c==100 and 5*a+3*b+c==100:
               print("公鸡：",a,"母鸡：",b,"小鸡：",c*3)
               result=result+1
print("总共的买法: ",result)