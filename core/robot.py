import pygame
import math
import numpy as np
from core.world import *

class Robot:
    def __init__(self,pos):
        self.x, self.y = pos
        self.size = 20
        self.angle = 180
        self.speed = 2
        self.turn_speed = 2

    def get_triangle(self):
        half_size = self.size / 2

        angle_rad = math.radians(self.angle)

        tip = (self.x + half_size * math.cos(angle_rad), self.y + half_size * math.sin(angle_rad))
        left = (self.x + half_size * math.cos(angle_rad + math.radians(120)),
                self.y + half_size * math.sin(angle_rad + math.radians(120)))
        right = (self.x + half_size * math.cos(angle_rad - math.radians(120)),
                 self.y + half_size * math.sin(angle_rad - math.radians(120)))

        return [tip, left, right]

    def move_forward(self, obstacles):
        rad = math.radians(self.angle)
        self.x += self.speed * math.cos(rad)
        self.y += self.speed * math.sin(rad)

        for obstacle in obstacles:
            if sat_collision(self.get_triangle(),obstacle.vertices):
                self.x -= self.speed * np.cos(rad)
                self.y -= self.speed * np.sin(rad)

    def reverse(self, obstacles):
        rad = np.radians(self.angle)
        self.x -= self.speed * np.cos(rad)
        self.y -= self.speed * np.sin(rad)

        for obstacle in obstacles:
            if sat_collision(self.get_triangle(), obstacle.vertices):
                self.x += self.speed * np.cos(rad)
                self.y += self.speed * np.sin(rad)

    def turn_left(self, obstacles):
        self.angle = (self.angle - self.turn_speed) % 360
        for obstacle in obstacles:
            if sat_collision(self.get_triangle(),obstacle.vertices):
                self.angle = (self.angle + self.turn_speed) % 360

    def turn_right(self, obstacles):
        self.angle = (self.angle + self.turn_speed) % 360
        for obstacle in obstacles:
            if sat_collision(self.get_triangle(),obstacle.vertices):
                self.angle = (self.angle + self.turn_speed) % 360
