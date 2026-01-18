import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread , imshow 
from skimage.color import rgb2hsv , rgb2gray

array_spectrum = np.array([np.arange(0,255,17),
                           np.arange(255,0,-17),
                           np.arange(0,255,17),
                           np.arange(255,0,-17)])
fig , ax = plt.subplots(1,2,figsize=(12,4))
ax[0].imshow(array_spectrum , cmap= 'gray')
ax[0].set_title("Arange Spectrum")

ax[1].imshow(array_spectrum.T , cmap= 'gray')
ax[1].set_title("Transpose Generation")

plt.show()
