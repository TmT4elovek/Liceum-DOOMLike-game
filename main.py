import pygame

from Player import Player
from Map import Map
from RayCasting import RayCasting

GAME_NAME = 'Our game'
GAME_ICON = './tools/img/icon.jpg' #!BAD
WINDOW_SIZE = (1300, 700)
FPS = 60
# file urls
PLAYER_SPRITE = './tools/sprite/player/sp.webp'
MAP = './tools/map.txt'


def main(size: tuple) -> None:
    pygame.init()
    pygame.font.init()
    clock = pygame.time.Clock()
    width, height = size
    players = pygame.sprite.Group()
    walls = pygame.sprite.Group()
    bottom = pygame.sprite.Group()

    pygame.display.set_caption(GAME_NAME)
    # pygame.display.set_icon(pygame.image.load('icon.png'))
    screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
    # PLAYER
    pl = Player(screen, PLAYER_SPRITE)
    players.add(pl)
    # MAP
    map = Map(walls, bottom, MAP)
    map.load()

    rc = RayCasting(screen, pl, map)

    running = True
    while running:
        # events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                exit()

        screen.fill((0, 0, 0))
        clock.tick(FPS)

        players.update(walls)

        rc.draw_rays(0.005, 425, 384) # 1920 / 5 <- pixels

        # Обновление экрана
        pygame.display.flip()


if __name__ == '__main__':
    main(WINDOW_SIZE)