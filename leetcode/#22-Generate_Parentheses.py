'''
Given n pairs of parentheses, write a function to generate all combinations 
of well-formed parentheses.
For example, given n = 3, a solution set is:
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
'''

class Solution:
    def generateParenthesis(self, n):
        if n == 0:
            return []
        
        result = []
        self.helper(n, n, '', result)
        return result

    def helper(self, l, r, item, result):
        if r < l:
            return
        if l == 0 and r == 0:
            result.append(item)
        if l > 0:
            self.helper(l-1,r,item+'(',result)
        if r > 0:
            self.helper(l, r-1,item+')',result)

A = Solution()
print(A.generateParenthesis(3))


