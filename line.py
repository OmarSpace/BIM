#line class
from point import point
import numpy as np

class line:
	l_=np.array([])
	length_=0
	#constructor
	def __init__(self,p1,p2):
		self.l_=[p1,p2]
		self.length_=self.l_[0].eDist(self.l_[1])
	#print points in the line 
	def printLine(self):
		self.l_[0].printPoint()
		self.l_[1].printPoint()
		print(self.length_)

