# coding=gbk
'''
��ϷҪ�����£�
1. ��Ϸ�н�ɫ��Ӣ�ۺ͹������ִ����͡�
2. ��Ϸ��Ӣ�ۺ͹����������͹�����ֱ����һ��������
3. Ӣ�۾������֡�����(��3��������ǰ��������ǰ�ȼ���������������������Ե����ԣ����й����ͷ���������
   ����ʱ�����ݵ�ǰ�ĵȼ�����һ��������Χ�ڲ���һ���������Ϊ���������������������ܵ��ε����Ĺ�����
   ���缶��Ϊ1ʱ��[0,10)��Χ���������һ������Ϊ������������Ϊ2����[0,20)��Χ�ڲ���һ������Ϊ��������
   Ӣ�۾���������ѡ���壬����;��顣 �������������Եĸߵ͡�
   �ܵ�����ʱ����������ԣ����Զ�ܵ��Է��Ĺ����� ���磺��ǰӢ�������Ϊ0.4�� ���ܵ��Է�m�㹥��ʱ����
   ��һ����0��1��֮������������������С�������0.4�����ܵ��˴ι������ܵ��˺��������ܵ�m���˺���
4. ����Ҳ�������֡�����(��3��������ǰ��������ǰ�ȼ�������������ԡ� ���й����ͷ���������
   ���޼���3������1����2��ֻ�м�������Ĺ��������졣 ������Ϊ����ޡ�
   ���й��޵Ĺ���������Ӣ�۵Ĺ�������ԭ����ͬ�����ݵ�ǰ�ĵȼ�����һ��������Χ�ڲ���һ���������Ϊ����������
   �����������ܵ��ε����Ĺ�����
   ����޾���һ������Ķ������ԡ��յ�������ʱ�����ȼ��ٶ��Ƶķ��������Ʒ�������Ϊ0 ���Ժ�ż���������
5. ��дһ���ܵ���ڳ�������һ��Ӣ�ۣ� �����͵ȼ����ޣ�һ������ޣ� �趨ѭ��������Ӣ�ۺ͹��ް�˳���������͹�����
   ֱ��Ӣ�����������й��ޱ�ɱ����
6. ��Ϸ��������ÿ�غϹ�����������Ӧ��ӡ����ܵ����˺����Լ���ǰ����������Ϸ����ӡӢ����Win����Lose��
'''

import random  as  rn

class monster:
    def __init__(self, name, lv, maxblood ):
        self.name = name
        self.lv = lv # max_lv = 3
        self.maxblood = maxblood
        self.blood = maxblood
        self.blood = self.maxblood + 10
        if self.lv == 1:
            self.att = rn.randint(0, 10)
        elif self.lv == 2:
            self.att = rn.randint(0, 20)
        elif self.lv == 3:
            self.att = rn.randint(0, 30)
    def attack(self, beattacked):
        if beattacked.has_living():
            if self.lv == 1:
                self.att = rn.randint(0, 10)
            elif self.lv == 2:
                self.att = rn.randint(0, 20)
            elif self.lv == 3:
                self.att = rn.randint(0, 30)
            print(self.att)
            if beattacked.flexibility < rn.random():
                beattacked.minus_blood(self.att)
            else:
                beattacked.minus_blood(0)
                print('����' + beattacked.name + '�����˹�����')
        if beattacked.blood <= (beattacked.maxblood + 10) & beattacked.lv == 3:
            print(beattacked.name + ' ʣ��Ѫ��:\n' + str(beattacked.blood) +
                  'ʣ�໤�ܣ�' + str(beattacked.maxblood + 10 - beattacked.blood) + "\n")
        else:
            print(beattacked.name + ' ʣ��Ѫ��:\n' + str(beattacked.blood) + "\n")
        print('------ս������-------')
        # ���ʣ��Ѫ��
    def minus_blood(self, num):
        self.blood -= num

    def has_living(self):  # �ж��Ƿ���Ѫ��
        if self.blood > 0:
            return True
        return False

class hero:
    def __init__(self, name, lv, race, maxblood ):
        self.name = name
        self.lv = lv # max_lv = 3
        self.race = race
        self.maxblood = maxblood
        self.blood = maxblood
        if self.race == 'humanity':
            self.flexibility = 0.2
        else :
            self.flexibility = 0.4
        if self.lv == 1:
            self.att = rn.randint(0, 10)
        elif self.lv == 2:
            self.att = rn.randint(0, 20)
        elif self.lv == 3:
            self.att = rn.randint(0, 30)
    def attack(self, beattacked):
        if beattacked.has_living():
            if self.lv == 1:
                self.att = rn.randint(0, 10)
            elif self.lv == 2:
                self.att = rn.randint(0, 20)
            elif self.lv == 3:
                self.att = rn.randint(0, 30)
            print(self.att)
            beattacked.minus_blood(self.att)
        if beattacked.blood <= (beattacked.maxblood + 10) & beattacked.lv == 3:
            print(beattacked.name+ '�Ļ��ܱ�������')
        print(beattacked.name + ' ʣ��Ѫ��:\n' + str(beattacked.blood) + "\n")
        print('------ս������-------')
        # ���ʣ��Ѫ��
    def minus_blood(self, num):
        self.blood -= num

    def has_living(self):  # �ж��Ƿ���Ѫ��
        if self.blood > 0:
            return True
        return False
m1 = monster(name='��1��С���ޡ�' , lv=1 , maxblood=20)  # ����1��С����
m2 = monster(name='��2��С���ޡ�' , lv=2 , maxblood=30)  # ����2��С����
m3 = monster(name='��3��С���ޡ�' , lv=3 , maxblood=50)  # ����3��С����
mo = [m1,m2,m3]
h = hero(name='�����ܶ���' , lv=3 , race='����',maxblood=100)  # ����Ӣ��
print(h.name + '�ĳ�ʼѪ��:' + str(h.maxblood) + '����һ��' + h.race)
for m in mo:
    print(h.name + '������Ѫ����' + str(h.blood))
    if m.lv == 3:
        print(m.name + '�ĵȼ��ﵽ�������������20�㻤��')
        print(m.name + '�ĳ�ʼѪ��:' + str(m.maxblood) + '  ���ܣ�' + str(10))
    else:
        print(m.name + '�ĳ�ʼѪ��:' + str(m.maxblood))
    print('------------ս������-------------')
    while m.has_living() and h.has_living():
        print(m.name + ' �� ' + h.name + ' ����˺�:')
        m.attack(h)
        print(h.name + ' �� ' + m.name + ' ����˺�:')
        h.attack(m)
    if m.has_living():
        print(m.name + ' ʤ��!')
    elif h.has_living():
        print(h.name + ' ʤ��~!')
    else:
        print(m.name + ' �� ' + h.name + '������!')
