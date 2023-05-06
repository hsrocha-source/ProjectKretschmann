import fzp
from screeninfo import get_monitors

for m in get_monitors():
    print(m)
    
from slmPy import slmpy
import numpy as np
import time
# slmPy requires wxPython
slm = slmpy.SLMdisplay()
resX, resY = slm.getSize()
print(resX)
print(resY)

