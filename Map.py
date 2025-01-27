import pygame

WALL_IMG = './tools/texture/wall.png'

class Map():
    def __init__(self,
                wall_group,
                bottom_group,
                mp: str) -> None:
        self.wall = wall_group
        self.bottom = bottom_group
        self._map_file = mp
        self._level_list = self.read_map()

    def read_map(self) -> None:
        output_map = list()
        with open(self._map_file, "r") as mf:
            for line in mf.readlines():
                output_map.append([simbol.strip() for simbol in line])
        return output_map
    
    def load(self) -> None:
        # Do we need to read map again??
        level_list = self.read_map()
        for y in range(len(level_list)):
            for x in range(len(level_list[y])):
                if level_list[y][x] == "0":
                    pass
                elif level_list[y][x] == "#":
                    Tile(64, WALL_IMG, (x, y), self.wall)

    def is_free(self, x: int, y: int) -> None:
        return not self._level_list[int(y // 64)][int(x // 64)] == "#"


class Tile(pygame.sprite.Sprite):
    def __init__(self,
                size: int, img: str,
                pos: tuple,
                *group) -> None:
        super().__init__(*group)

        width = height = size
        self.image = pygame.image.load(img).convert_alpha()
        self.rect = self.image.get_rect().move(
            width * pos[0], height * pos[1])
        