import pygame
import time
pygame.init()
def cordaddball(x,y):
    s.blit(ball,(x,y))
def reset():
    player = pygame.Rect(200,50,50,50)
    player2 = pygame.Rect(1000,50,50,50)
    x = 600
    y = 150
def onrect(rect,x,y):
    if rect[0]<x<rect[0]+rect[2] and rect[1]<y<rect[1]+rect[3]:
        return True
    return False
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
s_width = 1327
s_height = 700
s = pygame.display.set_mode((s_width,s_height))
run=True
#start_menu
font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render('start game', True, green, blue)
button = text.get_rect()
X = 670
Y = 500
button.center = (X // 2, Y // 2)
s.blit(text, button)
pygame.display.update()
s.fill(white)
while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                break
            if event.type == pygame.QUIT:
                pygame.quit()
s.fill(white)
pygame.display.update()
#نمونه توپ
player = pygame.Rect(200,50,50,50)
player2 = pygame.Rect(1000,50,50,50)
#نمونه تيرک
barrier1 = pygame.Rect(50,275,50,50)
barrier2 = pygame.Rect(1175,275,50,50)
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
sound.play()
sound.set_volume(0.1)
music_time = pygame.time.get_ticks()
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
    music_time2 = pygame.time.get_ticks()
    if ((music_time2 - music_time) // 1000) >= 170:
        music_time = pygame.time.get_ticks()
        sound.play()
        sound.set_volume(0.1)
    if y >=800:
        y = 200
    x += Vx
    y += Vy
    pygame.display.update()
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
    if ((player.x) - x) >= -30 and (player.x - x) <= 30 :
        if (abs(player.y - y) < 100 and abs(player.y - y) > 10):
            if (Vx<0):
                Vx *= -0.000000000001
            else:
                Vx += 5
    elif (player.x) - x >= 50 and player.x - x <= 100 :
        if (player.y - y < 100 and player.y - y > 50) or (y - player.y < 100 and y - player.y > 50):
            Vx -= 5
    pygame.draw.rect(s,(255,0,0),player)
    x += Vx
    cordaddball(x,y)
    #if (player.y) - y < 40  and player.y - y > -20 :
        #if (player.x - x < 100 and player.x - x > 50) or (x - player.x < 100 and x - player.x > 50):
            #Vy = -2        
    #elif (player.y) - y <= -50 and player.y - y >= -100 :
        #if (player.x - x < 100 and player.x - x > 50) or (x - player.x < 100 and x - player.x > 50):
            #Vy = 2
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
    cordaddball(x,y)
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
    if (player2.x) - x <= 30 and player2.x - x >= -30 :
        if (player2.y - y < 100 and player2.y - y > 50) or (y - player2.y < 100 and y - player2.y > 50):
            Vx += 5
    elif (player2.x) - x <= 100 and player2.x - x >= 50 :
        if (abs(player2.y - y) < 100 and abs(player2.y - y) > 10):
            if (Vx>0):
                Vx *= -0.000000000001 
            else:
                Vx -= 5
    pygame.draw.rect(s,(0,0,255),player2)
    x += Vx
    #if (player2.y) - y < 40  and player2.y - y > -20 :
        #if (player2.x - x < 100 and player2.x - x > 50) or (x - player2.x < 100 and x - player2.x > 50):
            # Vy = -2
    #elif (player2.y) - y <= -50 and player2.y - y >= -100 :
        #if (player2.x - x < 100 and player2.x - x > 50) or (x - player2.x < 100 and x - player2.x > 50):
            #Vy = 2
    cordaddball(x,y)
    pygame.display.update()
print(time1[0],":",time1[1])
pygame.quit()
