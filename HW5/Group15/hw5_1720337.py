#��Ŀ1
name=input("������������")
sex=input("�������Ա�")
age=input("���������䣺")
dict={
    '����':name,
    '�Ա�':age,
    '����':sex
      }
print(dict)

#��Ŀ2
print("�ҵ�������",name,",""����",age,"��,","�Ա�",sex,",ϲ���ô��롣")

#��Ŀ3

dict["���"]=input("��ߣ�")
dict["��ϵ��ʽ"]=input("��ϵ��ʽ��")
print(dict)

#��Ŀ4
for keys,values in dict.items():
    print(keys,values)

#��Ŀ5
li = [11,22,33,22,22,44,55,77,88,99,11]
sli=set(li)
print(len(sli))

#��Ŀ6
li =[1,2,3,4,5,6,7,8,9]
li[2::3]

#��Ŀ7
s='python java php'
s[7:11]
