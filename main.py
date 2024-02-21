import pygame
from random import randint
import entities

pygame.init()
clock = pygame.time.Clock()

run = True

font = pygame.font.Font('freesansbold.ttf', 32)
img1 = pygame.image.load("images/coin.png")
img2 = pygame.image.load("images/wheat.png")

class okno:
    x = 1920/4*3
    y = 1080/4*3

def mouse_pressed(x=0,y=0,button="LEFT"):
    if button == "RIGHT":
        for e in vse:
            if e.x < x < e.x+e.sirka:
                if e.y < y < e.y+e.vyska:
                    if char.wheat > 0:
                            char.wheat -= 1
                            char.coin += 1
                            if randint(1,10) == 6:
                                 snitch()
    else:
         vse.append(entities.Bullet(char.x,char.y,x,y,char))

middle = []
for i in range(0, int(okno.x//50)+1):
    if i%2 == 0:
        middle.append(pygame.rect.Rect(50*i,okno.y//2+5,50,10))
    middle.append(pygame.rect.Rect(0, okno.y//2+105,okno.x,15))
    middle.append(pygame.rect.Rect(0, okno.y//2-105,okno.x,15))

def redraw():
    window.fill((50,50,50))
    for rect in middle:
         pygame.draw.rect(window, (255,255,255), rect)
    window.blit(char.img,(char.x,char.y))
    for v in vse:
        window.blit(v.img,(v.x,v.y))
    window.blit(img1,(0,0))
    window.blit(img2, (0,30))
    text = font.render("%d" % char.coin ,True, (255,255,255))
    window.blit(text, (32, 0))
    text = font.render("%d" % char.wheat, True, (255, 255, 255))
    window.blit(text,(32, 30))
    pygame.display.update()

window = pygame.display.set_mode((okno.x,okno.y))
pygame.display.set_caption("dealer")

char = entities.Char()
vse = [char]
temp = pygame.image.load("images/client.png")
for i in range(0,3):
    vse.append(entities.Zakaznik(0,0,temp,7))
temp = None

def snitch():
    vse.append(entities.Cop(0,0,True,char.x,char.y))

def check_coll_class(prvni,druha):
    if prvni.x - druha.sirka < druha.x + druha.sirka//2 < prvni.x + prvni.sirka:
            if prvni.y - druha.sirka < druha.y + druha.sirka//2 < prvni.y + prvni.vyska:
                for x in range(0,prvni.sirka):
                    for y in range(0,prvni.vyska):
                        if druha.x < prvni.x+x < druha.x+druha.sirka:
                            if druha.y < prvni.y+y < druha.y+druha.vyska:
                                return(True)
snitch()
while run:
    clock.tick(60)
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if pygame.mouse.get_pressed()[0]:
                    mouse_pressed(pos[0],pos[1],"LEFT")
                if pygame.mouse.get_pressed()[2]:
                     mouse_pressed(pos[0],pos[1],"RIGHT")

    for e in vse:
         e.walk(vse,okno)

    redraw()

pygame.quit()
