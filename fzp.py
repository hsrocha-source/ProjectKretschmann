import numpy as np
from PIL import Image

# Experimental instructions: use a beam shaper to produce a flat radiance + experimental diagram in 2016 paper. 
# field on SLM needs to be FLAT
# all distances are in micrometers

pixel_pitch = 8 # distance between the pixels of the SLM
lambda_ =  0.6328 # distance: wavelength of incident light on the SLM
focal_distance = 900000 # desired focal distance (current: 0.9 m)

def phase_eq(x, y, x0, y0):
    ''' phase equation for a fresnel zone plate
        Input parameters:
            (x0, y0): center of the zone plate coordinates. Type: float
            (x, y): position. Type: float
        Returns:
            interp_phase: interpolated phase of the fresnel zone plate at point x,y. Modulo 2pi.
            mapped from [0, 2] to [0, 255] 
    '''
    phase = -(((x-x0)**2 + (y-y0)**2))/(lambda_*focal_distance) % 2

    interp_phase = np.interp(phase, [0, 2], [0, 255])

    return interp_phase


def generate_phase_array(x0, y0):
    '''
    generates a 1920x1080 array containing 8-bit grayscale pixels corresponding to phase values.
    pixel_pitch will be used to calculate phase for each pixel.
    
    Params: 
        x0, y0: center coordinates of FZP. type: int
        f: desired focal distance
    Returns:
        phase_array: 1920x1080 array containing phase information
    '''
    arr = np.empty((1080, 1920))

    #probably a faster way to implement this
    for height in range(1080):
        for width in range(1920):
            x = pixel_pitch*width
            y = pixel_pitch*height

            pixel_value = phase_eq(x, y, x0, y0)
            arr[height, width] = pixel_value

    return arr

for i in range(1, 2000):
    print(phase_eq(i, i, 512, 512))