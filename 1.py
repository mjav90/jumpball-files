import pygame
pygame.init()
def cordaddball(x,y):
    s.blit(ball,(x,y))
s_width = 1327
s_height = 700
s = pygame.display.set_mode((s_width,s_height))
run=True
#نمونه توپ
player= pygame.Rect(600,350,50,50)
ball=pygame.image.load('ball_prev_ui.png')
x = 600
y = 150
start_time = pygame.time.get_ticks()
##اهنگ بازي
sound = pygame.mixer.Sound('5.Mr. Blue Sky - Electric Light Orchestra Mr. Blue Sky.mp3')
sound.play()
##بکگراند و عکس و اسم صفحه
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
    if player.y > 800 :
        player.move_ip(0,-5)
    elif player.y <450 :
        player.move_ip(0,5)
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
        x = x + 20
    if (player.x) - x < 20 and player.x - x > 0 :
        if player.y - y < 20 or y - player.y < 20 :
            Vx += 4
    cordaddball(x,y)
    pygame.display.update()
print(time1[0],":",time1[1])
pygame.quit()
