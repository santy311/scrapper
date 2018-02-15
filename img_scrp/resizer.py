import os
from PIL import Image

def rezz(label):
    for imageFile in (os.listdir(label)):
        im1 = Image.open(open(os.path.join(label,imageFile),'rb'))

        width = 128
        height = 128

        im5 = im1.resize((width, height), Image.ANTIALIAS)
        ext = ".png"
        
        if not os.path.exists('{}_REZ/'.format(label)):
            os.makedirs('{}_REZ/'.format(label))
        im5.save('{}_REZ/'.format(label)+label+imageFile[:-4]+ext)
