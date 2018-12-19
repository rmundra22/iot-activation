########################################################################################################################
#                                                                                                                      #
# MIT License                                                                                                          #
#                                                                                                                      #
# Copyright (c) 2018 Telefonica R&D                                                                                    #
#                                                                                                                      #
# Permission is hereby granted, free of charge, to any person obtaining a copy  of this software and associated        #
# documentation files (the "Software"), to deal in the Software without restriction, including without limitation the  #
# rights in the Software without restriction, including without limitation the rights o use, copy, modify, merge,      #
# publish,  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and      #
# to permit persons to whom the Software is furnished to do so, subject to the following conditions:                   #
#                                                                                                                      #
########################################################################################################################
from __future__ import print_function
import yaml

class RGB:
    def __init__(self):
        self.R = 0
        self.G = 0
        self.B = 0

# Class Display
class Display:
    def __init__(self):
        self.val = ""
        self.R = 0
        self.G = 0
        self.B = 0

# RGB Colours
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
red = (255, 0, 0)
yellow = (255, 255, 0)


def read_config (file):
    with open(file, 'r') as f:
        config = yaml.load(f)
    f.close()
    return config

