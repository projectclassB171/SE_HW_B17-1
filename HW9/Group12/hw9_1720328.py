#编写一个打怪兽的小游戏。
# 游戏要求如下：
# 1. 游戏中角色有英雄和怪兽两种大类型。
# 2. 游戏中英雄和怪兽轮流发送攻击，知道有一方死亡。
# 3. 英雄具有名字、级别(共3级），当前生命，当前等级的最大生命、种族和灵活性等属性，具有攻击和防御方法；
#    攻击时，根据当前的等级，在一个给定范围内产生一个随机数作为攻击点数。被攻击对象即受到次点数的攻击。
#    例如级别为1时在[0,10)范围内随机产生一个数作为攻击力，级别为2级在[0,20)范围内产生一个数作为攻击力。
#    英雄具有两个可选种族，人类和精灵。 种族决定了灵活性的高低。
#    受到攻击时，根据灵活性，可以躲避掉对方的攻击。 例如：当前英雄灵活性为0.4， 在受到对方m点攻击时，产
#    生一个（0，1）之间的随机数，如果随机数小于灵活性0.4，则躲避掉此次攻击不受到伤害，否则受到m点伤害。
# 4. 怪兽也具有名字、级别(共3级），当前生命，当前等级的最大生命属性。 具有攻击和防御方法；
#    怪兽级别共3级，第1，第2级只有级别带来的攻击力差异。 第三级为大怪兽。
#    所有怪兽的攻击方法与英雄的攻击方法原理相同。根据当前的等级，在一个给定范围内产生一个随机数作为攻击点数。
#    被攻击对象即受到次点数的攻击。
#    大怪兽具有一个额外的盾牌属性。收到攻击的时候，首先减少盾牌的防御，盾牌防御减少为0 的以后才减少生命。
# 5. 编写一个总的入口程序，生成一个英雄， 两个低等级怪兽，一个大怪兽， 设定循环条件是英雄和怪兽按顺序轮流发送攻击，
#    直到英雄死亡或所有怪兽被杀死。
# 6. 游戏过程中在每回合攻击、防御后应打印输出受到的伤害，以及当前的生命。游戏最后打印英雄是Win还是Lose。

import random as r
from  Monster import  Monster,Boss
from  Hero import  Hero
def next_monster(monster_list: list):
    assert type(monster_list) is list
    if len(monster_list)>0:
        return monster_list[0]
def main():
     hero = Hero('张三丰',100,1,'human')
     print(hero.get_hp())
     montser1=Monster('虾兵')
     montser2=Monster('蟹将',80,1)
     boss=Boss('龙王',100)
     # print(montser1.get_hp())
     # print(montser2.get_hp())
     # print(boss.get_hp())
     montser_list =[montser1,montser2,boss]
     round=1
     while hero.get_hp()>0 and len(montser_list) >0:
         monster = next_monster(montser_list)
         print(monster)
         while monster.get_hp()>0:
             print('*'*20,'fighting of round {}'.format(round),'*'*20)
             hero.attack(monster)
             if monster.get_hp()>0:
                 monster.attack(hero)
                 if hero.get_hp()<=0:
                     break
             print(hero)
             print(monster)
             round+=1
         if monster.get_hp()<=0:
             montser_list.remove(monster)
             hero.upgrade()
             monster=next_monster(montser_list)
         if hero.get_hp()>0:
             print('You win,{}'.format(hero.get_name()))
         else:
             print('You lose')


if __name__=='__main__':
    main()


import random
class Person(object):
    def __init__(self,name,hp,level):
        self.name=name
        self.max=hp #血槽
        self._hp=hp  #血量
        self.level=level
    def get_name(self):
        return self.name
    def get_hp(self):
        return self._hp
    def get_level(self):
        return self.level
    def attack(self,target):
        raise NotImplementedError
    def __str__(self):
        return 'Name:{}\t HP:{}\t Level:{}'.format(self.name,self._hp,self.level)
class Hero(Person):
    def __init__(self,name,hp=30,level=1,race='human'):
        super().__init__(name,hp,level)
        self.race=race
        if self.race=='human': #人类
            self.agile=0.4
        elif self.race=='elves': #精灵
            self.agile=0.8
    def attack(self,monster):
        if self.level==1:
            hurt=random.randint(0,10)
        elif self.level==2:
            hurt=random.randint(0,20)
        elif self.level==3:
            hurt=random.randint(0,30)
        monster.defence(hurt)
    def defence(self,hurt):
        luck=random.random()
        if luck>=self.agile:
            self._hp -= hurt
            print('你受到了攻击！'.format(hurt))
        else:
            print('你躲避了攻击！')
    def upgrade(self):
        self.level += 1
        self.max=self.max+10
        self.hp=self.max
        print('-'*10,'你升到了{}级！'.format(self.level))


