  #1 �������ַ�����PHP�滻ΪPython      
  #best_language = "PHP is the best programming language in the world! "

best_language = "PHP is the best programming language in the world! "
print(best_language.replace("PHP","Python"))



  #2 ��д���룬��ʾ�û�����1-7�߸����֣��ֱ������һ�����գ���ӡ������������ܼ���

s="һ������������"
c=eval(input("������1-7�ڵ����֣�"))
if c in range(1,8):
 print("����Ϊ����{}".format(s[c-1]))



  #3 ����һ���ַ����� Python is the BEST programming Language��
  #��дһ��������ʽ�����жϸ��ַ����Ƿ�ȫ��ΪСд��
 
import re

line = "Python is the BEST programming Language!"
res = r'^[a-z\s]*$'
if re.match(res, line):
    print("ȫ����Сд")
else:
    print("��ȫ��Сд")



  #4  ��ȡһ���ַ�����Ҫ��ʹ��������ʽ����ȡ���еĵ绰���룬�绰����ĸ�ʽ�ٶ�Ϊ��
  #��xxx�� xxx-xxxx��xxx-xxx-xxxx��

import re
inputString = input('�������ַ���: ')
zfc = r'\(\d{3}\)\s\d{3}-\d{4}|\d{3}-\d{3}-\d{4}'  
result = re.findall(zfc, inputString)  
for i in range(len(result)):
    print(result[i])



  #5 ����������ʽ�����в�ͬ���ַ����л�ȡָ����ʽ�����ڡ����ڵĸ�ʽΪyyyy-mm-dd��
  #'������2022/9/24', '������2017/09/25', '������2012-07-25', '������2020��04��25',

import re
datetext = '������2022/9/24, ������2017/09/25, ������2012-07-25, ������2020��04��25'
result = re.findall(r"(\d{4}-\d{1,2}-\d{1,2})", datetext)
print("".join(result))