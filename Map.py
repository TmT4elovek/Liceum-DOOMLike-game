import pygame

WALL_IMG = './tools/texture/wall.png'

class Map():
    def __init__(self,
                wall_group,
                finish_goup,
                mp: str) -> None:
        self.wall = wall_group
        self.finish = finish_goup
        self._map_file = mp
        self._level_list = self.read_map()

    def read_map(self) -> list:
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
                if level_list[y][x] == ".":
                    pass
                elif level_list[y][x] == "#":
                    Tile(64, WALL_IMG, (x, y), self.wall)
                elif level_list[y][x] == 'F':
                    Finish(64, (x, y), self.finish)


    def is_free(self, x: int, y: int) -> bool:
        try:
            symb = self._level_list[int(y // 64)][int(x // 64)]
            return not symb in ["#", 'F'], symb
        except IndexError:
            print('Out of textures')
            exit()
        


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

class Finish(pygame.sprite.Sprite):
    def __init__(self,
                size: int,
                pos: tuple,
                *group) -> None:
        super().__init__(*group)

        width = height = size
        self.image = pygame.Surface([64, 64])
        self.rect = self.image.get_rect().move(
            width * pos[0], height * pos[1])