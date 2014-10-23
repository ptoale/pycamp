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

# For now, we just write out the data here
event_times = [
0.0,
0.25,
0.5,
0.75,
1.0,
1.25,
1.5,
1.75,
2.0,
2.25,
2.5,
2.75,
3.0,
3.25,
3.5,
3.75,
4.0,
4.25,
4.5,
4.75,
5.0,
5.25,
5.5,
5.75,
6.0,
6.25,
6.5,
6.75,
7.0,
7.25,
7.5,
7.75,
8.0,
8.25,
8.5,
8.75,
9.0,
9.25,
9.5,
9.75,
10.0,
10.25,
10.5,
10.75,
11.0,
11.25,
11.5,
11.75,
12.0,
12.25,
12.5,
12.75,
13.0,
13.25,
13.5,
13.75,
14.0,
14.25,
14.5,
14.75,
15.0,
15.25,
15.5,
15.75,
16.0,
16.25,
16.5,
16.75,
17.0,
17.25,
17.5,
17.75,
18.0,
18.25,
18.5,
18.75,
19.0,
19.25,
19.5,
19.75,
20.0,
20.25,
20.5,
20.75,
21.0,
21.25,
21.5,
21.75,
22.0,
22.25,
22.5,
22.75,
23.0,
23.25,
23.5,
23.75,
24.0,
24.25,
24.5,
24.75,
25.0,
25.25,
25.5,
25.75,
26.0,
26.25,
26.5,
26.75,
27.0,
27.25,
27.5,
27.75,
28.0,
28.25,
28.5,
28.75,
29.0,
29.25,
29.5,
29.75,
30.0,
30.25,
30.5,
30.75,
31.0,
31.25,
31.5,
31.75,
32.0,
32.25,
32.5,
32.75,
33.0,
33.25,
33.5,
33.75,
34.0,
34.25,
34.5,
34.75,
35.0,
35.25,
35.5,
35.75,
36.0,
36.25,
36.5,
36.75,
37.0,
37.25,
37.5,
37.75,
38.0,
38.25,
38.5,
38.75,
39.0,
39.25,
39.5,
39.75,
40.0,
40.25,
40.5,
40.75,
41.0,
41.25,
41.5,
41.75,
42.0,
42.25,
42.5,
42.75,
43.0,
43.25,
43.5,
43.75,
44.0,
44.25,
44.5,
44.75,
45.0,
45.25,
45.5,
45.75,
46.0,
46.25,
46.5,
46.75,
47.0,
47.25,
47.5,
47.75,
48.0,
48.25,
48.5,
48.75,
49.0,
49.25,
49.5,
49.75,
]
event_energies = [
-1.11684033322,
-0.262839620261,
-1.69807714422,
-0.424978810991,
-0.715540478299,
-1.35017761341,
1.76874083264,
-0.337162226964,
0.231556191427,
-0.47555094849,
-0.351123763242,
0.0656816367286,
-0.380435638748,
0.944334877863,
-0.612606942545,
0.472269610609,
-0.779491049448,
0.388620569847,
-0.194622721175,
-0.0598233421541,
0.105057073858,
-0.894037355015,
0.67058847019,
-1.18075117668,
0.391959249532,
0.70159096907,
1.12575135085,
-0.911876576618,
0.768528807618,
-1.37964763841,
-0.920487533658,
-0.950599364711,
1.33443685399,
0.916515320412,
0.0425564745525,
-0.297115861445,
0.70689874282,
0.94828469262,
0.0832162010204,
0.72988378361,
-0.00448288443295,
-0.724707875543,
0.0908226663263,
1.31808214711,
-1.21514727492,
-1.28771377612,
-1.15260462572,
-1.77379364657,
-1.93983945748,
1.66376401544,
1.3484810267,
-0.450425321197,
1.32845868246,
-1.00650841713,
1.51955101915,
-0.568907155305,
0.647625169428,
1.02299959499,
0.186238347057,
-0.23963555761,
-1.57546657618,
0.719288735437,
1.23829994768,
1.53301068661,
0.845965811145,
-0.242649007685,
0.370169314312,
1.18843568173,
-0.809416236565,
0.191744911713,
0.130458095343,
0.966945872809,
-2.42801949852,
-0.113531213577,
1.24371528331,
-0.928661428509,
-0.763707960073,
1.03129864439,
0.670437616112,
1.59041558449,
-1.15487269198,
0.748502035821,
1.09248947608,
-1.26174557111,
0.0782464973165,
1.00272429745,
-0.951608308359,
-0.161653261983,
0.330122455782,
0.857030672368,
-0.365055606245,
-1.27683218486,
0.42510239759,
0.0159714473779,
0.894887156346,
-0.127358523192,
-1.55041773641,
-0.584939244746,
0.773528467442,
-0.935258159047,
-1.7990017588,
0.269364142641,
1.90139682044,
0.392716677302,
0.795956774226,
-0.684940187829,
0.197961322276,
-0.696405851778,
-0.130124642131,
1.53744938502,
-0.422632050427,
0.0993889817069,
0.0895601054121,
-1.74996044215,
2.42308213277,
0.158176908496,
-0.601432113807,
-0.197880563687,
1.22164072292,
0.937863995164,
0.23025593336,
-1.03787915302,
2.46831409452,
1.31845466781,
2.06814564971,
0.713780270789,
-1.71497560144,
-0.196135349309,
-0.423046214638,
0.690731712895,
0.783975899034,
0.75825843385,
0.521329432827,
0.979051423251,
0.30863397097,
0.100687177364,
1.51556201374,
-0.964125973557,
0.748471879736,
-1.13636778816,
1.56911156909,
-0.252231314969,
-1.10228180986,
0.155605413871,
1.91227534893,
0.0432788820525,
-0.79729213389,
0.290517949197,
-0.167930712381,
-0.240616829364,
-0.433779815159,
-1.61600837502,
-0.166603071135,
-1.88687813787,
1.90237760214,
0.538192238002,
-0.616880067899,
1.80248269094,
0.624263677406,
-0.184785535665,
-0.922534779224,
0.582929550177,
0.731984582484,
1.32129383702,
-0.151046012372,
-0.477702818328,
-0.308121765417,
0.656215350139,
-0.717016900134,
0.596680498137,
0.261282373787,
0.248757408258,
0.531428674904,
0.320476324386,
-0.885557253933,
0.192431634778,
2.01642034533,
-1.70268054155,
-1.44917834248,
-1.17373362438,
1.87065857484,
-2.76283735221,
-0.738415363869,
0.510024162442,
-1.6382572098,
-0.902119651471,
0.191216683882,
0.0794540468057,
1.01068281976,
-0.618135573954,
1.40981228873,
1.88287077531,
1.1492419002,
-0.966507069623,
0.525596448382,
-0.266583469693,
1.56671140559,
1.38729498138,
-0.566142167457,
-0.619010995531,
]

f = open('data.dat', 'w')

# Iterate over the lists
for i in range(len(event_times)):
#    f.write(str(event_times[i]) + " " + str(event_energies[i]) + "\n")
    f.write("%f %f\n" % (event_times[i], event_energies[i]))

f.close()

