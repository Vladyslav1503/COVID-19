import cv2
import numpy as np


# TODO fix color range '1 - 5' and '1000 - 2000'
def image_preprocessing(image: str):
    """
    Reducing number of pixels by selecting specific colors on image and returning coordinates of them

    :param image: image of worlds population
    :return: coordinates as key to population in pixels and coordinates for county borders
    """
    img = cv2.imread(image)  # read the image
    border_color = cv2.inRange(img, np.array([119, 82, 82]), np.array([183, 203, 170]))  # making mask of borders
    # Specifying color mask for populations areas
    population_by_colors = {'1 - 5': (np.array([183, 203, 170]), np.array([208, 235, 222])),
                            '5 - 25': (np.array([140, 140, 70]), np.array([166, 172, 110])),
                            '25 - 250': (np.array([131, 105, 33]), np.array([154, 157, 75])),
                            '250 - 1000': (np.array([133, 60, 39]), np.array([136, 65, 39])),
                            '1000 - 2000': (np.array([102, 0, 0]), np.array([139, 64, 37]))}
    # Finding coordinates
    population_mask_points = {key: cv2.findNonZero(cv2.inRange(img, value[0], value[1])).tolist() for key, value in
                              population_by_colors.items()}
    # Reversing dict from {'1 - 5': (345, 694)} to {(345, 694): '1 - 5'}
    reverse_population_points = {tuple(*i): key for key, value in population_mask_points.items() for i in value}
    borders = cv2.findNonZero(border_color).tolist()  # Finding coordinates
    preprocessed_borders = tuple(tuple(i[0]) for i in borders)  # make coordinates more readable

    return reverse_population_points, preprocessed_borders, img


def showing(img: np.ndarray, infected: set):
    """
    Showing infected pixels on the map by color them in red
    :param img: image read by open-cv2
    :param infected: set of infected pixels
    """
    for i in infected:
        x, y = i[0], i[1]
        img[y, x] = (0, 0, 255)

    cv2.imshow('title', img)
    cv2.waitKey(1)
