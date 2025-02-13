import cv2
import numpy as np

def find_dot(img,bounds):
    lower, upper = bounds

    mask = cv2.inRange(img, lower, upper)

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        M = cv2.moments(contour)
        if M["m00"] != 0:
            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])

    return (cx,cy)

def load_world(world_img):
    world_img = cv2.imread(world_img)
    world_hsv = cv2.cvtColor(world_img,cv2.COLOR_BGR2HSV)
    world_size = (world_img.shape[1], world_img.shape[0])

    #FINDING START AND GOAL
    blue_bounds = (np.array([90, 50, 50]),np.array([130, 255, 255]))
    green_bounds = (np.array([40, 40, 40]),np.array([80, 255, 255]))
    start = find_dot(world_hsv, blue_bounds)
    goal = find_dot(world_hsv, green_bounds)

    #FIND OBSTACLES
    lower_red1 = np.array([0, 50, 50])
    upper_red1 = np.array([10, 255, 255])

    lower_red2 = np.array([170, 50, 50])
    upper_red2 = np.array([180, 255, 255])

    mask1 = cv2.inRange(world_hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(world_hsv, lower_red2, upper_red2)
    mask = cv2.bitwise_or(mask1, mask2)

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    obstacles = []

    for contour in contours:
        approx = cv2.approxPolyDP(contour, 0, True)
        points = approx.reshape(-1, 2).tolist()
        obstacle = Obstacle(points)
        obstacles.append(obstacle)

    return start, goal, obstacles, world_size

class Obstacle:
    def __init__(self, vertices):
        self.vertices = vertices