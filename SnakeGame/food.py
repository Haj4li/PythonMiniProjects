import pygame
import random

class Food:
    def __init__(self, width, height):
        self.position = (random.randint(0, width), random.randint(0, height))
        self.score = 10

    def respawn(self, width, height):
        self.position = (random.randint(0, width), random.randint(0, height))
