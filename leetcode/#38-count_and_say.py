#from collections import Counter
class Solution:
    def countAndSay(self, n):
        seq = '1'
        for i in range(n-1):
            seq = self.getNext(seq)
        return seq

    def getNext(self,seq):
        counter=1
        res=''
        if len(seq)==1:
            return '11'
        else:
            for i in range(len(seq)-1):
                if seq[i]==seq[i+1]:
                    counter+=1
                else:
                    res+=str(counter)+seq[i]
                    counter=1
            return res+str(counter)+seq[-1]



sol = Solution()
print(sol.countAndSay(4))

