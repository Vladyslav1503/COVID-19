import cv2
import numpy as np


def image_preprocessing(image: str):
    """
    Reducing number of pixels by selecting specific colors on image and returning coordinates of them

    :param image: image of worlds population
    :return: coordinates as key to population in pixels and coordinates for county borders
    """
    img = cv2.imread(image)  # read the image
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # Specifying color mask for populations areas
    population_by_colors = {'1 - 5': (np.array([35, 16, 146]), np.array([94, 100, 208])),
                            '5 - 25': (np.array([80, 28, 0]), np.array([96, 170, 255])),
                            '25 - 250': (np.array([90, 55, 75]), np.array([110, 200, 208])),
                            '250 - 1000': (np.array([100, 70, 110]), np.array([119, 255, 250])),
                            '1000 - 2000': (np.array([115, 5, 0]), np.array([180, 255, 250]))}
    # Finding coordinates
    population_mask_points = {key: cv2.findNonZero(cv2.inRange(hsv, value[0], value[1])) for key, value in
                              population_by_colors.items()}
    # Reversing dict from {'1 - 5': (345, 694)} to {(345, 694): '1 - 5'}
    reverse_population_points = {tuple(*i): key for key, value in population_mask_points.items() for i in value}

    return reverse_population_points, img


def showing(img: np.ndarray, pixel):
    """
    Showing infected pixels on the map by color them in red
    :param img: image read by open-cv2
    :param pixel:infected pixel
    """
    img[pixel[1], pixel[0]] = (0, 0, 255)

    cv2.imshow('title.png', img)
    cv2.waitKey(1)
    # cv2.destroyAllWindows()
