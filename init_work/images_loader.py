
from os import listdir
from os.path import isfile, join
import numpy as np

import cv2
import image

from PIL import Image

from hsv import Hsv

class Img_loader:
	
	def __init__(self, path):
		onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
		#print(onlyfiles)
		self.images = []
		
	def tiff_to_jpeg(self, path, n_images):
		"""
		path - Path to the multipage-tiff file
		n_images - Number of pages in the tiff file
		"""
		img = Image.open(path, 'r')
		outfile = path[:-4] + '.jpeg'
		print(path)
		try:
			im = Image.open(path, 'r')
			#print "Generating jpeg for %s" % name
			im.thumbnail(im.size)
			im.save(outfile, "JPEG", quality=100)
		except Exception, e:
			print e
			
	def load_jpegs(self, path, dir_to_save):
		onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
		for name in onlyfiles:
			print(name)
			h = Hsv(name, path)
			#h= Hsv('cloud14.jpg')
			hsv = h.to_hsv()
			img_hsv = h.blue_mask(hsv)
			cv2.imwrite(join(dir_to_save, name), img_hsv)
		
im_loader = Img_loader('dobre_fotky')
im_loader.load_jpegs('dobre_fotky_jpg', 'dobre_fotky_jpg/blue_mask2')