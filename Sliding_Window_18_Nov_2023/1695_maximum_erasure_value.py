class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        counter = [0] * 10001
        start, end, subarray_sum, _sum = 0, 0, 0, 0

        while end < len(nums):
            counter[nums[end]] += 1
            _sum += nums[end]

            while counter[nums[end]] > 1:
                counter[nums[start]] -= 1
                _sum -= nums[start]
                start += 1

            subarray_sum = max(subarray_sum, _sum)
            end += 1

        return subarray_sum
