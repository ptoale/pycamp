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
    return x*math.pow(x, 4)

def easy2(x):
    return x*math.pow(x, 8)
    
def easy3(x):
    return x*math.pow(x, 0.3)

def easy4(x):
    return x*math.pow(x, 1.9)
    
def hard1(x):
    p = 3.0*math.exp(-x)
    return x*math.pow(x, p)
    
def hard2(x):
    a = math.pow(x,3) + 1.0/(2.0-x)
    return x*math.sin(a)
    
def hard3(x):
    if x < 0.0 or x > 1.0:
        return float('nan')
    elif x <= 0.5:
        return x*math.sin(1.0/math.pow(3.0-x, 2.0))
    else:
        return x*math.sin(1.0/math.pow(2.0+x, 2.0))

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

def method1(n):

    ae1, se1 = calc_stats(easy1, n, 100, 1)
    ae2, se2 = calc_stats(easy2, n, 100, 1)
    ae3, se3 = calc_stats(easy3, n, 100, 1)
    ae4, se4 = calc_stats(easy4, n, 100, 1)
    ah1, sh1 = calc_stats(hard1, n, 100, 1)
    ah2, sh2 = calc_stats(hard2, n, 100, 1)
    ah3, sh3 = calc_stats(hard3, n, 100, 1)
    
    exact_e1 = 1.0/6.0
    exact_e2 = 1.0/10.0
    exact_e3 = 1.0/2.3
    exact_e4 = 1.0/3.9
    
    diff_e1 = math.fabs(exact_e1 - ae1)/se1
    diff_e2 = math.fabs(exact_e2 - ae2)/se2
    diff_e3 = math.fabs(exact_e3 - ae3)/se3
    diff_e4 = math.fabs(exact_e4 - ae4)/se4
    
    print "Method 1:"
    print "  Easy1 with n=%d: %f +/- %f (exact=%f error=%f)" % (n, ae1, se1, exact_e1, diff_e1)
    print "  Easy2 with n=%d: %f +/- %f (exact=%f error=%f)" % (n, ae2, se2, exact_e2, diff_e2)
    print "  Easy3 with n=%d: %f +/- %f (exact=%f error=%f)" % (n, ae3, se3, exact_e3, diff_e3)
    print "  Easy4 with n=%d: %f +/- %f (exact=%f error=%f)" % (n, ae4, se4, exact_e4, diff_e4)
    print "  Hard1 with n=%d: %f +/- %f" % (n, ah1, sh1)
    print "  Hard2 with n=%d: %f +/- %f" % (n, ah2, sh2)
    print "  Hard3 with n=%d: %f +/- %f" % (n, ah3, sh3)

 
def method2(n):

    ae1, se1 = calc_stats(easy1, n, 100, 2)
    ae2, se2 = calc_stats(easy2, n, 100, 2)
    ae3, se3 = calc_stats(easy3, n, 100, 2)
    ae4, se4 = calc_stats(easy4, n, 100, 2)
    ah1, sh1 = calc_stats(hard1, n, 100, 2)
    ah2, sh2 = calc_stats(hard2, n, 100, 2)
    ah3, sh3 = calc_stats(hard3, n, 100, 2)
    
    exact_e1 = 1.0/6.0
    exact_e2 = 1.0/10.0
    exact_e3 = 1.0/2.3
    exact_e4 = 1.0/3.9
    
    diff_e1 = math.fabs(exact_e1 - ae1)/se1
    diff_e2 = math.fabs(exact_e2 - ae2)/se2
    diff_e3 = math.fabs(exact_e3 - ae3)/se3
    diff_e4 = math.fabs(exact_e4 - ae4)/se4
    
    print "Method 2:"
    print "  Easy1 with n=%d: %f +/- %f (exact=%f error=%f)" % (n, ae1, se1, exact_e1, diff_e1)
    print "  Easy2 with n=%d: %f +/- %f (exact=%f error=%f)" % (n, ae2, se2, exact_e2, diff_e2)
    print "  Easy3 with n=%d: %f +/- %f (exact=%f error=%f)" % (n, ae3, se3, exact_e3, diff_e3)
    print "  Easy4 with n=%d: %f +/- %f (exact=%f error=%f)" % (n, ae4, se4, exact_e4, diff_e4)
    print "  Hard1 with n=%d: %f +/- %f" % (n, ah1, sh1)
    print "  Hard2 with n=%d: %f +/- %f" % (n, ah2, sh2)
    print "  Hard3 with n=%d: %f +/- %f" % (n, ah3, sh3)

def method3():

    e1 = scipy.integrate.quad(easy1, 0.0, 1.0)[0]
    e2 = scipy.integrate.quad(easy2, 0.0, 1.0)[0]
    e3 = scipy.integrate.quad(easy3, 0.0, 1.0)[0]
    e4 = scipy.integrate.quad(easy4, 0.0, 1.0)[0]
    h1 = scipy.integrate.quad(hard1, 0.0, 1.0)[0]
    h2 = scipy.integrate.quad(hard2, 0.0, 1.0)[0]
    h3 = scipy.integrate.quad(hard3, 0.0, 1.0)[0]

    exact_e1 = 1.0/6.0
    exact_e2 = 1.0/10.0
    exact_e3 = 1.0/2.3
    exact_e4 = 1.0/3.9
    
    diff_e1 = math.fabs(exact_e1 - e1)/exact_e1
    diff_e2 = math.fabs(exact_e2 - e2)/exact_e2
    diff_e3 = math.fabs(exact_e3 - e3)/exact_e3
    diff_e4 = math.fabs(exact_e4 - e4)/exact_e4
 
    print "Method 3:"
    print "  Easy1: %f (exact=%f pdiff=%f)" % (e1, exact_e1, diff_e1)
    print "  Easy2: %f (exact=%f pdiff=%f)" % (e2, exact_e2, diff_e2)
    print "  Easy3: %f (exact=%f pdiff=%f)" % (e3, exact_e3, diff_e3)
    print "  Easy4: %f (exact=%f pdiff=%f)" % (e4, exact_e4, diff_e4)
    print "  Hard1: %f" % h1
    print "  Hard2: %f" % h2
    print "  Hard3: %f" % h3

if __name__ == '__main__':

    n = 1000
    method1(n)
    method2(n)
    method3()
