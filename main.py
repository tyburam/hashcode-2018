#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 18:42:57 2018

@author: mateusztybura
"""

from classes.simulator import Simulator

sim = Simulator('./data/a_example.in', './results/a_example.out')
sim.run()