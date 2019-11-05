#brute force algorithm to calculate convex hull
import numpy as np
import matplotlib.pyplot as plt
from decimal import Decimal
from point import point

#main routine
def main():
	#read sequence of 2D points and store them in an array of points
	filename="2DPoints.txt"
	dim=2
	points=[]
	with open(filename,"r") as fp:
		line_=fp.readline()
		while line_:
			a=line_.split()
			b=[]
			for x in a :
				b.append(float(x))
			p=point(dim,np.asarray(b))
			points.append(p)
			line_=fp.readline()

	#loop the points to determine the convex hull
	mostLeft_=0
	for i in range(0,len(points)-1):
		#find the most left point
		if(points[i].isLeft(points[mostLeft_],"X")):
			mostLeft_=i
	print("The most left point is ")
	points[mostLeft_].printPoint()
	
main()
	

