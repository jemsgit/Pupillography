import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('images.png')
b,g,r = cv2.split(img)           # get b,g,r
rgb_img = cv2.merge([r,g,b])     # switch it to rgb

# Denoising
dst = cv2.fastNlMeansDenoisingColored(img,None,10,10,7,21)

#b,g,r = cv2.split(dst)           # get b,g,r
#rgb_dst = cv2.merge([r,g,b])     # switch it to rgb

cv2.imwrite('res.png',dst)
img_black = cv2.imread('res.png',0)

equ = cv2.equalizeHist(img_black)
res = np.hstack((img_black,equ)) #stacking images side-by-side

print(len(res))
print(res[0])

ret,th1 = cv2.threshold(equ,30,255,cv2.THRESH_BINARY)

titles = ['Original Image', 'Original Image', 'Global Thresholding (v = 30)']
images = [img, res, th1]
pixels = []


for i in range(3):
    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()

cv2.imwrite('res.png',res)
