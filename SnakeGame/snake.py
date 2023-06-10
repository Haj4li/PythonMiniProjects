import pygame

class Snake:
    def __init__(self, x, y):
        self.body = [(x, y)]
        self.direction = "right"
        self.speed = 5

    def move(self):
        if self.direction == "right":
            x = self.body[0][0] + self.speed
            y = self.body[0][1]
        elif self.direction == "left":
            x = self.body[0][0] - self.speed
            y = self.body[0][1]
        elif self.direction == "up":
            x = self.body[0][0]
            y = self.body[0][1] - self.speed
        elif self.direction == "down":
            x = self.body[0][0]
            y = self.body[0][1] + self.speed

        self.body.insert(0, (x, y))
        self.body.pop()

    def grow(self):
        x = self.body[-1][0]
        y = self.body[-1][1]
        self.body.append((x, y))

    def change_direction(self, direction):
        if direction == "right" and self.direction != "left":
            self.direction = "right"
        elif direction == "left" and self.direction != "right":
            self.direction = "left"
        elif direction == "up" and self.direction != "down":
            self.direction = "up"
        elif direction == "down" and self.direction != "up":
            self.direction = "down"
