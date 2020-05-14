import random


class Role:
    # 定义角色名字，当前血量，最大血量，角色等级
    def __init__(self, name, hp, level):
        self.name = name  # 角色名字
        self.hp = hp  # 当前血量
        self.max = hp  # 最大血量
        self.level = level  # 角色等级

    def get_name(self):
        return self.name

    def get_hp(self):
        return self.hp

    def get_level(self):
        return self.level

    def __str__(self):
        return '名字:{}\t 当前生命:{}\t 当前等级:{}'.format(self.name, self.hp, self.level)


class Hero(Role):
    # 定义英雄类，继承大类
    def __init__(self, name, hp=100, level=1, role="human"):
        super().__init__(name, hp, level)
        # 定义不同种族的灵敏度
        self.role = role
        if self.role == "human":  # 人类
            self.agile = 0.4
        if self.role == "spirit":  # 精灵
            self.agile = 0.6

    # 定义攻击方法
    def attack(self, monster):
        if self.level == 1:
            hurt = random.randint(0, 10)
        elif self.level == 2:
            hurt = random.randint(0, 20)
        elif self.level == 3:
            hurt = random.randint(0, 30)
        monster.defence(hurt)

    # 定义防御方法
    def defence(self, hurt):
        dodge = random.random()
        if dodge >= self.agile:
            self.hp -= hurt
            print('你受到{}点攻击！'.format(hurt))
        else:
            print('你躲避了攻击！')

    # 定义升级函数
    def upgrade(self):
        self.level += 1
        self.max = self.max + 20
        self.hp = self.max
        print('恭喜你，升级到了{}级!'.format(self.level))


class Monster1(Role):
    # 定义怪物类
    def __init__(self, name, hp=20, level=1):
        super().__init__(name, hp, level)

    # 定义攻击方法
    def attack(self, hero):
        hurt = random.randint(0, 10)
        hero.defence(hurt)

    # 定义防御方法
    def defence(self, hurt):
        self.hp -= hurt
        print('小怪受到{}点伤害'.format(hurt))


class Monster2(Role):
    # 定义怪物类
    def __init__(self, name, hp=20, level=2):
        super().__init__(name, hp, level)

    # 定义攻击方法
    def attack(self, hero):
        hurt = random.randint(0, 20)
        hero.defence(hurt)

    # 定义防御方法
    def defence(self, hurt):
        self.hp -= hurt
        print('大怪受到{}点伤害'.format(hurt))


class Boss(Role):
    # 定义Boss类
    def __init__(self, name, hp):
        super().__init__(name, hp, 3)
        self.shield = 30

    # 定义攻击方法
    def attack(self, hero):
        hurt = random.randint(0, 30)
        hero.defence(hurt)

    # 定义防御方法
    def defence(self, hurt):
        self.shield -= hurt
        if self.shield <= 0:
            self.hp -= hurt
        print('老王受到{}点伤害'.format(hurt))


# 定义主类
def main():
    round = 1
    hero = Hero('超人')
    monster1 = Monster1('小怪')
    monster2 = Monster2('大怪')
    boss = Boss('老王', 100)
    # 将三只怪放入列表
    monster_list = [monster1, monster2, boss]
    while hero.get_hp() > 0 and len(monster_list) > 0:
        monster = next_monster(monster_list)
        while monster.get_hp() > 0:
            print('------------', '第{}回合'.format(round), '------------')
            # 调用英雄攻击函数
            hero.attack(monster)
            if monster.get_hp() > 0:
                monster.attack(hero)
                if hero.get_hp() <= 0:
                    break

            print(hero)
            print(monster)
            round += 1
        # 当怪兽生命小于0时，访问列表中的下一只怪，英雄升级
        if monster.get_hp() <= 0:
            monster_list.remove(monster)
            hero.upgrade()
            monster = next_monster(monster_list)

    if hero.get_hp() > 0:
        print('You win,{}！'.format(hero.get_name()))
    else:
        print('You lose,{}！'.format(hero.get_name()))


# 定义访问下一只怪的方法
def next_monster(monster_list: list):
    assert type(monster_list) is list
    if len(monster_list) > 0:
        return monster_list[0]


if __name__ == '__main__':
    main()

'''
------------ 第1回合 ------------
小怪受到10点伤害
你受到7点攻击！
名字:超人	 当前生命:93	 当前等级:1
名字:小怪	 当前生命:10	 当前等级:1
------------ 第2回合 ------------
小怪受到2点伤害
你受到5点攻击！
名字:超人	 当前生命:88	 当前等级:1
名字:小怪	 当前生命:8	 当前等级:1
------------ 第3回合 ------------
小怪受到0点伤害
你躲避了攻击！
名字:超人	 当前生命:88	 当前等级:1
名字:小怪	 当前生命:8	 当前等级:1
------------ 第4回合 ------------
小怪受到5点伤害
你受到7点攻击！
名字:超人	 当前生命:81	 当前等级:1
名字:小怪	 当前生命:3	 当前等级:1
------------ 第5回合 ------------
小怪受到5点伤害
名字:超人	 当前生命:81	 当前等级:1
名字:小怪	 当前生命:-2	 当前等级:1
恭喜你，升级到了2级!
------------ 第6回合 ------------
大怪受到19点伤害
你受到7点攻击！
名字:超人	 当前生命:113	 当前等级:2
名字:大怪	 当前生命:1	 当前等级:2
------------ 第7回合 ------------
大怪受到17点伤害
名字:超人	 当前生命:113	 当前等级:2
名字:大怪	 当前生命:-16	 当前等级:2
恭喜你，升级到了3级!
------------ 第8回合 ------------
老王受到22点伤害
你受到24点攻击！
名字:超人	 当前生命:116	 当前等级:3
名字:老王	 当前生命:100	 当前等级:3
------------ 第9回合 ------------
老王受到10点伤害
你躲避了攻击！
名字:超人	 当前生命:116	 当前等级:3
名字:老王	 当前生命:90	 当前等级:3
------------ 第10回合 ------------
老王受到6点伤害
你受到21点攻击！
名字:超人	 当前生命:95	 当前等级:3
名字:老王	 当前生命:84	 当前等级:3
------------ 第11回合 ------------
老王受到25点伤害
你躲避了攻击！
名字:超人	 当前生命:95	 当前等级:3
名字:老王	 当前生命:59	 当前等级:3
------------ 第12回合 ------------
老王受到30点伤害
你受到21点攻击！
名字:超人	 当前生命:74	 当前等级:3
名字:老王	 当前生命:29	 当前等级:3
------------ 第13回合 ------------
老王受到23点伤害
你躲避了攻击！
名字:超人	 当前生命:74	 当前等级:3
名字:老王	 当前生命:6	 当前等级:3
------------ 第14回合 ------------
老王受到1点伤害
你受到24点攻击！
名字:超人	 当前生命:50	 当前等级:3
名字:老王	 当前生命:5	 当前等级:3
------------ 第15回合 ------------
老王受到26点伤害
名字:超人	 当前生命:50	 当前等级:3
名字:老王	 当前生命:-21	 当前等级:3
恭喜你，升级到了4级!
You win,超人！
'''