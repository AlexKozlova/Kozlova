import cv2
import numpy as np
import math
import sympy
from sympy import Symbol, solve, nsolve


img = cv2.imread('images/proba.png')

def on_EVENT_LBUTTONDOWN(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        xy = "%d,%d" % (x, y)
        #draw point
        cv2.circle(img, (x, y), 1, (255, 250, 0), 1)
        # write coordinates of point
        cv2.putText(img, xy, (x, y), cv2.FONT_HERSHEY_PLAIN,
                    1.0, (250,0,0),2)
        cv2.imshow("image", img)



#cv2.line(img, (mat[0][0], mat[0][1]), (mat[1][0], mat[1][1]), (250, 0, 0), 2)
cv2.namedWindow("image")
cv2.setMouseCallback("image", on_EVENT_LBUTTONDOWN)


#for i in range(2):
print(cv2.setMouseCallback("image", on_EVENT_LBUTTONDOWN))


#cv2.line(img, (266,236), (95,127), (250,0,0), 2)

#find distance between points of valve ring
r = math.sqrt((266 - 95)**2 + (236 - 127)**2)
#cv2.circle(img,(266,236),int(ser), (250,120,100), 2)

#find center of valve ring line
x = Symbol('x')
y = Symbol('y')
eq1 = 0.64*x - y + 66.2
eq2 = (266 - x)**2 + (236 - y)**2 - (r/2)**2
a, b = nsolve( (eq1, eq2) , (x,y), (1, 1))
image = cv2.circle(img, (int(a),int(b)), 3, (50, 200, 200), -1)

print(a,b)

#eq3 = -(1/0.64)*x - y + 66.2
#eq4 = (int(a) - x)**2 + (int(b) - y)**2 - (0.0000004)**2
#c, d = nsolve( (eq3, eq4) , (x,y), (100, 100))
#image = cv2.circle(img, (int(c),int(d)), 3, (50, 200, 200), -1)

#find center of electrode system
#eq3 = (abs(a*x + b*y))/((pow((a**2 + b**2),.5 )* pow((x**2 + y**2),.5)))
#eq4 = pow(((x - a)**2 + (y - b)**2), .5) - 10**2
#print(nsolve((eq3, eq4) , (x,y), (1, 1)))





cv2.imshow("image", img)
cv2.waitKey(0)

cv2.destroyAllWindows()


