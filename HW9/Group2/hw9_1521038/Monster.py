from random import randint
from 小游戏.Hero import person


class Monster(person):
    def __init__(self, name, hp=20, level=1):
        super().__init__(name, hp, level)

    def attack(self, hero):
        if self.level == 1:
            hurt = randint(0, 10)
        if self.level == 2:
            hurt = randint(0, 20)
        hero.defence(hurt)

    def defence(self, hurt):
        self.hp -= hurt
        print('怪兽受到{}点伤害'.format(hurt))

class Boss(person):
    def __init__(self, name, hp):
        super().__init__(name, hp, 3)
        self.shield = 30

    def attack(self, hero):
        hurt = randint(0, 30)
        hero.defence(hurt)

    def defence(self, hurt):
        self.shield -= hurt
        if self.shield <= 0:
            self.hp -= hurt
        print('Boss受到{}点伤害'.format(hurt))