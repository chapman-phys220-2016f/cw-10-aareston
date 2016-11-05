#!/usr/bin/env python3

import numpy as np
import matplotlib as mtplt
mtplt.use('Agg')
import matplotlib.pyplot as plt
import shutil as sh

"""
Implements an ensemble of random walks and returns the endpoint of each
"""

def walk(points, steps, plot_step):
    """
    Generates random walks for a given number of particles in a given number of steps. The steps are represented
    """
    xpositions = np.zeros(points)# These 2 lines generate a 2 by points array representing final positions for each point after the random walk
    ypositions = np.zeros(points)
    xymax = 3 * np.sqrt(steps)
    xymin = -xymax
    moves = np.random.random_integers(1, 4, size = points * steps)
    moves.shape = (steps, points)# Reshape random moves matrix so we have $steps rows and $points columns, each row vector is the moves for a single particle in the whole walk

    NORTH = 1
    SOUTH = 2
    EAST = 3
    WEST = 4

    for step in range(steps):
        this_move = moves[step, :]# Selects the row vector which represents one step for each particle in the walk
        ypositions += np.where(this_move == NORTH, 1, 0)
        ypositions -= np.where(this_move == SOUTH, 1, 0)
        xpositions += np.where(this_move == EAST, 1, 0)
        xpositions -= np.where(this_move == WEST, 1, 0)# These four lines update the array of particle positions based on what the current move was for each particle


        if (step + 1) % plot_step == 0:
            plot_title = '%d particles after %d steps' % (points, step + 1)
            file_name = 'tmp_%03d.png' % (step + 1)
            plt.title(plot_title)
            plt.xlim([xymin,xymax])
            plt.ylim([xymin,xymax])
            plt.plot(xpositions, ypositions, 'ko')
            plt.savefig(file_name)
            plt.clf()

def main(points, steps, plot_step):
    import datetime as dt
    time = dt.datetime.now()
    np.random.seed(time.microsecond)
    x = walk(points, steps, plot_step)

if __name__ == "__main__":
    import sys
    args = sys.argv
    points = int(args[1])
    steps = int(args[2])
    plot_step = int(args[3])
    main(points, steps, plot_step)
