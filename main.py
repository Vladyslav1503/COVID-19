from src.preprocessing import image_preprocessing
import cv2

IMAGE_SRC = "./src/images/VerdenPopMindre.png"
START_POINT = (530, 150)  # (659, 578)  # (800, 215)

population_points, borders = image_preprocessing(IMAGE_SRC)
img = cv2.imread(IMAGE_SRC)
for i in population_points.keys():
    x, y = i[0], i[1]
    img[y, x] = (0, 0, 255)

cv2.imshow('title',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
