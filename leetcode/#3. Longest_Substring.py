"""
Given a string, find the length of the longest substring without repeating characters.
Example 1:
Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:
Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:
Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

class Solution():
    def lengthOfLongestSubstring(self, s):
        substr=''
        tmp=[]
        for index, char in enumerate(s):
            if char not in substr:
                substr+=char
            else:
                substr=substr[substr.index(char)+1:]
                substr+=char
            tmp.append(substr)
        print(tmp,substr)
        return len(max(tmp,key=len))





class Solution2():
    def lengthOfLongestSubstring(self, s):
        last_seen = {}
        start = longest = 0

        for index, char in enumerate(s):
            if char in last_seen and last_seen[char] >= start:
                start = last_seen[char] + 1
            else:
                longest = max(longest, index-start+1)
            last_seen[char] = index
        return longest



sol=Solution2()
print(sol.lengthOfLongestSubstring('pwrtywkewopqsr'))
