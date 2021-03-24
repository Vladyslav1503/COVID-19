import cv2

from src.modell import coronaSIR
from src.preprocessing import image_preprocessing

IMAGE_SRC = "./src/images/VerdenPopMindre.png"
START_POINT = (800, 200)  # Point where virus take start

# Getting coordinates of population areas and country borders from image
population_points, borders = image_preprocessing(IMAGE_SRC)

# Here is it how will  it looks in the end
img = cv2.imread(IMAGE_SRC)
for i in population_points.keys():
    x, y = i[0], i[1]
    img[y, x] = (0, 0, 255)

cv2.imshow('title', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

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
pixler = [0]
Run = False

while Run:
    for i in pixler:
        pixler[i].spredning
        pixler[i].ny_S
        pixler[i].ny_I
        if pixler[i].infected == pixler[i].pop:
            pixler.pop(i)
    if total_infected == world_poulation:
        Run = False