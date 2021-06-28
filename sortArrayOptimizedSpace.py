# Removes duplicates in an array in O(1) space complexity

def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    # will tell us where to be in the array/list
    pos = 0

    # indexing using manual icrementation of pos
    for _ in range(pos, len(nums)):

        # check if array's value at index is a duplicated in the array
        if nums.count(nums[pos]) >= 2:

            # remove function at the current index (a duplicate), remove reorders arrays size and positioning
            nums.remove(nums[pos])

        # if we dont encounter a duplicate, increment index to check the next number
        else:
            pos += 1


# driver code
arr = [1, 2 ,2 ,3 ,3 ,3 ,2, 2, 5]
removeDuplicates(arr)
print(arr)
