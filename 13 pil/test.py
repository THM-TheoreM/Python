import Image
import numpy as np
import scipy.misc

width = 100
height = 40
bgcolor = (255,255,255)
image = Image.new('RGB',(width,height),bgcolor)
image.save('d:/1.jpg')

a = np.zeros([100,40,3])
a[:,:,0] = 225*np.ones([100,40])
scipy.misc.imsave('d:/2.jpg',a)

