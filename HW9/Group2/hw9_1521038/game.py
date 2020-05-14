from 小游戏.Hero import Hero
from 小游戏.Monster import Boss, Monster


def main():
    hero = Hero('叶问', 100, 1, 'human')
    monster1 = Monster('虾兵')
    monster2 = Monster('蟹将')
    boss = Boss('龙王', 100)
    monster_list = [monster1, monster2, boss]
    round = 1
    i = 0
    while hero.hp > 0 and len(monster_list) > 0:

        monster = monster_list[i]
        while monster.hp > 0:
            print('*'*20, '第{}回合'.format(round), '*'*20)
            hero.attack(monster)
            if monster.hp > 0:
                monster.attack(hero)
                if hero.hp <= 0:
                    break
            print(hero)
            print(monster)
            round += 1
        if monster.hp <= 0:
            monster_list.remove(monster)
            hero.upgrade()

    if hero.hp > 0:
        print('You win, {}'.format(hero.name))
    else:
        print('You lose,{}'.format(hero.name))


main()