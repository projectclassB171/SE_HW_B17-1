#鸡兔数量共有30只，脚共有90只

for x in range(1,30):                                 #鸡定义变量为x，从1到30遍历，最多为30只
    y = 30 - x                                        #通过鸡的数量x,算兔的数量y
    if x * 2 + y * 4 == 90:                           #若鸡兔数量符合脚的数量，则输出
        print("鸡的数量为%d，兔的数量为%d" %(x,y))
    


'''
#设定鸡兔数量a，脚的数量b
a = 30
b = 90
for x in range(1,a):                                
    y = 30 - x                                     
    if x * 2 + y * 4 == b:                          
        print("鸡的数量为%d，兔的数量为%d" %(x,y))
'''
