#��Ŀ<1>
print("����������Ϣ")
name = input("������������")
sex = input("�������Ա�")
age = input("���������䣺")
dict = {"����": name, "�Ա�": sex, "����": age}
print(" ")

# ��Ŀ<2>
name = input("������������")
sex = input("�������Ա�")
age = input("���������䣺")
dict = {"����": name, "�Ա�": sex, "����": age}
print("�ҵ�����{},���� {} �꣬�Ա� {},ϲ���ô���".format(dict["����"], dict["����"], dict["�Ա�"]))
print(" ")

# ��Ŀ<3>
print("��һ���˶���ܸ���Ȥ,ƽ̨��Ҫ������������ߺ���ϵ��ʽ")
height = input("���������:")
phone = input("��������ϵ��ʽ:")
dict.update({"����": name, "�Ա�": sex, "����": age,"���": height,"��ϵ��ʽ":phone})
print(" ")

# ��Ŀ<4>
print("������Ϣ")
for key in dict:
    print("{}:{}".format(key, dict[key]))

# ��Ŀ<5>
li = [11, 22, 33, 22, 22, 44, 55, 77, 88, 99, 11]
li2 = list()
for each in li:
    if each not in li2:
       li2.append(each)
#print("�б� li = [11,22,33,22,22,44,55,77,88,99,11]ȥ���ظ�Ԫ��֮����ͳ��Ԫ�ص�����")
#print("Ԫ�ص�����Ϊ��"+str(len(li2)))

# ��Ŀ<6>
li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
li2 = li[2::3]
print("��Ƭ���:", li2)
print(" ")

# ��Ŀ<7>
s = 'python java php'
print("��Ƭ���:", s.split(' ')[1])