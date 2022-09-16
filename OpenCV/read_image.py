import cv2
import matplotlib.pyplot as plt
import random

# read the image 
img = cv2.imread('IMG_6617.PNG', cv2.IMREAD_GRAYSCALE)
# print(img.shape)
# get the window for the image
# cv2.namedWindow('image', cv2.WINDOW_NORMAL)
img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
plt.imshow(img, cmap='gray', interpolation= 'bicubic')
plt.show()
# cv2.imshow('image', img)

print(img.shape[1])

cv2.imwrite('new.png', img)
cv2.waitKey(0)

cv2.destroyAllWindows()



