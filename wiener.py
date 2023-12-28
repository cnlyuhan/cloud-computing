import numpy as np
import matplotlib.pyplot as plt
from skimage import data
from skimage import io
from skimage import color
from skimage import restoration

# 读取图像
image = data.camera()

# 将图像转换为浮点数类型
image_float = image.astype(float)

# 指定局部窗口大小
window_size = (5, 5)

# 对图像进行维纳滤波
filtered_image = restoration.wiener(image_float, window_size)

# 显示原始图像和滤波后的图像
plt.figure(figsize=(8, 4))
plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(filtered_image, cmap='gray')
plt.title('Wiener Filtered Image')
plt.axis('off')

plt.show()
