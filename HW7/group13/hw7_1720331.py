# coding=gbk
#1.��д����������������������Ϊ����������һ��Ԫ�飬���е�һ��Ԫ��Ϊ���Լ�����ڶ���Ԫ��Ϊ��С��������

import math
def ���Լ����С������():
    a,b=map(int,input('��Ŀһ,������������������Ϊ������').split())
    d = math.gcd(a,b)
    x = (a*b)//d
    tupl = (d,x)
    print("��Ŀһ��������Ϊ;",tupl)#��һ��Ԫ��Ϊ���Լ�����ڶ���Ԫ��Ϊ��С������.
���Լ����С������()




#2.��д����������һ���ַ�����Ϊ���������㲢��ӡ�����ַ��������֣���ĸ���ո��Լ������ĸ�����

def �ַ�������():
    num_number = char_number = space_number = other_number = 0
    str_2 = input("��Ŀ��,������һ���ַ���:")
    for char in str_2:
        if char.isdigit():
            num_number += 1
        elif char.isalpha():
            char_number += 1
        elif char == ' ':
            space_number += 1
        else:
            other_number += 1
    print("��Ŀ��������,���ָ�����%d,��ĸ������%d,�ո������%d,�����ַ���%d" % (num_number,char_number,space_number,other_number))
�ַ�������()
