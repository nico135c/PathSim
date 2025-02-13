from ui.simulator import Simulator
import core.world as world

params = world.load_world("assets/world_img_obstacles.png")

sim = Simulator(params)
sim.run()