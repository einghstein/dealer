import pygame
from random import randint
import math

def check_coll_class(prvni,druha):
    if prvni.x - druha.sirka < druha.x + druha.sirka//2 < prvni.x + prvni.sirka:
            if prvni.y - druha.sirka < druha.y + druha.sirka//2 < prvni.y + prvni.vyska:
                for x in range(0,prvni.sirka):
                    for y in range(0,prvni.vyska):
                        if druha.x < prvni.x+x < druha.x+druha.sirka:
                            if druha.y < prvni.y+y < druha.y+druha.vyska:
                                return(True)

class Zakaznik:
    def __init__(self, x, y, img, speed):
        self.img = img
        self.x=x
        self.y=y
        self.sirka = img.get_width()
        self.vyska = img.get_height()
        self.dir_x = 0
        self.dir_y = 0
        self.speed = speed
    def walk(self,vse,window):
        for i in range(1,self.speed):
            if self.dir_x == self.x:
                if self.dir_y == self.y:
                    self.dir_x = randint(0,window.x-self.sirka)
                    self.dir_y = randint(0,window.y-self.vyska)
            else:
                if self.x > self.dir_x:
                    self.x -= 1
                    self.img = pygame.image.load("images/c_left.png")
                else:
                    self.x += 1
                    self.img = pygame.image.load("images/c_right.png")
            if self.dir_y != self.y:
                if self.y > self.dir_y:
                    self.y -= 1
                    self.img = pygame.image.load("images/c_back.png")
                else:
                    self.y += 1
                    self.img = pygame.image.load("images/c_forward.png")
        
class Char:
    if randint(0,100) == 1:
        img = pygame.image.load("images/pe.png")
    else:
        img = pygame.image.load("images/forward.png")
    x = 1920//2
    y = 1080//2
    sirka = img.get_width()
    vyska = img.get_height()
    rychlost = 8
    wheat = 1
    coin = 0
    def walk(self,vse,window):
            keys = pygame.key.get_pressed()
            if keys[pygame.K_d] and self.x < 1920-self.sirka:
                self.x = self.x+self.rychlost
                self.img = pygame.image.load("images/right.png")
                for t in vse:
                    if t != self:
                        if check_coll_class(self,t):
                            self.x = (self.x-self.rychlost)

            if keys[pygame.K_a] and self.x > self.rychlost:
                self.x = self.x-self.rychlost
                self.img = pygame.image.load("images/left.png")
                for t in vse:
                    if t != self:
                        if check_coll_class(self,t):
                            self.x = (self.x+self.rychlost)

            if keys[pygame.K_w] and self.y > self.rychlost:
                self.y = self.y-self.rychlost
                self.img = pygame.image.load("images/back.png")
                for t in vse:
                    if t != self:
                        if check_coll_class(self,t):
                            self.y = self.y+self.rychlost

            if keys[pygame.K_s] and self.y < 1080-self.vyska:
                self.y = self.y+self.rychlost
                self.img = pygame.image.load("images/forward.png")
                for t in vse:
                    if t != self:
                        if check_coll_class(self,t):
                            self.y = self.y-self.rychlost

class Bullet:
    def __init__(self,x,y,mx,my,shooter):
        self.img = pygame.image.load("images/bullet.png")
        self.sirka = self.img.get_width()
        self.vyska = self.img.get_height()
        self.x = x
        self.y = y
        self.mx = mx + self.sirka
        self.my = my + self.vyska
        speed = 15
        self.angle = math.atan2(y - my, x - mx)
        self.x_vel = math.cos(self.angle) * speed
        self.y_vel = math.sin(self.angle) * speed
        self.shooter = shooter
    def walk(self,bullets,window):
        self.x -= self.x_vel
        self.y -= self.y_vel
        for e in bullets:
            if e != self.shooter and e != self:
                if check_coll_class(self,e):
                    bullets.remove(e)
                    bullets.remove(self)
        try:
            if self.x < 0 or self.x > window.get_width():
                bullets.pop(bullets.index(self))
            if self.y < 0 or self.y > window.get_width():
                bullets.pop(bullets.index(self))
        except:
            print("lag")  