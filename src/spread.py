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


def have_not_been_infected(not_infected: set, infected: set, borders: tuple, all_pixels) -> tuple:
    """
    Choosing next pixel of neighbor pixels that have not been infected for all time or available pixel
    :param not_infected: all neighbor pixels that have not been infected for all time
    :param infected: set of already infected pixels
    :param borders: tuple of county borders
    :param all_pixels: all pixels from the map
    :return: next randomly chosen pixel
    """
    if not_infected:
        return tuple(not_infected)[int(random() * len(not_infected))]
    available_pixels = tuple(set(all_pixels) - set(infected) - set(borders))
    return available_pixels[int(random() * len(available_pixels))]


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


def choosing_next_infected_pixel(pixel: tuple, infected: set, borders: tuple, airports: tuple,
                                 all_pixels: tuple) -> tuple:
    """
    Finding pixel that will be infected next by checking airports and neighbor pixels.
    If none of them are available chooses random a pixel beside already infected pixel or available pixel
    :param pixel: the infected pixel
    :param infected: set of already infected pixels
    :param borders: tuple of county borders
    :param airports: tuple of all airports
    :param all_pixels: all pixels from the map
    :return: next available pixel
    """
    next_pixel = None
    if not hasattr(choosing_next_infected_pixel, 'not_infected'):
        choosing_next_infected_pixel.not_infected = set()

    if pixel in airports:
        next_pixel = airports[int(random() * len(airports))]
    # Checking if any of neighbor pixels are available for infection
    elif neighbor_pixels := available_neighbor_pixels(pixel=pixel, infected=infected, borders=borders):
        if len(neighbor_pixels) > 1:
            # choosing a random pixel from neighbor pixels
            next_pixel = neighbor_pixels[int(random() * len(neighbor_pixels))]
            rest_of_neighbor_pixels = tuple(set(neighbor_pixels) - set(next_pixel))
            #  adding not infected pixels to set. The set uses if none of neighbor pixels are available
            choosing_next_infected_pixel.not_infected.add(rest_of_neighbor_pixels)
        elif len(neighbor_pixels) == 1:
            next_pixel = neighbor_pixels[0]
    else:
        # choosing next pixel from not infected neighbor pixels for all time and other available pixels
        next_pixel = have_not_been_infected(choosing_next_infected_pixel.not_infected, infected, borders, all_pixels)
        if next_pixel in choosing_next_infected_pixel.not_infected:
            choosing_next_infected_pixel.not_infected.remove(next_pixel)
    return next_pixel


def finding_total_population(coordinates: dict, pixel: tuple) -> int:
    """
    Calculation total population in the pixel in range that the map gives us
    :param coordinates: dict of coordinates as a key and population range as a value
    :param pixel: the pixel's coordinates
    :return: total population in the pixel
    """
    population_range = tuple(map(int, coordinates[pixel].split(' - ')))
    return int(random() * population_range[1] + population_range[0])
