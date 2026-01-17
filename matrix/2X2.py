import numpy as np
import matplotlib.pyplot as plt 
from skimage import img_as_uint
from skimage.io import imshow , imread 
from skimage.color import rgb2hsv
from skimage.color import rgb2hsv

a=np.array([[255,0],[0,255]])
plt.imshow(a,cmap='gray')
plt.show()