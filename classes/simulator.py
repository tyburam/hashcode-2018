#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 19:33:26 2018

@author: mateusztybura
"""

from .input_data import InputData
from .sorter import Sorter

class Simulator:
    def __init__(self, input_path, output_path):
        self.output = output_path
        self.data = InputData(self.readfile(input_path))
        self.current_step = 0
        self.car_rides = [[] for _ in range(self.data.vehicles)]
        self.car_pos = [[0,0] for _ in range(self.data.vehicles)]
        self.car_in_start = [False for _ in range(self.data.vehicles)]
        self.best_rides = [[] for _ in range(self.data.vehicles)]
        self.current_ride = 0
        self.rides_done = 0
    
    def readfile(self, filepath):
        with open(filepath) as f:
            content = f.readlines()
            return [x.strip() for x in content]
        
    def step(self):
        for i in range(self.data.vehicles):
            print('Vehicle: ', str(i))
            if len(self.car_rides[i]) == 0:
                available_ride = self.current_ride
                self.current_ride += 1
                if available_ride >= self.data.rides_count:
                    continue
                self.car_rides[i].append(available_ride)
            if len(self.car_rides[i]) > 0:
                ride_index = self.car_rides[i][0]
                start_point = self.data.rides[ride_index].start
                stop_point = self.data.rides[ride_index].stop
                
                print(' Ride index: ', str(ride_index), '\n')
                
                if not self.car_in_start[i]:
                    if (self.car_pos[i][0] == start_point[0]) and \
                        (self.car_pos[i][1] == start_point[1]):
                            self.car_in_start[i] = True
                    else:
                        if self.car_pos[i][0] != start_point[0]:
                            if self.car_pos[i][0] > start_point[0]:
                                self.car_pos[i][0] -= 1
                            else:
                                self.car_pos[i][0] += 1
                        elif self.car_pos[i][1] != start_point[1]:
                            if self.car_pos[i][1] > start_point[1]:
                                self.car_pos[i][1] -= 1
                            else:
                                self.car_pos[i][1] += 1
                                
                if (self.current_step >= self.data.rides[ride_index].earliest_start) \
                and self.car_in_start[i]:
                    if self.car_pos[i][0] != stop_point[0]:
                        if self.car_pos[i][0] > stop_point[0]:
                            self.car_pos[i][0] -= 1
                        else:
                            self.car_pos[i][0] += 1
                    elif self.car_pos[i][1] != stop_point[1]:
                        if self.car_pos[i][1] > stop_point[1]:
                            self.car_pos[i][1] -= 1
                        else:
                            self.car_pos[i][1] += 1
                    
                    if (self.car_pos[i][0] == stop_point[0]) and \
                        (self.car_pos[i][1] == stop_point[1]):
                            best_index = self.data.rides[ride_index].index
                            self.best_rides[i].append(best_index)
                            self.car_rides[i].clear()
                            self.rides_done += 1
                            self.car_in_start[i] = False
                            print('Ride done\n')
        self.current_step += 1
    
    def run(self):
        self.data.rides.sort(key = Sorter)
        while self.rides_done < self.data.rides_count:
            if self.current_ride > self.data.rides_count:
                break
            self.step()
        self.save()
            
    def save(self):
        with open(self.output, 'w') as f:
            index = 0
            for rides in self.best_rides:
                f.write(str(len(rides)) + " " + " ".join([str(x) for x in rides]))
                if index < len(self.best_rides) - 1:
                    f.write("\n")
                index += 1
        
        