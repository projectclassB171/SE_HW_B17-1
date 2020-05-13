面向对象编程练习
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

import random as r

#英雄函数，分别是精灵和人类2种选择
class Hero:
    #属性
    def __init__(hero, name):
        hero.name = name     # 英雄名字
        hero.level = 1       # 英雄等级
        hero.max_hp = hero.level*75  # 英雄最大生命
        hero.current_hp = hero.level*75  # 英雄当前生命
    #攻击
    def attack(hero):
        hd = r.randint(0, hero.level*10)
        print("-->英雄攻击回合!")
        return hd
    #升级
    def uplevel(hero):
        hero.current_hp= hero.current_hp+10  #当前血量
        hero.level = hero.level +1  #等级
        print("---->{} 升级,当前等级 {},当前血量 {}".format(hero.name, hero.level, hero.current_hp))
# 人类分支
class HeroHuman(Hero):
    # 属性函数
    def __init__(hero, name):
        super(HeroHuman, hero).__init__(name)
        hero.avd = 0.5        # 灵活性
    #防御函数
    def defense(hero, hd):
        is_hurt = r.random()#产生随机数，如果小于灵活性则躲避
        if hero.avd < is_hurt:
            hero.current_hp -= hd
            print("-->英雄_人类：受到 {}点伤害,当前血量 {}".format(hd, hero.current_hp))
        else:
            print("-->英雄_人类：miss!")

# 精灵分支
class HeroSpirit(Hero):
    # 属性函数
    def __init__(hero, name):
        super(HeroSpirit, hero).__init__(name)
        hero.avd = 0.8        # 灵活性
    # 防御函数
    def defense(hero, hd):
        is_hurt = r.random()
        if hero.avd < is_hurt:
            hero.current_hp -= hd
            print("-->英雄_精灵：受到 {}点伤害,当前血量 {}".format( hd, hero.current_hp))
        else:
            print("-->英雄_精灵：miss!")


class Monster:
    #属性
    def __init__(monster, name, level):
        monster.name = name      # 怪兽名字
        monster.level = level    # 怪兽等级
        monster.max_hp = int(level * 20)  # 怪兽最大生命
        monster.current_hp = int(level * 20)  # 怪兽当前生命


    # 攻击
    def attack(monster):
        hd = r.randint(0, monster.level * 10)
        print("-->怪兽攻击回合!".format(monster.name))
        return hd

        # 防御
    def defense(monster, hd):
        monster.current_hp -= hd
        print("-->怪兽受到 {} 点伤害,当前血量 {}".format( hd, monster.current_hp))

# 怪兽boss
class Monster_bigMonster(Monster):
    # 属性
    def __init__(BigBoss_Monster, name, level):
        super(Monster_bigMonster, BigBoss_Monster).__init__(name, level)
        BigBoss_Monster.shield = BigBoss_Monster.max_hp * 0.44  # 护盾值
    # 防御
    def defense(BigBoss_Monster, hd):   # 受到攻击时优先扣除护盾值，护盾值归0才会扣除生命
        if BigBoss_Monster.shield - hd >= 0:
            BigBoss_Monster.shield = hd-BigBoss_Monster.shield
            print("-->怪兽boss：受到 {}点伤害,当前护盾值 {} 血量 {}".format( hd, BigBoss_Monster.shield, BigBoss_Monster.current_hp))
        else:
            if BigBoss_Monster.shield > 0:
                BigBoss_Monster.current_hp -= BigBoss_Monster.shield
                BigBoss_Monster.shield = 0
                print("-->怪兽boss：受到 {}点伤害,当前护盾值 {} 血量 {}".format( hd, BigBoss_Monster.shield, BigBoss_Monster.current_hp))
            else:
                BigBoss_Monster.current_hp -= hd
                print("-->怪兽boss：受到 {}点伤害,当前护盾值 {} 血量 {}".format(BigBoss_Monster.name, hd, BigBoss_Monster.shield, BigBoss_Monster.current_hp))


