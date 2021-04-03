from math import log10
from random import random

infection_rate = 10


def finding_probability_of_infection(number_of_infected: int, total_population: int) -> True or False:
    """
    Function will return True if random number equals percentage of infected
    it will simulate when someone arrives to another pixel og infect another person

    :param number_of_infected: infected persons in the pixel, min 1
    :param total_population: total population in the pixel
    :return: True or None
    """
    global infection_rate
    assert (total_population >= number_of_infected), "Invalid args input in function {finding_probability_of_infection}"

    limiter = log10(infection_rate) / 20  # range between limiter and -limiter
    range_shift = 100 / infection_rate  # reducing the range of random numbers, will split percentage of infected
    percentage_of_infected = number_of_infected * 100 / total_population
    # random number from (percentage_og_infected / range_shift)
    random_number = random() * 100 + (percentage_of_infected / range_shift)

    return limiter >= percentage_of_infected - random_number >= -limiter


def available_neighbor_pixels(pixel: tuple, infected: set, borders: tuple) -> tuple:
    """
    Finding available neighbor pixels for infection
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


def choosing_next_infected_pixel(pixel: tuple, infected: set, borders: tuple, airports: tuple) -> tuple:
    """
    Finding pixel that will be infected next by checking airports and neighbor pixels.
    If none of them are available chooses random a pixel beside already infected pixel
    :param pixel: the infected pixel
    :param infected: set of already infected pixels
    :param borders: tuple of county borders
    :param airports: tuple of all airports
    :return: next available pixel
    """
    if pixel in airports:
        next_pixel = airports[int(random() * len(airports))]
    # Checking if any of neighbor pixels are available for infection
    elif neighbor_pixels := available_neighbor_pixels(pixel=pixel, infected=infected, borders=borders):
        if len(neighbor_pixels) > 1:
            next_pixel = neighbor_pixels[int(random() * len(neighbor_pixels))]
        elif len(neighbor_pixels) == 1:
            next_pixel = neighbor_pixels[0]
    else:
        pass  # TODO random chose pixels that has not been infected
    return next_pixel


def finding_total_population(coordinates: dict, pixel: tuple) -> int:
    """

    :param coordinates: dict of coordinates as a key and population range as a value
    :param pixel: the pixel's coordinates
    :return: total population in the pixel
    """
    population_range = tuple(map(int, coordinates[pixel].split(' - ')))
    return int(random() * population_range[1] + population_range[0])
