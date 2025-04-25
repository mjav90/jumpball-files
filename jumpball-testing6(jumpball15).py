# jumpball_final_combined.py

import pygame
import time
import socket
import struct

# Constants
WHITE = (255, 255, 255)
SCREEN_WIDTH = 1327
SCREEN_HEIGHT = 700
HOST = '127.0.0.1'
PORT = 12341

pygame.init()
s = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("jumpball")
score_font = pygame.font.Font('BigShouldersStencil_18pt-ExtraBold.ttf', 38)

# Utility Functions
def send_coordinates(x, y):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))
    data = struct.pack("!ii", x, y)
    client.sendall(data)
    response = client.recv(8)
    received_x, received_y = struct.unpack("!ii", response)
    client.close()
    return received_x, received_y

def on_rect(rect, x, y):
    return rect[0] < x < rect[0] + rect[2] and rect[1] < y < rect[1] + rect[3]

def blit_image(image, x, y):
    s.blit(image, (x, y))

# Asset Loading
def load_assets():
    assets = {}
    assets['scoreboard'] = pygame.transform.scale(pygame.image.load('images/scoreboard layout1.png'), (300, 100))
    assets['scoresound'] = pygame.mixer.Sound('sounds/Collect.wav')
    assets['jumpsound'] = pygame.mixer.Sound('sounds/jumping sound.wav')
    assets['bouncesound'] = pygame.mixer.Sound('sounds/bounce sound.wav')
    assets['music'] = pygame.mixer.Sound('sounds/lige_bartar.mp3')
    assets['gms'] = pygame.mixer.Sound('sounds/gamestartsound.wav')
    assets['countdown'] = {
        "3": ("images/3.png", "sounds/s3.wav"),
        "2": ("images/2.png", "sounds/s2.wav"),
        "1": ("images/1.png", "sounds/s1.wav")
    }
    assets['buttons'] = {
        'offline': pygame.transform.scale(pygame.image.load('images/offlinebutton.jpg'), (100, 100)),
        'ai': pygame.transform.scale(pygame.image.load('images/aibutton.png'), (100, 100)),
        'mobile': pygame.transform.scale(pygame.image.load('images/mobilebutton.png'), (100, 100)),
        'logo': pygame.transform.scale(pygame.image.load('images/jumpballlogo.jpeg'), (1327, 900))
    }
    return assets

# Countdown before game starts
def countdown_sequence(assets):
    for num in ["3", "2", "1"]:
        img_path, sound_path = assets['countdown'][num]
        img = pygame.image.load(img_path)
        sound = pygame.mixer.Sound(sound_path)
        s.fill(WHITE)
        s.blit(img, (0, 0))
        pygame.display.update()
        sound.play()
        sound.set_volume(0.1)
        time.sleep(1)
        sound.stop()

# Start Menu Display
def show_start_menu(assets):
    s.fill(WHITE)
    s.blit(assets['buttons']['logo'], (0, -100))
    s.blit(assets['buttons']['offline'], (100, 100))
    s.blit(assets['buttons']['ai'], (100, 300))
    s.blit(assets['buttons']['mobile'], (100, 550))
    pygame.display.update()
    pygame.mixer.Sound('sounds/menu sound2.wav').play()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                xm, ym = event.pos
                if 100 <= xm <= 200:
                    if 100 <= ym <= 200:
                        return False, False  # Offline
                    elif 300 <= ym <= 400:
                        return False, True   # AI Mode
                    elif 550 <= ym <= 650:
                        return True, False   # Mobile Mode

