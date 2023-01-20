# Modelo da câmera: DCU224M-GL. Incompativel com a biblioteca base da thorcam, usar a lib instrumental.
# Eventually play with more camera settings: https://instrumental-lib.readthedocs.io/en/stable/uc480-cameras.html
from PIL import Image
import numpy as np
from instrumental import list_instruments
from instrumental.drivers.cameras.uc480 import UC480_Camera
paramsets = list_instruments()
print(paramsets)

cam = UC480_Camera()
cam.set_auto_exposure(enable=True)

image_count = 90
n = 0
while n < image_count:
    cam.start_capture()
    arr = cam.get_captured_image()
    im = Image.fromarray(arr)
    im.save("imagens/im{}.jpg".format(n))
    n+=1