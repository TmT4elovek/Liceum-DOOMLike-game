import pygame

WALL_IMG = ''

class Map():
    def __init__(self, walls: pygame.sprite.Group, bottom: pygame.sprite.Group, map_file: str) -> None:
        self.walls = walls
        self.bottom = bottom
        self._map_file = map_file
        self._readed_map = self.read_map_file(map_file)

    def read_map_file(self) -> list:
        readed_map = list()

        with open(self._map_file, 'r') as f:
            for line in f.readlines():
                readed_map.append([elem.strip() for elem in line])
        return readed_map

    def load(self) -> None:
        for y in range(len(self._readed_map)):
            for x in range(len(self._readed_map[y])):
                if self._readed_map[y][x] == '#':
                    Tile(32, (x, y), WALL_IMG, self.walls)
                elif self._readed_map[y][x] == '0':
                    pass


class Tile(pygame.sprite.Sprite):
    def __init__(self, size: int, position: tuple, image: str, *group: pygame.sprite.Group) -> None:
        super().__init__(*group)

        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect().move(position[0] * size, position[1] * size)