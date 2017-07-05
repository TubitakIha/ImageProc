# -*- coding: utf-8 -*-
import cv2
import numpy as np
import time
MORPH = 11
CANNY = 250

DELAY = 0.02

_width  = 210.0*2
_height = 297.0*2

_width  = 100.0*6
_height = 78.0*6

_margin = 0.0

corners = np.array(
	[
		[[  		_margin, _margin 			]],
		[[ 			_margin, _height + _margin  ]],
		[[ _width + _margin, _height + _margin  ]],
		[[ _width + _margin, _margin 			]],
	]
)

pts_dst = np.array( corners, np.float32 )


def renkKirpmaAlani(image):
    #kirmizi
    lowerR=np.array([180,10,10])

    # Convert BGR to HSV
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    # define range of blue color in HSV
    lower_blue = np.array([110, 50, 50])
    upper_blue = np.array([130, 255, 255])
    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(image, image, mask=mask)
    cv2.imshow('image', image)
    cv2.imshow('mask', mask)
    cv2.imshow('result', res)
    #******************************** Bu alanin kose noktalarina gore kirpma yapip resim dondurulecek
    k = cv2.waitKey(5)

def renkTespit(image,centerX,centerY):
    color = int(image[centerX, centerY])
    #**************************************** Burada color 3 boyutlu rgb degeri dondurur(bgr) buna gore 3 tane if-else ile rengi tespit et ve string dondur


def rotate( image, angle, center = None, scale = 1.0 ):
	( h, w ) = image.shape[:2]
	if center is None: center = ( w / 2, h / 2 )
	# Perform the rotation
	M = cv2.getRotationMatrix2D( center, angle, scale )
	rotated = cv2.warpAffine( image, M, ( w, h ), flags = cv2.INTER_CUBIC )
	return rotated


if 0:
    print
else:
    ret = 1
    rgb = cv2.imread("c.jpg", 1)

    rgb = cv2.resize(rgb, (1024, 768))

if (ret):

    gray = cv2.cvtColor(rgb, cv2.COLOR_BGR2GRAY)

    gray = cv2.bilateralFilter(gray, 2, 10, 120)

    edges = cv2.Canny(gray, 10, CANNY)

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (MORPH, MORPH))

    closed = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)

    cv2.imshow('closed formu' ,closed)
    if cv2.waitKey(0) & 0xff == 27:
        cv2.destroyAllWindows()
    _,contours, h = cv2.findContours(closed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) #sekilin dort kosesini tutuyor eger tum kenar piksellerini tutmak istiyorsan approx_none gonder

    i = 0
    for cont in contours:

        # Küçük alanlarý pass geç

        if cv2.contourArea(cont) > 5000:

            arc_len = cv2.arcLength(cont, True) #bu deger seklin cevresidir.

            approx = cv2.approxPolyDP(cont, 0.1 * arc_len, True) #contour approximation. Kucuk olursa daha hatalý sekilleride alabilir.
            #amac contour sekli daha az koseli baska sekle yaklastirir. epsilon bu iki sekil arasýndaki farktýr.

            if (len(approx) == 4):
                IS_FOUND = 1
                i = i + 1
                M = cv2.moments( cont )
                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])
                cv2.putText(rgb, ".M"+ str(i), (cX, cY), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), 3)
                print str(i)+'.Sekil Bulundu'
                print approx
                """
                [
                    [[847 204]]
                    [[316 205]]
                    [[316 624]]
                    [[861 620]] gibi kose noktalari basar
                ]
                """

                pts_src = np.array(approx, np.float32)

                h, status = cv2.findHomography(pts_src, pts_dst)
                # out = cv2.warpPerspective(rgb, h, (int(_width + _margin * 2), int(_height + _margin * 2))) #ana fotograf icin eleme amaciyla kullanýlacak

                cv2.drawContours(rgb, [approx], -1, (255, 0, 0), 2)
                print '---------------------------'
            else:
                pass

        else:
            print 'contour area= '+ str(cv2.contourArea(cont))+' - kucuk oldugu icin pass gecildi'
            print '--------'
    # cv2.imshow( 'closed', closed )
    cv2.imshow( 'gray', gray )
    cv2.imshow('edges', edges)
    cv2.imshow('rgb', rgb)

    renkKirpmaAlani(rgb)
else:
    print "Stopped"

if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()