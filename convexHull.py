#brute force algorithm to calculate convex hull
import numpy as np
from copy import deepcopy
from point import point

class convexHull:
	points_=np.array([])
	indices_=[]
	hull=[]
	def __init__(self,array):
		self.points=np.copy(array)
		for i in range(0,len(array)):
			indices_.append(i)

	def calcHull(self):
		

