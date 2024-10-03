import openslide
import matplotlib.pyplot as plt
import numpy as np
"""
# load ndpi image
ndpi_image = openslide.OpenSlide('/Users/harrysun/Documents/Wencheng/3c9f3faf341f1787498279daf3e9.ndpi')
# image dimensions
print(ndpi_image.dimensions)
# image level count
print(ndpi_image.level_count)
# plot the images at the lowest resolution
#plt.figure(figsize=(10,10))
print(ndpi_image.level_dimensions[-1])

img = ndpi_image.read_region((0,0), 8, ndpi_image.level_dimensions[-1])
# show the iamge in the terminal and close it later
plt.imshow(img)
plt.show()
"""
# load json file
import json
with open('/Users/harrysun/Downloads/3c9f3faf341f1787498279daf3e9.geojson') as f:
    data = json.load(f)

print(data.keys())

# get the number coordinates of the polygon
print(len(data['features']))

print()