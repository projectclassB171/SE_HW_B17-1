#coding=utf-8

#1.编写函数，接收两个正整数作为参数，返回一个元组，其中第一个元素为最大公约数，第二个元素为最小公倍数。
def demo(m,n):
     if m>n:
             m,n = n,m
     p = m*n
     while m!=0:
             r = n%m
             n = m
             m = r
     return(n,p//n)
print(demo(12,30))

#结果：(6, 60)

#2.编写函数，接受一个字符串作为参数，计算并打印传入字符串中数字，字母，空格，以及其它的个数。
def count(str1):
    """
 
    :param str1: 传入字符串
    :return: 数字个数、字母个数、空格个数以及其他字符的个数
    """
    num_number = char_number = space_number = other_number = 0
    for char in str1:
        if char.isdigit():
            num_number += 1
        elif char.isalpha():
            char_number += 1
        elif char == ' ':
            space_number += 1
        else:
            other_number += 1
 
    print("数字个数：%d,字母个数：%d,空格个数：%d,其他字符：%d" % (num_number,char_number,space_number,other_number))
    return
count("4 6as f65sa1f 56as56a as %^$^%")

#结果：数字个数：9,字母个数：11,空格个数：5,其他字符：5
