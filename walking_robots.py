#!/bin/python

'''
https://www.hackerrank.com/contests/101hack48/challenges/walking-robots
'''
import sys

def reduce_string(s):
    reduced_string = [[s[0], 1]]
    j = 0
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            reduced_string[j][1] += 1
        else:
            j += 1
            reduced_string.append([s[i], 1])
    return reduced_string
    
def howManyCollisions(s):
    collisions = 0
    reduced_string = reduce_string(s)
    for i in range(1, len(reduced_string)):
        if reduced_string[i-1][0] == 'r' and reduced_string[i][0] == 'l':
            collisions = collisions + reduced_string[i-1][1] + reduced_string[i][1]
            reduced_string[i][0] = 'd'
        elif reduced_string[i-1][0] == 'd' and reduced_string[i][0] == 'l':
            collisions = collisions + reduced_string[i][1]
        elif reduced_string[i-1][0] == 'r' and reduced_string[i][0] == 'd':
            collisions = collisions + reduced_string[i-1][1]
    return collisions
            
       
        
    # Complete this function

q = int(raw_input().strip())
for a0 in xrange(q):
    s = raw_input().strip()
    # Returns the number of times moving robots collide.
    result = howManyCollisions(s)
    print(result)
