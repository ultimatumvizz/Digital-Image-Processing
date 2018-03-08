import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from numpy import interp


"""Write a program to take the same image as input, and apply gamma transformation on all the 3
channels. Show the results for taking (a) gamma as 5 and (b) gamma as 0.2. """


#######   Reading Image    ######################

img = mpimg.imread('3.JPG')
M = len(img)    # length
N = len(img[0]) # breadth
MN = M*N

tempImg = img

imgplot = plt.imshow(img)
#plt.show()

################ GAMMA VALUES ############################
GAMMAVALUE_1 = 5
GAMMAVALUE_2 = 0.2

#############  rewriting the image pixels based on gamma transformation #######################

for i in range(M):
    for j in range(N):
        img[i][j][0]     = int(255 * (float(img[i][j][0])/255.0)**GAMMAVALUE_1)
        tempImg[i][j][0] = int(255 * (float(tempImg[i][j][0])/255.0)**GAMMAVALUE_2)

        img[i][j][1] 	 = int(255 * (float(img[i][j][1])/255.0)**GAMMAVALUE_1)
        tempImg[i][j][1] = int(255 * (float(tempImg[i][j][1])/255.0)**GAMMAVALUE_2)

        img[i][j][2] 	 = int(255 * (float(img[i][j][2])/255.0)**GAMMAVALUE_1)
        tempImg[i][j][2] = int(255 * (float(tempImg[i][j][2])/255.0)**GAMMAVALUE_2)
        

imgplot = plt.imshow(img)
plt.show()

imgplot1 = plt.imshow(tempImg)
plt.show()
