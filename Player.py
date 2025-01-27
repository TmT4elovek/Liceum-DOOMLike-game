import pygame
import math


class Player(pygame.sprite.Sprite):
    def __init__(
            self, 
            screen: pygame.surface.Surface,
            img: str,
            spawn_pos: tuple = (80, 80),
            hp: int = 100,
            speed: float = 2.5
            ):
        super().__init__()
        
        self._screen = screen
        self._spawn_pos = spawn_pos
        self.speed = speed
        self.cur_speed = speed
        self.health = hp
        self.image = pygame.image.load(img).convert_alpha()
        self.image = pygame.transform.scale(self.image, (10, 10))
        self.rect = self.image.get_rect().move(spawn_pos)
        self.angle = 0

    def movement(self) -> None:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.rect.x += self.cur_speed * (math.cos(self.angle) - math.sin(self.angle))
            self.rect.y += self.cur_speed * (math.sin(self.angle) + math.cos(self.angle))
        if keys[pygame.K_a]:
            self.rect.x += self.cur_speed * math.sin(self.angle)
            self.rect.y -= self.cur_speed * math.cos(self.angle)
        if keys[pygame.K_s]:
            self.rect.x += self.cur_speed * (math.sin(self.angle) - math.cos(self.angle))
            self.rect.y -= self.cur_speed * (math.sin(self.angle) + math.cos(self.angle))
        if keys[pygame.K_d]:
            self.rect.x -= self.cur_speed * math.sin(self.angle)
            self.rect.y += self.cur_speed * math.cos(self.angle)
        if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
            self.cur_speed = self.speed + 4
        else:
            self.cur_speed = self.speed
        if keys[pygame.K_LEFT]:
            self.angle -= 0.1
        if keys[pygame.K_RIGHT]:
            self.angle += 0.1

    def update(self, boxes_group: any) -> None:
        if boxes_group:
            old_rect_x, old_rect_y = self.rect.x, self.rect.y
            self.movement()
            if pygame.sprite.spritecollideany(self, boxes_group):
                self.rect.x, self.rect.y = old_rect_x, old_rect_y