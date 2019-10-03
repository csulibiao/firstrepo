class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2,nums1)
        x,y=len(nums1),len(nums2)
        start,end=0,x

        while start <= end:
            cut1=(start+end)//2
            cut2=(x+y+1)//2-cut1
            max_left1=float('-inf') if cut1==0 else nums1[cut1-1]
            max_left2=float('-inf') if cut2==0 else nums2[cut2-1]
            min_right1=float('inf') if cut1==x else nums1[cut1]
            min_right2=float('inf') if cut2==y else nums2[cut2]

            if cut1 > 0 and nums1[cut1-1] > nums2[cut2]:
                end = cut1 -1 

            elif cut1 < x and nums2[cut2-1] > nums1[cut1]:
                start = cut1 + 1

            elif max(max_left1,max_left2) <= min(min_right1,min_right2):

                if (x+y)%2==0:
                    return (max(max_left1,max_left2)+ min(min_right1,min_right2))/2
                else:
                    return max(max_left1,max_left2)

            
        




sol = Solution()
print(sol.findMedianSortedArrays([1],[3,4]))