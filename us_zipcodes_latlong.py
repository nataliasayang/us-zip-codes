# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 19:11:03 2019

Get latitude and longitude from Census ZIP Code shapefile

@author: Natalia
"""

# Source: https://www.census.gov/cgi-bin/geo/shapefiles/index.php
# INTPTLAT10 = 2010 Census latitude of the internal point
# INTPTLON10 = 2010 Census longitude of the internal point

import geopandas as gpd
import pandas as pd

# Read shapefile

data = gpd.read_file('tl_2018_us_zcta510/tl_2018_us_zcta510.shp')


# type(data)

# data.head()

# data.plot()

# Construct dataframe with zip code, latitude and longitude columns

df = pd.DataFrame(data, columns = ['ZCTA5CE10', 'INTPTLAT10', 'INTPTLON10'])

# df.head()

# type(df)

# Export to CSV

df.to_csv(r'us_zip_codes_latlong_census_2018.csv')