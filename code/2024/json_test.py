import json

with open(file="./sample_files/OpenStreetMap_example.geojson") as f:
    d = json.load(f)

#print(d)
print(d["features"][0])

import geopandas as gpd
import pandas as pd




