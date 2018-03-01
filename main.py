#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 18:42:57 2018

@author: mateusztybura
"""

from classes.input_data import InputData

def readfile(filepath):
    with open(filepath) as f:
        content = f.readlines()
    return [x.strip() for x in content]

raw_data = readfile('./data/a_example.in')
parsed_data = InputData(raw_data)