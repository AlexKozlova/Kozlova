import cv2
import numpy as np

img = cv2.imread('images/proba.png')

img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img = cv2.GaussianBlur(img,(11,11),0)
img = cv2.Canny(img,90,120)

con,hir = cv2.findContours(img , cv2.RETR_EXTERNAL, cv2. CHAIN_APPROX_SIMPLE)
print(con)


cv2.imshow("image", img)
cv2.waitKey(0)