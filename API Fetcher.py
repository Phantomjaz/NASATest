import cloudinary
import cloudinary.uploader
import json
from datetime import datetime
from io import BytesIO
import matplotlib.pyplot as plt
from owslib.wms import WebMapService
from PIL import Image


wms = WebMapService('https://gibs.earthdata.nasa.gov/wms/epsg4326/best/wms.cgi?', version='1.1.1')

# Configure request for MODIS_Terra_CorrectedReflectance_TrueColor
img = wms.getmap(layers=['AIRS_L3_Carbon_Dioxide_AIRS_AMSU_Monthly'],  # Layers
                 srs='epsg:4326',  # Map projection
                 bbox=(-180,-90,180,90),  # Bounds
                 size=(2000, 2000),  # Image size
                 format='image/jpeg',  # Image format
                 transparent=True)  # Nodata transparency

# Save output PNG to a file
image_in_memory = Image.open(BytesIO(img.read()))

image_in_memory.show()
