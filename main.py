import cv2
import numpy as np

def main():
   # print sys.argv[1]
    print "Train Baslatildi \n"



    img = cv2.imread("c.jpg")


    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(imgray, 127, 255, 0)
    im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


    cv2.drawContours(img, contours, -1, (0, 255, 0), 3)

    cv2.drawContours(img, contours, 3, (0, 255, 0), 3)

    cnt = contours[4]
    cv2.drawContours(img, [cnt], 0, (0, 255, 0), 3)
    cv2.imshow("asd", img)
    cv2.waitKey()

if __name__ == "__main__":
    main()