import random


class Person(object):
    def __init__(self, name, hp, level):
        self.name = name  # 名称
        self.max = hp  # 血槽
        self._hp = hp  # 血量
        self.level = level  # 等级

    def get_name(self):
        return self.name

    def get_hp(self):
        return self._hp

    def get_level(self):
        return self.level

    def attack(self, object1):
        raise NotImplementedError

    def __str__(self):  # 输出
        return "Name:{}\t HP:{}\t level:{}".format(self.name, self._hp, self.level)


class Hero(Person):
    def __init__(self, name, hp=30, level=1, race='human'):
        super().__init__(name, hp, level)
        self.race = race
        if self.race == 'human':  # 人类的灵活度
            self.agile = 0.4
        elif self.race == 'elves':  # 精灵的灵活度
            self.agile = 0.8

    def attack(self, monster):
        """
        攻击技能，根据角色的level随机生成一定的伤害
        :param monster:被攻击的怪兽
        :return:无
        """
        hurt = random.randint(0, self.level * 10)
        monster.defence(hurt)  # 怪兽进行防御

    def defence(self, hurt):
        """
        受到攻击后的防御；根据灵活性，具有一定机会躲避攻击
        :param hurt: 受到攻击的量
        :return: 无
        """
        luck = random.random()
        if luck >= self.agile:  # 躲避失败
            self._hp -= hurt
            print("你受到{}点攻击".format(hurt))
        else:
            print("你躲避了攻击！")

    def upgrade(self):
        """
        这里不需要规定只能到3级，在main()函数中，打败第三个怪兽就自动赢得对战，不会继续升级
        升级hero到下一级，更新血槽，回复hp
        :return: 无
        """
        self.level += 1
        self.max = self.max + 10
        self._hp = self.max
        print("-" * 10, "你升级到{}级".format(self.level))
