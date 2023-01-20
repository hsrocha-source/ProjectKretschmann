import cv2
import numpy as np
from instrumental.drivers.cameras import uc480

# init camera
instruments = uc480.list_instruments()
cam = uc480.UC480_Camera(instruments[0])

# params
cam.start_live_video(framerate = "30Hz")

while cam.is_open:
     
     frame = cam.grab_image(timeout='100s', copy=True, exposure_time='10ms')

     frame1 = frame.astype(np.uint8)

     #now I can apply opencv features

     cv2.imshow('Camera', frame1)
     
     #press q to kill the image
     if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cam.close()
cv2.destroyAllWindows()