# Briefing L04 C03

# Broken Robot
# We have a problem. Yesterday we sent out our remote tracking robot to collect some samples, but it's got a little lost and we need it back so we can send it back out to the alien landing site if they decide to land on the moon. Can you get it back to base?

# Some instructions to help you:
  # Import our robot module which communicates to our server and moves the robot.
  # The available functions are robot.right(), robot.left(), robot.up(), robot.down().
  # The robot can travel in 10x10 0-9 xy grid : start S = start 0,8 : F = finish 7,5.
  # The goal is to get the robot to the finishing co-ordinates without crashing or going out of bounds.
  # The server will respond with messages letting you know how the robot is doing after each function call.
  # There are also blocked coords blockedCoords = [[6,5], [6,6], [6,7], [7,7], [8,7], [9,7]].
  # Good luck agent!

# Tip: Navigate the robot back to base to get the flag.

#------------------------------------------------------

#
#  Robot Control Map
#
#  +-------------------+
# 9|                   |
# 8|S                  |
# 7|            x x x x|
# 6|            x      |
# 5|            x F    |
# 4|                   |
# 3|                   |
# 2|                   |
# 1|                   |
# 0|                   |
#  +-------------------+
#   0 1 2 3 4 5 6 7 8 9
#
#  S = Start position (0,8) F = Target destination (7,5),
#  x = Ravine, robot will be lost if hits these coords
#
# import robot module and use the robot.left(), robot.right(),
# robot.up() and robot.down() functions
#
import robot

#---------------------------------------------------------

# SOLUTION

#
#  Robot Control Map
#
#  +-------------------+
# 9|                   |
# 8|S                  |
# 7|            x x x x|
# 6|            x      |
# 5|            x F    |
# 4|                   |
# 3|                   |
# 2|                   |
# 1|                   |
# 0|                   |
#  +-------------------+
#   0 1 2 3 4 5 6 7 8 9
#
#  S = Start position (0,8) F = Target destination (7,5),
#  x = Ravine, robot will be lost if hits these coords
#
# import robot module and use the robot.left(), robot.right(),
# robot.up() and robot.down() functions
#
import robot
for i in range(4):
	robot.down()

for i in range(7):
  robot.right()

robot.up()
