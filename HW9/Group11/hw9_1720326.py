#coding=utf-8
'''
编写一个打怪兽的小游戏。
游戏要求如下：
1. 游戏中角色有英雄和怪兽两种大类型。
2. 游戏中英雄和怪兽轮流发送攻击，直到有一方死亡。
3. 英雄具有名字、级别(共3级），当前生命，当前等级的最大生命、种族和灵活性等属性，具有攻击和防御方法；
   攻击时，根据当前的等级，在一个给定范围内产生一个随机数作为攻击点数。被攻击对象即受到次点数的攻击。
   例如级别为1时在[0,10)范围内随机产生一个数作为攻击力，级别为2级在[0,20)范围内产生一个数作为攻击力。
   英雄具有两个可选种族，人类和精灵。 种族决定了灵活性的高低。
   受到攻击时，根据灵活性，可以躲避掉对方的攻击。 例如：当前英雄灵活性为0.4， 在受到对方m点攻击时，产
   生一个（0，1）之间的随机数，如果随机数小于灵活性0.4，则躲避掉此次攻击不受到伤害，否则受到m点伤害。
4. 怪兽也具有名字、级别(共3级），当前生命，当前等级的最大生命属性。 具有攻击和防御方法；
   怪兽级别共3级，第1，第2级只有级别带来的攻击力差异。 第三级为大怪兽。
   所有怪兽的攻击方法与英雄的攻击方法原理相同。根据当前的等级，在一个给定范围内产生一个随机数作为攻击点数。
   被攻击对象即受到次点数的攻击。
   大怪兽具有一个额外的盾牌属性。收到攻击的时候，首先减少盾牌的防御，盾牌防御减少为0 的以后才减少生命。
5. 编写一个总的入口程序，生成一个英雄， 两个低等级怪兽，一个大怪兽， 设定循环条件是英雄和怪兽按顺序轮流发送攻击，
   直到英雄死亡或所有怪兽被杀死。
6. 游戏过程中在每回合攻击、防御后应打印输出受到的伤害，以及当前的生命。游戏最后打印英雄是Win还是Lose。
'''
import random #导入random

class Ultraman:
    def __init__(self, name, level, smz, maxsmz, ):#定义基本信息
        self.name = name
        self.level = level 
        self.smz = smz 
        self.maxsmz = maxsmz  

    def attack(self, attacker, victim):  #设置攻击方法
        damageValue = random.randint(0, attacker.level * 10)
        victim.smz -= damageValue
        if victim.smz > 0:
            print("%s受到的伤害：%d\n生命值：%d" % (victim.name, damageValue, victim.smz))
        else:
            print("%s受到的伤害：%d\n生命值：0\n%s死亡！" % (victim.name, damageValue, victim.name))

class Hero(Ultraman):
    def setFlexibility(self, flexibility):  # 设置灵活性
        self.flexibility = flexibility

    def defense(self):  # 设置防御
        if random.uniform(0, 1) < self.flexibility:  
            print("%s防御成功！\n生命值：%d" % (self.name, self.smz))
            return False
        else:
            return True

class bigMonster(Ultraman):
    def setShield(self, shield):  # 设置盾牌
        self.shield = shield

    def defense(self, hero, monster):  
        if monster.shield > 0:
            damageValue = random.randint(0, hero.level * 10)
            monster.shield -= damageValue
            if monster.shield < 0:
                monster.smz += monster.shield
                monster.shield = 0
            print("%s受到攻击：%d\n剩余防御值：%d\n生命值%d：" % (monster.name, damageValue, monster.shield, monster.smz))
            return False
        else:
            return True

