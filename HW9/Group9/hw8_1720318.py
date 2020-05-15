# coding=utf-8
import random


class hero:
    def __init__(self, name='name'):
        hero.name = name
        hero.level = 1
        hero.max_hp = hero.level * 75
        hero.current_hp = hero.level * 75

    def attack(self):
        attack_hp = random.randint(0, hero.level * 10)
        print '--英雄攻击回合--!'
        return attack_hp

    def uplevel(self):
        hero.current_hp += 10
        hero.level += 1
        print '--{} 升级,当前等级 {},当前血量 {}--'.format(hero.name, hero.level, hero.current_hp)
