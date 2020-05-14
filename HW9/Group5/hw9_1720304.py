'''
#面向对象编程练习
编写一个打怪兽的小游戏。
游戏要求如下：
1. 游戏中角色有英雄和怪兽两种大类型。
2. 游戏中英雄和怪兽轮流发送攻击，知道有一方死亡。
3. 英雄具有名字、级别(共3级），当前生命，当前等级的最大生命、种族和灵活性等属性，具有攻击和防御方法；
   攻击时，根据当前的等级，在一个给定范围内产生一个随机数作为攻击点数。被攻击对象即受到次点数的攻击。
   例如级别为1时在[0,10)范围内随机产生一个数作为攻击力，级别为2级在[0,20)范围内产生一个数作为攻击力。
   英雄具有两个可选种族，人类和精灵。 种族决定了灵活性的高低。
   受到攻击时，根据灵活性，可以躲避掉对方的攻击。 例如：当前英雄灵活性为0.4， 在受到对方m点攻击时，产
   生一个（0，1）之间的随机数，如果随机数小于灵活性0.4，则躲避掉此次攻击不受到伤害，否则受到m点伤害。
4. 怪兽也具有名字、级别(共3级），当前生命，当前等级的最大生命属性。 具有攻击和防御方法；
   怪兽级别共3级，第1，第2级只有级别带来的攻击力差异。 第三级为大怪兽。
   所有怪兽的攻击方法与英雄的攻击方法原理相同。根据当前的等级，在一个给定范围内产生一个随机数作为攻击点数。
   被攻击对象即受到次点数的攻击。
   大怪兽具有一个额外的盾牌属性。收到攻击的时候，首先减少盾牌的防御，盾牌防御减少为0 的以后才减少生命。
5. 编写一个总的入口程序，生成一个英雄， 两个低等级怪兽，一个大怪兽， 设定循环条件是英雄和怪兽按顺序轮流发送攻击，
   直到英雄死亡或所有怪兽被杀死。
6. 游戏过程中在每回合攻击、防御后应打印输出受到的伤害，以及当前的生命。游戏最后打印英雄是Win还是Lose。
'''

import random as x

class Hero:
    def __init__(self, name):       #初始函数
        self.name = name     # 英雄名字
        self.level = 1       # 英雄等级
        self.max_hp = self.level*80  # 最大生命值为80
        self.current_hp = self.level*80  # 当前生命值为80

    def attack(self):
        atk = x.randint(0, self.level*5)
        print("---{}发动攻击回合---".format(self.name))
        return atk           # 传入defense方法

    def upgrade(self):  #升级函数
        self.current_hp += 10    #当前血量值
        Hero.level += 1
        print("{} 升级,当前等级 {},当前血量 {}".format(self.name, self.level, self.current_hp))


class human(Hero):            # 英雄种族：人类
    def __init__(self, name):
        super(human, self).__init__(name)   #继承属性
        self.avd = 0.5        # 灵敏度数值

    def defense(self, atk):      #防御函数
        is_hurt = r.random()        #产生随机数
        if self.avd < is_hurt:
            self.current_hp -= atk
            print("{} 受到 {}点伤害,当前血量为{}".format(self.name, atk, self.current_hp))
        else:
            print("{}成功躲闪了")


class hero_Spirit(Hero):           # 英雄种族：精灵
    def __init__(self, name):
        super(hero_Spirit, self).__init__(name)
        self.avd = 0.7        # 灵敏度数值

    def defense(self, atk):     #防御函数
        is_hurt = x.random()
        if self.avd < is_hurt:
            self.current_hp -= atk
            print("{} 受到 {}点伤害,当前血量为 {}".format(self.name, atk, self.current_hp))
        else:
            print("孙尚香没有被攻击击中")

    def death(self):       # 死亡方法
        print("游戏胜利".format(self.name))

class Monster:
    def __init__(self, name, level):
        self.name = name      # 名字
        self.level = level    # 等级
        self.max_hp = int(level * 30)  # 最大生命值为30
        self.current_hp = int(level * 30)  # 当前生命值为30

    def attack(self):
        atk = x.randint(0, self.level*10)
        print("---{} 发起攻击回合---".format(self.name))
        return atk

    def defense(self, atk):     #进攻方法
        self.current_hp -= atk
        print("{} 受到 {} 点伤害,当前血量 {}".format(self.name, atk, self.current_hp))

    def death(self):        # 死亡方法
        print("{}已无血量，游戏成功过关".format(self.name))


class BigMonster(Monster):       # 怪兽Boss继承了所有怪兽属性，攻击和防御方法，拥有护盾属性并重写防御方法
    def __init__(self, name, level):
        super(BigMonster, self).__init__(name, level)
        self.shield = self.max_hp * 0.2  # 护盾值为最大生命的20%

    def defense(self, atk):   # 重新编写防御方法，受到攻击优先扣除护盾
        if self.shield - atk >= 0:
            self.shield -= atk
            print("{} 受到 {}点伤害,当前护盾值 {} 血量 {}".format(self.name, atk, self.shield, self.current_hp))
        else:
            if self.shield > 0:
                self.current_hp -= self.shield
                self.shield = 0
                print("{} 受到 {}点伤害,当前护盾值 {} 血量 {}".format(self.name, atk, self.shield, self.current_hp))
            else:
                self.current_hp -= atk
                print("{} 受到 {}点伤害,当前护盾值 {} 血量 {}".format(self.name, atk, self.shield, self.current_hp))


