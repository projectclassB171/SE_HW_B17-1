import sys
from random import randrange

from Hero import Hero
from Monster import Monster, Boss


def main():
    print('游戏开始')
    hero = Hero('大英雄', 100, 1, 'human')
    monster1 = Monster('第一个怪兽')
    monster2 = Monster('第二个怪兽', 70, 1)
    boss = Boss('大BOSS', 100)
    monster_list = [monster1, monster2, boss]
    round = 1
    while hero.get_hp() > 0 and len(monster_list) > 0:

        monster = next_monster(monster_list)
        while monster.get_hp() > 0:
            print('*' * 20, '回合 {}'.format(round), '*' * 20)
            hero.attack(monster)
            if monster.get_hp() > 0:
                monster.attack(hero)
                if hero.get_hp() <= 0:
                    break

                print(hero)
                print(monster)
                round += 1
            if monster.get_hp() <= 0:
                monster_list.remove(monster)
                hero.upgrade()
                monster = next_monster(monster_list)

            if hero.get_hp() > 0:
                print('英雄赢了，{}'.format(hero.get_name()))
            else:
                print('英雄输了')
    print('游戏结束')


def is_any_alive(monster_list):
    for monster in monster_list:
        if monster.get_hp() > 0:
            return True
        return False


def next_monster(monster_list):
    # assert type(monster_list) is list
    monster_len = len(monster_list)
    while True:
        if monster_len > 0:
            index = randrange(monster_len)
            monster = monster_list[index]
            if monster.get_hp() > 0:
                return monster
        else:
            print('你已经打败了所有的怪兽！')
            sys.exit(0)

if __name__ == '__main__':
    main()
