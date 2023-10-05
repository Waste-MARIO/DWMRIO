# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 11:53:18 2023

@author: loren
"""


import pandas as pd

user = 'LR'
year = 2011
paths = pd.read_excel("Paths.xlsx", index_col=[0]).loc[:,"LR"]

import sys
sys.path.insert(1, paths['MARIO'])

import mario

#%% Parse exiobase IOT ixi of given year
world = mario.parse_exiobase(
    table='IOT',
    unit='Monetary',
    path=paths['IOT folder']+f"\\IOT_{year}_ixi.zip"
    )

#%% creating template for new sectors
new_sectors = [
    "Electric Vehicles",
    "e-bikes",
    "Wind turbine",
    "Permanent Magnet",
    "Cobalt",
    "Lithium",
    "Neodymium",
    "Dysprosium",
    ]

world.get_add_sectors_excel(
    new_sectors=new_sectors,
    regions=world.get_index('Region'),
    path=paths['Add sectors non waste'],
    )

#%% adding new empty sectors
world.add_sectors(
    new_sectors=new_sectors,
    regions=world.get_index('Region'),
    io=paths['Add sectors non waste'],
    item='Sector',
    )

#%% aggregating regions
# world.get_aggregation_excel(...)

#%% export 
world.to_txt(
    path=paths['Database']+"\\DB1",
    # coefficients = True
    )



