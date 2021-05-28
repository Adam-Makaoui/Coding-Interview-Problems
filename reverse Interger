# Given a signed 32-bit integer x, return x with its digits reversed.
# If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned). 
  
    import math
    import sys

    def reverse(x):
        """
        :type x: int
        :rtype: int
        """

        if(x > sys.maxsize or x < -sys.maxsize+1):
            return 0

        neg = False

        s = str(x) # int -> str
        
        # check to see if neg exists
        if s[0] == "-":
            neg = True

        s = s[::-1] # reversed str


        # remove last index
        if neg == True:
            s = s[:-1]

        s = int(s) # str -> int

        print(s)
        return(s)
