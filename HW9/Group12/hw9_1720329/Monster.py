from random import randint

from Hero import Person


class Monster(Person):
    def __init__(self, name, hp=20, level=1):
        super().__init__(name, hp, level)

    def attack(self, hero):
        if self.level == 1:
            hurt = randint(0, 10)
        if self.level == 2:
            hurt = randint(0, 20)

        hero.defence(hurt)

    def defence(self, hurt):
        self._hp -= hurt
        print('怪兽受到{}点伤害！'.format(hurt))


class Boss(Person):
    def __init__(self, name, hp):
        super().__init__(name, hp, 3)
        self.shield = 30  # 盾牌

    def attack(self, hero):
        hurt = randint(0, 30)
        hero.defence(hurt)

    def defence(self, hurt):
        self.shield -= hurt
        if self.shield <= 0:
            self._hp -= hurt
        print('Boss受到了{}点伤害'.format(hurt))
