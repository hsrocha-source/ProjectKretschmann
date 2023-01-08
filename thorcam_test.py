#Modelo da câmera: DCU224M-GL. Incompativel com a biblioteca base da thorcam

import clr
import os

bin_path = r'DCx_Camera_SDK\Develop\DotNet'
driver_path = r'DCx_Camera_Drivers\64'

os.environ['PATH'] += os.pathsep + bin_path + os.pathsep + driver_path
clr.AddReference(os.path.join(bin_path, 'uc480DotNet.dll'))
from uc480 import Camera, Defines

# get list of all possible status, comment out as needed
# print(dir(Defines.Status))

# create camera
cam = Camera()
# print all camera methods
# print(dir(cam))

# init first camera
status = cam.Init(0)
if status != Defines.Status.SUCCESS:
    ValueError(f'Got error code {status}')

# Set display mode to bitmap (DiB)
cam.Display.Mode.Set(Defines.DisplayMode.DiB)

# Set color mode to 8-bit RGB
cam.PixelFormat.Set(Defines.ColorMode.RGBA8Packed)

# Set trigger mode to software (single image acquisition)
cam.Trigger.Set(Defines.TriggerMode.Software)

# Allocate image memory
mem_id = cam.Memory.Allocate(True)

# Obtain image information
w, h, pixel_depth, pitch = cam.Memory.Inquire(mem_id)
# Acquire image
cam.Acquisition.Freeze(Defines.DeviceParameter.Wait)
# Copy image from memory
buffer = cam.Memory.CopyToArray(mem_id)

# Close camera
cam.Exit()