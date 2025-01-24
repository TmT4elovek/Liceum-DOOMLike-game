import pygame

class Monster(pygame.sprite.Sprite):
    def __init__(self, screen: pygame.surface.Surface, sprite: str, spawn_pos: tuple, hp:int=100, speed:float=1) -> None:
        super().__init__()
        self._screen = screen
        self.image = pygame.transform.scale(pygame.image.load(sprite).convert_alpha(), (10, 10))
        self.rect = self.image.get_rect().move(spawn_pos)
        self.spawn_pos = spawn_pos
        self.hp = hp
        self.speed = speed
        self.angle = 0

    def get_hp(self, hp):
        return hp
    # для добавления всяких бустов, если нужно или просто отслеживать состояние.

    def get_attac(self, attac):
        return attac
    # тоже, что и для hp

    def born(self):
        pass
    #создание монстра

    def death(self):
        pass
    #уничтожение, засчет очков


class BossMonster(Monster):
    def __init__(self):
        super.__init__()
