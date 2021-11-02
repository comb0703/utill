# read images with Opencv
import cv2
import sys

img = cv2.imread('cat.bmp') # imread로 영상을 불러온다.

if img is None:
    print('Imager load failed!') # 이미지가 없으면 출력
    sys.exit()

cv2.imwrite('저장할이미지이름.jpg', 이미지 파일)
cv2.namedWindow('image') # OpenCV에서 지원하는 창을 생성하는 명령어
cv2.imshow('image', img) # 첫 번째는 어떤 창에 불러올 것이냐, 두 번째는 어떤 것을 불러올 것이냐
cv2.waitKey()            # 키보드입력을 누를떄까지 보여줌

cv2.destroyAllWindows() # 모든 창을 닫음

#ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

# read images with matplotlib
import matplotlib.image as img 
import matplotlib.pyplot as pp 

fileName = "c:\\sample.png" 
ndarray = img.imread(fileName) 
pp.imshow(ndarray)
pp.show()


#ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

# read images with PIL
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
%matplotlib inline

path = './dog.jpg'

image_pil = Image.open(path)
image = np.array(image_pil)
image.shape

# 이미지 range 확인
np.min(image), np.max(image)

# 이미지 시각화
plt.hist(image.ravel(),256,[0,256])
plt.show()

# 이미지 보기
plt.imshow(image)
plt.show()
