import pygame
import pygame_menu
import pygame_menu.events
import pygame_menu.themes

from Player import Player
from Map import Map
from RayCasting import RayCasting

GAME_NAME = 'Our game'
GAME_ICON = './tools/img/icon.jpg' #!BAD
WINDOW_SIZE = (1920, 1080)
FPS = 60
# file urls
PLAYER_SPRITE = './tools/sprite/player/sp.webp'

SKY_COLOR = (0, 0, 0)#(94, 100, 114)
FLOOR_COLOR = (200, 200, 200)

difficulty = 0


def set_difficulty(value, selected_difficulty):
    global difficulty
    difficulty = selected_difficulty

def main() -> None:
    clock = pygame.time.Clock()
    width, height = WINDOW_SIZE
    players = pygame.sprite.Group()
    walls = pygame.sprite.Group()
    finish = pygame.sprite.Group()
    if difficulty == 0:
        MAP = r'tools\map_low.txt'
        timer = 30
    elif difficulty == 1:
        MAP = r'tools\map_med.txt'
        timer = 60
    elif difficulty == 2:
        MAP = r'tools\map_hard.txt'
        timer = 150
    
    # PLAYER
    pl = Player(screen, PLAYER_SPRITE)
    players.add(pl)
    # MAP
    map = Map(walls, finish, MAP)
    map.load()

    rc = RayCasting(screen, pl, map)
    
    start_ticks = pygame.time.get_ticks()
    running = True
    while running:
        # events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                exit()

        screen.fill(SKY_COLOR)
        pygame.draw.rect(screen, FLOOR_COLOR, (0, height-height*0.5, width, height))
        clock.tick(FPS)

        players.update(walls)
        if pygame.sprite.spritecollideany(pl, finish):
            running = False
            pygame.mixer.stop()
            exit()

        rc.draw_rays(0.005, 10000, 384) # 1920 / 5 <- pixels

        secunds = round((pygame.time.get_ticks()-start_ticks)/1000, 3)
        live_timer = timer - secunds
        f1 = pygame.font.Font(size=30)
        text = f1.render(f'Time: {int(live_timer // 60)}.{round(live_timer % 60, 3)}', True, 'red', 'black')
        screen.blit(text, (80, 80))
        # Обновление экрана
        pygame.display.flip()

    

if __name__ == '__main__':
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption(GAME_NAME)
    # pygame.display.set_icon(pygame.image.load('icon.png'))
    screen = pygame.display.set_mode(WINDOW_SIZE, pygame.RESIZABLE)
    #MENU
    menu = pygame_menu.Menu('Welcome', *WINDOW_SIZE, theme=pygame_menu.themes.THEME_DARK)
    menu.add.selector('Difficulty: ', [('Low', 0), ('Medium', 1), ('Hard', 2)], onchange=set_difficulty)
    menu.add.button('Play', main)
    menu.add.button('Quit', exit)
    #Start
    menu.mainloop(screen)