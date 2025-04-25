import pygame
import time
import socket
import asyncio
import struct
pygame.init()
HOST = '127.0.0.1'  # Server's IP address; change as necessary for online deployment.
PORT = 12341       # The same port as used by the server.

pause_button = pygame.image.load("images/pause button.png")
pause_button = pygame.transform.scale(pause_button,(50,50))
def send_coordinates(x, y):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))
    
    # Pack the x and y coordinates into 8 bytes.
    data = struct.pack("!ii", x, y)
    
    # Send the packed data to the server.
    client.sendall(data)
    
    # Receive the server's response (expecting 8 bytes in this case).
    response = client.recv(8)
    received_x, received_y = struct.unpack("!ii", response)
    
    print(f"Server responded with: x={received_x}, y={received_y}")
    client.close()
    return x,y
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
scorefont = pygame.font.Font('BigShouldersStencil_18pt-ExtraBold.ttf',38)
scoreboard = pygame.image.load('images/scoreboard layout1.png')
scoreboard = pygame.transform.scale(scoreboard, (300,100))
scoresound = pygame.mixer.Sound('sounds/Collect.wav')
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
strtimg2 = pygame.image.load('images/offlinebutton.jpg')
strtimg3 = pygame.image.load('images/aibutton.png')
strtimg5 = pygame.image.load('images/mobilebutton.png')
jumpballlogo = pygame.image.load('images/jumpballlogo.jpeg')
strtimg2 = pygame.transform.scale(strtimg2,(100,100))
strtimg3 = pygame.transform.scale(strtimg3,(100,100))
strtimg5 = pygame.transform.scale(strtimg5,(100,100))
jumpballlogo = pygame.transform.scale(jumpballlogo,(1327,900))
strtsound = pygame.mixer.Sound('sounds/menu sound2.wav')
strtsound.play()
strtsound.set_volume(0.3)
stime = pygame.time.get_ticks()
s.fill(white)
s.blit(jumpballlogo, (0,-100))
s.blit(strtimg2, (100,100))
s.blit(strtimg3, (100,300))
s.blit(strtimg5, (100,550))
pygame.display.update()
run1 = True
jump1 = True
jump2 = True
mobile_mode = False 
AImode = False
while run1:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                (xm,ym) = event.pos 
                if xm >= 100 and xm <= 200:
                    #offline
                    if (ym >= 100 and ym <= 200):
                        jump1 = False
                        jump2 = False              
                        strtsound.stop()
                        run1 = False
                    #mobile mode
                    if (ym >= 550 and ym <= 650):
                        jump1 = False
                        jump2 = False
                        mobile_mode = True 
                        strtsound.stop()
                        run1 = False
                        # Client setup
                        HOST = '192.168.1.5'  # Same as server's HOST
                        PORT = 12341       # Same as server's PORT

                        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        client_socket.connect((HOST, PORT))

                        print("Connected to the server!")
                    if (ym >= 300 and ym <= 400):
                        AImode = True 
                        jump1 = False 
                        jump2 = False 
                        strtsound.stop()
                        run1 = False 
                        break
            if event.type == pygame.QUIT:
                pygame.quit()
        if (pygame.time.get_ticks() - stime) >= 4400:
            strtsound.play()
            strtsound.set_volume(0.1)
strtsound.stop()
mobile_mode = False
if mobile_mode == True:
    arrow_right = pygame.image.load('images/rightarrow.png')
    arrow_left = pygame.image.load('images/leftarrow.png')
    jumpbutton = pygame.image.load('images/jumpbutton.png')
    arrow_right = pygame.transform.scale(arrow_right,(50,50))
    arrow_left = pygame.transform.scale(arrow_left,(60,100))
    jumpbutton = pygame.transform.scale(jumpbutton,(50,50))
    while True:
        try:
            response = client_socket.recv(1024).decode()
            print(response)
            if response != 1:
                data = 1
                client_socket.sendall(data.encode())
                player = 1 
            else:
                player = 2
                break 
        except:
            print("waiting for player 2......")
