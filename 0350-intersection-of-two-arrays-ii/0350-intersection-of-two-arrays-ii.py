class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        i,j=0,0
        nums1.sort()
        nums2.sort()
        ans=[]
        while i<len(nums1) and j<len(nums2):
            if nums1[i] > nums2[j]:
                j+=1
            elif nums1[i] < nums2[j]:
                i+=1
            else:
                ans.append(nums1[i])
                j+=1
                i+=1
                
                
        return ans
        
        