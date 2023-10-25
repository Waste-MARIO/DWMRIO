# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 11:53:18 2023

@author: loren
"""


import pandas as pd

user = 'CF'
year = 2011
paths = pd.read_excel("Paths.xlsx", index_col=[0]).loc[:,"CF"]

import sys
sys.path.insert(1, paths['MARIO'])

import mario

#%% Parse exiobase IOT ixi of given year
world = mario.parse_exiobase(
    table='IOT',
    unit='Monetary',
    path=paths['IOT folder']+f"\\IOT_{year}_ixi.zip"
    )

#%% aggregating regions
world.get_aggregation_excel(path=paths['Region aggregation'])

#%% aggregating regions                            
world.aggregate(io=paths['Region aggregation'])


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
    path=paths['New sectors'],
    )


#%% adding new empty sectors
world.add_sectors(
    new_sectors=new_sectors,
    regions=world.get_index('Region'),
    io=paths['New sectors'],
    item='Sector',
    )

#Creating MRWIO
#%% creating template for waste sectors
waste_sectors = [
    "Refinery of Nd and Dy from permanent magnet" ,
    "Refinery of Co and Li",
    "Disassembler of permanent magnet",
    "Disassembler of products containing Co and Li",
    "Landifill",
    ]

world.get_add_sectors_excel(
    new_sectors=waste_sectors,
    regions=world.get_index('Region'),
    path=paths['Waste sectors'],
    )

#%% adding new empty sectors
world.add_sectors(
    new_sectors=waste_sectors,
    regions=world.get_index('Region'),
    io=paths['Waste sectors'],
    item='Sector',
    )

#%% creating template for type of waste
type_waste = [
    "End of Life of fabricated metal products (28)",
    "End of Life of machinery and equipment n.e.c. (29)",
    "End of Life of office machinery and computers (30)",
    "End of Life of electrical machinery and apparatus n.e.c. (31)",
    "End of Life of radio, television and communication equipment and apparatus",
    "End of Life of medical, precision and optical instruments, watches and clocks (33)",
    "End of Life of motor and electric vehicles, trailers and semi-trailers (34)",
    "End of Life of wind turbine",
    "End of Life of e-bikes",
    "End of Life of product containing Co",
    "End of Life of lithium-ion batteries",
    "scraps of sector m.28",
    "scraps of sector m.29",
    "scraps of sector m.30",
    "scraps of sector m.31",
    "scraps of sector m.32",
    "scraps of sector m.33",
    "scraps of sector m.34",
    "scraps of wind turbine",
    "scraps of e-bikes",
    "scraps of products containing Co",
    "scraps of lithium-ion batteries",
    "Residue",
]

world.get_add_sectors_excel(
    new_sectors=type_waste,
    regions=world.get_index('Region'),
    path=paths['Type of waste'],
    )

#%% adding new empty sectors
world.add_sectors(
    new_sectors=type_waste,
    regions=world.get_index('Region'),
    io=paths['Type of waste'],
    item='Sector',
    )

#%% export 
world.to_txt(
    path=paths['Database']+"\\DB1",
    #  coefficients = True
    )