#主方法函数
def main():
    #生成一个英雄，两个小怪兽，一个大怪兽boss
    hero = HeroSpirit("精灵")
    Monster1 = Monster("小怪兽1", 1)
    Monster2 = Monster("小怪兽2", 2)
    Monster3 = Monster_bigMonster("大怪兽boss", 3)
    MonsterNumber = [Monster1, Monster2, Monster3]
    r = 1
    while True:
        print("回合{}：".format(r))
        MonsterNumber[0].defense(hero.attack())   # 英雄依次对战小怪兽1,2和大怪兽boss
        if MonsterNumber[0].current_hp <= 0:   # 如果怪兽被击败，则从列表中删除怪兽，然后英雄升级
            print("{} 阵亡".format(MonsterNumber[0].name))
            hero.uplevel()
            del MonsterNumber[0]
        if len(MonsterNumber) == 0:      # 英雄胜利的条件是击杀全部怪兽
            print("---->英雄：恭喜您！成功歼灭所有怪兽，保卫了世界和平，获得了胜利!")
            return

        for each in MonsterNumber:       # 回合攻击机制
            hero.defense(each.attack())
        if hero.current_hp <= 0:    # 失败条件是英雄阵亡
            print("---->英雄：对不起！您已被击败，请尝试再次挑战!")
            return
        r += 1    # 回合数加1

if __name__ == '__main__':
  main()

选择精灵分支：

回合1：
-->英雄攻击回合!
-->怪兽受到 4 点伤害,当前血量 16
-->怪兽攻击回合!
-->英雄_精灵：miss!
-->怪兽攻击回合!
-->英雄_精灵：miss!
-->怪兽攻击回合!
-->英雄_精灵：受到 30点伤害,当前血量 45
回合2：
-->英雄攻击回合!
-->怪兽受到 8 点伤害,当前血量 8
-->怪兽攻击回合!
-->英雄_精灵：miss!
-->怪兽攻击回合!
-->英雄_精灵：miss!
-->怪兽攻击回合!
-->英雄_精灵：miss!
回合3：
-->英雄攻击回合!
-->怪兽受到 1 点伤害,当前血量 7
-->怪兽攻击回合!
-->英雄_精灵：miss!
-->怪兽攻击回合!
-->英雄_精灵：miss!
-->怪兽攻击回合!
-->英雄_精灵：miss!
回合4：
-->英雄攻击回合!
-->怪兽受到 10 点伤害,当前血量 -3
小怪兽1 阵亡
---->精灵 升级,当前等级 2,当前血量 55
-->怪兽攻击回合!
-->英雄_精灵：受到 17点伤害,当前血量 38
-->怪兽攻击回合!
-->英雄_精灵：miss!
回合5：
-->英雄攻击回合!
-->怪兽受到 3 点伤害,当前血量 37
-->怪兽攻击回合!
-->英雄_精灵：受到 12点伤害,当前血量 26
-->怪兽攻击回合!
-->英雄_精灵：miss!
回合6：
-->英雄攻击回合!
-->怪兽受到 17 点伤害,当前血量 20
-->怪兽攻击回合!
-->英雄_精灵：受到 0点伤害,当前血量 26
-->怪兽攻击回合!
-->英雄_精灵：miss!
回合7：
-->英雄攻击回合!
-->怪兽受到 0 点伤害,当前血量 20
-->怪兽攻击回合!
-->英雄_精灵：miss!
-->怪兽攻击回合!
-->英雄_精灵：miss!
回合8：
-->英雄攻击回合!
-->怪兽受到 4 点伤害,当前血量 16
-->怪兽攻击回合!
-->英雄_精灵：miss!
-->怪兽攻击回合!
-->英雄_精灵：miss!
回合9：
-->英雄攻击回合!
-->怪兽受到 18 点伤害,当前血量 -2
小怪兽2 阵亡
---->精灵 升级,当前等级 3,当前血量 36
-->怪兽攻击回合!
-->英雄_精灵：miss!
回合10：
-->英雄攻击回合!
-->怪兽boss：受到 14点伤害,当前护盾值 -12.399999999999999 血量 60
-->怪兽攻击回合!
-->英雄_精灵：miss!
回合11：
-->英雄攻击回合!
-->怪兽boss：受到 大怪兽boss点伤害,当前护盾值 17 血量 -12.399999999999999
-->怪兽攻击回合!
-->英雄_精灵：miss!
回合12：
-->英雄攻击回合!
-->怪兽boss：受到 大怪兽boss点伤害,当前护盾值 29 血量 -12.399999999999999
-->怪兽攻击回合!
-->英雄_精灵：miss!
回合13：
-->英雄攻击回合!
-->怪兽boss：受到 大怪兽boss点伤害,当前护盾值 26 血量 -12.399999999999999
大怪兽boss 阵亡
---->精灵 升级,当前等级 4,当前血量 46
---->英雄：恭喜您！成功歼灭所有怪兽，保卫了世界和平，获得了胜利!


