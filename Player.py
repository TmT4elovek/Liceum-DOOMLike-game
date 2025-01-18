import pygame
import math


class Player(pygame.sprite.Sprite):
    def __init__(self, screen: pygame.surface.Surface, sprite: str, spawn_pos: tuple, hp:int=100, speed:float=1) -> None:
        super().__init__()

        self._screen = screen
        self.image = pygame.transform.scale(pygame.image.load(sprite).convert_alpha(), (10, 10))
        self.rect = self.image.get_rect().move(spawn_pos)
        self.spawn_pos = spawn_pos
        self.hp = hp
        self.speed = speed
        self.angle = 0
    
    def move(self) -> None:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.rect.x += math.cos(math.radians(self.angle)) * self.speed
            self.rect.y += math.sin(math.radians(self.angle)) * self.speed
        
        if keys[pygame.K_a]:
            self.rect.x +=  math.sin(math.radians(self.angle)) * self.speed
            self.rect.y -=  math.cos(math.radians(self.angle)) * self.speed

        if keys[pygame.K_s]:
            self.rect.x -=  math.cos(math.radians(self.angle)) * self.speed
            self.rect.y +=  math.sin(math.radians(self.angle)) * self.speed

        if keys[pygame.K_d]:
            self.rect.x -=  math.sin(math.radians(self.angle)) * self.speed
            self.rect.y +=  math.cos(math.radians(self.angle)) * self.speed
        
        if keys[pygame.K_LEFT]:
            self.angle -= 1
        elif keys[pygame.K_RIGHT]:
            self.angle += 1
    
    def upadte(self, walls_group: pygame.sprite.Group) -> None:
        if walls_group is not None:
            old_x, old_y = self.rect.x, self.rect.y
            self.move()
            if pygame.sprite.spritecollideany(self, walls_group):
                self.rect.x, self.rect.y = old_x, old_y
