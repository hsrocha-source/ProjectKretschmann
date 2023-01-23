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


def generate_phase_array(center_width, center_height):
    '''
    generates a 1920x1080 array containing 8-bit grayscale pixels corresponding to phase values.
    pixel_pitch will be used to calculate phase for each pixel.
    
    Params: 
        center_width, center_height: center coordinates of FZP in pixel space. type: int
    Returns:
        phase_array: 1920x1080 array containing phase information. type: uint8
    '''
    arr = np.empty((1080, 1920))
    x0 = pixel_pitch * center_width
    y0 = pixel_pitch * center_height

    #probably a faster way to implement this
    for height in range(1080):
        for width in range(1920):
            x = pixel_pitch * width
            y = pixel_pitch * height

            pixel_value = round(phase_eq(x, y, x0, y0))
            arr[height, width] = pixel_value

    phase_array = np.uint8(arr)
    return phase_array



# Translating the FZP moves the focal point in the focal plane by the corresponding distance. 

def generate_angled_beam(theta):
    '''
    generates a fresnel zone plate for steering a beam by an angle theta using the SLM. vertical position is centered
    
    params:
        theta: steering angle in degrees. type: float
    returns: 
        phase_array: 1920x1080 array containing phase information. type: uint8
    '''

    theta_rad = theta * 180 / np.pi

    distance = focal_distance * np.tan(theta_rad)
    pixel_shift = distance / pixel_pitch

    phase_array = generate_phase_array(960 + pixel_shift, 540)

    return phase_array

# next up: test angled beam in sw. create sweeping routine. create a CLI for this file


# im = Image.fromarray(arr)
# im.save("test_fresnel.jpg")