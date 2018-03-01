#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 18:55:34 2018

@author: mateusztybura
"""

class Ride:
    def __init__(self, data):
        #ride from [0, 0] to [1, 3], earliest start 2, latest finish 9
        row = data.split(" ")
        self.start = (int(row[0]), int(row[1]))
        self.stop = (int(row[2]), int(row[3]))
        self.earliest_start = int(row[4])
        self.latest_finish = int(row[5])
        self.base_distance = self.start[0] + self.start[1]