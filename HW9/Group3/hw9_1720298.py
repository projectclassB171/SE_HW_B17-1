from random import randint


class Hero():
    def __init__(self, name, hp, grade):
        self._name = name
        self._hp = hp
        self._grade = grade

    @property
    def name(self):
        return self._name

    @property
    def hp(self):
        return self._hp

    def upgrade(self):
        self._grade += 1
        self.hp +=200
        print("奖励：英雄 {}等级提升，血量+200".format(self.name))

    @hp.setter
    def hp(self, hp):
        self._hp = hp if hp >= 0 else 0

    def shanbi(self,m_grade):
        k = randint(0,100)
        if m_grade == 1:
            if k <10:
                return True
        elif m_grade == 2:
            if k <15:
                return True
        else:
            if k <20:
                return True
        return False


    def attack(self, monster):
        if self.shanbi(monster._grade):
            print("{}的攻击被闪避了，伤害为0".format(self.name))
        else:
            if self._grade == 1:
                harm = randint(10, 25)
            elif self._grade ==2:
                harm = randint(30, 50)
            else:
                harm = randint(60, 100)
            monster.hp -= harm
            print("{}造成了{}伤害".format(self.name, harm))

    def __str__(self):
        return '英雄:%s\n' % self._name + \
               '剩余生命值：%d\n' % self._hp + \
               '等级：%d\n' % self._grade


class Monster(Hero):


    @property
    def name(self):
        return self._name

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, hp):
        self._hp = hp if hp >= 0 else 0

    def shanbi(self, hero):
        k = randint(0,100)
        if hero._grade == 1:
            if k <10:
                return True
        elif hero._grade == 1:
            if k <20:
                return True
        else:
            if k <30:
                return True
        return False

    def attack(self, hero):  # 定义动态属性（攻击）
        if self.shanbi(hero):
            print("{}的攻击被闪避了，伤害为0".format(self.name))
        else:
            if self._grade == 1:
                harm = randint(10, 25)
            elif self._grade ==2:
                harm = randint(25, 50)
            else:
                harm = randint(50, 75)
            hero.hp -= harm
            print("{}造成了{}伤害".format(self.name,harm))

    def __str__(self):
        return '魂兽：%s\n' % self.name + \
               '生命值：%d\n' % self.hp


def main():
    u = Hero('霍雨浩', 600, 1)
    m1 = Monster('熊君', 200, 1)
    m2 = Monster('斜眼', 400,2)
    m3 = Monster('金眼黑龙王', 600,3)
    ms = [m1, m2, m3]
    at_round = 1
    for i in ms:
        while u.hp > 0 and i.hp > 0:
            print('===第%d回合===' % at_round)
            u.attack(i)
            print(i)
            if i.hp > 0:
                i.attack(u)
            print(u)
            at_round += 1
        if u.hp > 0:
            print('英雄  %s 胜利！' % u.name)
            if i == m3:
                print('屠龙的少年终成龙……')
            else:
                u.upgrade()

        else:
            print('魂兽 %s 胜利' % i.name)
            break


if __name__ == '__main__':
    main()


