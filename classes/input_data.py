#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 18:49:23 2018

@author: mateusztybura
"""

from .ride import Ride

class InputData:
    #3 rows, 4 columns, 2 vehicles, 3 rides, 2 bonus and 10 steps
    def __init__(self, data, index=0):
        first_row_data = data[0].split(' ')
        self.rows = int(first_row_data[0])
        self.columns = int(first_row_data[1])
        self.vehicles = int(first_row_data[2])
        self.rides_count = int(first_row_data[3])
        self.bonus = int(first_row_data[4])
        self.steps = int(first_row_data[5])
        self.rides = [];
        
        del data[0]
        index = 0
        for row in data:
            self.rides.append(Ride(row, index))
            index += 1
    