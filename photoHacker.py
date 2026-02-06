# # Creating the Night Vison Filter Image

# import numpy as np
# import matplotlib.pyplot as plt


# color_img = np.random.randint(0,256,(10,10,3))

# # creatig the nigth vision effect by killing   the blue and res

# nightvision = color_img.copy()
# # killing red color
# nightvision[: ,: ,0] = 0
# # killing blue color
# nightvision[:, :,2] = 0
# # Increasing Green 
# nightvision[:, :,1] *=2

# # also adding Cap of 255 if the value is greater then 255
# nightvision[nightvision>255] = 255 


# plt.subplot(1, 2, 1)
# plt.title("Original")
# plt.imshow(color_img)

# plt.subplot(1, 2, 2)
# plt.title("Night Vidion")
# plt.imshow(nightvision)

# plt.show()

# Mini-Project Part 2: The "Noir" (Black & White) Challenge


import numpy as np
import matplotlib.pyplot as plt

color_image = np.random.randint(0,256,(10,10,3))


# Turn your random color image into Grayscale.

grey_scale = color_image.copy()

red = grey_scale[:,:,0]
blue = grey_scale[:,:,1]
green  = grey_scale[:,:,2]


# add astype to avoide decimal
average = ((red+blue+green)/3).astype(int)


grey_scale[:,:,0] = average
grey_scale[:,:,1] = average
grey_scale[:,:,2]  = average


plt.subplot(1,2,1)
plt.title("Color Image")
plt.imshow(color_image)

plt.subplot(1,2,2)
plt.title("Noir Image")
plt.imshow(grey_scale)


plt.show()
