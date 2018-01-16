# coding:utf-8
# findline with color
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
image = mpimg.imread('test.png')
# type判断类型
print('this image is :', type(image), 'with dimensions: ', image.shape)
ysize = image.shape[0]
xsize = image.shape[1]
region_select = np.copy(image)
color_select = np.copy(image)

left_bottom = [0, 462]
right_bottom = [829, 462]
apex = [414.5, 280]
fit_left = np.polyfit((left_bottom[0], apex[0]), (left_bottom[1], apex[1]), 1)
fit_right = np.polyfit((right_bottom[0], apex[0]), (right_bottom[1], apex[1]), 1)
fit_bottom = np.polyfit((left_bottom[0], right_bottom[0]), (left_bottom[1], right_bottom[1]), 1)
xx, yy = np.meshgrid(np.arange(0, xsize), np.arange(0, ysize))
region_thresholds = (yy > (xx * fit_left[0] + fit_left[1])) & \
                    (yy > (xx * fit_right[0] + fit_right[1])) & \
                    (yy < (xx * fit_bottom[0] + fit_bottom[1]))

red_threshold = 0.85
green_threshold = 0.85
blue_threshold = 0.85
rgb_threshold = [red_threshold, green_threshold, blue_threshold]
color_thresholds = (image[:, :, 0] < rgb_threshold[0])\
             | (image[:, :, 1] < rgb_threshold[1]) \
             | (image[:, :, 2] < rgb_threshold[2])

color_select[color_thresholds] = [0, 0, 0, 1]
region_select[~color_thresholds & region_thresholds] = [255, 0, 0, 1]
# plt.imshow(color_select)
plt.imshow(region_select)

plt.show()
plt.show()


