import pygame
import math



class Player(pygame.sprite.Sprite):
    def __init__(
            self, 
            screen: pygame.surface.Surface,
            img: str,
            spawn_pos: tuple = (80, 80),
            speed: float = 2.5
            ):
        super().__init__()
        
        self._screen = screen
        self._spawn_pos = spawn_pos
        self.speed = speed
        self.cur_speed = speed
        self.image = pygame.image.load(img).convert_alpha()
        self.image = pygame.transform.scale(self.image, (10, 10))
        self.rect = self.image.get_rect().move(spawn_pos)
        self.angle = 0

        self.WALK_CHANNEL = pygame.mixer.Channel(1)
        self.walk_sound = pygame.mixer.Sound(r'tools\music\shagi-s-effektom-eho-24256.ogg')

    def movement(self) -> None:
        keys = pygame.key.get_pressed()
        old_x, old_y = self.rect.x, self.rect.y
        if keys[pygame.K_w]:
            self.rect.x += self.cur_speed * (math.cos(self.angle) - math.sin(self.angle))
            self.rect.y += self.cur_speed * (math.sin(self.angle) + math.cos(self.angle))
            self.walk()
        if keys[pygame.K_a]:
            self.rect.x += self.cur_speed * (math.cos(self.angle) + math.sin(self.angle))
            self.rect.y += self.cur_speed * (math.sin(self.angle) - math.cos(self.angle))
            self.walk()
        if keys[pygame.K_s]:
            self.rect.x += self.cur_speed * (math.sin(self.angle) - math.cos(self.angle))
            self.rect.y -= self.cur_speed * (math.sin(self.angle) + math.cos(self.angle))
            self.walk()
        if keys[pygame.K_d]:
            self.rect.x -= self.cur_speed * math.sin(self.angle)
            self.rect.y += self.cur_speed * math.cos(self.angle)
            self.walk()
        if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
            self.cur_speed = self.speed + 4
        else:
            self.cur_speed = self.speed
        if keys[pygame.K_LEFT]:
            self.angle -= 0.05
        if keys[pygame.K_RIGHT]:
            self.angle += 0.05
        
        if old_x == self.rect.x and old_y == self.rect.y:
            self.WALK_CHANNEL.stop()

    def update(self, boxes_group: any) -> None:
        if boxes_group:
            old_rect_x, old_rect_y = self.rect.x, self.rect.y
            self.movement()
            if pygame.sprite.spritecollideany(self, boxes_group):
                self.rect.x, self.rect.y = old_rect_x, old_rect_y

    def walk(self):
        if not self.WALK_CHANNEL.get_busy():
            self.WALK_CHANNEL.play(self.walk_sound)