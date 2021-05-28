  # Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
  # You may assume that each input would have exactly one solution, and you may not use the same element twice.
  # You can return the answer in any order
  
  def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        # my code here
        l = list()

        for i in nums:
            for j in nums:
                if i + j == target:
                    l.append(index(i))
                    l.append(index(j))
                    return l
