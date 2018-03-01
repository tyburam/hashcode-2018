#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 20:55:54 2018

@author: mateusztybura
"""

def mycmp(a, b):
    if a.base_distance == b.base_distance:
        return 0
    else:
        return 1 if a.base_distance > b.base_distance else -1

class Sorter(object):
        def __init__(self, obj, *args):
            self.obj = obj
            
        def __lt__(self, other):
            return mycmp(self.obj, other.obj) < 0
        
        def __gt__(self, other):
            return mycmp(self.obj, other.obj) > 0
        
        def __eq__(self, other):
            return mycmp(self.obj, other.obj) == 0
        
        def __le__(self, other):
            return mycmp(self.obj, other.obj) <= 0  
        
        def __ge__(self, other):
            return mycmp(self.obj, other.obj) >= 0
        
        def __ne__(self, other):
            return mycmp(self.obj, other.obj) != 0