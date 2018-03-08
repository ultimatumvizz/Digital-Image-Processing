""" Take an RGB color image and obtain the histograms of the image separately in Hue, Saturation
and Intensity channels.   """


import cv2
import math
from matplotlib.pylab import plt
img = cv2.imread("anadka.jpg")
#print img

M = len(img)    # length
N = len(img[0]) # breadth
print M,N
a = []

##################### init HSI matrix ###############

H_matrix = dict()
S_matrix = dict()
I_matrix = dict()

for i in range(M):
	for j in range(N):
	    B = img[i][j][0]
	    G = img[i][j][1]
	    R = img[i][j][2]
	    theta = 1
	
	    a = (2*R - G - B)/2.0
	    b = math.sqrt((R-G)**2 + (R-G)*(G-B) )
            try :
                theta = math.degrees(math.acos(float(a)/float(b)))
            except ValueError: 
                pass
            except ZeroDivisionError:
                pass
    
            try :
    		S = 1 - ( 3.0/sum([R,G,B]) * min([R,G,B])) 
            except ZeroDivisionError :
                pass


	    if B<=G : 
		H = theta
	    else:
		H = 360 - theta

	    I =  1.0/3  * sum([R,G,B])



	    if round(H,2) in H_matrix.keys() :
		H_matrix[round(H,2)] += 1
	    else :
		H_matrix[round(H,2)] = 1 

	    if round(S,2) in S_matrix.keys() :	
		S_matrix[round(S,2)] += 1
	    else :
		S_matrix[round(S,2)] = 1 

	    if round(I,2) in I_matrix.keys() :
		I_matrix[round(I,2)] += 1
	    else :
		I_matrix[round(I,2)] = 1 			
            print i,j
del H_matrix[1.0]     

#########   green --- H

plt.bar(H_matrix.keys(),H_matrix.values(),color = 'g')
plt.show()


########   blue   ---- S
plt.bar(S_matrix.keys(),S_matrix.values(),color = 'b')
plt.show()


########   red    ----- I
plt.bar(I_matrix.keys(),I_matrix.values(),color = 'r')
plt.show()