def main():     #执行函数
    print("\033[1;37;40m欢迎进入英雄和怪兽之战!\033[0m")
    hero_Spirit_name=input("请输入您选择的英雄种族：")
    monster_name = input("请输入您选择的怪兽个数：")
    H = hero_Spirit("孙尚香")  # 生成英雄和怪兽实例
    m1 = Monster("怪兽1号：李白", 1)
    m2 = Monster("怪兽2号:孙悟空", 2)
    m3 = BigMonster("怪兽boss：虞姬", 2)
    enemy = [m1, m2, m3]

    r = 1
    while True:
        print("---第{}回合---".format(r))
        enemy[0].defense(H.attack())   # 每回合英雄先攻击第一个怪兽，必须杀死第一个怪兽才能攻击第二个
        if enemy[0].current_hp <= 0:   # 如果怪兽阵亡，则删除这个怪兽，从而英雄升级
            print("{} 阵亡".format(enemy[0].name))
            H.upgrade()
            del enemy[0]
        if len(enemy) == 0:      # 怪兽数量为0，英雄胜利
            print("{} 成功击败怪兽们".format(h.name))
            return
        for each in enemy:       # 英雄攻击完后，怪兽轮流攻击英雄
            H.defense(each.attack())
        if H.current_hp <= 0:    # 英雄阵亡，导致最终失败
            print("{}血量不足，攻击失败，阵亡".format(H.name))
            return
        r += 1    # 回合数


if __name__ == '__main__':
    main()

    print("---游戏结束---")

'''
C:\Users\Administrator\PycharmProjects\untitled\venv\Scripts\python.exe D:/xyq.code/untitled/pyhw9.py
欢迎进入英雄和怪兽之战!
请输入您选择的英雄种族：精灵
请输入您选择的怪兽个数：2
---第1回合---
---孙尚香发动攻击回合---
怪兽1号：李白 受到 1 点伤害,当前血量 29
---怪兽1号：李白 发起攻击回合---
孙尚香 受到 7点伤害,当前血量为 73
---怪兽2号:孙悟空 发起攻击回合---
孙尚香 受到 19点伤害,当前血量为 54
---怪兽boss：虞姬 发起攻击回合---
孙尚香没有被攻击击中
---第2回合---
---孙尚香发动攻击回合---
怪兽1号：李白 受到 0 点伤害,当前血量 29
---怪兽1号：李白 发起攻击回合---
孙尚香没有被攻击击中
---怪兽2号:孙悟空 发起攻击回合---
孙尚香 受到 9点伤害,当前血量为 45
---怪兽boss：虞姬 发起攻击回合---
孙尚香没有被攻击击中
---第3回合---
---孙尚香发动攻击回合---
怪兽1号：李白 受到 5 点伤害,当前血量 24
---怪兽1号：李白 发起攻击回合---
孙尚香 受到 4点伤害,当前血量为 41
---怪兽2号:孙悟空 发起攻击回合---
孙尚香 受到 7点伤害,当前血量为 34
---怪兽boss：虞姬 发起攻击回合---
孙尚香没有被攻击击中
---第4回合---
---孙尚香发动攻击回合---
怪兽1号：李白 受到 1 点伤害,当前血量 23
---怪兽1号：李白 发起攻击回合---
孙尚香 受到 8点伤害,当前血量为 26
---怪兽2号:孙悟空 发起攻击回合---
孙尚香没有被攻击击中
---怪兽boss：虞姬 发起攻击回合---
孙尚香没有被攻击击中
---第5回合---
---孙尚香发动攻击回合---
怪兽1号：李白 受到 4 点伤害,当前血量 19
---怪兽1号：李白 发起攻击回合---
孙尚香没有被攻击击中
---怪兽2号:孙悟空 发起攻击回合---
孙尚香没有被攻击击中
---怪兽boss：虞姬 发起攻击回合---
孙尚香 受到 12点伤害,当前血量为 14
---第6回合---
---孙尚香发动攻击回合---
怪兽1号：李白 受到 1 点伤害,当前血量 18
---怪兽1号：李白 发起攻击回合---
孙尚香没有被攻击击中
---怪兽2号:孙悟空 发起攻击回合---
孙尚香没有被攻击击中
---怪兽boss：虞姬 发起攻击回合---
孙尚香没有被攻击击中
---第7回合---
---孙尚香发动攻击回合---
怪兽1号：李白 受到 5 点伤害,当前血量 13
---怪兽1号：李白 发起攻击回合---
孙尚香 受到 8点伤害,当前血量为 6
---怪兽2号:孙悟空 发起攻击回合---
孙尚香没有被攻击击中
---怪兽boss：虞姬 发起攻击回合---
孙尚香没有被攻击击中
---第8回合---
---孙尚香发动攻击回合---
怪兽1号：李白 受到 2 点伤害,当前血量 11
---怪兽1号：李白 发起攻击回合---
孙尚香没有被攻击击中
---怪兽2号:孙悟空 发起攻击回合---
孙尚香没有被攻击击中
---怪兽boss：虞姬 发起攻击回合---
孙尚香没有被攻击击中
---第9回合---
---孙尚香发动攻击回合---
怪兽1号：李白 受到 5 点伤害,当前血量 6
---怪兽1号：李白 发起攻击回合---
孙尚香没有被攻击击中
---怪兽2号:孙悟空 发起攻击回合---
孙尚香没有被攻击击中
---怪兽boss：虞姬 发起攻击回合---
孙尚香没有被攻击击中
---第10回合---
---孙尚香发动攻击回合---
怪兽1号：李白 受到 0 点伤害,当前血量 6
---怪兽1号：李白 发起攻击回合---
孙尚香 受到 6点伤害,当前血量为 0
---怪兽2号:孙悟空 发起攻击回合---
孙尚香没有被攻击击中
---怪兽boss：虞姬 发起攻击回合---
孙尚香没有被攻击击中
孙尚香血量不足，攻击失败，阵亡
---游戏结束---
'''