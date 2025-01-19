from __future__ import print_function
from __future__ import division
import cv2 as cv
import argparse

alpha_slider_max = 100
title_window = 'Linear Blend'

def on_trackbar(val):
    alpha = val / alpha_slider_max
    beta = ( 1.0 - alpha )
    src1 = cv.imread("temp/bw_image.jpg")
    src2 = cv.imread("temp/screen.png")
    rows, cols, _ = src1.shape
    src2 = src2[:rows, :cols]
    dst = cv.addWeighted(src1, alpha, src2, beta, 0.0)
    cv.imshow(title_window, dst)

cv.namedWindow(title_window)

trackbar_name = 'Alpha x %d' % alpha_slider_max
cv.createTrackbar(trackbar_name, title_window , 0, alpha_slider_max, on_trackbar)

on_trackbar(0)

cv.waitKey()
