import numpy as np
from scipy.signal import convolve2d
from scipy import misc

def imfilter(image, kernel):
    # 如果输入图像是彩色图像，将其转换为灰度图像
    if len(image.shape) == 3:
        image = np.dot(image[...,:3], [0.299, 0.587, 0.114])

    # 对图像进行滤波
    filtered_image = convolve2d(image, kernel, mode='same', boundary='symm')

    return filtered_image

# 读取图像
image = misc.ascent()

# 定义一个平滑滤波器
kernel_smooth = np.ones((3, 3)) / 9.0

# 定义一个锐化滤波器
kernel_sharpen = np.array([[0, -1, 0],
                           [-1, 5, -1],
                           [0, -1, 0]])

# 对图像分别使用平滑滤波器和锐化滤波器进行滤波
filtered_image_smooth = imfilter(image, kernel_smooth)
filtered_image_sharpen = imfilter(image, kernel_sharpen)

# 显示原始图像和滤波后的图像
import matplotlib.pyplot as plt
plt.figure(figsize=(12, 6))

plt.subplot(1, 3, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(filtered_image_smooth, cmap='gray')
plt.title('Smoothed Image')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(filtered_image_sharpen, cmap='gray')
plt.title('Sharpened Image')
plt.axis('off')

plt.show()
