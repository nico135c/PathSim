from ui.simulator import Simulator
import core.world as world
from core.algorithms import main

params = world.load_world("assets/world_img_obstacles2.png")

sim = Simulator(params)
sim.run()