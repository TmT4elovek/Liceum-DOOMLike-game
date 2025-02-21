import pygame
import math

class RayCasting():
    def __init__(self,
                screen: pygame.surface.Surface,
                player: pygame.sprite.Sprite,
                map: any) -> None:
        self._screen = screen
        self._player = player
        self._map = map
        self.sc_height = 1080
        self.wall_height = 1920

    def draw_rays(self, delta: int, distance: int, num_of_rays: float) -> None:
        start_coord = (self._player.rect.left, self._player.rect.top)
        angle = self._player.angle
        for ray in range(num_of_rays):
            cos_a = math.cos(angle)
            sin_a = math.sin(angle)
            for length in range(0, distance):
                end_coord = (start_coord[0] + cos_a * length, start_coord[1] + sin_a * length)
                answ = self._map.is_free(*end_coord)
                if not answ[0]:
                    break
            if length != 0:
                self.draw_screen(length, ray, answ[1]) # 3D view
            # pygame.draw.aaline(self._screen, (0, 0, 255), start_coord, end_coord) # 2D view
            angle += delta

    def draw_screen(self, leng: int, x: int, symb: str) -> None:
        proection = 10
        if symb == '#':
            shadow = round(int(leng) * 0.3)
            color = (3 - shadow, 4 - shadow, 94 - shadow)
            color = tuple(map(lambda x: 0 if x < 0 else x, color))
            pygame.draw.line(
                self._screen,
                color, [x * 5, (self.sc_height // 2 - ((self.wall_height * proection) // leng))], #x*5 - Each ray is drawn 5 pixels apart. Pos on x axis.
                [x * 5, (self.sc_height // 2 + ((self.wall_height * proection) // leng))],
                5
                )
        if symb == 'F':
            shadow = round(int(leng) * 0.2)
            color = (204 - shadow, 255 - shadow, 51 - shadow)
            color = tuple(map(lambda x: 0 if x < 0 else x, color))
            pygame.draw.line(
                self._screen,
                color, [x * 5, (self.sc_height // 2 - ((self.wall_height * proection) // leng))], #x*5 - Each ray is drawn 5 pixels apart. Pos on x axis.
                [x * 5, (self.sc_height // 2 + ((self.wall_height * proection) // leng))],
                5
                )