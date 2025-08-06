import cv2
import numpy as np

def gray(img):
    gray_img = []
    for row in img:
        gray_row = []
        for pixel in row:
            r = pixel[0]
            g = pixel[1]
            b = pixel[2]
            gray = r * 0.299 + g * 0.587 + b * 0.114 # ITU-R BT.601 formula
            gray_row.append(gray)
        gray_img.append(gray_row)
    gray_np = np.array(gray_img, dtype=np.uint8)
    return gray_np


def bwhite(img, threshold=128):
    gray_img = gray(img)
    black_img = []
    for row in gray_img:
        black_row = [0]
        for gray_tone in row:
            pixel = 0 if gray_tone < threshold else 255
            black_row.append(pixel)
        black_img.append(black_row)
    black_np = np.array(black_img, dtype=np.uint8)
    return black_np


if __name__ == "__main__":
    img = cv2.imread("./images/bird-andrei-r-popescu.jpg") 
    # img = cv2.imread("./images/pexels.jpg") 
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # By default, OpenCV uses BGR colors
    img = img.tolist()

    gray_img = gray(img)
    bwhite_img = bwhite(img, 90)

    # Save
    cv2.imwrite("./images/gray.jpg", gray_img)
    cv2.imwrite("./images/black_white.jpg", bwhite_img)
    
