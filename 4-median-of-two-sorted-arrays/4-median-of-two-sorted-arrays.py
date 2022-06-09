import numpy as np
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        con = np.concatenate((nums1,nums2))
        con = sorted(con)
        print(con)
        l = len(con)
        if (l%2!=0):
            median = int(l/2)
            return(con[median])
        else :
            median1 = int(l/2)
            median2 = median1
            print(median1)
            print(median2)
            return ((con[median1-1]+con[median2])/2)
        