result=0
for i in range(0,20):
   for j in range(0,33):
       for k in range(0,100):
           if 5*i+3*j+k==100 and i+j+3*k==100:
               result=result+1
               print("公鸡：",i,"母鸡：",j,"小鸡：",k*3)
print(result)



