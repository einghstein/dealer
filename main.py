import pygame
from random import randint
import entities

pygame.init()
clock = pygame.time.Clock()

run = True

font = pygame.font.Font('freesansbold.ttf', 32)

img1 = pygame.image.load("images/coin.png")

class okno:
    x = 1920
    y = 1080

def mouse_pressed(x=0,y=0,button="LEFT"):
    if button == "RIGHT":
        for e in vse:
            if e.x < x < e.x +e.sirka:
                if e.y < y < e.y+e.vyska:
                    if char.wheat > 0: 
                            char.wheat -= 1
                            char.coin += 1
    else:
        if char.shoot_cooldown < 0:
            vse.append(entities.Bullet(char.x,char.y,x,y,char))
            char.shoot_cooldown = 15
        else:
            pass
            #play empty shoot sound

def redraw():
    window.fill((50,50,50))
    window.blit(char.img,(char.x,char.y))
    for v in vse:
        window.blit(v.img,(v.x,v.y))
    window.blit(img1,(0,0))
    text = font.render("%d" % char.coin ,True, (255,255,255))
    window.blit(text, (32, 0))
    pygame.display.update()

window = pygame.display.set_mode((okno.x,okno.y))
pygame.display.set_caption("change me")

char = entities.Char()
vse = [char]
temp = pygame.image.load("images/client.png")
for i in range(0,3):
    vse.append(entities.Zakaznik(0,0,temp,7))
temp = None

def check_coll_class(prvni,druha):
    if prvni.x - druha.sirka < druha.x + druha.sirka//2 < prvni.x + prvni.sirka:
            if prvni.y - druha.sirka < druha.y + druha.sirka//2 < prvni.y + prvni.vyska:
                for x in range(0,prvni.sirka):
                    for y in range(0,prvni.vyska):
                        if druha.x < prvni.x+x < druha.x+druha.sirka:
                            if druha.y < prvni.y+y < druha.y+druha.vyska:
                                return(True)

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
    if char.shoot_cooldown > -1:
        char.shoot_cooldown -= 1
    
    for e in vse:
         e.walk(vse,okno)

    redraw()

pygame.quit()
