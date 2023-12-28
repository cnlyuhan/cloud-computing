import numpy as np
import matplotlib.pyplot as plt
from skimage import data
from skimage import io
from skimage import color
from skimage import filters
from skimage.morphology import square

# 读取图像
image = data.camera()

# 指定滤波窗口的大小
window_size = 5

# 对图像进行标准差滤波
filtered_image = filters.rank.std(image, square(window_size))

# 显示原始图像和滤波后的图像
plt.figure(figsize=(8, 4))
plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(filtered_image, cmap='gray')
plt.title('Standard Deviation Filtered Image')
plt.axis('off')

plt.show()
