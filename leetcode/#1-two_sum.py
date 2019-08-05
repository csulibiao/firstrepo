'''
Given an array of integers, return indices of the two numbers 
such that they add up to a specific target.You may assume that 
each input would have exactly one solution, and you may not use 
the same element twice.
Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''

class solution():
    def twoSum(self, nums, target):
        nums_dict={}
        for i, num in enumerate(nums):
            if target-num not in nums_dict:
                nums_dict[num]=i
                #print(nums_dict, i)
            else:
                return [nums_dict[target-num],i]

A = solution()
print(A.twoSum([2,6,3,7,11,15],18))

##思路：1.暴力解法: 两次嵌套循环枚举，空间复杂度O(1)，时间复杂度O(n²)
##     2. hash表: 利用hash(dict)的快速索引，如果列表当前值与target的差
# 不在hash表(key)中，就添加到hash表，key=当前值，value=位置索引，
# 否则说明target-当前值的结果存在于hash表的key中，从而获得其value，也就是位置索引