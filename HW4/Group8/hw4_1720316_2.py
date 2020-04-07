a=30                               #设a为头的个数
b=90                               #设b为脚的个数
for x in range(1,a):               #设x为鸡的个数，且x的个数最多为a-1个
    y=a-x                          #设y为兔的个数
    if 2 * x + 4 * y ==b:
        print("鸡有"+str(x)+"只，兔有"+str(y)+"只。")