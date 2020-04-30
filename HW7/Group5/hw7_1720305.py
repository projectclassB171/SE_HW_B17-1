#1.编写函数，接收两个正整数作为参数，返回一个元组，其中第一个元素为最大公约数，第二个元素为最小公倍数。
def demo(m,n):
    if m>n:
        m,n = n,m
    p = m*n
    while m!=0:
        r = n%m
        n = m
        m = r
    return (n,int(p/n))
prin(demo(10,12))

# 结果(2, 60)

#2.编写函数，接受一个字符串作为参数，计算并打印传入字符串中数字，字母，空格，以及其它的个数。
a = input("请输入一个字符串:")
num = 0
letter = 0
space = 0
other = 0
for s in a:
    if s.isdigit():
        num += 1
    elif s.isspace():
        space += 1
    elif s.isalpha():
        letter += 1
    else :
        other += 1
print("数字=%d,字母=%d,空格=%d,其他=%d"%(num,letter,space,other))




#   结果：请输入一个字符串:aasd156  ###
#         数字=3,字母=4,空格=2,其他=3
