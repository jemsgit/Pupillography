import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('images.png')

# Denoising
dst = cv2.fastNlMeansDenoisingColored(img,None,10,10,7,21)

cv2.imwrite('res.png',dst)
img_black = cv2.imread('res.png',0)

equalized = cv2.equalizeHist(img_black)
res = np.hstack((img_black,equalized)) #stacking images side-by-side

ret,th1 = cv2.threshold(equalized,30,255,cv2.THRESH_BINARY)
cv2.imwrite('res3.png',th1)
img_black = cv2.imread('res3.png',0)
height, width, channels = img.shape
centre = [width/2, height/2]
points = []
vertical = [centre[1], centre[1]+5, centre[1]+10, centre[1]+15, centre[1]+20, centre[1]+25]
while (len(vertical) > 0):
    left = int(centre[0])
    right = int(centre[0])
    vartical_point = int(vertical[0])
    value = th1[left][vartical_point]
    while (value == 0 and left!=0):
        left-=1
        value = th1[left][vartical_point]
    left+=1
    value = th1[right][vartical_point]
    while (value == 0 and right!=width):
        right+=1
        value = th1[right][vartical_point]
    right-=1
    points.append([left, vartical_point])
    points.append([right, vartical_point])
    vertical.remove(vartical_point)
    cv2.line(th1, (left, vartical_point), (right, vartical_point), (155, 155, 155), 2)
print(points)
cv2.line(th1, (int(centre[0]), 0), (int(centre[0]), height), (155, 155, 155), 2)
titles = ['Original Image', 'Original Image', 'Global Thresholding (v = 30)']
images = [img, res, th1]

cv2.imwrite('res2.png',th1)

for i in range(3):
    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()

cv2.imwrite('res.png',res)
