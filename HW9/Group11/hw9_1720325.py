import random


class attribute():
    def __init__(self, name, level, max):
        self.name = name
        self.level = level
        self.hp = max
        self.max = max


class Hero(attribute):
    def __init__(self, name, level, max, race):
        super().__init__(name, level, max)
        self.race = race
        if self.race == 'human':
            self.Dodge = 0.3
        else:
            self.Dodge = 0.6

    def hurt(self, Monster):
        s = random.randint(0, self.level * 10)
        Monster.defense(s)

    def defense(self, s):
        lm = random.random()
        if lm > self.Dodge:
            self.hp -= s
            if self.hp > 0:
                print("Name:{}\t受到攻击:{}\tHP:{}\tLevel:{}\t".format(self.name, s, self.hp, self.level))
            else:
                print("Name:{}\t受到攻击:{}\tHP:0\t,阵亡！".format(self.name, s))
        else:
            print("Name:{}\t躲避了攻击\tHP:{}\tLevel:{}\t".format(self.name, self.hp, self.level))

    def upgrade(self):
        self.level += 1
        self.max = self.max + 10
        self.hp = self.max
        print("Name:{}\t获胜！\tHP:{}\tLevel:{}\t".format(self.name, self.hp, self.level))


class Monster(attribute):
    def __init__(self, name, level, max):
        super().__init__(name, level, max)

    def hurt(self, Hero):
        s = random.randint(0, self.level * 10)
        Hero.defense(s)

    def defense(self, s):
        self.hp = self.hp - s
        if self.hp > 0:
            print("Name:{}\t受到攻击:{}\tHP:{}\tLevel:{}\t ".format(self.name, s, self.hp, self.level))
        else:
            print("Name:{}\t受到攻击:{}\tHP:0\t阵亡！\t".format(self.name, s))


class boss(attribute):
    def __init__(self, name, level, max):
        super().__init__(name, level, max)
        self.shield = 3

    def hurt(self, Hero):
        s = random.randint(0, self.level * 10)
        Hero.defense(s)

    def defense(self, s):
        self.shield -= 2
        if self.shield >= 0:
            print("Name:{}\t受到攻击:{}\t护盾-1\t当前护盾:{}点".format(self.name, s, self.shield))
        else:
            self.hp = self.hp - s
            if self.hp > 0:
                print("Name:{}\t受到攻击:{}\tHP:{}\t".format(self.name, s, self.hp))
            else:
                print("Name:{}\t受到攻击:{}\tHP:0\t阵亡!".format(self.name, s))


def main():
    a = random.random()
    if a >= 0.5:
        hero = Hero("人类", 1, 35, 'human')
    else:
        hero = Hero("精灵", 1, 25, 'spirit')
    m1 = Monster("怪兽1", 1, 30)
    m2 = Monster("怪兽2", 2, 50)
    m3 = boss("BOSS", 3, 80)
    mo = [m1, m2, m3]
    time = 1
    while True:
        print('-' * 15, "第{}回合".format(time), '-' * 15)
        hero.hurt(mo[0])
        if mo[0].hp > 0:
            mo[0].hurt(hero)
        else:
            hero.upgrade()
            del mo[0]
        time += 1

        if len(mo) == 0:
            print("英雄Win!")
            break
        elif hero.hp <= 0:
            print("英雄Lose!")
            break


if __name__ == '__main__':
    main()
