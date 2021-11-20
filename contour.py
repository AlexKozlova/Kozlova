import cv2
import numpy as np

img = cv2.imread('images/proba.png')

def on_EVENT_LBUTTONDOWN(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        xy = "%d,%d" % (x, y)
        # draw point
        cv2.circle(img, (x, y), 1, (255, 250, 0), 1)
        # write coordinates of point
        cv2.putText(img, xy, (x, y), cv2.FONT_HERSHEY_PLAIN,
                    1.0, (250, 0, 0), 2)
        cv2.imshow("image", img)

#img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#_, binary = cv2.threshold(img, 125, 255, cv2.THRESH_BINARY)

cv2.namedWindow("image")
cv2.setMouseCallback("image", on_EVENT_LBUTTONDOWN)

#con = cv2.findContours(binary , cv2.RETR_EXTERNAL, cv2. CHAIN_APPROX_SIMPLE)


#con, hir = cv2.findContours(img , cv2.RETR_EXTERNAL, cv2. CHAIN_APPROX_SIMPLE)
#print(con[0])

new_img = np.zeros(img.shape)
#cv2.drawContours(new_img, con, -1, (230, 111, 170), -1)

cv2.imshow("Image", img)
cv2.waitKey(0)