from Hero import Person
import random


class Monster(Person):
    def __init__(self, name, hp=20, level=1):
        super().__init__(name, hp, level)

    def attack(self, hero):
        hurt = random.randint(0, self.level * 10)
        hero.defence(hurt)  # 英雄进行防御

    def defence(self, hurt):
        self._hp -= hurt
        print("怪兽受到{}点伤害".format(hurt))


class Boss(Person):
    def __init__(self, name, hp=40):
        super().__init__(name, hp, 3)
        self.shield = 30  # 盾牌

    def attack(self, hero):
        hurt = random.randint(0, 30)
        hero.defence(hurt)  # 英雄进行防御

    def defence(self, hurt):
        if self.shield <= 0:  # 盾牌已经失效
            self._hp -= hurt
        elif self.shield > 0:  # 盾牌未失效，先用盾牌抵挡
            self.shield -= hurt
            if self.shield <= 0:  # 如果超出了盾牌的抵挡范围
                self._hp += self.shield  # 超出的部分是英雄受到的伤害
        if self.shield > 0:
            print("{}受到{}点伤害,{}使用盾牌抵挡住了攻击，盾牌:{}".format(self.name,hurt,self.name,self.shield))
        else:
            print("{}受到{}点伤害".format(self.name,hurt))
