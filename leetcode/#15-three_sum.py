'''
Given an array nums of n integers, are there elements a, b, c in nums such 
that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
Note:
The solution set must not contain duplicate triplets.
Example:
Given array nums = [-1, 0, 1, 2, -1, -4],
A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''
class Solution:
    def threeSum(self, nums):
        N = len(nums)
        if N <3:
          return []
        nums.sort()
        res = []
        for i in range(N-2):
          if i > 0 and nums[i]==nums[i-1]:
            continue
          low, high = i+1, N-1
          while low < high:
            sum = nums[i]+nums[low]+nums[high]
            if sum == 0:
              res.append([nums[i],nums[low],nums[high]])
              low += 1
              high -= 1
              while low < high and nums[low] == nums[low - 1]:
                low += 1
              while low < high and nums[high] == nums[high + 1]:
                high -= 1
            elif sum < 0:
              low += 1
            else:
              high -= 1
        return res
              
            

A=Solution()
print(A.threeSum([-1, 0, 1, 2, -1, -4]))