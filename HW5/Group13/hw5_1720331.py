# coding=gbk
#��Ŀ<1>
name = input("�������������:")
gender = input("����������Ա�:")
age = input("P�������������:")
dic = {}
dic.update({"����": name, "�Ա�": gender, "����": age})

#��Ŀ<2>
print("�ҵ�����{}������{}�꣬�Ա�{}��ϲ���ô���".format(dic["����"], dic["����"], dic["�Ա�"]))

#��Ŀ<3>
high = input("������������ߣ�")
mobil_phone = input("������������ϵ��ʽ��")
dic.update({"���": high, "��ϵ��ʽ": mobil_phone})

#��Ŀ<4>
for k, v in dic.items():
    print(k + ':' + v)

#��Ŀ<5>
li = [11,22,33,22,22,44,55,77,88,99,11]
s = set(li)
li = list(s)
print(len(li))

#��Ŀ<6>
li = [1,2,3,4,5,6,7,8,9]
print(li[2::3])

#��Ŀ<7>
s = 'python java php'
print(s[7: 11])
