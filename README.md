# storm
In this program, you will solve a problem related to thunderstorms on a radar map. The radars indicate the number of stormy fields in each row and column.
* The storms are rectangular.
* The storms do not touch each other with their corners.
* The storms have a dimension of at least 2 × 2.

The variable domains (storm fields) are 0 or 1.
Declaration of constraints:
for every three fields (lying next to each other, horizontally or vertically) the condition must be satisfied: a+2b+3c != 2
for every 2 x 2 squares the condition must be satisfied: there can be no arrangement [1,0,1,0] or [0,1,0,1] or any triplet of painted fields
the sum of colored fields in rows and columns must equal the numbers given as input.

To run a test: python validator.py --stdio zad5 python storm.py 
