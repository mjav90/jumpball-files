import pygame
import time
pygame.init()
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
def cordaddball(ball,x,y):
    s.blit(ball,(x,y))
def addplayer(player,x,y):
    s.blit(player,(x,y))
def addnet(net,x,y):
    s.blit(net,(x,y))
def reset():
    player = pygame.Rect(200,50,50,50)
    player2 = pygame.Rect(1000,50,50,50)
    x = 600
    y = 150
def onrect(rect,x,y):
    if rect[0]<x<rect[0]+rect[2] and rect[1]<y<rect[1]+rect[3]:
        return True
    return False
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
run1 = True
while run1:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                run1 = False
            if event.type == pygame.QUIT:
                pygame.quit()
s.fill(white)
pygame.display.update()
#نمونه توپ
player = pygame.image.load('player 1 (1)_prev_ui (1).png')
px = 100
py = 600
jump1 = False
Vyp = -5
player2 = pygame.image.load('player 1_prev_ui (2).png')
px2 = 1200
py2 = 600
jump2 = False
Vyp2 = -5
#نمونه تيرک
barrier1 = pygame.image.load('football2 net_prev_ui.png')
bx = 0
by = 0
barrier2 = pygame.image.load('football net_prev_ui.png')
bx2 = 0
by2 = 0
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
pygame.display.set_icon(ball)
tm = start_time
m=0
y_time=0
Vy = 0
alpha = -1
MaxVy = 10
Vx = 0
while run:
    #ضافه کردن بازيکن ها
    addplayer(player,px,py)
    addplayer(player2,px2,py2)
    #اگر آهنگ تمام شد دوباره اجراش کند
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
    key = pygame.key.get_pressed()
    if key[pygame.K_SPACE] == True:
        jump1 == True
    if jump1 == True:
        py += Vyp
        if key[pygame.K_a] == True:
            px -= 5
        if key[pygame.K_d] == True :
            px += 5
        py += Vyp
    if py <= 400:
        Vyp = -Vyp
    if py > 600:
        jump1 = False
        py = 600
    if px >1250 :
        px -= 5
    elif px <50 :
        px += 5
    if py >600 :
        py -= 5
    elif py <50 :
        py += 5
    if ((px) - x) >= -30 and (px - x) <= 30 :
        if (abs(py - y) < 100 and abs(py - y) > 10):
            if (Vx<0):
                Vx *= -0.000000000001
            else:
                Vx += 5
    elif (px) - x >= 50 and px - x <= 100 :
        if (py - y < 100 and py - y > 50) or (y - py < 100 and y - py > 50):
            Vx -= 5
    x += Vx
    cordaddball(ball,x,y)
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
    cordaddball(ball,x,y)
    ##player2
    if key[pygame.K_LEFT] == True:
        px2 -= 5
    if key[pygame.K_RIGHT] == True :
        px2 += 5
    if key[pygame.K_UP] == True:
        py2 -= 5
    if key[pygame.K_DOWN] == True :
        py2 += 5
    if px2 >1250 :
        px2 -= 5
    elif px2 <50 :
        px2 += 5
    if py2 >600:
        py2 -= 5
    elif py2 <50 :
        py2 += 5
    if (px2) - x <= 30 and px2 - x >= -30 :
        if (py2 - y < 100 and py2 - y > 50) or (y - py2 < 100 and y - py2 > 50):
            Vx += 5
    elif (px2) - x <= 100 and px2 - x >= 50 :
        if (abs(py2 - y) < 100 and abs(py2 - y) > 10):
            if (Vx>0):
                Vx *= -0.000000000001 
            else:
                Vx -= 5
    x += Vx
    #if (player2.y) - y < 40  and player2.y - y > -20 :
        #if (player2.x - x < 100 and player2.x - x > 50) or (x - player2.x < 100 and x - player2.x > 50):
            # Vy = -2
    #elif (player2.y) - y <= -50 and player2.y - y >= -100 :
        #if (player2.x - x < 100 and player2.x - x > 50) or (x - player2.x < 100 and x - player2.x > 50):
            #Vy = 2
    cordaddball(ball,x,y)
    addplayer(player,px,py)
    addplayer(player2,px2,py2)
    pygame.display.update()
print(time1[0],":",time1[1])
pygame.quit()
