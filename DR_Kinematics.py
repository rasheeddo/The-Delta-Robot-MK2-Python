from LabDeltaRobot import *
import time

deltarobot = DeltaRobot()

#deltarobot.RobotTorqueOff()
deltarobot.RobotTorqueOn()

deltarobot.GoHome()

deltarobot.GotoPoint(150,-150,-700)

deltarobot.KinematicsCheck()

