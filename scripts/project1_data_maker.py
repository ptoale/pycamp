"""
Make some data for Project 1.

"""
import argparse
import random

# Set some defaults
DEFAULT_N_DATA = 100
DEFAULT_FIRST_TIME = 0.0
DEFAULT_TIME_STEP = 0.25
DEFAULT_TRIGGER_START = DEFAULT_FIRST_TIME + 0.1*DEFAULT_N_DATA*DEFAULT_TIME_STEP
DEFAULT_TRIGGER_STOP = DEFAULT_FIRST_TIME + 0.9*DEFAULT_N_DATA*DEFAULT_TIME_STEP
DEFAULT_OFF_MEAN = 10.0
DEFAULT_ON_MEAN = 20.0
DEFAULT_SIGMA = 5.0

# Setup the command line argument parser
parser = argparse.ArgumentParser(description='Project 1 data maker')
parser.add_argument('datafile', type=str, 
                    help='Name of file to write times and energies to')
parser.add_argument('--n', type=int, default=DEFAULT_N_DATA,
                    help='The number of data points to generate [%d]' % DEFAULT_N_DATA)
parser.add_argument('--first_time', type=float, default=DEFAULT_FIRST_TIME,
                    help='The earliest time to generate data for [%4.2f]' % DEFAULT_FIRST_TIME)
parser.add_argument('--time_step', type=float, default=DEFAULT_TIME_STEP,
                    help='The size of the time step [%4.2f]' % DEFAULT_TIME_STEP)
parser.add_argument('--start', type=float, default=DEFAULT_TRIGGER_START,
                    help='Trigger start time [%4.2f]' % DEFAULT_TRIGGER_START)
parser.add_argument('--stop', type=float, default=DEFAULT_TRIGGER_STOP,
                    help='Trigger stop time (must be larger than start time) [%4.2f]' % DEFAULT_TRIGGER_STOP)
parser.add_argument('--off_mean', type=float, default=DEFAULT_OFF_MEAN,
                    help='Mean off-trigger energy [%4.2f]' % DEFAULT_OFF_MEAN)
parser.add_argument('--on_mean', type=float, default=DEFAULT_ON_MEAN,
                    help='Mean on-trigger energy [%4.2f]' % DEFAULT_ON_MEAN)
parser.add_argument('--sigma', type=float, default=DEFAULT_SIGMA,
                    help='Energy spread [%4.2f]' % DEFAULT_SIGMA)
# Parse the command line
args = parser.parse_args()

# Make sure trigger stop comes after trigger start
assert args.stop > args.start

# Open the file for writing
with open(args.datafile, 'w') as fp:

    # Make data
    for i in range(args.n):
        # Calculate the next time
        t = args.first_time + i*args.time_step

        # Determine if we are on or off trigger and pull from a gaussian rng
        if t >= args.start and t <= args.stop:
            e = random.gauss(args.on_mean, args.sigma)
        else:
            e = random.gauss(args.off_mean, args.sigma)

        # Make sure energies are positive
        if e < 0.0:
            e = 0.0
    
        fp.write('%4.3f %f\n' % (t, e))
    
