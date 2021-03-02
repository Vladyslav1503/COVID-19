import cv2
import numpy as np

image = cv2.imread('./images/VerdenPopMindre.png')

# TODO Refactor
population15 = np.array([184, 203, 170])
population15_mask = cv2.inRange(image, population15, population15)
population15_mask_points = cv2.findNonZero(population15_mask).tolist()

confines = cv2.inRange(image, np.array([119, 82, 82]), np.array([149, 156, 156]))
