import pygame
from core.robot import Robot
#VARIOUS DEBUGGING FUNCTIONS

def manual_control(robot: Robot,obstacles):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        robot.move_forward(obstacles)
    if keys[pygame.K_DOWN]:
        robot.reverse(obstacles)
    if keys[pygame.K_LEFT]:
        robot.turn_left(obstacles)
    if keys[pygame.K_RIGHT]:
        robot.turn_right(obstacles)