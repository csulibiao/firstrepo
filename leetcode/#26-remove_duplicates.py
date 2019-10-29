# Given a sorted array nums, remove the duplicates in-place 
# such that each element appear only once and return the new length.
# input: [1,1,2], return 2, [1,2]

class Solution:
    def removeDuplicates(self, nums):
        i = 1
        for j in range(1,len(nums)):
            if nums[j]!=nums[j-1]:
                nums[i]=nums[j]
                i+=1
        print(nums[:i])
        return i
##前提是排序数组，利用双指针，快指针枚举元素，慢指针记录不重复的元素位置
##当遇到与前一个元素相同的时候，满指针不动，不同时则将当前元素赋值给
##慢指针位，并往后移动一位

sol = Solution()
print(sol.removeDuplicates([1,1,2,3,3,4,5]))