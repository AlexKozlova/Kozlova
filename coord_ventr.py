import cv2
import math
from sympy import Symbol, nsolve


img = cv2.imread('images/p1_res.png')
x1 = 0
y1 = 0
x2 = 0
y2 = 0

def on_EVENT_LBUTTONDOWN(event, x, y, flags, param):
    global x1, y1,x2,y2
    if event == cv2.EVENT_LBUTTONDOWN:
        xy = "%d,%d" % (x, y)
        #draw point
        cv2.circle(img, (x, y), 3, (255, 250, 0), -1)
        # write coordinates of start point
        #cv2.putText(img, xy, (x, y), cv2.FONT_HERSHEY_PLAIN,
                   # 1.0, (250,0,0),2)
        cv2.imshow("image", img)
        x1, y1 = x, y
        #print(x1,y1)
    elif  event == cv2.EVENT_RBUTTONDOWN:
        xy = "%d,%d" % (x, y)
        #draw point
        cv2.circle(img, (x, y), 3, (255, 250, 0), -1)
        # write coordinates of end point
        #cv2.putText(img, xy, (x, y), cv2.FONT_HERSHEY_PLAIN,
                   # 1.0, (250,0,0),2)
        cv2.imshow("image", img)
        x2, y2 = x, y
        #print(x2, y2)
        #if x1 != 0 and x2 != 0:
            # draw line which is shown valve ring
            #cv2.line(img, (x1,y1), (x2,y2), (250, 0, 0), 1)

        # find distance between points of valve ring
        r = round(math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2), 2)
        #print('Расстояние между точками', r)

        # find equation of line of valve ring
        k = Symbol('k')
        b = Symbol('b')
        eq1 = k*x1 + b - y1
        eq2 = k*x2 + b - y2
        k_, b_ = nsolve( (eq1, eq2), (k, b), (1, 1))
        #print(k_, b_)

        # find center of valve ring line
        x = Symbol('x')
        y = Symbol('y')
        eq3 = k_ * x - y + b_
        eq4 = (x2 - x) ** 2 + (y2 - y) ** 2 - (r / 2) ** 2
        xc, yc = nsolve((eq3, eq4), (x, y), (1, 1))
       # cv2.circle(img, (int(xc), int(yc)), 3, (150, 100, 200), -1)

        # find center of electrode system
        alpha = math.asin((x2 - xc)/(r/2))
        betta = 1.5708 - alpha
        #print('Betta',betta)
        xce = 23* math.sin(betta)
        yce = 23* math.cos(betta)
        cv2.circle(img, (int(xc + xce), int(yc - yce)), 3, (0, 250, 200), -1)

        # draw lines fol electrode system
        b2 = (yc - yce) - k_*(xc + xce)
        y1out = k_*(x1 - 50) + b2
        y2out = k_*(x2 + 50) + b2
        cv2.line(img, ((x1-50), int(y1out)), ((x2 + 50), int(y2out)), (250, 0, 0), 1)
        r2 = round(math.sqrt(((x1-50) - (x2 + 50)) ** 2 + (int(y1out) - int(y2out)) ** 2), 2)
        #print('Расстояние между точками 1 и 5',r2)
        xdiff = (100)*math.sin(0.785398 + betta)
        ydiff = (100)*math.cos(0.785398 + betta)
        cv2.line(img, (int(x1 - 50+xdiff), 0),
                 (int(xc + xce), int(yc - yce)), (250, 0, 0), 1)
        ydiff2 = (r2/2)*math.cos(0.785398 - betta)
        cv2.line(img, (int(img.shape[1]), int(y2out - ydiff2)),
                 (int(xc + xce), int(yc - yce)), (250, 0, 0), 1)
        x5 = r2 * math.sin(betta)
        y5 = r2 * math.cos(betta)
        cv2.line(img, (int(xc + xce + x5), int(yc - yce - y5)),
                 (int(xc + xce), int(yc - yce)), (250, 0, 0), 1)



cv2.namedWindow("image")
cv2.setMouseCallback("image", on_EVENT_LBUTTONDOWN)

cv2.imshow("image", img)
cv2.waitKey(0)

cv2.destroyAllWindows()


