from random import randint


# 定义基本类（英雄）
class basic():
    def __init__(self, name, identity, hp, grade):
        self._idty = identity
        self._name = name
        self._hp = hp
        self._grade = grade

    # 名字
    @property
    def name(self):
        return self._name
    
    # 身份
    @property
    def identity(self):
        return self._idty

    # 生命值
    @property
    def hp(self):
        return self._hp

    # 级别
    def grades(self):
        return self._grade

    # 提示奖励
    def upgrade(self):
        self._grade += 1
        self.hp += 200
        print("奖励：英雄 {}等级提升，血量+200".format(self.name))

    @hp.setter
    def hp(self, hp):
        self._hp = hp if hp >= 0 else 0

    # 防御(闪避)等级为3的小怪兽具有防御能力
    def defense(self):
        k = randint(0, 100)
        if self._grade == 3:
            if k <= 40:
                return True
            else:
                return False
        else:
            return False

    # 攻击
    def attack(self, monster):
        if self.defense():
            print("_{}的攻击被防御，伤害为0_".format(self.name))
        else:
            if self._grade == 1:
                harm = randint(0, 20)
            elif self._grade == 2:
                harm = randint(0, 30)
            else:
                harm = randint(0, 60)
            monster.hp -= harm
            print("_{}造成了{}点伤害_".format(self.name, harm))

    def __str__(self):  # 返回每次调用之后的剩余参数（名字、血量、等级）
        return '小英雄:%s\n' % self._name + \
               '种族:%s\n' % self._idty + \
               '剩余生命值：%d\n' % self._hp + \
               '等级：%d\n' % self._grade


# 定义基本类（小怪兽）
class Monster(basic):

    def __init__(self, name, level, hp, grade):
        self._level = level
        self._name = name
        self._hp = hp
        self._grade = grade

    @property
    def name(self):
        return self._name

    # 类型
    @property
    def level(self):
        return self._level

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, hp):
        self._hp = hp if hp >= 0 else 0

    # 防御（按级别进行灵活性反应）
    def shield(self, hero):
        k = randint(0, 1)
        if hero._grade == 1:
            if k <= 0.4:
                return True
        elif hero._grade == 2:
            if k <= 0.6:
                return True
        elif hero._grade == 3:
            if k <= 0.8:
                return True
        return False
    
    # 攻击
    def attack(self, hero):  # 定义动态属性（攻击）
        if self.shield(hero):
            print("{}的攻击被防御，伤害为0".format(self.name))
        else:
            if self._grade == 1:
                harm = randint(0, 20)
            elif self._grade == 2:
                harm = randint(0, 40)
            else:
                harm = randint(0, 80)
            hero.hp -= harm
            print("{}造成了{}伤害".format(self.name, harm))

    def __str__(self):
        return '魂兽：%s\n' % self.name + \
               '等级：%s\n' % self.level + \
               '生命值：%d\n' % self.hp


def main():  # 最终调用所有的类对象的属性进行动作，最终的命令执行以上的函数及各种方法
    hero = basic('圣骑士', '人族', 600, 2)
    m1 = Monster('绿蒙斯', '1级', 200, 1)
    m2 = Monster('拉贡', '2级', 300, 2)
    m3 = Monster('泰兰特', '3级', 600, 3)
    # monsters = [m1, m3]
    monsters = [m2, m3]  # 一个英雄与两个小怪兽厮打
    # monsters = [m1, m2]
    at_round = 1
    print('欢迎玩家来到英雄对战小怪兽的小游戏！')
    print('英雄：%s\n' % hero.name + \
          '种族:%s\n' % hero.identity + \
          '剩余生命值：%d\n' % hero.hp + \
          '等级：%d\n' % hero.grades())
    for i in monsters:
        while hero.hp > 0 and i.hp > 0:
            print()
            print('=== ===第%d回合=== ===' % at_round)
            hero.attack(i)
            print(i)
            if i.hp > 0:
                i.attack(hero)
            print(hero)
            at_round += 1
        if hero.hp > 0:
            print('Finally:')
            print('英雄： %s 胜利！' % hero.name)
            hero.upgrade()

        else:
            print('Finally:')
            print('魂兽： %s 胜利！' % i.name)
            break


if __name__ == '__main__':
    main()
