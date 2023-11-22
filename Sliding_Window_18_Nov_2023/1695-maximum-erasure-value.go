package main

func maximumUniqueSubarray(nums []int) int {
    counter := [10001]int{}
    start, end, subArraySum, tempSum := 0, 0, 0, 0

    for end < len(nums) {
        counter[nums[end]]++
        tempSum += nums[end]

        for counter[nums[end]] > 1 {
            counter[nums[start]]--
            tempSum -= nums[start]
            start++
        }

        subArraySum = max(subArraySum, tempSum)
        end++
    }

    return subArraySum
}
