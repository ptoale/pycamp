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
  v3: main, plotting
  v4: optimization
"""
import sys
import argparse

def read_data(filename):
    # Read in the data file.
    # The assumption is that there are two columns separated by one or more spaces
    event_times = []
    event_energies = []
    with open(filename) as fp:
        for line in fp:
            t, e = line.split()
            event_times.append(float(t))
            event_energies.append(float(e))
    return event_times, event_energies

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

# Function that plots energies vs time and adds some useful information.
def plot(t_start, t_stop, event_times, event_energies, average_on, average_off):
    import matplotlib.pyplot as plt

    fig = plt.figure()
    fig.suptitle('Project 1')
    ax = fig.add_subplot(111)
    ax.set_xlabel('Time')
    ax.set_ylabel('Energy')
    
    ax.plot(event_times, event_energies)

    t0 = event_times[0]
    tN = event_times[-1]
    if t_start <= t0:
        if t_stop >= tN:
            # Trigger is on to begin with and stays on
            ax.plot([t0, tN], [average_on, average_on], color='green', 
                    label='On=%4.3f' % average_on)
            ax.axvspan(t0, tN, alpha=0.25, color='green')
        else:
            # Trigger is on to begin with and stops at some point
            ax.plot([t0, t_stop], [average_on, average_on], color='green', 
                     label='On=%4.3f' % average_on)
            ax.plot([t_stop, tN], [average_off, average_off], color='red', 
                     label='Off=%4.3f' % average_off)
            ax.axvspan(t0, t_stop, alpha=0.25, color='green')
            ax.axvspan(t_stop, tN, alpha=0.25, color='red')
    else:
        # Trigger is off to begin with
        ax.plot([t0, t_start], [average_off, average_off], color='red', 
                label='Off=%4.3f' % average_off)
        ax.axvspan(t0, t_start, alpha=0.25, color='red')
        if t_stop >= tN:
            # Trigger turns on and stays on
            ax.plot([t_start, tN], [average_on, average_on], color='green', 
                     label='On=%4.3f' % average_on)
            ax.axvspan(t_start, tN, alpha=0.25, color='green')
        else:
            # Trigger turns on and then off
            ax.plot([t_start, t_stop], [average_on, average_on], color='green', 
                    label='On=%4.3f' % average_on)
            ax.plot([t_stop, tN], [average_off, average_off], color='red')
            ax.axvspan(t_start, t_stop, alpha=0.25, color='green')
            ax.axvspan(t_stop, tN, alpha=0.25, color='red')
    
    ax.legend()
    plt.show()

def optimize(size, event_times, event_energies):

    n = len(event_times)
    t_start = event_times[0]
    t_stop = event_times[-1]
    max_on = None
    max_off = None
    max_n = 0
    max_diff = -sys.float_info.max


    for i in range(0,n-1):
        t1 = event_times[i]
        
        for j in range(i+size,n):
            t2 = event_times[j]

            energies_on = event_energies[i:j]
            energies_off = event_energies[0:i] + event_energies[j:n-1]


            # Now take some averages, using our function above
            average_on = average(energies_on)
            average_off = average(energies_off)
            
            if average_on and average_off:
                if average_on-average_off > max_diff:
                    print "NEW MAX = %f [%f:%f]" % (average_on-average_off, t1, t2)
                    max_diff = average_on-average_off
                    max_on = average_on
                    max_off = average_off
                    max_n = len(energies_on)
                    t_start = t1
                    t_stop = t2

            #print i, j, average_on, average_off

    return t_start, t_stop, max_n, max_on, max_off

# This is the main function
def main():

    # Setup the command line argument parser
    #  Add one required, positional argument: the name of the file
    #  Add two optional arguments: the trigger start and stop,
    #    both of which have appropriate default values
    parser = argparse.ArgumentParser(description='Project 1 program')
    parser.add_argument('datafile', type=str, 
                        help='Name of file containing times and energies')
    parser.add_argument('-s', '--size', type=int, default=1,
                        help='Size (in bins) of minimum trigger window')
    parser.add_argument('-p', '--plot', action='store_true', 
                        help='Set this to plot the data')
    # Parse the command line
    #   The three variables are accessed by: args.datafile, args.start, args.stop
    args = parser.parse_args()

    # Read the data
    event_times, event_energies = read_data(args.datafile)

    # Make sure that the lists of times and energies are the same length.
    # If the assert fails, an AssertionError is raised, terminating execution.
    assert len(event_times) == len(event_energies)

    average_all = average(event_energies)
    t_start, t_stop, n_on, average_on, average_off = optimize(args.size, event_times, event_energies)

    # Print the results
    print "Trigger Window = [%g, %g]" % (t_start, t_stop) 
    print "  Overall    : %3d measurements with an average energy of %f" % (len(event_energies), average_all)
    # Check if there is an average for the on-trigger before printing
    if average_on:
        print "  On Trigger : %3d measurements with an average energy of %f" % (n_on, average_on)
    # Check if there is an average for the off-trigger before printing
    if average_off:
        print "  Off Trigger: %3d measurements with an average energy of %f" % (len(event_energies)-n_on, average_off)
    # Check if there is an average for both before printing the difference
    if average_on and average_off:
        print "  On - Off = %f" % (average_on-average_off)

    # Plot the data
    if args.plot:
        plot(t_start, t_stop, event_times, event_energies, average_on, average_off)

# This funny business is what actually calls the main function
if __name__ == '__main__':
    main()
