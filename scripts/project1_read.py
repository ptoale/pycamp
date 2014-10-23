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
"""


f = open('data.dat', 'r')

event_times = []
event_energies = []

for line in f:
    t, e = line.split()
    event_times.append(float(t))
    event_energies.append(float(e))

f.close()

print event_times
print event_energies
