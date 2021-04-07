from src.preprocessing import image_preprocessing, showing
from src.spread import choosing_next_infected_pixel, finding_probability_of_infection, finding_total_population

IMAGE_SRC = "./src/images/VerdenPopMindre.png"
START_POINT = (800, 200)  # Point where virus take start
AIRPORTS = ()

# Getting coordinates of population areas and country borders from image
population_points, picture = image_preprocessing(IMAGE_SRC)
infected_pixels = [START_POINT]


def main(point_of_population, airports: tuple, image):
    global infected_pixels

    available_pixels = set(point_of_population.keys())
    while available_pixels:
        next_pixel = choosing_next_infected_pixel(pixel=infected_pixels[-1], airports=airports,
                                                  all_pixels=available_pixels)
        available_pixels.remove(next_pixel)
        population = finding_total_population(coordinates=point_of_population, pixel=infected_pixels[-1])

        # if finding_probability_of_infection(number_of_infected=, total_population=population):
        infected_pixels.append(next_pixel)  # TODO Multiprocessing
        showing(img=image, pixel=infected_pixels[-1])


if __name__ == '__main__':
    main(population_points, AIRPORTS, picture)
