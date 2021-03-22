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

    return reverse_population_points, preprocessed_borders


def spread_infection(pixel: tuple, infected: set, borders: tuple) -> tuple:
    """
    Finding available pixels for infection
    Example
    [18,19][19,19][20,19]
    [18,20][19,20][20,20]
    [18,21][19,20][20,21]
    Where (19,20) is pixel that gives in parameter.
    Function returns another pixels around the main. So function's return will see like this
    ((20, 19), (20, 21), (20, 20), (18, 20), (18, 19)) with following parameters
    spread_infection(tuple(19,20), set{(1, 2), (19, 19)}, tuple((19, 21), (18, 21)))

    :param pixel: coordinates of the pixel
    :param infected: set of already infected pixels
    :param borders: tuple of county borders
    :return: tuple of available for infection pixels
    """
    finding_neighboring_pixel = {1: lambda x: (x[0] - 1, x[1]),
                                 2: lambda x: (x[0] - 1, x[1] - 1),
                                 3: lambda x: (x[0], x[1] - 1),
                                 4: lambda x: (x[0] + 1, x[1] - 1),
                                 5: lambda x: (x[0] + 1, x[1]),
                                 6: lambda x: (x[0] + 1, x[1] + 1),
                                 7: lambda x: (x[0], x[1] + 1),
                                 8: lambda x: (x[0] - 1, x[1] + 1)}
    # set of 8 neighbor pixels
    neighboring_pixels = {finding_neighboring_pixel[i](pixel) for i in finding_neighboring_pixel.keys()}
    # removing pixels that are infected or border
    available_pixels = tuple((neighboring_pixels - set(infected)) - set(borders))

    return available_pixels
