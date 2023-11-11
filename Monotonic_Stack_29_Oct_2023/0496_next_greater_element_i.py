class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nextGreater = {}
        s = []
        
        for i, v in enumerate(nums2):
            nextGreater[v] = -1
            while s and s[-1] < v:
                k = s.pop()
                nextGreater[k] = v
            s.append(v)

        result = []
        for k in nums1:
            result.append(nextGreater[k])

        return result
