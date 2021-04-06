from src.preprocessing import image_preprocessing, showing
from src.spread import choosing_next_infected_pixel, finding_probability_of_infection, finding_total_population

IMAGE_SRC = "./src/images/VerdenPopMindre.png"
START_POINT = (800, 200)  # Point where virus take start
AIRPORTS = ()

# Getting coordinates of population areas and country borders from image
population_points, borders, picture = image_preprocessing(IMAGE_SRC)
infected_pixels = [START_POINT]


def main(point_of_population, county_borders: tuple, airports: tuple, image):
    global infected_pixels
    t = set()
    while set(infected_pixels) != set(population_points.keys()):  #
        next_pixel = choosing_next_infected_pixel(pixel=infected_pixels[-1], infected=set(infected_pixels),
                                                  borders=county_borders, airports=airports,
                                                  all_pixels=tuple(point_of_population.keys()),
                                                  population_points=point_of_population)
        population = finding_total_population(coordinates=point_of_population, pixel=infected_pixels[-1])

        # TODO Run model
        # if finding_probability_of_infection(number_of_infected=1, total_population=population):
        infected_pixels.append(next_pixel)  # TODO Multiprocessing

        showing(img=image, infected=set(infected_pixels))
    print('Max', max(t))
    print('Min', min(t))
    print('lol', sum(t) / len(t))


if __name__ == '__main__':
    main(population_points, borders, AIRPORTS, picture)

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
