import cv2
import numpy as np


# TODO comments, fix border coordinates, fix color range
def image_preprocessing(image: str):
    img = cv2.imread(image)
    border_color = cv2.inRange(img, np.array([119, 82, 82]), np.array([183, 203, 170]))
    population_by_colors = {'1 - 5': (np.array([183, 203, 170]), np.array([208, 235, 222])),
                            '5 - 25': (np.array([140, 140, 70]), np.array([166, 172, 110])),
                            '25 - 250': (np.array([131, 105, 33]), np.array([150, 112, 33])),
                            '250 - 1000': (np.array([133, 60, 39]), np.array([136, 65, 39])),
                            '1000 - 2000': (np.array([102, 0, 0]), np.array([139, 64, 37]))}

    population_mask_points = {key: cv2.findNonZero(cv2.inRange(img, value[0], value[1])).tolist() for key, value in
                              population_by_colors.items()}
    reverse_population_points = {tuple(*i): key for key, value in population_mask_points.items() for i in value}
    borders = cv2.findNonZero(border_color).tolist()
    preprocessed_borders = tuple(tuple(i[0]) for i in borders)

    return reverse_population_points, preprocessed_borders
