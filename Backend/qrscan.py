from pyzbar import pyzbar
import argparse
import numpy as np
import cv2

image =cv2.imread("12.png")

# thresholds image to white in back then invert it to black in white
#   try to just the BGR values of inRange to get the best result
mask = cv2.inRange(image,(0,0,0),(200,200,200))
thresholded = cv2.cvtColor(mask,cv2.COLOR_GRAY2BGR)
inverted = 255-thresholded # black-in-white
barcodes = pyzbar.decode(inverted)
print (barcodes)