import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from numpy import interp

"""Write a program to smoothen a greyscale image by a 3X3 smoothing filter, which emphasizes on
the current pixel value, gives lesser weightage to its 4-neighbors and much lesser weightage to the
8-neighbor pixels. Compare the result with median filter."""

centerPoint        = float(1.0/4.0)
fourNeighborPoint  = float(1.0/8.0)
eightNeighborPoint = float(1.0/16.0)

medianFilterWindowPoint = float(1.0/9.0)

#######   Reading Image    ######################

img = mpimg.imread('3.JPG')
M = len(img)    # length
N = len(img[0]) # breadth
MN = M*N



imgplot = plt.imshow(img)
#plt.show()

###### Greyscaling the image ###################
for i in range(1,M-1):
	for j in range(1,N-1):	
		img[i][j][0] = img[i][j][1] = img[i][j][2] = 0.2989*img[i][j][0] + 0.5870*img[i][j][1] + 0.1140*img[i][j][2]

tempImg = img
print img[1][10]
imgplot = plt.imshow(img)
#plt.show()

###############  Applying smoothing filter of 3 by 3 window #################### Median filter applied on tempImg #########
for i in range(1,M-1):
	for j in range(1,N-1):
		a =eightNeighborPoint*(img[i-1][j-1][0]+img[i-1][j+1][0]+img[i+1][j-1][0]+img[i+1][j+1][0]) + fourNeighborPoint*(img[i][j-1][0]+img[i][j+1][0]+img[i-1][j][0]+img[i+1][j][0]) + centerPoint*img[i][j][0]
		img[i][j][0] = img[i][j][1] = img[i][j][2] = a 
		a = medianFilterWindowPoint*(tempImg[i-1][j-1][0]+tempImg[i-1][j+1][0]+tempImg[i+1][j-1][0]+tempImg[i+1][j+1][0] + tempImg[i][j-1][0]+tempImg[i][j+1][0]+tempImg[i-1][j][0]+tempImg[i+1][j][0] + tempImg[i][j][0] )
		tempImg[i][j][0] = tempImg[i][j][1] = tempImg[i][j][2] = a

imgplot = plt.imshow(img)
plt.show()

imgplot = plt.imshow(tempImg)
plt.show()
