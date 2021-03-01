import cv2
import numpy as np

image = cv2.imread('./images/VerdenPopMindre.png')
population15 = np.array([184, 203, 170])
population15_mask = cv2.inRange(image, population15, population15)
population15_mask_points = cv2.findNonZero(population15_mask).tolist()

# TODO Refactor
confines = cv2.inRange(image, np.array([119, 82, 82]), np.array([149, 156, 156]))
scale_percent = 60  # percent of original size
width = int(confines.shape[1] * scale_percent / 100)
height = int(confines.shape[0] * scale_percent / 100)
dim = (width, height)

# resize image
resized = cv2.resize(confines, dim, interpolation=cv2.INTER_AREA)
img = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)

contours, hierarchy = cv2.findContours(resized, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# create an empty image for contours
img_contours = np.zeros(img.shape)
# draw the contours on the empty image
cv2.drawContours(img_contours, contours, -1, (0, 255, 0), 1)
cv2.imshow('lol', img_contours)

# waits for user to press any key
# (this is necessary to avoid Python kernel form crashing)
cv2.waitKey(0)

# closing all open windows
cv2.destroyAllWindows()
print(*contours)
