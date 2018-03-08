import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

""" Write a program to implement histogram equalization. Capture a photograph in dark. No light (or
less light) should be visible in the photograph. Then, apply your histogram equalization program on
all the 3 channels (R,G,B) of your dark image, and show the result  """

#######   Reading Image    ######################

img = mpimg.imread('3.JPG')
M = len(img)    # length
N = len(img[0]) # breadth
MN = M*N
newRange = 100
temimg = img
imgplot1 = plt.imshow(temimg)
#plt.show()
#print img
######  Histogram Equalization dictionary init #################

intenDictR = dict()
intenDictG = dict()
intenDictB = dict()


####  Initializing a dictionary to store histogram data for three channels (Red , Green , Blue)  ########

for i in range(256):
	intenDictB[i] = 0
	intenDictR[i] = 0
	intenDictG[i] = 0

#### Calculating the magnitude of each pixel intensity for each channels ########

for i in range(M):
    for j in range(N):
        intenDictR[img[i][j][0]] += 1
        intenDictG[img[i][j][1]] += 1
        intenDictB[img[i][j][2]] += 1
#print intenDictR
####  probability distribuation of pixel intensity 

for i in range(256):
	intenDictB[i] = float(intenDictB[i]) / float(MN)
	intenDictG[i] =	float(intenDictG[i]) / float(MN)
	intenDictR[i] = float(intenDictR[i]) / float(MN)

#print intenDictR
#### cumulative probablity distribution of pixel intensity

for i in range(1,256):
	intenDictB[i] += intenDictB[i-1]
	intenDictG[i] += intenDictG[i-1]
	intenDictR[i] += intenDictR[i-1]
#print intenDictR
######  CPD * newRange #############

for i in range(256):
	intenDictR[i] *= newRange
	intenDictG[i] *= newRange
	intenDictB[i] *= newRange

#####  flooring the values
for i in range(256):
	intenDictB[i] = int(intenDictB[i])
	intenDictR[i] = int(intenDictR[i])
	intenDictG[i] = int(intenDictG[i])
#print intenDictR
##### Replace the values in the  original image
for i in range(M):
    for j in range(N):
        img[i][j][0] = intenDictR[img[i][j][0]]
        img[i][j][1] = intenDictG[img[i][j][1]]
        img[i][j][2] = intenDictB[img[i][j][2]]

#print img
imgplot = plt.imshow(img)
plt.show()
