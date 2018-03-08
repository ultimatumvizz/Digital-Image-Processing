""" Take a grayscale image and apply Haar transform. For ease in computation resize the input image
by downsampling. """


import cv2
import math
import numpy as np
from matplotlib.pylab import plt

def kpq(k_value):
    p =[0] * k_value
    q = [0] * k_value
    for i in range(1,k_value):
        p[i] = int(math.floor(math.log(i,2)))
        q[i] = i + 1 - 2**p[i]
    return p,q

def power2Matrix(num):
    matrix = []
    for i in range(num+1):
        matrix.append(2**i)
    return matrix

def haarTransformMatrix(rows,cols):
        haarMatrix = []
        p,q = kpq(cols)
        print p,q
        pwMat = power2Matrix(p[-1])
        print pwMat 
        for i in range(rows):
            z = float(i)/float(rows)
            print z
            rowMatrix = []
            for k in range(cols):
                if k == 0 :
                    rowMatrix.append(1.0)
                elif  (float((q[k]-1.0))/float(pwMat[p[k]])) <= z < (float((q[k] - 0.5))/float(pwMat[p[k]])):
                    rowMatrix.append(math.pow(2,p[k]/2.0))
                elif  (float((q[k]-0.5))/float(pwMat[p[k]])) <= z  < ((float(q[k]))/float(pwMat[p[k]])):
                    rowMatrix.append( -1 * math.pow(2,p[k]/2.0))
                else :
                    rowMatrix.append(0.0)
            haarMatrix.append(rowMatrix)
        return haarMatrix

haarMatrix = np.array(haarTransformMatrix(64,64))
haarTranspose = haarMatrix.transpose()

img = cv2.imread("kudremukha.jpg")
img = cv2.resize(img,(64,64))

#################### GreyScaling the image #######################

newImg = [[0]*64]*64
for i in range(64):
    for j in range(64):
       newImg[i][j] = img[i][j][0]
newImg = np.array(newImg)                                
###################################################################
"""  Hr * imageMatrix * Hr(traspose)  """
finalMatrix = (1/64.0) * np.dot(np.dot(haarMatrix,newImg),haarTranspose)
print finalMatrix 
######################################################################
for i in range(64):
    for j in range(64):
        img[i][j][0] = img[i][j][1] = img[i][j][2] = finalMatrix[i][j]
plt.imshow(img)
plt.show()
