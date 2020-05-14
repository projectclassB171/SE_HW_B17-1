import random
from random import randrange
from random import randint
class Person(object):
    def __init__(self,name,hp,level):
        self.name = name    #人物名称
        self.max = hp        #人物最大血量
        self.hp = hp        #人物血量
        self.level = level  #人物等级

    def get_name(self):
        return self.name

    def get_hp(self):
        return self.hp

    def get_grade(self):
        return self.level

    def attack(self,target):    #人物攻击方法
        raise NotImplementedError

    def __str__(self):
        return "Name:{}\t HP:{}\tGrade:{}".format(self.name,self.hp,self.level)

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
            self.hp -= hurt
            print('英雄受到了{}点伤害！'.format(hurt))
        else:
            print('英雄躲避了攻击！')

    def upgrade(self):
        self.level += 1
        self.max = self.max + 10
        self.hp = self.max
        print('-' * 10, '英雄升级到{}级！'.format(self.level))

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
        self.hp -= hurt
        print('怪兽受到{}点伤害！'.format(hurt))


class Boss(Person):
    def __init__(self, name, hp):
        super().__init__(name, hp, 3)
        self.shield = 30  #盾牌

    def attack(self, hero):
        hurt = randint(0, 30)
        hero.defence(hurt)

    def defence(self, hurt):
        self.shield -= hurt
        if self.shield <= 0:
            self._hp -= hurt
        print('Boss受到了{}点伤害'.format(hurt))

def main():
    print('开始游戏')
    hero = Hero('英雄', 100, 1, 'human')
    monster1 = Monster('怪兽1')
    monster2 = Monster('怪兽2', 60, 1)
    boss = Boss('BOSS', 100)
    monster_list = [monster1, monster2, boss]
    round = 1
    while hero.get_hp() > 0 and len(monster_list) > 0:
        monster = next_monster(monster_list)
        while monster.get_hp() > 0:
            print('-' * 10, '回合 {}'.format(round), '-' * 10)
            hero.attack(monster)
            if monster.get_hp() > 0:
                monster.attack(hero)
                if hero.get_hp() <= 0:
                    break

                print(hero)
                print(monster)
                round += 1
            if monster.get_hp() <= 0:
                monster_list.remove(monster)
                hero.upgrade()
                monster = next_monster(monster_list)

            if hero.get_hp() > 0:
                print('英雄赢了，{}'.format(hero.get_name()))
            else:
                print('英雄输了')
    print('游戏结束')


def is_any_alive(monster_list):
    for monster in monster_list:
        if monster.get_hp() > 0:
            return True
        return False


def next_monster(monster_list):
    # assert type(monster_list) is list
    monster_len = len(monster_list)
    while True:
        if monster_len > 0:
            index = randrange(monster_len)
            monster = monster_list[index]
            if monster.get_hp() > 0:
                return monster
        else:
            print('你已经打败了所有的怪兽！')
            sys.exit(0)

if __name__ == '__main__':
    main()