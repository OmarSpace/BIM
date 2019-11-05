#point class
import numpy as np
from copy import deepcopy

class point:
	p_=np.array([])
	dim_=0
	small_=1e-14
	#constructor
	def __init__(self,dim,array):
		self.dim_=dim
		array=np.asarray(array)
		self.p_=np.copy(array)
	#equality overloading/copy constructor
	def __eq__(other):
		copied_=point(deepcopy(other.dim_),np.copy(other.p_))
		return copied_
	#addition + overloading
	def __add__(self,other):
		self.p_=self.p_+other.p_
	#subtraction - overloading
	def __sub__(self,other):
		self.p_=self.p_-other.p_
	#dot product * overloading
	def __mul__(self,other):
		dotProd_=0
		for i in range(0,self.dim_):
			dotProd_=dotProd_+self.p_[i]*other.p_[i]
		return dotProd_
	#cross product & overloading
	def __and__(self,other):
		crossProd_=np.cross(self.p_,other.p_)
		return crossProd_
	#eucledian distance 
	def eDist(self,other):
		dist_=0
		for i in range(0,self.dim_):
			dist_=dist_+(self.p_[i]-other.p_[i])*(self.p_[i]-other.p_[i])
		dist_=pow(dist_,0.5)
		return dist_
	#mag 
	def mag(self):
		mag_=0
		for i in range(0,self.dim_):
			mag_=mag_+(self.p_[i]*self.p_[i])
		mag_=pow(mag_,0.5)
		return mag_
	#to determine if a point left or right another point
	def isLeft(self,other,axis):
		index_=0
		if (axis=="X"):
			index_=0
		elif (axis=="Y"):
			index_=1
		elif (axis=="Z"):
			index_=2
		if(self.p_[index_]<=other.p_[index_]):
			return True 
		else:
			return False
	def angle(self,other):
		angle_=-10000
		a_=self*other
		b_=self.mag()
		c_=other.mag()
		thetaRad_= np.arccos(a_/(b_*c_+self.small_))
		return (thetaRad_*180/np.pi)
	#print attributes of the point class
	def printPoint(self):
		print('Dimension is ',self.dim_)
		for i in range (0,self.dim_):
			print(self.p_[i])
