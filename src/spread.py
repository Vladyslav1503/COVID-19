from math import log10
from random import random, choice

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


def spread_to_neighboring(pixel, keys):
    finding_neighboring_pixel = {1: lambda x: (x[0] - 1, x[1]),
                                 2: lambda x: (x[0] - 1, x[1] - 1),
                                 3: lambda x: (x[0], x[1] - 1),
                                 4: lambda x: (x[0] + 1, x[1] - 1),
                                 5: lambda x: (x[0] + 1, x[1]),
                                 6: lambda x: (x[0] + 1, x[1] + 1),
                                 7: lambda x: (x[0], x[1] + 1),
                                 8: lambda x: (x[0] - 1, x[1] + 1)}

    neighboring_pixels = [finding_neighboring_pixel[i](pixel) for i in range(1, 9) if
                          finding_neighboring_pixel[i](pixel) in keys]
    return choice(neighboring_pixels) if neighboring_pixels else False


def choosing_next_infected_pixel(pixel: tuple, airports: tuple, all_pixels):
    """
    Finding pixel that will be infected next by checking airports and neighbor pixels.
    If none of them are available chooses random a pixel beside already infected pixel or available pixel
    :param pixel: the infected pixel
    :param airports: tuple of all airports
    :param all_pixels: all pixels from the map
    :return: next available pixel
    """
    if pixel in airports:
        return choice(airports)

    elif neighbor_pixels := spread_to_neighboring(pixel, all_pixels):
        return neighbor_pixels
    return choice(tuple(all_pixels))


def finding_total_population(coordinates: dict, pixel: tuple) -> int:
    """
    Calculation total population in the pixel in range that the map gives us
    :param coordinates: dict of coordinates as a key and population range as a value
    :param pixel: the pixel's coordinates
    :return: total population in the pixel
    """
    start, end = tuple(map(int, coordinates[pixel].split(' - ')))
    return int(random() * end + start)
