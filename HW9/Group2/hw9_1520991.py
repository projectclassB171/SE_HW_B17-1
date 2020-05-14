
import random as x

class Hero:
    def __init__(self, name):    
        self.name = name     
        self.level = 1       
        self.max_hp = self.level*80
        self.current_hp = self.level*80 

    def attack(self):
        atk = x.randint(0, self.level*5)
        print("---{}进攻回合---".format(self.name))
        return atk           
def upgrade(self): 
    self.current_hp =Hero.current_hp+ 10    #当前血量值
        Hero.level = Hero.level + 1
        print("{} 升级,当前等级 {},当前血量 {}".format(self.name, self.level, self.current_hp))


class human(Hero):            
    def __init__(self, name):
        super(human, self).__init__(name)   
        self.avd = 0.5   
     
def defense(self, atk):     
        is_hurt = r.random()        
        if self.avd < is_hurt:
            self.current_hp -= atk
            print("{} 受到 {}点伤害,当前血量为{}".format(self.name, atk, self.current_hp))
        else:
            print("{}MISS")


class hero_Spirit(Hero):          
    def __init__(self, name):
        super(hero_Spirit, self).__init__(name)
        self.avd = 0.7      

def defense(self, atk):    
        is_hurt = x.random()
        if self.avd < is_hurt:
            self.current_hp -= atk
            print("{} 受到 {}点伤害,当前血量为 {}".format(self.name, atk, self.current_hp))
        else:
            print("PDDMISS")


class Monster:
    def __init__(self, name, level):
        self.name = name      
        self.level = level    
        self.max_hp = int(level * 30) 
        self.current_hp = int(level * 30)  

    def attack(self):
        atk = x.randint(0, self.level*10)
        print("---{} 发起攻击回合---".format(self.name))
        return atk

    def defense(self, atk):
        self.current_hp -= atk
        print("{} 受到 {} 点伤害,当前血量 {}".format(self.name, atk, self.current_hp))


class BigMonster(Monster):      
    def __init__(self, name, level):
        super(BigMonster, self).__init__(name, level)
        self.shield = self.max_hp * 0.2  

    def defense(self, atk):  
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


def main():
h = hero_Spirit("PDD")  
m1 = Monster("怪兽1号：55Whtie", 1)
    m2 = Monster("怪兽2号:一条小团团", 2)
    m3 = BigMonster("怪兽boss：智勋", 2)
    enemy = [m1, m2, m3]
    r = 1
    while True:
        print("---第{}回合---".format(r))
        enemy[0].defense(h.attack())   
        if enemy[0].current_hp <= 0:  
            print("{} 阵亡".format(enemy[0].name))
            h.upgrade()
            del enemy[0]
        if len(enemy) == 0:     
            print("{} YOU WIN ".format(h.name))
            return
        for each in enemy:      
            h.defense(each.attack())
            print("{}YOU LOSE".format(h.name))
            return
        r += 1   

if __name__ == '__main__':
    main()

#
---第1回合---
---PDD发动攻击回合---
怪兽1号：55Whtie 受到 1 点伤害,当前血量 29
---怪兽1号：55Whtie 发起攻击回合---
PDD MISS
---怪兽2号:一条小团团 发起攻击回合---
PDD受到 5点伤害,当前血量为 75
---怪兽boss：智勋 发起攻击回合---
PDD MISS
---第2回合---
---PDD发动攻击回合---
怪兽1号：55Whtie 受到 2 点伤害,当前血量 27
---怪兽1号：55Whtie 发起攻击回合---
PDD 受到 5点伤害,当前血量为 70
---怪兽2号:一条小团团 发起攻击回合---
PDD MISS
---怪兽boss：智勋 发起攻击回合---
PDD 受到 5点伤害,当前血量为 65
---第3回合---
---PDD发动攻击回合---
怪兽1号：55Whtie 受到 2 点伤害,当前血量 25
---怪兽1号：55Whtie 发起攻击回合---
PDD 受到 2点伤害,当前血量为 63
---怪兽2号:一条小团团 发起攻击回合---
PDD MISS
---怪兽boss：智勋 发起攻击回合---
PDD MISS
---第4回合---
---PDD发动攻击回合---
怪兽1号：55Whtie 受到 2 点伤害,当前血量 23
---怪兽1号：55Whtie 发起攻击回合---
PDD MISS
---怪兽2号:一条小团团 发起攻击回合---
PDD 受到 8点伤害,当前血量为 55
---怪兽boss：智勋 发起攻击回合---
PDD MISS
---第5回合---
---PDD发动攻击回合---
怪兽1号：55Whtie 受到 3 点伤害,当前血量 20
---怪兽1号：55Whtie 发起攻击回合---
PDD 受到 4点伤害,当前血量为 51
---怪兽2号:一条小团团 发起攻击回合---
PDDMISS
---怪兽boss：智勋 发起攻击回合---
PDD 受到 7点伤害,当前血量为 44
---第6回合---
---PDD发动攻击回合---
怪兽1号：55Whtie 受到 1 点伤害,当前血量 19
---怪兽1号：55Whtie 发起攻击回合---
PDD 受到 4点伤害,当前血量为 40
---怪兽2号:一条小团团 发起攻击回合---
PDDMISS
---怪兽boss：智勋 发起攻击回合---
PDD 受到 0点伤害,当前血量为 40
---第7回合---
---PDD发动攻击回合---
怪兽1号：55Whtie 受到 8 点伤害,当前血量 11
---怪兽1号：55Whtie 发起攻击回合---
PDDMISS
---怪兽2号:一条小团团 发起攻击回合---
PDDMISS
---怪兽boss：智勋 发起攻击回合---
PDD 受到 10点伤害,当前血量为 30
---第8回合---
---PDD发动攻击回合---
怪兽1号：55Whtie 受到 2 点伤害,当前血量 9
---怪兽1号：55Whtie 发起攻击回合---
PDDMISS
---怪兽2号:一条小团团 发起攻击回合---
PDD 受到 3点伤害,当前血量为 27
---怪兽boss：智勋 发起攻击回合---
PDD 受到 0点伤害,当前血量为 27
---第9回合---
---PDD发动攻击回合---
怪兽1号：55Whtie 受到 2 点伤害,当前血量 7
---怪兽1号：55Whtie 发起攻击回合---
PDDMISS
---怪兽2号:一条小团团 发起攻击回合---
PDD 受到 14点伤害,当前血量为 13
---怪兽boss：智勋 发起攻击回合---
PDDMISS
---第10回合---
---PDD发动攻击回合---
怪兽1号：55Whtie 受到 1 点伤害,当前血量 6
---怪兽1号：55Whtie 发起攻击回合---
PDDMISS
---怪兽2号:一条小团团 发起攻击回合---
PDD 受到 8点伤害,当前血量为 5
---怪兽boss：智勋 发起攻击回合---
PDD 受到 14点伤害,当前血量为 -9
PDD YOU LOSE
'''