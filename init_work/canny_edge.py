import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

class Canny:
	
	def __init__(self, filename, ind):
		self.img = cv.imread(filename ,0)
		self.ind = ind
		
	def do_canny(self):
		edges = cv.Canny(self.img,200,200, apertureSize = 3)
		#plt.subplot(121),plt.imshow(self.img, cmap = 'gray')
		#plt.title('Original Image'), plt.xticks([]), plt.yticks([])
		#plt.subplot(122),
		plt.imshow(edges,cmap = 'gray')
		
		plt.savefig('cannyimg' + str(self.ind) + '.png')
		#plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
		#plt.show()
		return edges
		
	def do_hough(self, edges):
		minLineLength = 100
		maxLineGap = 10
		lines = cv.HoughLinesP(edges,1,np.pi/180,100,minLineLength,maxLineGap)
		print lines
		for line in lines:
			for x1,y1,x2,y2 in line:
				print('x ', x1, x2)
				print('y', y1, y2)
				cv.line(self.img,(x1,y1),(x2,y2),(0,255,0),2)
				
		cv.imwrite('houghlines1.jpg',self.img)
c = Canny('cloud14.jpg', 2)
edges = c.do_canny()
c.do_hough(edges)