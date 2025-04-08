import pygame
import time
pygame.init()
def cordaddball(x,y):
    s.blit(ball,(x,y))
def cordaddplayer(player,x,y):
    s.blit(player,(x,y))
s_width = 1327
s_height = 700
s = pygame.display.set_mode((s_width,s_height))
run=True
#نمونه توپ
player = pygame.image.load('player2.png')
player2 = pygame.image.load('player1.png')
player_x = 200
player_y = 200
player2_x = 1000
player2_y = 200
ball=pygame.image.load('ball_prev_ui.png')
x = 600
y = 150
start_time = pygame.time.get_ticks()
start_time2 = pygame.time.get_ticks()
##اهنگ اولیه
#sound3
sound3 = pygame.mixer.Sound("s3.wav") 
i3 = pygame.image.load('3.png')
s.blit(i3,(0,0))
pygame.display.update()
sound3.play()
time.sleep(1) 
sound3.stop()
#sound2
sound2 = pygame.mixer.Sound("s2.wav") 
i2 = pygame.image.load('2.png')
s.blit(i2,(0,0))
pygame.display.update()
sound2.play()  
time.sleep(1) 
sound2.stop()
#sound1
sound1 = pygame.mixer.Sound("s1.wav") 
i1 = pygame.image.load('1.png')
s.blit(i1,(0,0))
pygame.display.update()
sound1.play()  
time.sleep(1) 
sound1.stop()
##اهنگ بازي
sound = pygame.mixer.Sound('5.Mr. Blue Sky - Electric Light Orchestra Mr. Blue Sky.mp3')
sound.play()
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
    cordaddplayer(player,player_x,player_y)
    key = pygame.key.get_pressed()
    if key[pygame.K_a] == True:
        player_x -= 5
    if key[pygame.K_d] == True :
        player_x += 5
    if key[pygame.K_w] == True:
        player_y -= 5
    if key[pygame.K_s] == True :
        player_y += 5
    if player_x >1250 :
        player_x -= 5
    elif player_x <50 :
        player_x += 5
    if player_y >600 :
        player_y -= 5
    elif player_y <50 :
        player_y += 5
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
    if  y<600 and y_time2>=3000:
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
    if (player_x) - x < 40 and player_x - x > 10 :
        if (player_y - y < 30 and player_y - y > -20) or (y - player_y < 30 and y - player_y > -10):
            Vx += 3
    elif (player_x) - x <= 5 and player_x - x >= -40 :
        if (player_y - y < 30 and player_y - y > -20) or (y - player_y < 30 and y - player_y > -10):
            Vx -= 3
    ##player2
    cordaddplayer(player2,player2_x,player2_y)
    if key[pygame.K_LEFT] == True:
        player2_x -= 5
    if key[pygame.K_RIGHT] == True :
        player2_x += 5
    if key[pygame.K_UP] == True:
        player2_y -= 5
    if key[pygame.K_DOWN] == True :
        player2_y += 5
    if player2_x >1250 :
        player2_x -= 5
    elif player2_x <50 :
        player2_x += 5
    if player2_y >600:
        player2_y -= 5
    elif player2_y <50 :
        player2_y += 5
    if (player2_x) - x < 30 and player2_x - x > 10 :
        if (player2_y - y < 30 and player2_y - y > -20) or (y - player2_y < 30 and y - player2_y > -10):
            Vx += 3
    elif (player2_x) - x <= 5 and player2_x - x >= -50 :
        if (player2_y - y < 30 and player2_y - y > -20) or (y - player2_y < 30 and y - player2_y > -10):
            Vx -= 3
    cordaddball(x,y)
    pygame.display.update()
print(time1[0],":",time1[1])
pygame.quit()
