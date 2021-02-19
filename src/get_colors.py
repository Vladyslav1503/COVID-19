import cv2
import numpy as np

image = cv2.imread('./images/VerdenPopMindre.png')
population15 = np.array([184, 203, 170])
population15_mask = cv2.inRange(image, population15, population15)
population15_mask_points = cv2.findNonZero(population15_mask).tolist()

