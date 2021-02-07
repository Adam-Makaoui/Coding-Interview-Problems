
# returns a string were each alphabet char is reversed
# do nothing to special characters or numbers
# s = input string
def swap_case(s):
    # temp is the string to return
    temp = ""
    for e in s:
        # if char is lower, turn to upper
        if(e.lower() == e):
            temp += e.upper()
        
        #else (char is upper, turn to lower)
        else:
            temp += e.lower()
    
    return temp

# test via user Input
if __name__ == '__main__':
    s = input("enter a string : ")
    result = swap_case(s)
    print(result)