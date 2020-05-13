from random import randint


class Devil(object):
    def __init__(self,name,lev,hp,lev_hp,atk,armor):
        self.name = name
        self.lev = lev
        self.hp = hp
        self.lev_hp = lev_hp
        self.atk = atk
        self.armor = armor

    def attack(self,hero):
        self.hp = self.hp - hero.atk + self.armor
        print(hero.name, "造成了", hero.atk, "点伤害，", self.name, "防御了", self.armor, "伤害,最终受到的伤害为",
              hero.atk - self.armor, ",", self.name, "剩余生命值为：", self.hp)


class Hero(object):
    def __init__(self, name, lev, hp, lev_hp, atk, armor):
        self.name = name
        self.lev = lev
        self.hp = hp
        self.lev_hp = lev_hp
        self.atk = atk
        self.armor = armor

    def attack(self,devil):
        self.hp = self.hp - devil.atk + self.armor
        print(devil.name, "造成了", devil.atk, "点伤害，", self.name, "防御了", self.armor, "伤害,最终受到的伤害为",
              devil.atk - self.armor, ",", self.name, "剩余生命值为：", self.hp)

class main(object):
    hero = Hero("hero",1,500,500,15,8)
    d1 = Devil('一号',1,100,100,5,5)
    d2 = Devil('二号',2,600,600,20,15)
    d3 = Devil('三号',3,1000,1000,50,35)
    devils = [d1,d2,d3]
    VS_round = 1
    print("第",VS_round,"回合")
    for i in devils:
        while hero.hp > 0:
            hero.atk = randint(10,80)
            if i.atk <= hero.armor:
                print("本次攻击被防御")
            else:
                hero.attack(i)
            VS_round +=1
            print("第",VS_round,"回合")
            i.atk = randint(5,30)
            if hero.atk <= i.armor:
                print("本次攻击被防御")
            else:
                i.attack(hero)
            VS_round += 1
            print("第", VS_round, "回合")
            if i.hp<=0:
                print("恭喜你已通过本关")
                hero.lev += 1
                if hero.lev == 2:
                   hero.lev_hp += 1000
                   hero.hp = hero.lev_hp
                elif hero.lev == 3:
                     hero.lev_hp += 1000
                     hero.hp = hero.lev_hp
                break
    if hero.hp<=0:
        print("怪兽胜利")
    else:
        print("英雄胜利")



if __name__ == '__main__':
    main()