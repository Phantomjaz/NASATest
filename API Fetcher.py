from datetime import date, timedelta
from io import BytesIO
import matplotlib.pyplot as plt
from owslib.wms import WebMapService
from PIL import Image
import numpy

mapWidth = 720
mapHeight = 360

min_lon = -180
max_lon = 180
min_lat = -90
max_lat = 90

wms = WebMapService('https://gibs.earthdata.nasa.gov/wms/epsg4326/best/wms.cgi?', version='1.1.1')

# Configure request for MODIS_Terra_CorrectedReflectance_TrueColor
img = wms.getmap(layers=['AIRS_L3_Carbon_Monoxide_500hPa_Volume_Mixing_Ratio_Daily_Day'], # Layers
                 srs='epsg:4326',  # Map projection
                 bbox=(min_lon,min_lat,max_lon,max_lat), # Bounds
                 size=(mapWidth,mapHeight), # Image size
                 format='image/jpeg', # Image format
                 transparent=True,
                 time= date.today() - timedelta(days=7)) # Get data from 7 days before today to get fully processed data

heatImage = Image.open(BytesIO(img.read()))

def findPixelCoordinates(longitude,latitude):
    latRad = latitude * numpy.pi / 180
    return [((longitude-min_lon)/(max_lon-min_lon)) * mapWidth, ((max_lat-latitude)/(max_lat-min_lat))*mapHeight]

def getPixelColorAtCoordinates(longitude,latitude):
    coordinates = findPixelCoordinates(longitude,latitude)
    return heatImage.getpixel((coordinates[0],coordinates[1]))

# Show fetched image
heatImage.show()

print(getPixelColorAtCoordinates(72.877,19.07))
