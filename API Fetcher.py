import cloudinary
import cloudinary.uploader
import json
from datetime import datetime
from io import BytesIO
import matplotlib.pyplot as plt
from owslib.wms import WebMapService
from PIL import Image


wms_url = "https://gibs.earthdata.nasa.gov/wms/epsg4326/best/wms.cgi?"
wms = WebMapService(wms_url, version="1.1.1")

target_layer = "TEMPO_L2_Ozone_UV_Aerosol_Index_Granule"
current_date = datetime.now().strftime("%Y-%m-%d")    

raw_img_response = wms.getmap(
    layers=[target_layer],
    srs="epsg:4326",                 
    bbox=(-180, -90, 180, 90),       
    size=(1200, 600),                
    time=current_date,               
    format="image/jpeg"              
)

image_in_memory = Image.open(BytesIO(raw_img_response.read()))

image_in_memory.show()
