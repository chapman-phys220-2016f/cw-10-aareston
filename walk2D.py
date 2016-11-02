#!/usr/bin/env python3

import numpy as np


"""
Implements an ensemble of random walks and returns the endpoint of each
"""

def walk(points, steps, plot_step):
    """
    Generates random walks for a given number of particles in a given number of steps. The steps are represented 
    """
    xpositions = np.zeros(points)
    ypositions = np.zeros(points)
