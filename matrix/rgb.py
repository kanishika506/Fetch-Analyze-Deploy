import numpy as np 
import matplotlib.pyplot as plt
from skimage.io import imshow , imread 
from skimage.color import rgb2hsv ,rgb2gray

array=np.array([[[255,0,0],[0,255,0],[0,0,255]]])
plt.imshow(array)
plt.show()