class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        for i in range(len(nums2)):
            nums1.append(nums2[i])
        for i in range(len(nums1)):
            for j in range(len[nums1]):
                if nums1[i] < nums1[j]:
                    x = nums1[i]
                    nums1[i] = nums1[j]
                    nums1[j] = x

        print(nums1) 