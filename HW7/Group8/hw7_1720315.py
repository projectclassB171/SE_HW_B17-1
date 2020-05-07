#1.编写函数，接收两个正整数作为参数，返回一个元组，其中第一个元素为最大公约数，第二个元素为最小公倍数



def demo(m,n):

    if m>n:

        m,n = n,m  #交换m,n

    p = m*n

    while m!=0:

        r=n%m

        n=m

        m=r

    return (int(p/n),n)

print(demo(2,3))





#2.编写函数，接受一个字符串作为参数，计算并打印传入字符串中数字，字母，空格，以及其它的个数



string = input("请输入一句话：")

def count(s):

    words = 0

    number = 0

    blank = 0

    other = 0

    for each in s:

        if each.encode().isalpha():

            words += 1

        elif each.isdigit():

            number += 1

        elif each.isspace():

            blank += 1

        else:

            other +=1

    print("数字{}个,字母{}个,空格{}个,其他字符{}个".format(number, words, blank, other))



count(string)



#也可以用unicode编码来进行编写函数，比如数字 的十进制范围为【48，57】

# 字母的范围：小写【97，122】 大写【65，90】