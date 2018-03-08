import matplotlib.pyplot as plt
import pylab
import matplotlib.image as mpimg
import numpy as np
from numpy.fft import fft2
from numpy import interp
from math import pi
from math import cos
from math import sin

"""
Write a program to transform a greyscale image to frequency domain by Fourier transform.
Apply any three low-pass filters on it and transform back each of the results to spatial domain and
display the result images.

"""
def fourierSum(u,v,M,N,img):
	totalSum = complex(0,0)
	for i in range(M):
		for j in range(N):
			a = 2*pi*(float(u)*float(i)/float(M) + float(v)*float(j)/float(N) )
			totalSum += img[i][j] * complex(cos(a),-sin(a))

	return totalSum

#######   Reading Image    ######################

img = mpimg.imread('img.jpg')
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

imgplot = plt.imshow(img)
#plt.show()

######  Fourier Transform of the image into frequency domain #############

F = fft2(img[:][:][0])

ARRAY = []

for i in range(len(F)):
	for j in range(len(F[0])):
		ARRAY.append([F[i][j].real,F[i][j].imag])

x = np.linspace(-0.5,0.5,100)
y = np.linspace(-3,0,100)
X, Y = np.meshgrid(x,y)

def f(x, y):
    return 1./(1+1j*(x+1j*y))

pylab.imshow(np.abs(f(X,Y)))
pylab.show()
pylab.imshow(ARRAY)
pylab.show()
