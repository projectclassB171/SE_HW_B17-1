'''
编写一个打怪兽的小游戏。
游戏要求如下： 
1. 游戏中角色有英雄和怪兽两种大类型。
2. 游戏中英雄和怪兽轮流发送攻击，知道有一方死亡。
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

import random

class 角色(object):#命名可以为中文
    def __init__(self,name,blood,level):
        self.max = blood #最大生命值
        self._blood = blood #生命值
        self.name = name    #名称
        self.level = level  #等级
    def get_name(self):
        return self.name
    def get_blood(self):
        return self._blood
    def get_level(self):
        return self.level
    def attack(self,target):
        raise NotImplementedError

    
    def __str__(self):
        return '角色名称:{}\t 当前生命值:{}\t 角色等级(level):{}'.format(self.name,self._blood,self.level)

    
class 英雄(角色):# 英雄（等级1—3，共3级）
    def __init__(self,name,blood=30,level=1,race='human'):
        super().__init__(name,blood,level)
        self.race=race#种族值不同，闪避能力不同
        if self.race == 'human':
            self.agile = 0.4
        elif self.race == 'elf':
            self.agile = 0.8

    def attack(self,monster):#对怪兽造成伤害,攻击力为对应范围内的随机数
        if self.level ==1:
            hurt = random.randint(0,10)
        elif self.level ==2:
            hurt = random.randint(0,20)
        elif self.level ==3:
            hurt = random.randint(0,30)
        monster.defence(hurt)
    
    def defence(self,hurt):#闪避
        luck =random.random()
        if luck >= self.agile:
            self._blood -= hurt
            print('英雄受到攻击,造成{}点伤害'.format(hurt))
        else:
            print('英雄闪避成功')
    def upgrade(self):#打怪升级
        
        if self.level<3:#由题意,限制等级上限为3级，否则当人物初始等级大于1时会超出范围报错
            self.level +=1
            return self.level
        
        self.max = self.max +10
        self.blood = self.max
        print('='*13,'英雄等级为{}级,最大生命值为{}'.format(self.level,self.max),'='*13)#显示升级信息,同时显示升级后最大生命值

    
class 怪兽(角色):#怪兽（低等级怪兽,等级1—2）
    def __init__(self,name,blood,level):#怪兽前两级仅仅有攻击力差异
        super().__init__(name,blood,level)
        
    def attack(self,hero):#对英雄造成伤害,攻击力为对应范围内的随机数
        if self.level ==1:
            hurt = random.randint(0,10)    
        if self.level ==2:
            hurt = random.randint(0,20)
            
        hero.defence(hurt)
        
    def defence(self,hurt):#防御
        self._blood -= hurt
        print('怪兽受到攻击,造成{}点伤害'.format(hurt))
        
class Boss(角色):#Boss（等级3）
    def __init__(self,name,blood):
        super().__init__(name,blood,3)
        self.shield =30#大怪兽具有一个额外的盾牌属性,盾牌可为BOSS抵消一定伤害值后在扣除血量
    def attack(self,hero):
        hurt = random.randint(0,30)
        hero.defence(hurt)
    def defence(self,hurt):#防御
        self._blood -=hurt#如果没有这句话，会导致虽然显示对Boss造成伤害的数值，但Boss不扣血的问题
        if self.shield<=0:
            self._blood -=hurt
        print('Boss受到攻击,造成{}点伤害'.format(hurt))

        
def main():
    hero = 英雄('卖鱼强',172,2,'elf')#英雄初始等级1-3均可,对老师上课的设计加以修改，避免了当初始等级大于1时，最终等级超过限定范围1-3,导致报错
    monster1 = 怪兽('臭鱼',20,1)     
    monster2 = 怪兽('烂虾',20,2)     #生成两只低等级怪兽和一只大怪兽
    boss =Boss('老板',299)
    monster_list = [monster1,monster2,boss]
    round = 1
    while hero.get_blood()>0 and len(monster_list)>0:#循环条件是英雄和怪兽按顺序轮流发送攻击，直到英雄死亡或所有怪兽被杀死。
        monster = next_monster(monster_list)
        while monster.get_blood()>0:
            print('<'*21,'当前回合数：{}'.format(round),'>'*21)#显示当前回合数
            hero.attack(monster)
            if monster.get_blood()>0:
                monster.attack(hero)
                if hero.get_blood()<=0:
                    break
            print(monster)    
            print(hero)
            round += 1
        if monster.get_blood() <= 0:#杀怪升级，并且从monster_list找下一只活着的怪兽对战
            monster_list.remove(monster)
            hero.upgrade()
            monster = next_monster(monster_list)
            
    if hero.get_blood()>0:#游戏最后打印英雄是Win还是Lose
        print('挑战成功,{}胜利!!! Win!!!'.format(hero.get_name()))
    else:
        print('挑战失败,输了... Lose...')
 
def next_monster(monster_list:list):
    assert type(monster_list) is list
    if len(monster_list) > 0:
        return monster_list[0]
        

main()   
    

