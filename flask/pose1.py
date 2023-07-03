from pyniryo import *
from os import chdir


robot = NiryoRobot("169.254.200.200")
#NiryoRobot.release_with_tool()

robot.calibrate_auto()


#j1 -3.053 +3.053
#j2 -1.91 +0.64
#j3 -1.39 +1.57
#j4 -3.049 +3.053
#j5 -1.744 +1.919
#j6 -2.529 +2.529


#x -0.455 +0.455 / Avant-Arrière
#y -0.455 +0.455 / Gauche-Droite
#z +0.135  +0.640 / Haut-Bas

robot.joints = [-0.680, -0.091, -1.273, 0.033, 0.637, -0.220]
robot.open_gripper()
robot.move_joints([0.125, -0.494, -1.166, 0.206, 1.315, -0.235])
robot.close_gripper()
robot.move_joints([0.15, -0.561, -1.281, 0.207, 1.805, -0.225])
robot.move_joints([1.525, -0.523, -1.100, -0.147, 1.805, -0.112])
robot.move_joints([1.552, -0.730, -1.062, -0.138, 1.858, -0.102])
robot.open_gripper()
robot.move_joints([0.128, -0.606, -1.100, 0.204, 1.514, -0.210])
robot.close_gripper()


robot.update_tool()

