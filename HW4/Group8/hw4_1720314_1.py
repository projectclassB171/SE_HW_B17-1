for x in range(21):for cock in range(0,101):   # 公鸡
 for y in range(34): #母鸡
         z = 100-x-y #小鸡
 if (z%3==0 and
             5*x + 3*y + z//3 == 100):
 print(x,y,z)