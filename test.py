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
	print("########################")
	#n^2 Algorithm
	hull=[]
	p=mostLeft_
	q=0
	n=len(points)	
	while(True):
		epsilon=1e-3 
		hull.append(p)
		q = (p + 1) % n 
		for i in range(n): 
			#we want to check the angle formed by two vectors pq and qr
			vector1=deepcopy(points[q])
			vector1-points[p]
			vector2=deepcopy(points[i])
			vector2-points[q]
			theta=vector1.angle(vector2)
			if(theta<=(90-epsilon) and theta>epsilon): 
				print(theta)
				q=i
        	p = q 
        	if(p == mostLeft_): 
            		break	
	print("########################")
	print("The points indices that form a convex hull are  ")
	for i in hull:
		points[i].printPoint()
	print("########################")
	
main()
