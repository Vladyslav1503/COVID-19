from src.preprocessing import image_preprocessing
from src.spread import choosing_next_infected_pixel, finding_probability_of_infection, finding_total_population

IMAGE_SRC = "./src/images/VerdenPopMindre.png"
START_POINT = (800, 200)  # Point where virus take start
AIRPORTS = ()

# Getting coordinates of population areas and country borders from image
population_points, borders = image_preprocessing(IMAGE_SRC)
infected_pixels = [START_POINT]


def main(point_of_population, county_borders: tuple, airports: tuple):
    global infected_pixels

    while set(infected_pixels) != set(population_points.keys()):
        next_pixel = choosing_next_infected_pixel(pixel=infected_pixels[-1], infected=set(infected_pixels),
                                                  borders=county_borders, airports=airports)
        population = finding_total_population(coordinates=point_of_population, pixel=infected_pixels[-1])
        # TODO run the model
        if finding_probability_of_infection(number_of_infected=1, total_population=population):
            infected_pixels.append(next_pixel)  # TODO Multiprocessing


if __name__ == '__main__':
    main(population_points, borders, AIRPORTS)
################
#  Here is all things we need to do
#
#  1. Spreading function f(x) = x**2; Function will take number of infected as x and return value in range(0, 1.0).
#     It is probability for next pixel will be infected. Where 0 is 0% and 1 is 100%.
#     Beta will change by population number in the pixel.
#
#  2. Function, that will take coordinate to check 8 neighboring pixels and return which pixel will be infected.
#     Function includes country borders check, already infected pixels and airports.
#     If it is several pixels that can be infected will we use random numbers.
#
#  3. All infected pixels will be added to a list and colored in red.
#
#  4. Multiprocessing
# pixler = [0]
# Run = False
#
# while Run:
#     for i in pixler:
#         pixler[i].spredning
#         pixler[i].ny_S
#         pixler[i].ny_I
#         if pixler[i].infected == pixler[i].pop:
#             pixler.pop(i)
#     if total_infected == world_poulation:
#         Run = False
