#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 18:42:57 2018

@author: mateusztybura
"""

from classes.simulator import Simulator

sim = Simulator('./data/e_high_bonus.in', './results/e_high_bonus.out')
sim.run()