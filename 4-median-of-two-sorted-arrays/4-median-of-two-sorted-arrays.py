import numpy as np
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        con = np.concatenate((nums1,nums2))
        con = sorted(con)
        if (len(con)%2!=0):
            median = int(len(con)/2)
            return(con[median])
        else :
            median1 = int(len(con)/2)
            median2 = median1-1
            return ((con[median1]+con[median2])/2)
        