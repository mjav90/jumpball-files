import pygame
import time
import socket
import asyncio
pygame.init()
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
scorefont = pygame.font.Font('BigShouldersStencil_18pt-ExtraBold.ttf',40)
scoreboard = pygame.image.load('images/scoreboard layout1.png')
scoreboard = pygame.transform.scale(scoreboard, (300,100))
def connect(a,b,c,d):
    host = "0.0.0.0"
    port = 5000

    print(socket.gethostname())

    mySocket = socket.socket()
    mySocket.bind((host,port))

    mySocket.listen(1)
    conn, addr = mySocket.accept()
    print ("Connection from: " + str(addr))
    while True:
            data = conn.recv(1024).decode()
            if not data:
                break
            data1 = str(a,b,c,d).upper()
            print ("sending: " + str(data1))
            conn.send(data1.encode())
            return data
    conn.close()
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
strtimg = pygame.image.load('images/onlinebutton.jpg')
strtimg2 = pygame.image.load('images/offlinebutton.jpg')
strtimg3 = pygame.image.load('images/aibutton.png')
strtimg4 = pygame.image.load('images/autojumpbutton.png')
jumpballlogo = pygame.image.load('images/jumpballlogo.jpg')
strtimg = pygame.transform.scale(strtimg,(100,100))
strtimg2 = pygame.transform.scale(strtimg2,(100,100))
strtimg3 = pygame.transform.scale(strtimg3,(100,100))
strtimg4 = pygame.transform.scale(strtimg4,(100,100))
jumpballlogo = pygame.transform.scale(jumpballlogo,(800,700))
strtsound = pygame.mixer.Sound('sounds/menu sound2.wav')
strtsound.play()
strtsound.set_volume(0.3)
stime = pygame.time.get_ticks()
s.fill(white)
s.blit(jumpballlogo, (300,0))
s.blit(strtimg, (100,100))
s.blit(strtimg2, (100,200))
s.blit(strtimg3, (100,300))
s.blit(strtimg4, (100,450))
pygame.display.update()
run1 = True
jump1 = True
jump2 = True
while run1:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                (xm,ym) = event.pos 
                if xm >= 100 and xm <= 200:
                    if (ym >= 100 and ym <= 200) or (ym >= 200 and ym <= 300) or (ym >= 300 and ym <= 400):
                        jump1 = False
                        jump2 = False              
                        strtsound.stop()
                        run1 = False
                    if (ym >= 450 and ym <= 550):
                        jump1 = True
                        jump2 = True
                        strtsound.stop()
                        run1 = False
            if event.type == pygame.QUIT:
                pygame.quit()
        if (pygame.time.get_ticks() - stime) >= 4400:
            strtsound.play()
            strtsound.set_volume(0.1)
