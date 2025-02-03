import pygame
import sys


class Coin:
    def __init__(self):
        self.gold_color = (255, 215, 0)
        self.shadow_gold_color = (200, 180, 0)
        self.silver_color = (211, 211, 211)
        self.shadow_silver_color = (105, 105, 105)
        self.bronze_color = (238, 118, 33)
        self.shadow_bronze_color = (139, 69, 19)

    def draw_gold_coin(self, surface, x, y, radius):
        ball = 3
        pygame.draw.circle(surface, self.shadow_gold_color, (x + 5, y + 5), radius)
        pygame.draw.circle(surface, self.gold_color, (x, y), radius)

    def draw_silver_coin(self, surface, x, y, radius):
        ball = 2
        pygame.draw.circle(surface, self.shadow_silver_color, (x + 5, y + 5), radius)
        pygame.draw.circle(surface, self.silver_color, (x, y), radius)

    def draw_coin(self, surface, x, y, radius):
        ball = 1
        pygame.draw.circle(surface, self.shadow_bronze_color, (x + 5, y + 5), radius)
        pygame.draw.circle(surface, self.bronze_color, (x, y), radius)
