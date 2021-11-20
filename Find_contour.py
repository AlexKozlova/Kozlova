import cv2

img = cv2.imread('images/p.png')
# change color model of image
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# image is conversed in binary format
_, binary = cv2.threshold(img, 125, 255, cv2.THRESH_BINARY)
cv2.imshow('Source image', img)

# user select necessary area by buttons of the mouse
# left button is black
# right button is white
def on_EVENT_LBUTTONDOWN(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        xy = "%d,%d" % (x, y)
        # draw point
        cv2.circle(binary, (x, y), 1, (0, 0, 0), 35)
        cv2.imshow("image", binary)
    elif  event == cv2.EVENT_RBUTTONDOWN:
        xy = "%d,%d" % (x, y)
        # draw point
        cv2.circle(binary, (x, y), 1, (255, 255, 255), 30)
        cv2.imshow("image", binary)


cv2.namedWindow("image")
cv2.setMouseCallback("image", on_EVENT_LBUTTONDOWN)

cv2.waitKey(0)

# write choosing area of blood in other image file
cv2.imwrite('images/p1.png', binary)

# find contour of blood
new_img = cv2.imread('images/p1.png')
new_img = cv2.Canny(new_img, 170, 170)
con, hir = cv2.findContours(new_img, cv2.RETR_EXTERNAL, cv2. CHAIN_APPROX_SIMPLE)
img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
cv2.drawContours(img, con, -1, (230, 111, 240), 2)
cv2.imshow("Result Image with contour", img)

# write result in other image file
cv2.imwrite('images/p1_res.png', img)
cv2.waitKey(0)