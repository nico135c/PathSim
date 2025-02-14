import pygame
import math

class Robot:
    def __init__(self,pos):
        self.pos = pos
        self.size = 20
        self.angle = 0
        self.speed = 2
        self.rotation_speed = 2

    def get_triangle(self):
        cx, cy = self.pos
        half_size = self.size / 2

        angle_rad = math.radians(self.angle)

        tip = (cx + half_size * math.cos(angle_rad), cy + half_size * math.sin(angle_rad))
        left = (cx + half_size * math.cos(angle_rad + math.radians(120)),
                cy + half_size * math.sin(angle_rad + math.radians(120)))
        right = (cx + half_size * math.cos(angle_rad - math.radians(120)),
                 cy + half_size * math.sin(angle_rad - math.radians(120)))

        return [tip, left, right]