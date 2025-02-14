import pygame

from core.debug import manual_control
from core.robot import Robot
from core.algorithms import main
import core.debug

class Simulator:
    def __init__(self, params):
        # WORLD PARAMETERS
        self.start, self.goal, self.obstacles, self.world_size = params

        #INITIATING ROBOT
        self.robot = Robot(self.start)

        #PYGAME STUFF
        pygame.init()
        self.screen = pygame.display.set_mode((self.world_size))
        pygame.display.set_caption('PathSim')
        pygame.display.set_icon(pygame.image.load('assets/pathsim_icon.png'))
        self.clock = pygame.time.Clock()

        #SIMULATION SETTINGS
        self.fps = 30

        #COLORS
        self.white = (255,255,255)

    def run(self):
        running = True
        while running:
            main(self.start, self.goal, self.obstacles, self.world_size, self.robot)

            manual_control(self.robot,self.obstacles)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.fill((self.white))

            pygame.draw.circle(self.screen, (0, 255, 0), self.goal, 10) #GOAL POINT
            pygame.draw.polygon(self.screen, (0,0,255), self.robot.get_triangle())

            for obstacle in self.obstacles:
                pygame.draw.polygon(self.screen, (255, 0, 0), obstacle.vertices)

            pygame.display.flip()
            self.clock.tick(self.fps)
        pygame.quit()