strtsound.stop()
s.fill(white)
pygame.display.update()
#نمونه توپ
player = pygame.image.load('images/player 1 (1)_prev_ui (1).png')
px = 100
py = 600
Vyp = -6
player2 = pygame.image.load('images/player 1_prev_ui (2).png')
px2 = 1200
py2 = 600
Vyp2 = -6
#نمونه تيرک
barrier1 = pygame.image.load('images/images-Photoroom.png')
bx = 1130
by = 100
barrier1 = pygame.transform.scale(barrier1,(200,200))
barrier2 = pygame.image.load('images/images-Photoroom2.png')
bx2 = 0
by2 = 100
barrier2 = pygame.transform.scale(barrier2,(200,200))
ball=pygame.image.load('images/ball_prev_ui.png')
x = 600
y = 150
start_time = pygame.time.get_ticks()
start_time2 = pygame.time.get_ticks()
##اهنگ اولیه
#sound3
sound3 = pygame.mixer.Sound("sounds/s3.wav") 
i3 = pygame.image.load('images/3.png')
s.fill((255,255,255))
s.blit(i3,(0,0))
pygame.display.update()
sound3.play()
sound3.set_volume(0.1)
time.sleep(1) 
sound3.stop()
#sound2
sound2 = pygame.mixer.Sound("sounds/s2.wav") 
i2 = pygame.image.load('images/2.png')
s.fill((255,255,255))
s.blit(i2,(0,0))
pygame.display.update()
sound2.play()  
sound2.set_volume(0.1)
time.sleep(1) 
sound2.stop()
#sound1
sound1 = pygame.mixer.Sound("sounds/s1.wav") 
i1 = pygame.image.load('images/1.png')
s.fill((255,255,255))
s.blit(i1,(0,0))
pygame.display.update()
sound1.play()  
sound1.set_volume(0.1)
time.sleep(1) 
sound1.stop()
##اهنگ بازي
sound = pygame.mixer.Sound('sounds/lige_bartar.mp3')
sound.play()
sound.set_volume(0.4)
music_time = pygame.time.get_ticks()
#بکگراند و عکس و اسم صفحه
backg= pygame.image.load('images/Screenshot (1).png')
cap=pygame.display.set_caption("jumpball")
pygame.display.set_icon(ball)
tm = start_time
m=0
y_time=0
Vy = 0
alpha = -1
MaxVy = 10
Vx = 0
score1,score2 = 0,0
#jumpingsound
jumpsound = pygame.mixer.Sound('sounds/jumping sound.wav')
gms = pygame.mixer.Sound('sounds/gamestartsound.wav')
gms.play()
bouncesound = pygame.mixer.Sound('sounds/bounce sound.wav')
scoretime = pygame.time.get_ticks()
while run:
    #scores
    if x >= 1130 and x<=1230:
        if y >= 100 and y <= 200 and pygame.time.get_ticks() - scoretime >= 1000:
            score1 += 1
            scoretime = pygame.time.get_ticks()
            Vx = -7
    if x >= 0 and x<=100:
        if y >= 100 and y <= 200 and pygame.time.get_ticks() - scoretime >= 1000:
            score2 += 1
            scoretime = pygame.time.get_ticks()
            Vx = 7
    score = scorefont.render(f'{score1} - score - {score2}',True,(0,0,0))
    s.blit(scoreboard, (530,10))
    s.blit(score,(580,35))
    addnet(barrier1,bx,by)
    addnet(barrier2,bx2,by2)
    if y <= 110:
        if Vy < 0:
            Vy = -Vy 
    # also player 1 (I say also because this is newer than the other part)
    Vy += 0.0001
    if Vyp < 0:
        Vyp += 0.3
    elif Vyp > 0:
        Vyp += 0.5
    if Vyp > 7:
        Vyp = 7
    if jump1 == True:
        Vyp = -6
        jumpsound.play()
        jumpsound.set_volume(0.1)
    #ضافه کردن بازيکن ها
    addplayer(player,px,py)
    addplayer(player2,px2,py2)
    #اگر آهنگ تمام شد دوباره اجراش کند
    music_time2 = pygame.time.get_ticks()
    if ((music_time2 - music_time) // 1000) >= 170:
        music_time = pygame.time.get_ticks()
        sound.play()
        sound.set_volume(0.4)
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
    addnet(barrier1,bx,by)
    addnet(barrier2,bx2,by2)
    s.blit(scoreboard, (530,10))
    s.blit(score,(580,35))
    #player1#################################################################
    py += Vyp
    key = pygame.key.get_pressed()
    if Vyp == 0:
        if key[pygame.K_SPACE] == True:
            jump1 == True 
            Vyp = -6    
    if Vyp != 0:
        if key[pygame.K_a] == True:
            px -= 5
        if key[pygame.K_d] == True :
            px += 5
    if py <= 500:
        Vyp = -Vyp
    if py > 600:
        Vyp = 0
        py = 600
        jump1 = False
    if px >1250 :
        px -= 5
    elif px <50 :
        px += 5
    elif py <50 :
        py += 5
    addplayer(player,px,py)
    if ((px) - x) >= -30 and (px - x) <= 30 :
        if (abs(py - y) < 100 and abs(py - y) > 10):
            if (Vx<0):
                Vx *= -0.000000000001
            else:
                Vx += 5
    elif (px) - x >= 50 and px - x <= 100 :
        if (py - y < 100 and py - y > 50) or (y - py < 100 and y - py > 50):
            Vx -= 5
    if px - x >= -100 and px - x <= 0:
        if py - y < 100 and py - y >= 0:
            if Vy < 0:
                Vy -= 2
            else:
                Vy = -Vy + 1
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
        bouncesound.play()
        bouncesound.set_volume(0.4)
    if x>=1200 :
        Vx = -2
        x = x + Vx
        bouncesound.play()
        bouncesound.set_volume(0.4)
    elif x<=50 :
        Vx = 2
        x = x + Vx
        bouncesound.play()
        bouncesound.set_volume(0.4)
    if y < 30 :
        Vy = 5
        y += Vy
        bouncesound.play()
        bouncesound.set_volume(0.4)
    cordaddball(ball,x,y)
    ##player2
    if Vyp2 < 0:
        Vyp2 += 0.3
    elif Vyp2 > 0:
        Vyp2 += 0.5
    if Vyp2 > 7:
        Vyp2 = 7
    if Vyp2 == 0:
        Vyp2 = -6
        jumpsound.play()
        jumpsound.set_volume(0.1)
    key = pygame.key.get_pressed()
    if jump2 != True:
        if key[pygame.K_w] == True:
            jump2 == True      
    if jump2 == True:
        py2 += Vyp2
        if key[pygame.K_LEFT] == True:
            px2 -= 5
        if key[pygame.K_RIGHT] == True :
            px2 += 5
        py2 += Vyp2
    if py2 <= 500:
        Vyp2 = -Vyp2
    if py2 > 600:
        Vyp2 = 0
        py2 = 600
    if px2 >1250 :
        px2 -= 5
    elif px2 <50 :
        px2 += 5
    if py2 >600:
        py2 -= 5
    elif py2 <50 :
        py2 += 5
    addplayer(player2,px2,py2)
    if (px2) - x <= 20 and px2 - x >= -40 :
        if (py2 - y < 100 and py2 - y > 50) or (y - py2 < 100 and y - py2 > 50):
            Vx += 5
    elif (px2) - x <= 100 and px2 - x >= 40 :
        if (abs(py2 - y) < 100 and abs(py2 - y) > 10):
            if (Vx>0):
                Vx *= -0.000000000001 
            else:
                Vx -= 5
    if px2 - x >= -70 and px2 - x <= 70:
        if py2 - y < 50 and py2 - y >= 0:
            if Vy < 0:
                Vy -= 2
            else:
                Vy = -Vy + 1
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
    addnet(barrier1,bx,by)
    addnet(barrier2,bx2,by2)
    s.blit(scoreboard, (530,10))
    s.blit(score,(580,35))
    pygame.display.update()
    pygame.time.Clock().tick(5000)
    addnet(barrier1,bx,by)
    addnet(barrier2,bx2,by2)
print(time1[0],":",time1[1])
pygame.quit()
