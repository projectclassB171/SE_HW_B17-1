import random


class person(object):
    def __init__(self, name, hp, level):
        self.name = name
        self.max = hp
        self.level = level
        self.hp = hp

    def __str__(self):
        return 'Name : {}\t HP: {} \t Level:{}'.format(self.name, self.hp, self.level)

class Hero(person):
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
            self.hp -= hurt
            print('你受到{}点攻击！'.format(hurt))
        else:
            print('你躲避了攻击！')

    def upgrade(self):
        self.level += 1
        self.hp = self.hp
        print('-'*10, '你升级到{}级！'.format(self.level))