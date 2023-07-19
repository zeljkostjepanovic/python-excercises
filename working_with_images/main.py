#!/usr/bin/env python3
import cv2

def resize_image(img, factor, resname):
    resized = (int(img.shape[1] / reduce_factor), int(img.shape[0] / reduce_factor))
    resized_image = cv2.resize(img,resized)
    cv2.imwrite(resname, resized_image)
    cv2.imshow("Resized_image", resized_image)
    cv2.waitKey(3000)
    cv2.destroyAllWindows


img = cv2.imread(input("Please enter image path: "), 1)
reduce_factor = float(input("Please input reduce factor: "))
resname = input("Please enter location for resized image: ")

resize_image(img, reduce_factor, resname)