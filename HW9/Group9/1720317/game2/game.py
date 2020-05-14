from Hero import Hero
from Monster import Monster, Boss


def main():
    # hero = Hero("张三丰", 30, 1, "human")
    hero = Hero("蓝精灵", 30, 1, "elves")
    monster1 = Monster("虾兵")
    monster2 = Monster("蟹将")
    boss = Boss("龙王")
    monster_list = [monster1, monster2, boss]
    round = 1
    while hero.get_hp() > 0 and len(monster_list) > 0:  # 当英雄未死亡，并且怪兽列表还有列表
        monster = next_monster(monster_list)  # 取第一个怪兽
        while monster.get_hp() > 0:  # 当怪兽的血量还有时，英雄开始攻击
            print("*" * 20, "第{}回合".format(round), "*" * 20)
            hero.attack(monster)  # 调用英雄的攻击方法
            if monster.get_hp() > 0:  # 如果怪兽未死亡，怪兽开始攻击英雄
                monster.attack(hero)  # 调用怪兽的攻击方法
                if hero.get_hp() <= 0:  # 如果英雄死亡，结束本层循环
                    break

            print(hero)
            print(monster)
            round += 1  # 回合次数加一
        if monster.get_hp() <= 0:  # 如果怪兽的血量小于等于1
            monster_list.remove(monster)  # 从怪兽列表中移除怪兽
            monster = next_monster(monster_list)  # 取下一个怪兽
            if monster:  # 如果怪兽存在
                hero.upgrade()  # 英雄升级，继续下一次作战

    if hero.get_hp() > 0:
        print("你赢了,{}".format(hero.get_name()))
    else:
        print("你输了,{}".format(hero.get_name()))


def next_monster(monster_list):
    """
    返回下一个怪兽
    :param monster_list:怪兽列表
    :return: 一个怪兽对象
    """
    assert type(monster_list) is list
    if monster_list:
        return monster_list[0]  # 取列表的第一个


main()
