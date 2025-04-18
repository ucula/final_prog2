import random
from spritesheet import SpriteSheet
import pygame as pg
from config import Configs
from ui import AllUI
import math


class Monster_TMP:
    monster = ["slime", "goblin", "hop"]
    def __init__(self, screen, x_off=0, y_off=0, x=0, y=0, name="", health=0, damage=0, level=0, evasion=0,
                steps=0, size=0, pixel=0):
        self.ui = AllUI(screen)
        self.name = name
        self.x_offset = x_off
        self.y_offset = y_off
        self.encounter_dist = 25
        self.x = x
        self.y = y
        self.health = health
        self.damage = damage
        self.level = level
        self.evasion = evasion

        self.ready = False
        
        # For animating
        self.animation = []
        self.animation_steps = steps
        self.last_up = pg.time.get_ticks()
        self.cool_down = 100
        self.frame = 0
        self.size = size
        self.pixel = pixel

    def reduce_hp(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.die()

    # Show mob info and ready for start fight trigger
    # รอใส่ข้อมูลมอน
    def draw_mon(self):
        sprite_sheet_image = pg.image.load(Configs.monster(self.name)).convert_alpha()
        sprite_sheet = SpriteSheet(sprite_sheet_image)
        current_time = pg.time.get_ticks()
        if current_time - self.last_up >= self.cool_down:
            self.frame += 1
            self.last_up = current_time
            if self.frame >= len(self.animation):
                self.frame = 0
        for i in range(self.animation_steps):
            self.animation.append(sprite_sheet.get_monster((0, 0), i, self.pixel, self.pixel, self.size, Configs.get('BLACK')))
    
    def in_range(self, player):
        distance = self.calculate_dist(player)
        if distance < self.encounter_dist:
            self.show_info(self.name)
            return True
        else:
            self.ui.prep_size = 0

    def show_info(self, name=None):
        self.ui.draw_mob_info(name)
        # print(self.ready)  

    # Calculate dist player from mobs
    def calculate_dist(self, player):
        a = player.x - (self.x + self.x_offset)
        b = player.y - (self.y + self.y_offset)
        distance = math.hypot(a, b)
        return distance 

    def die(self):
        pass

    def attack(self):
        pass

    def dodge(self):
        pass

class Slime(Monster_TMP):
    def __init__(self, screen, x_off, y_off, x, y, name="SLIME", health=10, damage=1, level=1, evasion=0.1,
                 steps=6, size=1, pixel=128):
        super().__init__(screen, x_off, y_off, x, y, name, health, damage, level, evasion, steps, size, pixel) 
   
class Goblin(Monster_TMP):
    def __init__(self, screen, x_off, y_off, x, y, name="GOBLIN", health=30, damage=5, level=2, evasion=0.2,
                 steps=3, size=1, pixel=300):
        super().__init__(screen, x_off, y_off, x, y, name, health, damage, level, evasion, steps, size, pixel) 

        # Skill rate
        self.hunter_instinct_rate = 0.14
    
    def hunter_instinct(self):
        self.damage += 2

class Dark_Goblin(Goblin):
    def __init__(self, screen, x_off, y_off, x, y, name="DARK", health=30, damage=10, level=5, evasion=0.7,
                 steps=3, size=3, pixel=64):
        super().__init__(screen, x_off, y_off, x, y, name, health, damage, level, evasion, steps, size, pixel) 