import random as r
from Hero import Person
class Monster(Person):
    def __init__(self,name,hp=20,level=1):
          super().__init__(name,hp,level)
    def attack(self,hero):
        if self.level==1:
            hurt=r.randint(0,10)
        if self.level==2:
            hurt=r.randint(0,20)
            hero.defence(hurt)
    def defence(self,hurt):
        self._hp -= hurt
        print('怪兽受到{}点伤害'.format(hurt))
class Boss(Person):
      def __init__(self,name,hp):
          super().__init__(name,hp,3)
          self.shield=30 #盾牌
      def attack(self,hero):
          hurt=r.randint(0,30)
          hero.defence(hurt)
      def defence(self,hurt):
          self.shield -= hurt
          if self.shield<=0:
              self._hp -= hurt
          print('Boss受到{}点伤害'.format(hurt))



'''
运行结果：
C:\Users\ycz11\PycharmProjects\untitled7\venv\Scripts\python.exe C:/Users/ycz11/PycharmProjects/untitled7/game2/allgame.py
100
Name:虾兵	 HP:20	 Level:1
******************** fighting of round 1 ********************
怪兽受到6点伤害
Name:张三丰	 HP:100	 Level:1
Name:虾兵	 HP:14	 Level:1
******************** fighting of round 2 ********************
怪兽受到5点伤害
Name:张三丰	 HP:100	 Level:1
Name:虾兵	 HP:9	 Level:1
******************** fighting of round 3 ********************
怪兽受到4点伤害
Name:张三丰	 HP:100	 Level:1
Name:虾兵	 HP:5	 Level:1
******************** fighting of round 4 ********************
怪兽受到6点伤害
Name:张三丰	 HP:100	 Level:1
Name:虾兵	 HP:-1	 Level:1
---------- 你升到了2级！
You win,张三丰
Name:蟹将	 HP:80	 Level:1
******************** fighting of round 5 ********************
怪兽受到18点伤害
Name:张三丰	 HP:100	 Level:2
Name:蟹将	 HP:62	 Level:1
******************** fighting of round 6 ********************
怪兽受到5点伤害
Name:张三丰	 HP:100	 Level:2
Name:蟹将	 HP:57	 Level:1
******************** fighting of round 7 ********************
怪兽受到16点伤害
Name:张三丰	 HP:100	 Level:2
Name:蟹将	 HP:41	 Level:1
******************** fighting of round 8 ********************
怪兽受到9点伤害
Name:张三丰	 HP:100	 Level:2
Name:蟹将	 HP:32	 Level:1
******************** fighting of round 9 ********************
怪兽受到6点伤害
Name:张三丰	 HP:100	 Level:2
Name:蟹将	 HP:26	 Level:1
******************** fighting of round 10 ********************
怪兽受到17点伤害
Name:张三丰	 HP:100	 Level:2
Name:蟹将	 HP:9	 Level:1
******************** fighting of round 11 ********************
怪兽受到17点伤害
Name:张三丰	 HP:100	 Level:2
Name:蟹将	 HP:-8	 Level:1
---------- 你升到了3级！
You win,张三丰
Name:龙王	 HP:100	 Level:3
******************** fighting of round 12 ********************
Boss受到12点伤害
你躲避了攻击！
Name:张三丰	 HP:100	 Level:3
Name:龙王	 HP:100	 Level:3
******************** fighting of round 13 ********************
Boss受到15点伤害
你受到了攻击！
Name:张三丰	 HP:93	 Level:3
Name:龙王	 HP:100	 Level:3
******************** fighting of round 14 ********************
Boss受到19点伤害
你受到了攻击！
Name:张三丰	 HP:92	 Level:3
Name:龙王	 HP:81	 Level:3
******************** fighting of round 15 ********************
Boss受到24点伤害
你躲避了攻击！
Name:张三丰	 HP:92	 Level:3
Name:龙王	 HP:57	 Level:3
******************** fighting of round 16 ********************
Boss受到28点伤害
你躲避了攻击！
Name:张三丰	 HP:92	 Level:3
Name:龙王	 HP:29	 Level:3
******************** fighting of round 17 ********************
Boss受到13点伤害
你躲避了攻击！
Name:张三丰	 HP:92	 Level:3
Name:龙王	 HP:16	 Level:3
******************** fighting of round 18 ********************
Boss受到11点伤害
你受到了攻击！
Name:张三丰	 HP:76	 Level:3
Name:龙王	 HP:5	 Level:3
******************** fighting of round 19 ********************
Boss受到18点伤害
Name:张三丰	 HP:76	 Level:3
Name:龙王	 HP:-13	 Level:3
---------- 你升到了4级！
You win,张三丰

Process finished with exit code 0
'''