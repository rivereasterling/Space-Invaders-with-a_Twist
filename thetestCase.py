import unittest
from Lab10 import Laser
from Lab10 import Player
from Lab10 import Ship
from Lab10 import Enemy
from Lab10 import collide
class All_Test(unittest.TestCase):
	def test_will_work(self):
		pass
	#the above test wouldn't work for me so I know that somethings up with how pycharm does unit tests in pygame
	# I tried doing unit test examples outside of pygame and they worked fine so I am completely stumped the above works when put outside pygame but won't even run a test when its in here.
	def Laser_test(self):
		self.assertTrue(Laser, "there are no lasers")
	def Ship_test(self):
			self.assertTrue(Ship, "There are no ships")
	def Enemy_test(self):
			self.assertTrue(Enemy, "There are no enemies on screen")
	def Player_test(self):
			self.assertTrue(Player, "The player isn't on screen")
	def Collide_Test(self):
			self.assertTrue(collide(obj1=Player,obj2= Enemy), "The Player can not collide with an enemie")


if __name__ == '__main__':unittest.main()
