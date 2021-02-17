import math
import numpy as np
import pygame
import cv2

x = 1
y = 1
All_infected = True

while x < 1000:
    image = cv2.imread("./src/images/VerdenPopMindre.png")
    p = image[x, y]
    white = np.array([255, 255, 255])
    comparioson_white = p == white
    if not comparioson_white.all():
        print(p)
    x += 1
    y += 1
