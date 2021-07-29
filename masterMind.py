#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'evaluateGuess' function below.
#
# The function is expected to return an INTEGER_ARRAY, where:
#  - the first  value is the number of red   pegs
#  - the second value is the number of white pegs
# The function accepts following parameters:
#  1. STRING_ARRAY solution
#  2. STRING_ARRAY guess
#

def evaluateGuess(solution, guess):
    # solution = ['purple', 'purple', 'green', 'yellow']
    # guess =    [ black     black black   purple ]
    red = 0
    white = 0
    #visited = []
    guessSet = set(guess)
    # Write your code here
    
    # counting reds
    for i in range(0, len(guess)):
        if guess[i] == solution[i]:
            red += 1
    
    res = 0
    # counting whites
    for i in guessSet:
        #if guess not in visited:
        res += min( guess.count(i), solution.count(i) )
            #visited.append(guess)
    
    white = res - red
    
    return [red, white] # 1st index is red, 2nd is white

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    solution_count = int(input().strip())

    solution = []

    for _ in range(solution_count):
        solution_item = input()
        solution.append(solution_item)

    guess_count = int(input().strip())

    guess = []

    for _ in range(guess_count):
        guess_item = input()
        guess.append(guess_item)

    result = evaluateGuess(solution, guess)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
