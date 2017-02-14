from PIL import Image, ImageFilter
import numpy as np
jpgfile = Image.open("images/1.jpg")
pixels = np.asarray(jpgfile)