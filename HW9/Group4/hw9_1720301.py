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

import random


class role(object):
    def __init__(self, name, blood, level):
        self.max = blood  # 最大生命值
        self._blood = blood  # 当前生命值
        self.name = name  # 名称
        self.level = level  # 等级

    def get_name(self):
        return self.name

    def get_blood(self):
        return self._blood

    def get_level(self):
        return self.level

    def attack(self, target):
        raise NotImplementedError

    def __str__(self):
        return ' 角色名称:{}\n 当前生命值:{}\n 角色等级(level):{}\n'.format(self.name, self._blood, self.level)


class Hero(role):
    def __init__(self, name, blood=30, level=1, race='human'):
        super().__init__(name, blood, level)
        self.race = race  # 种族决定闪避能力
        if self.race == 'human':
            self.agile = 0.4
        elif self.race == 'elf':
            self.agile = 0.8

    def attack(self, monster):  # 英雄对怪兽造成的伤害,等级越高伤害越高，伤害值取随机数
        if self.level == 1:
            hurt = random.randint(0, 10)
        elif self.level == 2:
            hurt = random.randint(5, 20)
        elif self.level == 3:
            hurt = random.randint(10, 30)
        monster.defence(hurt)

    def defence(self, hurt):
        luck = random.random()
        if luck >= self.agile:
            self._blood -= hurt
            print(' 英雄受到攻击,造成{}点伤害\n'.format(hurt))
        else:
            print(' 闪避一次攻击\n')

    def upgrade(self):  # 升级

        if self.level < 3:
            self.level += 1
            self.max = self.max + 100   # 每升一级最大生命值＋100
            self._blood = self.max
            print('#' * 10, '升级！！！英雄等级为{}级,最大生命值为{}'.format(self.level, self.max), '#' * 10)
            return self.level

        self.max = self.max + 200   # 击败Boss的奖励，最大生命值+200
        self.blood = self.max
        print('!' * 10, '通关！英雄等级为{}级,最大生命值为{}'.format(self.level, self.max), '!' * 10)

class Monster(role):  # 低等怪
    def __init__(self, name, blood, level):
        super().__init__(name, blood, level)

    def attack(self, hero):  # 对英雄造成伤害,攻击力为对应范围内的随机数
        if self.level == 1:
            hurt = random.randint(0, 10)
        if self.level == 2:
            hurt = random.randint(0, 20)

        hero.defence(hurt)

    def defence(self, hurt):  # 防御
        self._blood -= hurt
        print(' 怪兽受到攻击,造成{}点伤害\n'.format(hurt))


class Boss(role):  # Boss（等级3）
    def __init__(self, name, blood):
        super().__init__(name, blood, 3)
        self.shield = 200  # Boss具有一个额外的盾牌属性,盾牌可为BOSS抵消一定伤害值后在扣除血量

    def attack(self, hero):
        hurt = random.randint(10, 30)
        hero.defence(hurt)

    def defence(self, hurt):  # 防御
        self._blood -= hurt
        if self.shield <= 0:
            self._blood -= hurt
        print(' Boss受到攻击,造成{}点伤害\n'.format(hurt))


def main():
    hero = Hero('木桶骑士',100,1,'human')
    monster1 = Monster('骷髅卫兵',80,1)
    monster2 = Monster('骷髅军士长',100,2)
    boss = Boss('骷髅将军',400)
    monster_list = [monster1, monster2, boss]
    round = 1
    while hero.get_blood() > 0 and len(monster_list) > 0:  # 循环,英雄和怪兽按顺序轮流发送攻击，直到英雄死亡或所有怪兽被杀死。
        monster = next_monster(monster_list)
        while monster.get_blood() > 0:
            print('<','-' * 20, '第{}回合'.format(round), '-' * 20,'>')  # 显示回合数
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
        print('\n****** Win!!! ******\n   {}获胜！！！'.format(hero.get_name()))
    else:
        print('\n****** Lose!!! ******\n   {}死亡'.format(hero.get_name()))


def next_monster(monster_list: list):
    assert type(monster_list) is list
    if len(monster_list) > 0:
        return monster_list[0]


main()