def main():#最终调用所有的类对象的属性进行动作
    hero2 = Hero("精灵英雄", 2, 300, 600)
    monster1 = Ultraman("1级小怪兽", 1, 50, 180)
    monster2 = Ultraman("2级小怪兽", 2, 50, 260)
    monster3 = bigMonster("3级大怪兽", 3, 150, 300)
    hero2.setFlexibility(0.5)  # 设置灵活度
    monster3.setShield(100)  
    allMonster = [monster1, monster2, monster3] 
    i = 0  
    number = 1  
    while hero2.smz > 0 and allMonster[i].smz > 0:#设定循环条件是英雄和怪兽按顺序轮流发送攻击
        print("=====第%d回合=====" % number)
        number += 1
        print("%s攻击\n" % allMonster[i].name)
        if hero2.defense(): 
            allMonster[i].attack(allMonster[i], hero2)
        if hero2.smz <= 0: 
            print("\n%sLose!"  % hero2.name)
            break
        print("\n%s攻击" % hero2.name) 
        if i < 2:  
            hero2.attack(hero2, allMonster[i])
            if allMonster[i].smz <= 0:  
                i += 1
        elif i >= 2:  
            if allMonster[i].defense(hero2, allMonster[i]):  
                hero2.attack(hero2, allMonster[i])
                if allMonster[i].smz<= 0:  
                    print("\n%sWin!" % hero2.name)
                    break
        print("\n***************************")


if __name__ == '__main__':
    main()


