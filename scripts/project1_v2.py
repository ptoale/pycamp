"""
Project 1:
During sometime in the given time interval, a signal turns on, but the data is 
very noisy. Write a python script that does the following:

 - For a given proposed trigger time, make two lists of event energies
 - Average the energies before and after the trigger value and compute and 
   report the difference in averages
 - Make a small test data set to confirm that your program does what you intend.

Have each member of your group choose several times for a proposed trigger and 
run their script. Find the trigger value for which the difference between 
averages is largest.

  v2: argparse, data i/o
"""
import sys
import argparse

# Setup the command line argument parser
#  Add one required, positional argument: the name of the file
#  Add two optional arguments: the trigger start and stop,
#    both of which have appropriate default values
parser = argparse.ArgumentParser(description='Project 1 program')
parser.add_argument('datafile', type=str, 
                    help='Name of file containing times and energies')
parser.add_argument('--start', dest='start', type=float, default=-sys.float_info.max,
                    help='Trigger start time [%g]' % -sys.float_info.max)
parser.add_argument('--stop', dest='stop', type=float, default=sys.float_info.max,
                    help='Trigger stop time (must be larger than start time) [%g]' 
                         % sys.float_info.max)
# Parse the command line
#   The three variables are accessed by: args.datafile, args.start, args.stop
args = parser.parse_args()

# Read in the data file.
# The assumption is that there are two columns separated by one or more spaces
event_times = []
event_energies = []
with open(args.datafile) as fp:
    for line in fp:
        t, e = line.split()
        event_times.append(float(t))
        event_energies.append(float(e))

# Make sure that the lists of times and energies are the same length.
# If the assert fails, an AssertionError is raised, terminating execution.
assert len(event_times) == len(event_energies)

# Helper function for doing averages
#  It takes a list of energies and returns the average value, or returns None
#  if the list is empty.
def average(energies):
    if len(energies) > 0:
        sum = 0.0
        for e in energies:
            sum += e
        return sum/len(energies)
    else:
#        print "ERROR! Empty list"
        return None

# Create two empty lists to hold the energies for the two time periods
energies_on  = []
energies_off = []

# Iterate over the lists
for i in range(len(event_times)):
#   The energy will be added to one of the lists based on the time
    if event_times[i] >= args.start and event_times[i] <= args.stop:
        energies_on.append(event_energies[i])
    else:
        energies_off.append(event_energies[i])

# Now take some averages, using our function above
average_all = average(event_energies)
average_on = average(energies_on)
average_off = average(energies_off)

# Print the results
print "Trigger Window = [%g, %g]" % (args.start, args.stop) 
print "  Overall    : %3d measurements with an average energy of %f" % (len(event_energies), average_all)
# Check if there is an average for the on-trigger before printing
if average_on:
    print "  On Trigger : %3d measurements with an average energy of %f" % (len(energies_on), average_on)
# Check if there is an average for the off-trigger before printing
if average_off:
    print "  Off Trigger: %3d measurements with an average energy of %f" % (len(energies_off), average_off)
# Check if there is an average for both before printing the difference
if average_on and average_off:
    print "  On - Off = %f" % (average_on-average_off)
