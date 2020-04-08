chickNum=[['公鸡','母鸡','小鸡']]
x=0
while x<=20 :
    y=0
    while y<=30 : 
        z=100-x-y
        if z%3==0 and 5*x+3*y+z/3==100  :
            chickNum.append([x,y,z])
        y+=1
    x+=1
print('\'百元买百鸡\'共有%d种方案：'%(len(chickNum)-1))
print()
for i in chickNum :    
    for j in i :
        print(j,end='\t')
    print()