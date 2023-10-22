import cv2 as cv
from PIL import Image

video = cv.VideoCapture(0)

WIDTH = 150
# ASCII_CHARS = """&@WM%8D#b$0NqGXOEyVS2xCj}t?lv^i/r7<+!*~";_:,'-.`"""
ASCII_CHARS = """@%#*+=-:. """


def pixels_to_ascii(image):
    pixels = image.getdata()
    characters = "".join(
        [ASCII_CHARS[pixel//(255//len(ASCII_CHARS)+1)] for pixel in pixels])
    return(characters)


def image_to_ascii(image, new_width=WIDTH):
    new_image_data = pixels_to_ascii(image)

    pixel_count = len(new_image_data)
    ascii_image = "\n".join([new_image_data[index:(index+new_width)]
                            for index in range(0, pixel_count, new_width)])

    print(ascii_image)


while True:
    isTrue, frame = video.read()
    frame = cv.flip(frame, 1)
    frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    ratio = frame.shape[0]/frame.shape[1]
    new_height = int(WIDTH * ratio)

    # frame = cv.resize(frame, (WIDTH, new_height), interpolation=cv.INTER_AREA)
    frame = cv.resize(frame, (WIDTH, 100), interpolation=cv.INTER_AREA)
    image_to_ascii(Image.fromarray(frame))

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

video.release()
cv.destroyAllWindows()
