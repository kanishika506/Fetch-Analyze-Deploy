from skimage.io import imread , imshow
import matplotlib.pyplot as plt 

panda=imread("actual_image/panda.jpg")
plt.imshow(panda)
plt.axis('off')
plt.show()