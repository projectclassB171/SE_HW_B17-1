"""
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
"""
import random
class Person(object):
    #定义大类共同拥有名字，血量，血槽，等级，攻击函数，防御函数
    def __init__(self, name, hp, level):
        self.name = name #名字
        self.max = hp    #最大血量
        self.hp = hp     #当前血量
        self.level = level #等级

    def get_name(self):
        return self.name
    def get_hp(self):
        return self.hp
    def get_level(self):
        return self.level
    def attack(self,target):
        raise NotImplementedError
        #raise语句自己触发异常
    def __str__(self):
        #重载函数，返回名字，生命，等级
        return '名字:{}\t 当前生命:{}\t 当前等级:{}'.format(self.name,self.hp,self.level)


class Hero(Person):
    #定义英雄类，继承大类
    #__init__构造函数初始化方法
    def __init__(self, name, hp=30, level=1, race="human"):
        #super() 函数是用于调用父类(超类)的一个方法
        super().__init__(name, hp, level)
        #定义种族灵敏度
        self.race = race
        if self.race == "human": #人类
            self.agile = 0.4
        if self.race =="elf": #精灵
            self.agile = 0.7

    #定义攻击的方法，不同等级随机出不同范围的攻击伤害
    def attack(self, monster):
        if self.level == 1:
            hurt = random.randint(0, 10)
        elif self.level ==2:
            hurt = random.randint(0, 20)
        elif self.level ==3:
            hurt = random.randint(0, 30)
        monster.defence(hurt)

    #定义防御的方法，产生随机数，如果随机数0-1之间大于灵敏度，才能造成伤害，否则闪避。
    def defence(self, hurt):
        luck = random.random()
        if luck >= self.agile:
            self.hp -= hurt
            print('你受到{}点攻击！'.format(hurt))
        else:
            print('你躲避了攻击！')

    #定义升级函数，升级之后最大生命值上限+10，并回复满生命
    def upgrade(self):
        self.level +=1
        self.max = self.max + 10
        self.hp = self.max
        print('-'*10, '你升级到{}级!'.format(self.level))

class Monster(Person):
    #定义怪物类
    #初始怪物10生命值，等级1
    def __init__(self, name, hp=20, level=1):
        super().__init__(name, hp, level)

    #定义攻击方法，怪物等级不同造成伤害不同
    def attack(self, hero):
        if self.level==1:
           hurt = random.randint(0, 10)
        if self.level==2:
           hurt = random.randint(0, 20)
        hero.defence(hurt)

    #定义防御方法
    def defence(self, hurt):
        self.hp -= hurt
        print('小怪兽{}点伤害'.format(hurt))

class Boss(Person):
    #定义Boss类，初始等级3级，有护盾
    def __init__(self, name, hp):
        super().__init__(name, hp, 3)
        self.shield = 30 #盾牌

    # 定义攻击方法
    def attack(self, hero):
        hurt = random.randint(0, 30)
        hero.defence(hurt)

    # 定义防御方法，先用护盾抵挡伤害，护盾为0时候，再扣生命值
    def defence(self, hurt):
        self.shield -=hurt
        if self.shield <=0 :
            self.hp -= hurt
        print('大怪兽Boss受到{}点伤害'.format(hurt))

#定义主类
def main():
    #生成英雄一个，小怪两只，Boss一只
    hero = Hero('小学生', 100, 1, 'human')
    monster1 = Monster('月考')
    monster2 = Monster('期中考试', 80, 1)
    boss = Boss('期末考试', 100)
    #将三只怪兽放入list列表中
    monster_list = [monster1, monster2, boss]
    round = 1
    #当英雄生命大于0，怪兽列表长度大于0
    while hero.get_hp() > 0 and len(monster_list) >0:
        #访问怪兽列表
        monster = next_monster(monster_list)
        #怪兽生命大于0
        while monster.get_hp() >0:
            print('*'*10, '回合{}'.format(round), '*'*10)
            #调用英雄攻击函数
            hero.attack(monster)
            if monster.get_hp() >0:
                monster.attack(hero)
                if hero.get_hp() <= 0:
                    break

            print(hero)
            print(monster)
            round += 1
        #当怪兽生命小于0，访问列表，产生下一个怪兽，英雄升级
        if monster.get_hp() <= 0:
            monster_list.remove(monster)
            hero.upgrade()
            monster = next_monster(monster_list)

    if hero.get_hp() >0:
        print('恭喜你胜利了, {}！'.format(hero.get_name()))
    else:
        print('你输了，下次努力！')

#定义访问下一个怪兽的方法
def next_monster(monster_list:list):

    assert type(monster_list) is list
    if len(monster_list) >0:
        return monster_list[0]

if __name__=='__main__':
    main()


