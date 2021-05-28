# Given an integer x, return true if x is palindrome integer.

# An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.
    
    def isPalindrome(x):
        """
        :type x: int
        :rtype: bool
        """
        strX = str(x)
        revX = ""
        
        for i in range(1, len(strX) + 1):
            revX += strX[-i]
        return strX == revX
