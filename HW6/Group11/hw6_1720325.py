#1 �������ַ�����PHP�滻ΪPython      
#best_language = "PHP is the best programming language in the world! "

best_language = "PHP is the best programming language in the world! "
print(best_language.replace("PHP","Python"))

#2 ��д���룬��ʾ�û�����1-7�߸����֣��ֱ������һ�����գ���ӡ������������ܼ���

list_a=["һ","��","��","��","��","��","��"]
number=int(input("������1-7�����֣�"))
if number in range(1,8):
    print("����Ϊ����{}".format(list_a[number-1]))

#3 ����һ���ַ����� Python is the BEST programming Language��
#��дһ��������ʽ�����жϸ��ַ����Ƿ�ȫ��ΪСд��
 
import re
str="Python is the BEST programming Language"
str1=re.search('^[a-z\s]+$',str)
if str1:
    print(str+"ȫ��Сд")
else:
    print(str+"��ȫ��Сд")

#4  ��ȡһ���ַ�����Ҫ��ʹ��������ʽ����ȡ���еĵ绰���룬�绰����ĸ�ʽ�ٶ�Ϊ��
#��xxx�� xxx-xxxx��xxx-xxx-xxxx��

import re
str=input("������һ�������绰���룩�ַ���:")
phone=re.findall(r'\(\d{3}\)[ ]?\d{3}-\d{4}|\d{3}-\d{3}-\d{4}',str)
for i in range(len(phone)):
    print(phone[i],end=" ")
print("\n")

#5 ����������ʽ�����в�ͬ���ַ����л�ȡָ����ʽ�����ڡ����ڵĸ�ʽΪyyyy-mm-dd��
#'������2022/9/24', '������2017/09/25', '������2012-07-25', '������2020��04��25',

import re
str=input("������һ���������ڣ��ַ���:")
date=re.findall(r'\d{4}\-\d{2}\-\d{2}',str)
for i in range(len(date)):
     print(date[i],end=" ")