'''
其1种可能游戏过程：
=====第1回合=====
1级小怪兽攻击

精灵英雄受到的伤害：2
生命值：298

精灵英雄攻击
1级小怪兽受到的伤害：10
生命值：40
***************************
=====第2回合=====
1级小怪兽攻击

精灵英雄防御成功！
生命值：298

精灵英雄攻击
1级小怪兽受到的伤害：7
生命值：33
***************************
=====第3回合=====
1级小怪兽攻击

精灵英雄防御成功！
生命值：298

精灵英雄攻击
1级小怪兽受到的伤害：5
生命值：28
***************************
=====第4回合=====
1级小怪兽攻击

精灵英雄受到的伤害：10
生命值：288

精灵英雄攻击
1级小怪兽受到的伤害：1
生命值：27
***************************
=====第5回合=====
1级小怪兽攻击

精灵英雄受到的伤害：1
生命值：287

精灵英雄攻击
1级小怪兽受到的伤害：8
生命值：19
***************************
=====第6回合=====
1级小怪兽攻击

精灵英雄防御成功！
生命值：287

精灵英雄攻击
1级小怪兽受到的伤害：10
生命值：9
***************************
=====第7回合=====
1级小怪兽攻击

精灵英雄受到的伤害：1
生命值：286

精灵英雄攻击
1级小怪兽受到的伤害：6
生命值：3
***************************
=====第8回合=====
1级小怪兽攻击

精灵英雄受到的伤害：5
生命值：281

精灵英雄攻击
1级小怪兽受到的伤害：0
生命值：3
***************************
=====第9回合=====
1级小怪兽攻击

精灵英雄受到的伤害：3
生命值：278

精灵英雄攻击
1级小怪兽受到的伤害：5
生命值：0
1级小怪兽死亡！
***************************
=====第10回合=====
2级小怪兽攻击

精灵英雄受到的伤害：11
生命值：267

精灵英雄攻击
2级小怪兽受到的伤害：10
生命值：40
***************************
=====第11回合=====
2级小怪兽攻击

精灵英雄防御成功！
生命值：267

精灵英雄攻击
2级小怪兽受到的伤害：17
生命值：23
***************************
=====第12回合=====
2级小怪兽攻击

精灵英雄受到的伤害：10
生命值：257

精灵英雄攻击
2级小怪兽受到的伤害：8
生命值：15
***************************
=====第13回合=====
2级小怪兽攻击

精灵英雄受到的伤害：19
生命值：238

精灵英雄攻击
2级小怪兽受到的伤害：6
生命值：9
***************************
=====第14回合=====
2级小怪兽攻击

精灵英雄受到的伤害：8
生命值：230

精灵英雄攻击
2级小怪兽受到的伤害：6
生命值：3
***************************
=====第15回合=====
2级小怪兽攻击

精灵英雄受到的伤害：19
生命值：211

精灵英雄攻击
2级小怪兽受到的伤害：4
生命值：0
2级小怪兽死亡！
***************************
=====第16回合=====
3级大怪兽攻击

精灵英雄防御成功！
生命值：211

精灵英雄攻击
3级大怪兽受到攻击：16
剩余防御值：84
生命值150：
***************************
=====第17回合=====
3级大怪兽攻击

精灵英雄受到的伤害：20
生命值：191

精灵英雄攻击
3级大怪兽受到攻击：17
剩余防御值：67
生命值150：
***************************
=====第18回合=====
3级大怪兽攻击

精灵英雄受到的伤害：5
生命值：186

精灵英雄攻击
3级大怪兽受到攻击：12
剩余防御值：55
生命值150：
***************************
=====第19回合=====
3级大怪兽攻击

精灵英雄受到的伤害：18
生命值：168

精灵英雄攻击
3级大怪兽受到攻击：6
剩余防御值：49
生命值150：
***************************
=====第20回合=====
3级大怪兽攻击

精灵英雄受到的伤害：6
生命值：162

精灵英雄攻击
3级大怪兽受到攻击：16
剩余防御值：33
生命值150：
***************************
=====第21回合=====
3级大怪兽攻击

精灵英雄防御成功！
生命值：162

精灵英雄攻击
3级大怪兽受到攻击：11
剩余防御值：22
生命值150：
***************************
=====第22回合=====
3级大怪兽攻击

精灵英雄受到的伤害：8
生命值：154

精灵英雄攻击
3级大怪兽受到攻击：15
剩余防御值：7
生命值150：
***************************
=====第23回合=====
3级大怪兽攻击

精灵英雄受到的伤害：18
生命值：136

精灵英雄攻击
3级大怪兽受到攻击：5
剩余防御值：2
生命值150：
***************************
=====第24回合=====
3级大怪兽攻击

精灵英雄防御成功！
生命值：136

精灵英雄攻击
3级大怪兽受到攻击：14
剩余防御值：0
生命值138：
***************************
=====第25回合=====
3级大怪兽攻击

精灵英雄防御成功！
生命值：136

精灵英雄攻击
3级大怪兽受到的伤害：20
生命值：118
***************************
=====第26回合=====
3级大怪兽攻击

精灵英雄受到的伤害：2
生命值：134

精灵英雄攻击
3级大怪兽受到的伤害：9
生命值：109
***************************
=====第27回合=====
3级大怪兽攻击

精灵英雄受到的伤害：16
生命值：118

精灵英雄攻击
3级大怪兽受到的伤害：10
生命值：99
***************************
=====第28回合=====
3级大怪兽攻击

精灵英雄防御成功！
生命值：118

精灵英雄攻击
3级大怪兽受到的伤害：20
生命值：79
***************************
=====第29回合=====
3级大怪兽攻击

精灵英雄受到的伤害：12
生命值：106

精灵英雄攻击
3级大怪兽受到的伤害：10
生命值：69
***************************
=====第30回合=====
3级大怪兽攻击

精灵英雄受到的伤害：7
生命值：99

精灵英雄攻击
3级大怪兽受到的伤害：1
生命值：68
***************************
=====第31回合=====
3级大怪兽攻击

精灵英雄防御成功！
生命值：99

精灵英雄攻击
3级大怪兽受到的伤害：8
生命值：60
***************************
=====第32回合=====
3级大怪兽攻击

精灵英雄受到的伤害：30
生命值：69

精灵英雄攻击
3级大怪兽受到的伤害：9
生命值：51
***************************
=====第33回合=====
3级大怪兽攻击

精灵英雄受到的伤害：7
生命值：62

精灵英雄攻击
3级大怪兽受到的伤害：17
生命值：34
***************************
=====第34回合=====
3级大怪兽攻击

精灵英雄受到的伤害：8
生命值：54

精灵英雄攻击
3级大怪兽受到的伤害：6
生命值：28
***************************
=====第35回合=====
3级大怪兽攻击

精灵英雄受到的伤害：17
生命值：37

精灵英雄攻击
3级大怪兽受到的伤害：12
生命值：16
***************************
=====第36回合=====
3级大怪兽攻击

精灵英雄防御成功！
生命值：37

精灵英雄攻击
3级大怪兽受到的伤害：6
生命值：10
***************************
=====第37回合=====
3级大怪兽攻击

精灵英雄受到的伤害：18
生命值：19

精灵英雄攻击
3级大怪兽受到的伤害：0
生命值：10
***************************
=====第38回合=====
3级大怪兽攻击

精灵英雄防御成功！
生命值：19

精灵英雄攻击
3级大怪兽受到的伤害：19
生命值：0
3级大怪兽死亡！

精灵英雄Win!
MacBook-Pro:- hannah$ python /Users/hannah/-/1720326-陈悦.py 
=====第1回合=====
1级小怪兽攻击

精灵英雄受到的伤害：2
生命值：298

精灵英雄攻击
1级小怪兽受到的伤害：18
生命值：32

***************************
=====第2回合=====
1级小怪兽攻击

精灵英雄受到的伤害：1
生命值：297

精灵英雄攻击
1级小怪兽受到的伤害：12
生命值：20

***************************
=====第3回合=====
1级小怪兽攻击

精灵英雄受到的伤害：7
生命值：290

精灵英雄攻击
1级小怪兽受到的伤害：5
生命值：15

***************************
=====第4回合=====
1级小怪兽攻击

精灵英雄受到的伤害：9
生命值：281

精灵英雄攻击
1级小怪兽受到的伤害：11
生命值：4

***************************
=====第5回合=====
1级小怪兽攻击

精灵英雄受到的伤害：6
生命值：275

精灵英雄攻击
1级小怪兽受到的伤害：15
生命值：0
1级小怪兽死亡！

***************************
=====第6回合=====
2级小怪兽攻击

精灵英雄防御成功！
生命值：275

精灵英雄攻击
2级小怪兽受到的伤害：10
生命值：40

***************************
=====第7回合=====
2级小怪兽攻击

精灵英雄受到的伤害：2
生命值：273

精灵英雄攻击
2级小怪兽受到的伤害：3
生命值：37

***************************
=====第8回合=====
2级小怪兽攻击

精灵英雄受到的伤害：15
生命值：258

精灵英雄攻击
2级小怪兽受到的伤害：19
生命值：18

***************************
=====第9回合=====
2级小怪兽攻击

精灵英雄受到的伤害：5
生命值：253

精灵英雄攻击
2级小怪兽受到的伤害：8
生命值：10

***************************
=====第10回合=====
2级小怪兽攻击

精灵英雄防御成功！
生命值：253

精灵英雄攻击
2级小怪兽受到的伤害：5
生命值：5

***************************
=====第11回合=====
2级小怪兽攻击

精灵英雄防御成功！
生命值：253

精灵英雄攻击
2级小怪兽受到的伤害：7
生命值：0
2级小怪兽死亡！

***************************
=====第12回合=====
3级大怪兽攻击

精灵英雄防御成功！
生命值：253

精灵英雄攻击
3级大怪兽受到攻击：8
剩余防御值：92
生命值150：

***************************
=====第13回合=====
3级大怪兽攻击

精灵英雄受到的伤害：16
生命值：237

精灵英雄攻击
3级大怪兽受到攻击：12
剩余防御值：80
生命值150：

***************************
=====第14回合=====
3级大怪兽攻击

精灵英雄受到的伤害：5
生命值：232

精灵英雄攻击
3级大怪兽受到攻击：8
剩余防御值：72
生命值150：

***************************
=====第15回合=====
3级大怪兽攻击

精灵英雄防御成功！
生命值：232

精灵英雄攻击
3级大怪兽受到攻击：0
剩余防御值：72
生命值150：

***************************
=====第16回合=====
3级大怪兽攻击

精灵英雄防御成功！
生命值：232

精灵英雄攻击
3级大怪兽受到攻击：10
剩余防御值：62
生命值150：

***************************
=====第17回合=====
3级大怪兽攻击

精灵英雄防御成功！
生命值：232

精灵英雄攻击
3级大怪兽受到攻击：1
剩余防御值：61
生命值150：

***************************
=====第18回合=====
3级大怪兽攻击

精灵英雄防御成功！
生命值：232

精灵英雄攻击
3级大怪兽受到攻击：6
剩余防御值：55
生命值150：

***************************
=====第19回合=====
3级大怪兽攻击

精灵英雄受到的伤害：18
生命值：214

精灵英雄攻击
3级大怪兽受到攻击：12
剩余防御值：43
生命值150：

***************************
=====第20回合=====
3级大怪兽攻击

精灵英雄防御成功！
生命值：214

精灵英雄攻击
3级大怪兽受到攻击：4
剩余防御值：39
生命值150：

***************************
=====第21回合=====
3级大怪兽攻击

精灵英雄防御成功！
生命值：214

精灵英雄攻击
3级大怪兽受到攻击：20
剩余防御值：19
生命值150：

***************************
=====第22回合=====
3级大怪兽攻击

精灵英雄受到的伤害：19
生命值：195

精灵英雄攻击
3级大怪兽受到攻击：5
剩余防御值：14
生命值150：

***************************
=====第23回合=====
3级大怪兽攻击

精灵英雄防御成功！
生命值：195

精灵英雄攻击
3级大怪兽受到攻击：12
剩余防御值：2
生命值150：

***************************
=====第24回合=====
3级大怪兽攻击

精灵英雄受到的伤害：26
生命值：169

精灵英雄攻击
3级大怪兽受到攻击：16
剩余防御值：0
生命值136：

***************************
=====第25回合=====
3级大怪兽攻击

精灵英雄受到的伤害：22
生命值：147

精灵英雄攻击
3级大怪兽受到的伤害：13
生命值：123

***************************
=====第26回合=====
3级大怪兽攻击

精灵英雄受到的伤害：26
生命值：121

精灵英雄攻击
3级大怪兽受到的伤害：6
生命值：117

***************************
=====第27回合=====
3级大怪兽攻击

精灵英雄防御成功！
生命值：121

精灵英雄攻击
3级大怪兽受到的伤害：10
生命值：107

***************************
=====第28回合=====
3级大怪兽攻击

精灵英雄受到的伤害：2
生命值：119

精灵英雄攻击
3级大怪兽受到的伤害：16
生命值：91

***************************
=====第29回合=====
3级大怪兽攻击

精灵英雄受到的伤害：21
生命值：98

精灵英雄攻击
3级大怪兽受到的伤害：14
生命值：77

***************************
=====第30回合=====
3级大怪兽攻击

精灵英雄防御成功！
生命值：98

精灵英雄攻击
3级大怪兽受到的伤害：0
生命值：77

***************************
=====第31回合=====
3级大怪兽攻击

精灵英雄受到的伤害：24
生命值：74

精灵英雄攻击
3级大怪兽受到的伤害：8
生命值：69

***************************
=====第32回合=====
3级大怪兽攻击

精灵英雄防御成功！
生命值：74

精灵英雄攻击
3级大怪兽受到的伤害：14
生命值：55

***************************
=====第33回合=====
3级大怪兽攻击

精灵英雄受到的伤害：28
生命值：46

精灵英雄攻击
3级大怪兽受到的伤害：11
生命值：44

***************************
=====第34回合=====
3级大怪兽攻击

精灵英雄受到的伤害：10
生命值：36

精灵英雄攻击
3级大怪兽受到的伤害：18
生命值：26

***************************
=====第35回合=====
3级大怪兽攻击

精灵英雄受到的伤害：18
生命值：18

精灵英雄攻击
3级大怪兽受到的伤害：2
生命值：24

***************************
=====第36回合=====
3级大怪兽攻击

精灵英雄受到的伤害：30
生命值：0
精灵英雄死亡！

精灵英雄Lose!
'''