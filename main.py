import pygame

from Player import Player
from Map import Map

GAME_NAME = 'Our game'
GAME_ICON = ''
SIZE = (500, 500)
FPS = 60
# file urls
PLAYER_SPRITE = ''
MAP = ''


def main(size: tuple) -> None:
    pygame.init()

    width, height = size
    clock = pygame.time.Clock()

    # Sprite groups
    players = pygame.sprite.Group()
    bottom = pygame.sprite.Group()
    walls = pygame.sprite.Group()
    # Create and setup screen
    screen = pygame.display.set_mode(size, pygame.RESIZABLE)
    pygame.display.set_caption(GAME_NAME)
    pygame.display.set_icon(pygame.image.load(GAME_ICON))
    # Create player
    player = Player(screen, PLAYER_SPRITE)
    players.add(player)
    # Create map
    map = Map(walls, bottom, MAP)
    map.load()

    ray_casting = RayCasting(screen, player, map)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill('black')
        clock.tick(FPS)


if __name__ == "__main__":
    main(SIZE)