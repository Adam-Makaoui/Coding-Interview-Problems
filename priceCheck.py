import math
import os
import random
import re
import sys

# The 'priceCheck' function below checks if there is a charge error
# by comparing the interconnected products & productPrices arrays
# to the productSold and soldPrice Arrays

#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING_ARRAY products
#  2. FLOAT_ARRAY productPrices
#  3. STRING_ARRAY productSold
#  4. FLOAT_ARRAY soldPrice

def priceCheck(products, productPrices, productSold, soldPrice):
    # Write your code here

    error = 0

    # i = index for sold; loc = index for actual

    for i in range(0, len(productSold)):
        loc = products.index(productSold[i])  # get the index of the productsold item in the products

        if productPrices[loc] != soldPrice[i]:
            error += 1

    return error

