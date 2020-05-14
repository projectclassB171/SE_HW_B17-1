import random


class Person(object):
    def __init__(self, name, hp, level):
        self.name = name
        self.max = hp
        self._hp = hp
        self.level = level

    def get_name(self):
        return self.name

    def get_hp(self):
        return self._hp

    def get_level(self):
        return self.level

    def attack(self, target):
        raise NotImplementedError

    def __str__(self):
        return 'Name:{}\t HP: {} \t Level:{}'.format(self.name, self._hp, self.level)


class Monster(Person):
    def __init__(self, name, hp=20, level=1):
        super().__init__(name, hp, level)

    def attack(self, hero):
        if self.level == 1:
            hurt = random.randint(0, 10)
        if self.level == 2:
            hurt = random.randint(0, 20)

        hero.defence(hurt)

    def defence(self, hurt):
        self._hp -= hurt
        print('{}�ܵ���{}���˺�'.format(self.name, hurt))


class Boss(Person):
    def __init__(self, name, hp):
        super().__init__(name, hp, 4)
        self.shield = 30

    def attack(self, hero):
        hurt = random.randint(0, 30)
        hero.defence(hurt)

    def defence(self, hurt):
        if self.shield - hurt >= 0:
            self.shield -= hurt
            print("{}�ܵ�{}���˺�,��ǰʣ�໤��{}".format(self.name, hurt, self.shield))
        else:
            if self.shield > 0:
                self._hp -= self.shield
                self.shield = 0
                print("{}�ܵ�{}���˺�,��ǰʣ�໤��{}".format(self.name, hurt, self.shield))
            else:
                self._hp -= hurt
                print("{}�ܵ�{}���˺�,��ǰʣ�໤��{}".format(self.name, hurt, self.shield))


class Hero(Person):
    def __init__(self, name, hp=30, level=1, race='����'):
        super().__init__(name, hp, level)
        self.race = race
        if self.race == '����':
            self.agile = 0.4
        elif self.race == '����':
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
            print('�ܵ���{}���˺�'.format(hurt))
        else:
            print('�����˹���')

    def upgrade(self):
        self.level += 1
        self.max = self.max + 10
        self._hp = self.max
        print('-'*10, '��������{}��,Ѫ������Ϊ{}'.format(self.level, self._hp), '-'*10)


def next_monster(monster_list: list):
    assert type(monster_list) is list
    if len(monster_list) > 0:
        return monster_list[0]


def main():
    hero = Hero("���", 100, 1, '����')
    m1 = Monster("ħ��")
    m2 = Monster("����", 80, 2)
    boss = Boss("����", 100)
    monster_list = [m1, m2, boss]
    r = 1
    while hero.get_hp() > 0 and len(monster_list) > 0:

        monster = next_monster(monster_list)
        while monster.get_hp() > 0:
            print('*'*20, '��{}�غ�'.format(r), '*'*20)
            hero.attack(monster)
            if monster.get_hp() > 0:
                monster.attack(hero)
                if hero.get_hp() <= 0:
                    break

            print(hero)
            print(monster)
            r += 1
        if monster.get_hp() <= 0:
            monster_list.remove(monster)
            hero.upgrade()
            monster = next_monster(monster_list)

    if hero.get_hp() > 0:
        print('��ʤ���ˣ���{}'.format(hero.get_name()))
    else:
        print('������...')


if __name__ == '__main__':
    main()