选择人类分支：

回合1：
-->英雄攻击回合!
-->怪兽受到 2 点伤害,当前血量 18
-->怪兽攻击回合!
-->英雄_人类：受到 2点伤害,当前血量 73
-->怪兽攻击回合!
-->英雄_人类：受到 15点伤害,当前血量 58
-->怪兽攻击回合!
-->英雄_人类：miss!
回合2：
-->英雄攻击回合!
-->怪兽受到 8 点伤害,当前血量 10
-->怪兽攻击回合!
-->英雄_人类：miss!
-->怪兽攻击回合!
-->英雄_人类：miss!
-->怪兽攻击回合!
-->英雄_人类：miss!
回合3：
-->英雄攻击回合!
-->怪兽受到 3 点伤害,当前血量 7
-->怪兽攻击回合!
-->英雄_人类：miss!
-->怪兽攻击回合!
-->英雄_人类：受到 8点伤害,当前血量 50
-->怪兽攻击回合!
-->英雄_人类：受到 18点伤害,当前血量 32
回合4：
-->英雄攻击回合!
-->怪兽受到 9 点伤害,当前血量 -2
小怪兽1 阵亡
---->人类 升级,当前等级 2,当前血量 42
-->怪兽攻击回合!
-->英雄_人类：miss!
-->怪兽攻击回合!
-->英雄_人类：miss!
回合5：
-->英雄攻击回合!
-->怪兽受到 19 点伤害,当前血量 21
-->怪兽攻击回合!
-->英雄_人类：受到 8点伤害,当前血量 34
-->怪兽攻击回合!
-->英雄_人类：受到 10点伤害,当前血量 24
回合6：
-->英雄攻击回合!
-->怪兽受到 11 点伤害,当前血量 10
-->怪兽攻击回合!
-->英雄_人类：受到 3点伤害,当前血量 21
-->怪兽攻击回合!
-->英雄_人类：miss!
回合7：
-->英雄攻击回合!
-->怪兽受到 8 点伤害,当前血量 2
-->怪兽攻击回合!
-->英雄_人类：miss!
-->怪兽攻击回合!
-->英雄_人类：miss!
回合8：
-->英雄攻击回合!
-->怪兽受到 14 点伤害,当前血量 -12
小怪兽2 阵亡
---->人类 升级,当前等级 3,当前血量 31
-->怪兽攻击回合!
-->英雄_人类：miss!
回合9：
-->英雄攻击回合!
-->怪兽boss：受到 20点伤害,当前护盾值 -6.399999999999999 血量 60
-->怪兽攻击回合!
-->英雄_人类：miss!
回合10：
-->英雄攻击回合!
-->怪兽boss：受到 大怪兽boss点伤害,当前护盾值 4 血量 -6.399999999999999
-->怪兽攻击回合!
-->英雄_人类：miss!
回合11：
-->英雄攻击回合!
-->怪兽boss：受到 大怪兽boss点伤害,当前护盾值 24 血量 -6.399999999999999
-->怪兽攻击回合!
-->英雄_人类：miss!
回合12：
-->英雄攻击回合!
-->怪兽boss：受到 大怪兽boss点伤害,当前护盾值 1 血量 -6.399999999999999
-->怪兽攻击回合!
-->英雄_人类：受到 28点伤害,当前血量 3
回合13：
-->英雄攻击回合!
-->怪兽boss：受到 大怪兽boss点伤害,当前护盾值 22 血量 -6.399999999999999
-->怪兽攻击回合!
-->英雄_人类：受到 11点伤害,当前血量 -8
---->英雄：对不起！您已被击败，请尝试再次挑战!

