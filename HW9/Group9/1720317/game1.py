"""
游戏要求如下：
1. 游戏中角色有英雄和怪兽两种大类型。
2. 游戏中英雄和怪兽轮流发送攻击，直到有一方死亡。
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
"""

# 定义大类（怪兽和英雄共同有的属性：名字、级别、当前生命值、最大生命值，共同的方法：攻击和防御）
# 类变量：所有实例共享（在实例外，可以通过类名或对象名访问）
# 实例变量（self.变量名 ）：每个实例单独拥有的变量（1.在类外通过对象直接调用 ；2.在类内通过self间接调用 ）
import random


class Character:
    def __init__(self, name, level, currentHP, maxHP, ):
        self.name = name  # 姓名
        self.level = level  # 等级
        self.currentHP = currentHP  # 当前生命值
        self.maxHP = maxHP  # 最大生命值

    def attackMethods(self, attacker, victim):  # 攻击方法,根据攻击对象的属性攻击(attacker:攻击方，victim:被攻击方)
        damageValue = random.randint(0, attacker.level * 10)
        victim.currentHP -= damageValue
        if victim.currentHP > 0:
            print("%s受到的伤害%d，当前生命%d" % (victim.name, damageValue, victim.currentHP))
        else:
            print("%s受到的伤害%d，当前生命0，%s死亡" % (victim.name, damageValue, victim.name))


class Hero(Character):
    def setFlexibility(self, flexibility):  # 设置灵活性
        self.flexibility = flexibility

    def defense(self):  # 防御方法
        if random.uniform(0, 1) < self.flexibility:  # 如果随机数小于灵活性，则躲避掉此次攻击不受到伤害
            print("%s防御成功,当前生命值%d" % (self.name, self.currentHP))
            return False
        else:
            return True


class bigMonster(Character):
    def setShield(self, shield):  # 设置盾牌值
        self.shield = shield

    def defense(self, hero, monster):  # 防御方法
        if monster.shield > 0:
            damageValue = random.randint(0, hero.level * 10)
            monster.shield -= damageValue
            if monster.shield < 0:
                monster.currentHP += monster.shield
                monster.shield = 0
            print("%s受到攻击%d,剩余防御值%d，剩余生命%d" % (monster.name, damageValue, monster.shield, monster.currentHP))
            return False
        else:
            return True


def main():
    hero2 = Hero("奥特曼", 2, 200, 400)
    monster1 = Character("1级小怪兽", 1, 50, 50)
    monster2 = Character("2级小怪兽", 2, 50, 50)
    monster3 = bigMonster("3级小怪兽", 3, 150, 150)
    hero2.setFlexibility(0.5)  # 设置英雄的灵活度
    monster3.setShield(50)  # 设置3级小怪兽的防御值
    allMonster = [monster1, monster2, monster3]  # 将小怪兽全部放入列表中，依次攻击
    i = 0  # 第几个小怪兽
    number = 1  # 第几回合
    while hero2.currentHP > 0 and allMonster[i].currentHP > 0:
        print("******第%d回合*************************" % number)
        number += 1
        print("------%s正在攻击------" % allMonster[i].name)  # 怪兽先开始攻击
        if hero2.defense():  # 如果英雄防御失败
            allMonster[i].attackMethods(allMonster[i], hero2)
        if hero2.currentHP <= 0:  # 如果英雄死亡
            print("%s胜利" % allMonster[i].name)
            break
        print("------%s正在攻击------" % hero2.name)  # 英雄开始攻击
        if i < 2:  # 如果是1、2级小怪兽被攻击，没有盾牌
            hero2.attackMethods(hero2, allMonster[i])
            if allMonster[i].currentHP <= 0:  # 如果小怪兽死亡，换下一小怪兽
                i += 1
        elif i >= 2:  # 如果是3级小怪兽被攻击，先减少防御值
            if allMonster[i].defense(hero2, allMonster[i]):  # 防御值为0时
                hero2.attackMethods(hero2, allMonster[i])
                if allMonster[i].currentHP <= 0:  # 如果3级小怪兽死亡
                    print("%s胜利" % hero2.name)
                    break
        print()


main()
