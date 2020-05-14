import random


class Person(object):
    def __init__(self, name, hp, level):
        self.name = name  # 名字
        self.max = hp  # 血槽
        self._hp = hp  # 血量
        self.level = level  # 等级

    def get_name(self):
        return self.name

    def get_hp(self):
        return self._hp

    def get_level(self):
        return self.level

    def attack(self, target):
        raise NotImplementedError

    def __str__(self):
        return '名字：{} \t 血量：{} \t 等级：{}'.format(self.name, self._hp, self.level)


class Hero(Person):
    def __init__(self, name, hp=30, level=1, race='human'):
        super().__init__(name, hp, level)
        self.race = race
        if self.race == 'human':
            self.agile = 0.4
        elif self.race == 'elves':
            self.agile = 0.8

    def attack(self, monster):
        if self.level == 1:
            hurt = random.randint(0, 10)
        elif self.level == 2:
            hurt = random.randint(0, 20)
        elif self.level == 3:
            hurt = random.randint(0, 30)
        monster.defence(hurt)

    def defence(self, hurt):
        luck = random.random()
        if luck >= self.agile:
            self._hp -= hurt
            print('英雄受到了{}点攻击！'.format(hurt))
        else:
            print('英雄躲避了攻击！')

    def upgrade(self):
        self.level += 1
        self.max = self.max + 10
        self._hp = self.max
        print('-' * 10, '英雄升级到{}级！'.format(self.level))
