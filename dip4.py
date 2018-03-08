import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from numpy import interp

""" Write a program to sharpen the same image by (a) gradient and (b) Laplacian and compare the
results. """


#######   Reading Image    ######################

img = mpimg.imread('3.JPG')
M = len(img)    # length
N = len(img[0]) # breadth
MN = M*N



#imgplot = plt.imshow(img)
#plt.show()

###### Greyscaling the image ###################
for i in range(1,M-1):
	for j in range(1,N-1):	
		img[i][j][0] = img[i][j][1] = img[i][j][2] = 0.2989*img[i][j][0] + 0.5870*img[i][j][1] + 0.1140*img[i][j][2]

tempImg = img

imgplot = plt.imshow(img)
#plt.show()

##########  Gradient method   ##################
""" F(x,y) = f(x+1,y) + f(x,y+1) - 2*f(x,y) """

for i in range(1,M-1):
	for j in range(1,N-1):
		img[i][j][0] = img[i+1][j][0] + img[i][j+1][0] - 2*img[i][j][0]
		img[i][j][1] = img[i][j][2] = img[i][j][0]	


########## Laplacian method ###################
""" F(x,y) = f(x+1,y) + f(x-1,y) + f(x,y+1) + f(x,y-1) - 4*f(x,y) """

for i in range(1,M-1):
	for j in range(1,N-1):
		tempImg[i][j][0] = tempImg[i+1][j][0] + tempImg[i-1][j][0] + tempImg[i][j+1][0] + tempImg[i][j-1][0] - 4*tempImg[i][j][0]
		tempImg[i][j][2] =tempImg[i][j][1] =tempImg[i][j][0] 

imgplot = plt.imshow(img)
plt.show()

imgplot = plt.imshow(tempImg)
plt.show()
