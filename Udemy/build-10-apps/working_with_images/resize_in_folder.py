import os
import cv2

def detect_orientation(img):
    if img.shape[1] > img.shape[0]:
        return "horizontal"
    elif img.shape[1] == img.shape[0]:
        return "square"
    else:
        return "vertical"

def longer(x,y):
    if x > y:
        return x
    elif x < y:
        return y
    else:
        return x

def shorter(x,y):
    if x < y:
        return x
    elif x > y:
        return y
    else:
        return x

def resize_images(path, x, y):
    for img in os.listdir(path):
        if img.endswith(".png") or img.endswith(".jpg"):
            image = cv2.imread(os.path.join(path,img), cv2.IMREAD_COLOR)
            if detect_orientation(image) == "horizontal":
                resized_image = cv2.resize(image,(int(longer(x,y)),int(shorter(x,y))), 
                interpolation=cv2.INTER_CUBIC)
            elif detect_orientation(image) == "vertical":
                resized_image = cv2.resize(image,(int(shorter(x,y)),int(longer(x,y))), 
                interpolation=cv2.INTER_CUBIC)
            else:
                resized_image = cv2.resize(image,(int(longer(x,y)),int(longer(x,y))), 
                interpolation=cv2.INTER_CUBIC)
            cv2.imwrite(os.path.join(path,"resized_{}".format(img)), resized_image)
        else:
            continue


resize_images("sample", 1440, 1024)