import cloudinary
import cloudinary.uploader
import json
from datetime import datetime
from io import BytesIO
import matplotlib.pyplot as plt
from owslib.wms import WebMapService
from PIL import Image
import numpy

mapWidth = 1800
mapHeight = 800

min_lon = -180
max_lon = 180
min_lat = -90
max_lat = 90

wms = WebMapService('https://gibs.earthdata.nasa.gov/wms/epsg4326/best/wms.cgi?', version='1.1.1')

# Configure request for MODIS_Terra_CorrectedReflectance_TrueColor
img = wms.getmap(layers=['AIRS_L3_Carbon_Monoxide_500hPa_Volume_Mixing_Ratio_Daily_Day'],  # Layers
                 srs='epsg:4326',  # Map projection
                 bbox=(min_lon,min_lat,max_lon,max_lat),  # Bounds
                 size=(mapWidth,mapHeight),  # Image size
                 format='image/png',  # Image format
                 transparent=True,
                 time='2026-09-14')  # Nodata transparency

heatImage = Image.open(BytesIO(img.read()))

def findPixelCoordinates(longitude,latitude):
    latRad = latitude * numpy.pi / 180
    return [((longitude-min_lon)/(max_lon-min_lon)) * mapWidth, ((max_lat-latitude)/(max_lat-min_lat))*mapHeight]

def getPixelColorAtCoordinates(longitude,latitude):
    coordinates = findPixelCoordinates(longitude,latitude)
    return heatImage.getpixel((coordinates[0],coordinates[1]))


# Save output PNG to a file


heatImage.show()

print(getPixelColorAtCoordinates(72.877,19.07))
