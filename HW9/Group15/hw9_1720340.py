'''
#面向对象编程练习  1720340 李昀燕
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


class juese(object):
    def __init__(self, name, blood, level):
        self.name = name   # 英雄名称
        self.level = level  # 等级
        self.max = blood    # 最大生命值
        self.tblood = blood  # 生命值


    def get_name(self):
        return self.name   #类的属性变量

    def get_blood(self):
        return self.tblood

    def get_level(self):
        return self.level

    def attack(self, target):
        raise NotImplementedError

    def __str__(self):
        return '角色名称为:{}\t 当前生命值为:{}\t 角色等级为:{}'.format(self.name, self.tblood, self.level)



class yingxiong(juese):  # 定义英雄类
    def __init__(self, name, blood=30, level=1, race='ren'):
        super().__init__(name, blood, level)
        self.race = race   #定义英雄的种族
        if self.race == 'ren':
            self.agile = 0.4
        elif self.race == 'jingling':
            self.agile = 0.6

    def attack(self, monster):  # 英雄对怪兽造成伤害,其攻击数值为对应等级范围内的随机数
        if self.level == 1:
            hurt = random.randint(0, 10)
        elif self.level == 2:
            hurt = random.randint(0, 20)
        elif self.level == 3:
            hurt = random.randint(0, 30)
        monster.defence(hurt)

    def defence(self, hurt):  # 英雄避闪事件
        luck = random.random()
        if luck >= self.agile:
            self.tblood -= hurt
            print('英雄受到攻击,造成{}点伤害'.format(hurt))
        else:
            print('英雄闪避成功')

    def upgrade(self):  # 打败怪兽可以对人物角色进行升级

        if self.level < 3:
            self.level += 1
            return self.level

        self.max = self.max + 10
        self.blood = self.max
        print('=' * 13, '当前英雄等级为{}级,最大生命值为{}'.format(self.level, self.max), '=' * 13)


class guaishou(juese):  # 怪兽类
    def __init__(self, name, blood, level):
        super().__init__(name, blood, level)

    def attack(self, hero):  # 怪兽对英雄造成伤害,攻击数值是对应等级范围内的随机数
        if self.level == 1:
            hurt = random.randint(0, 10)
        if self.level == 2:
            hurt = random.randint(0, 20)

        hero.defence(hurt)

    def defence(self, hurt):  # 怪兽防御事件
        self.tblood -= hurt
        print('怪兽受到攻击,造成{}点伤害'.format(hurt))


class Boss(juese):  # 终极boss类
    def __init__(self, name, blood):
        super().__init__(name, blood, 3)
        self.shield = 30     # 大怪兽具有一个额外的盾牌属性,盾牌可为BOSS抵消一定伤害值后在扣除血量

    def attack(self, hero):
        hurt = random.randint(0, 30)
        hero.defence(hurt)

    def defence(self, hurt):
        self.tblood -= hurt
        if self.shield <= 0:
            self.tblood -= hurt
        print('Boss受到攻击,造成{}点伤害'.format(hurt))


def main():
    hero = yingxiong('超人', 200, 2, 'ren')   #定义英雄的相关信息
    monster1 = guaishou('怪兽小一', 20, 1)
    monster2 = guaishou('怪兽小二', 20, 2)  # 生成两只低等级怪兽和一只大怪兽
    boss = Boss('终极大怪兽', 300)
    monster_list = [monster1, monster2, boss]
    round = 1
    while hero.get_blood() > 0 and len(monster_list) > 0:  # 循环条件是英雄和怪兽按顺序轮流发送攻击，直到英雄死亡或所有怪兽被杀死。
        monster = next_monster(monster_list)
        while monster.get_blood() > 0:
            print('<' * 21, '当前回合：{}'.format(round), '>' * 21)  # 显示当前回合数
            hero.attack(monster)
            if monster.get_blood() > 0:
                monster.attack(hero)
                if hero.get_blood() <= 0:
                    break
            print(monster)
            print(hero)
            round += 1
        if monster.get_blood() <= 0:
            monster_list.remove(monster)
            hero.upgrade()
            monster = next_monster(monster_list)

    if hero.get_blood() > 0:
        print('挑战成功,{}胜利!'.format(hero.get_name()))
    else:
        print('挑战失败,你输了，请再接再厉！')


def next_monster(monster_list: list):
    assert type(monster_list) is list
    if len(monster_list) > 0:
        return monster_list[0]


main()


