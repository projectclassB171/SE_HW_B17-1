# 1.编写函数，接收两个正整数作为参数，返回一个元组，其中第一个元素为最大公约数，第二个元素为最小公倍数。

def demo(m,n):
    p = m*n
    while m%n != 0:
        m,n = n,m%n
    return(n,p//n)

print(demo(12, 45))

#运行结果：(3, 180)

# 2.编写函数，接受一个字符串作为参数，计算并打印传入字符串中数字，字母，空格，以及其它的个数。

s=input('input a string:\n')
char=0
space=0
digit=0
others=0
for c in s:
    if c.isalpha():     #isalpha 判断有没有字符
        char+=1
    elif c.isspace():   # isspace 判断有没有空格
        space+=1
    elif c.isdigit():   # isdigit 判断有没有数字
        digit+=1
    else:
        others+=1
print('char=%d,space=%d,digit=%d,others=%d'%(char,space,digit,others))

#运算结果：input a string:
#"ylionman0802 "
#char=8,space=1,digit=4,others=2