stime = pygame.time.get_ticks()
gtime = 90
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
MaxVy = 6
Vx = 0
MaxVx = 4
score1,score2 = 0,0
#jumpingsound
jumpsound = pygame.mixer.Sound('sounds/jumping sound.wav')
gms = pygame.mixer.Sound('sounds/gamestartsound.wav')
gms.play()
bouncesound = pygame.mixer.Sound('sounds/bounce sound.wav')
scoretime = pygame.time.get_ticks()
#all the things on top for returning to the main menu
def show_start_menu_and_initialize():
    # Load images
    strtimg2 = pygame.image.load('images/offlinebutton.jpg')
    strtimg3 = pygame.image.load('images/aibutton.png')
    strtimg5 = pygame.image.load('images/mobilebutton.png')
    jumpballlogo = pygame.image.load('images/jumpballlogo.jpeg')
    strtimg2 = pygame.transform.scale(strtimg2, (100, 100))
    strtimg3 = pygame.transform.scale(strtimg3, (100, 100))
    strtimg5 = pygame.transform.scale(strtimg5, (100, 100))
    jumpballlogo = pygame.transform.scale(jumpballlogo, (1327, 900))

    # Load and play start sound
    strtsound = pygame.mixer.Sound('sounds/menu sound2.wav')
    strtsound.play()
    strtsound.set_volume(0.3)

    stime = pygame.time.get_ticks()
    s.fill(((255,255,255)))
    s.blit(jumpballlogo, (0, -100))
    s.blit(strtimg2, (100, 100))
    s.blit(strtimg3, (100, 300))
    s.blit(strtimg5, (100, 550))
    pygame.display.update()

    run1 = True
    jump1 = True
    jump2 = True
    mobile_mode = False
    AImode = False

    while run1:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                (xm, ym) = event.pos
                if 100 <= xm <= 200:
                    if 100 <= ym <= 200:
                        jump1 = False
                        jump2 = False
                        strtsound.stop()
                        run1 = False
                    elif 550 <= ym <= 650:
                        jump1 = False
                        jump2 = False
                        mobile_mode = True
                        strtsound.stop()
                        run1 = False
                        HOST = '192.168.1.5'
                        PORT = 12341
                        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        client_socket.connect((HOST, PORT))
                        print("Connected to the server!")
                    elif 300 <= ym <= 400:
                        AImode = True
                        jump1 = False
                        jump2 = False
                        strtsound.stop()
                        run1 = False
                        break
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        if (pygame.time.get_ticks() - stime) >= 4400:
            strtsound.play()
            strtsound.set_volume(0.1)

    strtsound.stop()

    if mobile_mode:
        arrow_right = pygame.image.load('images/rightarrow.png')
        arrow_left = pygame.image.load('images/leftarrow.png')
        jumpbutton = pygame.image.load('images/jumpbutton.png')
        arrow_right = pygame.transform.scale(arrow_right, (50, 50))
        arrow_left = pygame.transform.scale(arrow_left, (60, 100))
        jumpbutton = pygame.transform.scale(jumpbutton, (50, 50))

        while True:
            try:
                response = client_socket.recv(1024).decode()
                print(response)
                if response != '1':
                    data = '1'
                    client_socket.sendall(data.encode())
                    player = 1
                else:
                    player = 2
                    break
            except:
                print("waiting for player 2......")

    stime = pygame.time.get_ticks()
    gtime = 90
    s.fill(((0,0,0)))
    pygame.display.update()

    # Countdown sequence
    for count, sound_path in [("3", "sounds/s3.wav"), ("2", "sounds/s2.wav"), ("1", "sounds/s1.wav")]:
        sound = pygame.mixer.Sound(sound_path)
        img = pygame.image.load(f'images/{count}.png')
        s.fill((255, 255, 255))
        s.blit(img, (0, 0))
        pygame.display.update()
        sound.play()
        sound.set_volume(0.1)
        time.sleep(1)
        sound.stop()

    # Game music
    sound = pygame.mixer.Sound('sounds/lige_bartar.mp3')
    sound.play()
    sound.set_volume(0.4)
    music_time = pygame.time.get_ticks()

    # Load game assets
    backg = pygame.image.load('images/Screenshot (1).png')
    pygame.display.set_caption("jumpball")
    ball = pygame.image.load('images/ball_prev_ui.png')
    pygame.display.set_icon(ball)

    start_time = pygame.time.get_ticks()
    tm = start_time
    m = 0
    y_time = 0
    Vy = 0
    alpha = -1
    MaxVy = 6
    Vx = 0
    MaxVx = 4
    score1, score2 = 0, 0

    jumpsound = pygame.mixer.Sound('sounds/jumping sound.wav')
    gms = pygame.mixer.Sound('sounds/gamestartsound.wav')
    gms.play()
    bouncesound = pygame.mixer.Sound('sounds/bounce sound.wav')
    scoretime = pygame.time.get_ticks()
    