# Run the full game loop (from testing5)
def run_game(assets, mobile_mode, ai_mode):
    # Game Variables
    run = True
    jump1 = True
    jump2 = True
    score1, score2 = 0, 0
    MaxVx = 4
    MaxVy = 6
    Vx = 0
    Vy = 0
    Vyp = -6
    Vyp2 = -6
    px, py = 100, 600
    px2, py2 = 1200, 600
    x, y = 600, 150
    alpha = -1
    gtime = 90
    time1 = [0, 0]

    scoreboard = assets['scoreboard']
    scorefont = pygame.font.Font('BigShouldersStencil_18pt-ExtraBold.ttf', 38)

    # Load assets
    backg = pygame.image.load('images/Screenshot (1).png')
    pygame.display.set_icon(pygame.image.load('images/ball_prev_ui.png'))

    player = pygame.image.load('images/player 1 (1)_prev_ui (1).png')
    player2 = pygame.image.load('images/player 1_prev_ui (2).png')
    ball = pygame.image.load('images/ball_prev_ui.png')

    barrier1 = pygame.transform.scale(pygame.image.load('images/images-Photoroom.png'), (200, 200))
    barrier2 = pygame.transform.scale(pygame.image.load('images/images-Photoroom2.png'), (200, 200))
    bx, by = 1130, 100
    bx2, by2 = 0, 100

    arrow_right = pygame.transform.scale(pygame.image.load('images/rightarrow.png'), (50, 50))
    arrow_left = pygame.transform.scale(pygame.image.load('images/leftarrow.png'), (60, 100))
    jumpbutton = pygame.transform.scale(pygame.image.load('images/jumpbutton.png'), (50, 50))

    # Sounds
    scoresound = assets['scoresound']
    jumpsound = assets['jumpsound']
    bouncesound = assets['bouncesound']
    music = assets['music']
    gms = assets['gms']

    gms.play()
    music.play(-1)
    music.set_volume(0.4)

    stime = pygame.time.get_ticks()
    start_time = pygame.time.get_ticks()
    tm = start_time
    m = 0
    y_time = 0

    while run:
        s.fill((0, 0, 0))
        s.blit(backg, (0, 0))
        s.blit(scoreboard, (530, 10))
        score = scorefont.render(f'{score1} - score - {score2}', True, (0, 0, 0))
        time_remaining = scorefont.render(str(gtime), True, (0, 0, 0))
        s.blit(score, (580, 35))
        s.blit(time_remaining, (650, 120))

        if gtime != 0 and pygame.time.get_ticks() - stime >= 1000:
            gtime -= 1
            stime = pygame.time.get_ticks()
        elif gtime == 0:
            s.fill((255, 255, 255))

        # Draw barriers
        s.blit(barrier1, (bx, by))
        s.blit(barrier2, (bx2, by2))

        # Ball physics
        x += Vx
        y += Vy
        if y >= 600:
            Vy *= alpha
            bouncesound.play()
        if x >= 1200 or x <= 50:
            Vx *= -1
            bouncesound.play()
        if y <= 30:
            Vy = 5
            bouncesound.play()

        Vy += 0.2
        if Vy > MaxVy:
            Vy = MaxVy
        if Vx > MaxVx:
            Vx = MaxVx

        # Check scores
        if 1130 <= x <= 1230 and 100 <= y <= 200:
            score1 += 1
            Vx = -7
            scoresound.play()
        if 0 <= x <= 100 and 100 <= y <= 200:
            score2 += 1
            Vx = 7
            scoresound.play()

        # Player controls
        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
            px -= 5
        if key[pygame.K_d]:
            px += 5
        if key[pygame.K_SPACE] and py >= 600:
            Vyp = -6
            jumpsound.play()
        py += Vyp
        if py > 600:
            py = 600
            Vyp = 0

        if key[pygame.K_LEFT]:
            px2 -= 5
        if key[pygame.K_RIGHT]:
            px2 += 5
        if key[pygame.K_UP] and py2 >= 600:
            Vyp2 = -6
            jumpsound.play()
        py2 += Vyp2
        if py2 > 600:
            py2 = 600
            Vyp2 = 0

        Vyp += 0.5
        if Vyp > MaxVy:
            Vyp = MaxVy
        Vyp2 += 0.5
        if Vyp2 > MaxVy:
            Vyp2 = MaxVy

        # Ball collision with players
        #p2
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
        #p1
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
        # Draw all elements
        s.blit(player, (px, py))
        s.blit(player2, (px2, py2))
        s.blit(ball, (x, y))

        # Mobile controls
        if mobile_mode:
            s.blit(arrow_right, (300, 600))
            s.blit(arrow_left, (220, 575))
            s.blit(jumpbutton, (100, 600))

        pygame.display.update()
        pygame.time.Clock().tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

    pygame.quit()

# Main Entry Point
def main():
    assets = load_assets()
    mobile_mode, ai_mode = show_start_menu(assets)
    countdown_sequence(assets)
    run_game(assets, mobile_mode, ai_mode)

if __name__ == "__main__":
    main()
