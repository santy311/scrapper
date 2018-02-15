import os
from PIL import Image


def rezz(img_dir):
	img_dir = os.getcwd()	
	for label in (os.listdir(img_dir)):    
		for imageFile in (os.listdir(label)):
			im1 = Image.open(open(os.path.join(label,imageFile),'rb'))

			width = 28
			height = 28

			im5 = im1.resize((width, height), Image.ANTIALIAS)
			ext = ".png"
			im5.save('1.png')
			if not os.path.exists('{}_REZ/'.format(label)):
			    os.makedirs('{}_REZ/'.format(label))
			im5.save('{}_REZ/'.format(label)+imageFile+ext)

rezz()