#main game loop
while run:
    (xm,ym) = pygame.mouse.get_pos()
    mouse_clicked = pygame.mouse.get_pressed()
    mouse_clicked = mouse_clicked[0]
    if xm < 50 and ym < 50:
        pause_button = pygame.transform.scale(pause_button,(75,75))
        if mouse_clicked:
            run2 = True 
            while run2:
                pass 
                #here will be the restart , exit options
    else:
        pause_button = pygame.transform.scale(pause_button,(50,50))
    s.blit(pause_button,(0,0))
    mouse_clicked = pygame.mouse.get_pressed()
    mouse_clicked = mouse_clicked[0]
    if Vx > MaxVx:
        Vx = MaxVx
    if Vy > MaxVy:
        Vy = MaxVy
    if player == 1:
        pxx = px 
        pyy = py 
    elif player == 2:
        pxx = px2 
        pyy = py2
    if mobile_mode == True:
        if player == 1:
            px2,py2 = send_coordinates(pxx,pyy)
        elif player == 2:
            px,py == send_coordinates(pxx,pyy)
        event1 = pygame.event.get()
        (xm,ym) = pygame.mouse.get_pos()
        if Vyp == 0:
            if 100 < xm < 200 and 600 < ym < 700:
                jump1 == True 
                Vyp = -6    
        if Vyp != 0:
            if 200 < xm < 300 and 575 < ym < 700:
                px -= 5
            if 300 < xm < 400 and 600 < ym < 700:
                px += 5
    #mobile controls 
    if mobile_mode == True:
        s.blit(arrow_right,(300,600))
        s.blit(arrow_left,(220,575))
        s.blit(jumpbutton,(100,600))
    if gtime != 0:
        if pygame.time.get_ticks() - stime >= 1000:
            gtime -= 1
            stime = pygame.time.get_ticks()
    elif gtime == 0:
        s.fill((255,255,255))
    #scores
    if x >= 1130 and x<=1230:
        if y >= 100 and y <= 200 and pygame.time.get_ticks() - scoretime >= 1000:
            score1 += 1
            scoretime = pygame.time.get_ticks()
            Vx = -7
            scoresound.play()
            scoresound.set_volume(0.3)
    if x >= 0 and x<=100:
        if y >= 100 and y <= 200 and pygame.time.get_ticks() - scoretime >= 1000:
            score2 += 1
            scoretime = pygame.time.get_ticks()
            Vx = 7
            scoresound.play()
            scoresound.set_volume(0.3)
    if Vx > MaxVx:
        Vx = MaxVx
    if Vy > MaxVy:
        Vy = MaxVy
    score = scorefont.render(f'{score1} - score - {score2}',True,(0,0,0))
    time_remaining = scorefont.render(str(gtime),True,(0,0,0))
    s.blit(scoreboard, (530,10))
    s.blit(score,(580,35))
    s.blit(time_remaining, (650,120))
    addnet(barrier1,bx,by)
    addnet(barrier2,bx2,by2)
    #pygame.draw.rect(s,(1,0,1),(1280,150,90,10))
    #pygame.draw.rect(s,(1,0,1),(0,300,90,900))
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
    #mobile controls 
    if mobile_mode == True:
        s.blit(arrow_right,(300,600))
        s.blit(arrow_left,(220,575))
        s.blit(jumpbutton,(100,600))
    if gtime == 0:
        s.fill((255,255,255))
        s.blit(pause_button,(0,0))
    s.blit(pause_button,(0,0))
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
        if Vyp < 0:
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
    if Vx > MaxVx:
        Vx = MaxVx
    if Vy > MaxVy:
        Vy = MaxVy
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
    if not AImode:
        ##player2
        if Vyp2 < 0:
            Vyp2 += 0.3
        elif Vyp2 > 0:
            Vyp2 += 0.5
        if Vyp2 > 7:
            Vyp2 = 7
        if jump2 == True:
            Vyp2 = -6
            jumpsound.play()
            jumpsound.set_volume(0.1)
        py2 += Vyp2
        key = pygame.key.get_pressed()
        if Vyp2 == 0:
            if key[pygame.K_DOWN] == True or key[pygame.K_UP] == True:
                jump2 == True 
                Vyp2 = -6    
        if Vyp2 != 0:
            if key[pygame.K_LEFT] == True:
                px2 -= 5
            if key[pygame.K_RIGHT] == True :
                px2 += 5
        if py2 <= 500:
            Vyp2 = -Vyp2
        if py2 > 600:
            Vyp2 = 0
            py2 = 600
            jump2 = False
        if px2 >1250 :
            px2 -= 5
        elif px2 <50 :
            px2 += 5
        if py2 >600:
            py2 -= 5
        elif py2 <50 :
            py2 += 5
    else:
        ##player2
        if Vyp2 < 0:
            Vyp2 += 0.3
        elif Vyp2 > 0:
            Vyp2 += 0.5
        if Vyp2 > 7:
            Vyp2 = 7
        if jump2:
            Vyp2 = -6
            jumpsound.play()
            jumpsound.set_volume(0.1)
        py2 += Vyp2
        if Vyp2 == 0 :
            jump2 == True
        if py2 <= 500:
            if Vyp2 < 0 :
                Vyp2 = -Vyp2
        py2 += Vyp2
        if py2 > 600:
            Vyp2 = 0
            py2 = 600
            jump2 = False
        if px2 >1250 :
            px2 -= 5
        elif px2 <50 :
            px2 += 5
        if py2 >600:
            py2 -= 5
        elif py2 <50 :
            py2 += 5
        if x < px2 and Vx < 0:
            px2 -= 3 
        elif x > px2 and Vx > 0:
            px2 += 3
        elif x > px2 and Vx < 0:
            px2 -= 3
        elif x < px2 and Vx > 0:
            px2 -= 3
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
    if Vx > MaxVx:
        Vx = MaxVx
    if Vy > MaxVy:
        Vy = MaxVy
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
    s.blit(time_remaining, (650,120))
    #mobile controls 
    if mobile_mode == True:
        s.blit(arrow_right,(300,600))
        s.blit(arrow_left,(220,575))
        s.blit(jumpbutton,(100,600))
    if gtime == 0:
        s.fill((255,255,255))
        s.blit(pause_button,(0,0))
    s.blit(pause_button,(0,0))
    pygame.display.update()
    pygame.time.Clock().tick(5000)
    addnet(barrier1,bx,by)
    addnet(barrier2,bx2,by2)
print(time1[0],":",time1[1])
pygame.quit()
