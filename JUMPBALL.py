import pygame
from tkinter import Tk
import time
pygame.init()
def cordaddball(x,y):
    s.blit(ball,(x,y))
s_width = 1327
s_height = 700
s = pygame.display.set_mode((s_width,s_height))
run=True
#نمونه توپ
player = pygame.Rect(200,50,50,50)
player2 = pygame.Rect(1000,50,50,50)
ball=pygame.image.load('ball_prev_ui.png')
x = 600
y = 150
start_time = pygame.time.get_ticks()
start_time2 = pygame.time.get_ticks()
##اهنگ اولیه
#sound3
sound3 = pygame.mixer.Sound("s3.wav") 
i3 = pygame.image.load('3.png')
s.fill((255,255,255))
s.blit(i3,(0,0))
pygame.display.update()
sound3.play()
sound3.set_volume(0.1)
time.sleep(1) 
sound3.stop()
#sound2
sound2 = pygame.mixer.Sound("s2.wav") 
i2 = pygame.image.load('2.png')
s.fill((255,255,255))
s.blit(i2,(0,0))
pygame.display.update()
sound2.play()  
sound2.set_volume(0.1)
time.sleep(1) 
sound2.stop()
#sound1
sound1 = pygame.mixer.Sound("s1.wav") 
i1 = pygame.image.load('1.png')
s.fill((255,255,255))
s.blit(i1,(0,0))
pygame.display.update()
sound1.play()  
sound1.set_volume(0.1)
time.sleep(1) 
sound1.stop()
##اهنگ بازي
sound = pygame.mixer.Sound('lige_bartar.mp3')
#بکگراند و عکس و اسم صفحه
backg= pygame.image.load('Screenshot (1).png')
cap=pygame.display.set_caption("jumpball")
pygame.display.set_icon(backg)
tm = start_time
m=0
y_time=0
Vy = 0
alpha = -1
MaxVy = 10
Vx = 0
while run:
    pygame.mixer.music.queue('lige_bartar.mp3')
    pygame.mixer.music.set_volume(0.1)
    x+= Vx
    y += Vy
    y_time2=pygame.time.get_ticks()-y_time
    tim=tm
    tm=(pygame.time.get_ticks()-start_time)//1000
    if tm>tim:
        time1=[m,tm]
    if tm == 60 :
        start_time = pygame.time.get_ticks()
        m=m+1
    s.fill((0,0,0))
    s.blit(backg,(0,0))
    #player1
    pygame.draw.rect(s,(255,0,0),player)
    key = pygame.key.get_pressed()
    if key[pygame.K_a] == True:
        player.move_ip( -5 , 0)
    if key[pygame.K_d] == True :
        player.move_ip(5, 0)
    if key[pygame.K_w] == True:
        player.move_ip(0  , -5)
    if key[pygame.K_s] == True :
        player.move_ip(0, 5)
    if player.x >1250 :
        player.move_ip(-5,0)
    elif player.x <50 :
        player.move_ip(5,0)
    if player.y >600 :
        player.move_ip(0,-5)
    elif player.y <50 :
        player.move_ip(0,5)
    if (player.x) - x < 40  and player.x - x > -20 :
        if (player.y - y < 100 and player.y - y > 50) or (y - player.y < 100 and y - player.y > 50):
            Vx -= 5
    elif (player.x) - x <= -50 and player.x - x >= -100 :
        if (player.y - y < 100 and player.y - y > 50) or (y - player.y < 100 and y - player.y > 50):
            Vx += 6
    #if (player.y) - y < 40  and player.y - y > -20 :
        #if (player.x - x < 100 and player.x - x > 50) or (x - player.x < 100 and x - player.x > 50):
            #Vy -= 2
    #elif (player.y) - y <= -50 and player.y - y >= -100 :
        #if (player.x - x < 100 and player.x - x > 50) or (x - player.x < 100 and x - player.x > 50):
            #Vy += 4
    #events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
    #end of events 
    #ball mechanics 
    if  y<600 and y_time2>=1000:
            y=y+round(Vy)
            Vy += 0.2
            if (Vy > MaxVy):
                Vy=MaxVy
    elif y>=600:
        if (Vy > 3):
            Vy=alpha * Vy
            y = y + Vy
    if x>=1200 :
        Vx = -2
        x = x + Vx
    elif x<=127 :
        Vx = 2
        x = x + Vx
    ##player2
    pygame.draw.rect(s,(0,0,255),player2)
    if key[pygame.K_LEFT] == True:
        player2.move_ip( -5 , 0)
    if key[pygame.K_RIGHT] == True :
        player2.move_ip(5, 0)
    if key[pygame.K_UP] == True:
        player2.move_ip(0  , -5)
    if key[pygame.K_DOWN] == True :
        player2.move_ip(0, 5)
    if player2.x >1250 :
        player2.move_ip(-5,0)
    elif player2.x <50 :
        player2.move_ip(5,0)
    if player2.y >600:
        player2.move_ip(0,-5)
    elif player2.y <50 :
        player2.move_ip(0,5)
    if (player2.x) - x <= 100 and player2.x - x >= 50 :
        if (player2.y - y < 100 and player2.y - y > 50) or (y - player2.y < 100 and y - player2.y > 50):
            Vx -= 6
    elif (player2.x) - x <= 20 and player2.x - x >= -40 :
        if (player2.y - y < 100 and player2.y - y > 50) or (y - player2.y < 100 and y - player2.y > 50):
            Vx += 5
    #if (player2.y) - y < 40  and player2.y - y > -20 :
        #if (player2.x - x < 100 and player2.x - x > 50) or (x - player2.x < 100 and x - player2.x > 50):
            #Vy -= 2
    #elif (player2.y) - y <= -50 and player2.y - y >= -100 :
        #if (player2.x - x < 100 and player2.x - x > 50) or (x - player2.x < 100 and x - player2.x > 50):
            #Vy += 4
    cordaddball(x,y)
    pygame.display.update()
print(time1[0],":",time1[1])
pygame.quit()