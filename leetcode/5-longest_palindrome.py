"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
"""
"""
class Solution():
    def __init__(self):
        self.longestsize=0
        self.longeststart=0

    def longestPalindrome(self, s):
        for index, value in enumerate(s):
            self.findoddpalind(s, index)
            self.findevenpalind(s, index)
        return s[self.longeststart:self.longeststart+self.longestsize+1]


    def findoddpalind(self,s,index):
        start=index
        end=index
        while start >= 1 and end < len(s)-1 and s[start - 1] == s[end + 1]:
            start -= 1
            end += 1
        if end - start > self.longestsize:
            self.longestsize = end - start
            self.longeststart = start

    def findevenpalind(self,s,index):
        start = index
        end = min(index+1, len(s)-1)
        while start >= 1 and end < len(s)-1 and s[start-1] == s[end + 1] and s[start] == s[end]:
            start -= 1
            end += 1
        if end - start > self.longestsize and s[start]==s[end]:
            self.longestsize = end - start
            self.longeststart = start
"""

class Solution1():
    def longestPalindrome(self,s):
        palindrome = '' ##初始化字符串来存储回文

        for i in range(len(s)):
            len1 = len(self.getlongestpld(s,i,i))

            if len1 > len(palindrome):
                palindrome = self.getlongestpld(s,i,i)
            ##如果找到更长的回文，则更新
            len2 = len(self.getlongestpld(s,i,i+1))

            if len2 > len(palindrome):
                palindrome = self.getlongestpld(s,i,i+1)

        return palindrome

    def getlongestpld(self,s,l,r):
        ## 获取最长回文
        while l>=0 and r<len(s) and s[l]==s[r]:
            l-=1
            r+=1
        return s[l+1:r]
        ## 注意边界值，因为l,r 本身已经—1或+1了


#sol = Solution1()
#print(sol.longestPalindrome('eabcddcbaf'))



# Note that Manacher's algorithm provides a O(n) time solution. 
class Solution2(object):
    def longestPalindrome(self, s): 
        """ :type s: str :rtype: str """ 
        longest = "" 
        # create list of 2n-1 possible centres, each letter and between each pair 
        # even indices represent letters, odd represent between letters 
        # # start with middle index that potentially creates longest paliindrome 
        centres = [len(s) - 1] 
        for diff in range(1, len(s)):
             # build list of indices from long to short 
             centres.append(centres[0] + diff) 
             centres.append(centres[0] - diff) 

        for centre in centres: 

            if (min(centre + 1, 2 * len(s) - 1 - centre) <= len(longest)):
                break # return if cannot make a longer palindrome 
            if centre % 2 == 0: 
                left, right = (centre // 2) - 1, (centre // 2) + 1 
            else: 
                left, right = centre // 2, (centre // 2) + 1 
            while left >= 0 and right < len(s) and s[left] == s[right]: 
                left -= 1 
                right += 1 
                 # left and right are now beyond the ends of the substring 
            if right - left - 1 > len(longest): 
                longest = s[left + 1:right] 
        
        return longest

sol2 = Solution2()
print(sol2.longestPalindrome('eabcddcbaf'))
