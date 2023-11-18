class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sub_sum = sum(nums[:k])
        maximum = sub_sum

        for i in range(k, len(nums)):
            sub_sum += nums[i] - nums[i-k]
            maximum = max(maximum, sub_sum)

        return maximum / k
