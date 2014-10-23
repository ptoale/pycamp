"""
Project 2.

Choose one of the following easy functions:

    x**4, x**8, x**0.3, x**1.9

and one (or more) of the following hard functions

    x**(3 exp(-x))
    sin(x**3+1/(2-x))
    sin(1/(3-x)**2) for [0,0.5], sin(1/(2+x)**2) for (0.5,1]

Define a python function that takes x as an argument and calculates your function.

We want to find the average value of f over the interval x=[0,1].

Create another function that does the following, for an integer argument n:

 - Creates an array of length n (a parameter we will vary) of random numbers 
   between zero and 1.
 - Averages the value of the function at all of these x values and returns 
   the results.

Have each person in your group choose a value of n. Write a script that repeats 
the calculation for the same value of n, computing the average and standard 
deviation of the result you find. Using the correct answer for the easy problem, 
or higher n values for the harder function, does the standard deviation provide 
a reasonable estimate for the error at a given n?

Now instead of averaging, use the sort() method to sort the random sequence 
first, then compute the average by integrating using the trapezoidal rule with 
the random sequence. Repeat the above tests for the dependence on n.

Try integrating with scipy.integrate.quad( myfunc, 0, 1.0 ). Don't forget to 
import scipy.integrate first.

"""
import math
import random
import scipy.integrate

def easy1(x):
    return math.pow(x, 4)

def avg_easy1(x):
    return x*easy1(x)

def easy2(x):
    return math.pow(x, 8)
    
def avg_easy2(x):
    return x*easy2(x)

def easy3(x):
    return math.pow(x, 0.3)

def avg_easy3(x):
    return x*easy3(x)

def easy4(x):
    return math.pow(x, 1.9)
    
def avg_easy4(x):
    return x*easy4(x)

def hard1(x):
    p = 3.0*math.exp(-x)
    return math.pow(x, p)
    
def avg_hard1(x):
    return x*hard1(x)

def hard2(x):
    a = math.pow(x,3) + 1.0/(2.0-x)
    return math.sin(a)
    
def avg_hard2(x):
    return x*hard2(x)

def hard3(x):
    if x < 0.0 or x > 1.0:
        return float('nan')
    elif x <= 0.5:
        return math.sin(1.0/math.pow(3.0-x, 2.0))
    else:
        return math.sin(1.0/math.pow(2.0+x, 2.0))

def avg_hard3(x):
    return x*hard3(x)

func_names = {'easy1': r'$f(x) = x^4$',
              'easy2': r'$f(x) = x^8$',
              'easy3': r'$f(x) = x^{0.3}$',
              'easy4': r'$f(x) = x^{1.9}$',
              'hard1': r'$f(x) = x^{3 \exp{(-x)}}$',
              'hard2': r'$f(x) = \sin{[x^3 + 1/(2-x)]}$',
              'hard3': r'$f(x) = (\sin[1/(3-x)^2],\ \sin[1/(2+x)^2])$',
              }

def points(n):
    ps = []
    for i in range(n):
        ps.append(random.uniform(0.0, 1.0))
    return ps

def average(func, points):
    sum_y = 0.0
    for p in points:
        y = func(p)
        sum_y += y
    return sum_y/len(points)

def trap(func, points):
    points.sort()
    sum = 0.0
    a = None
    for p in points:
        if not a:
            a = p
            continue
        y_a = func(a)
        y_p = func(p)
        sum += 0.5*(p - a)*(y_a + y_p)
        a = p
    return sum

def calc_stats(func, n_points, n_tries, method):
    sum_a = 0.0
    sum_a2 = 0.0
    for i in range(n_tries):
        ps = points(n_points)
        if method == 1:
            a = average(func, ps)
        elif method == 2:
            a = trap(func, ps)
        sum_a += a
        sum_a2 += a*a
    avg_a = sum_a/n_tries
    avg_a2 = sum_a2/n_tries
    sigma = math.sqrt(avg_a2 - avg_a*avg_a)
        
    return avg_a, sigma

if __name__ == '__main__':
    import argparse
    import numpy as np
    import matplotlib.pyplot as plt

    # Setup the parser
    parser = argparse.ArgumentParser(description='Project 2 program')
    parser.add_argument('--n', type=int, default=100,
                        help='Number of sample points [100]')
    parser.add_argument('--func', choices=['easy1', 'easy2', 'easy3', 'easy4', 'hard1', 'hard2', 'hard3'],
                        default='easy1', help='The function to average')
    parser.add_argument('-p', '--plot', action='store_true', 
                        help='Set this to plot the data')
    # Parse the command line
    args = parser.parse_args()

    # This is how you access a function by its name
    #   args.func is a string containing the name of one of our functions
    #   f will be a callable object (function)
    f = locals()['avg_' + args.func]

    # if one of our functions has an exact solution, put it here
    exact = None
    if args.func == 'easy1':
        exact = 1.0/6.0
    elif args.func == 'easy2':
        exact = 1.0/10.0
    elif args.func == 'easy3':
        exact = 1.0/2.3
    elif args.func == 'easy4':
        exact = 1.0/3.9

    avg0, err0 = scipy.integrate.quad(f, 0.0, 1.0)
    avg1, err1 = calc_stats(f, 100, 100, 1)
    avg2, err2 = calc_stats(f, 100, 100, 2)

    print "Function %s:" % args.func
    if exact:
        print "  Exact Average     = %g" % exact
    print "  Scipy Integration = %g +/- %g" % (avg0, err0)
    print "  Random Trapazoid  = %g +/- %g" % (avg1, err1)
    print "  Random Average    = %g +/- %g" % (avg2, err2)

    if args.plot:
        fp = locals()[args.func]
        xs = np.arange(0, 1, 0.01)
        ys = []
        max = 0
        for x in xs:
            y = fp(x)
            ys.append(y)
            if y > max:
                max = y
        plt.plot(xs, ys, label=func_names[args.func])
        plt.ylim(0.0, 1.1*max)
        plt.plot([0.0, 1.0], [avg0, avg0])
        plt.legend()
        plt.show()