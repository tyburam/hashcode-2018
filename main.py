#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 18:42:57 2018

@author: mateusztybura
"""

from classes.simulator import Simulator

sim = Simulator('./data/b_should_be_easy.in', './results/b_should_be_easy.out')
sim.run()