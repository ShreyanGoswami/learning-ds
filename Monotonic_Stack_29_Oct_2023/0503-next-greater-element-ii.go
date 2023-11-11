package main

func nextGreaterElements(nums []int) []int {
    n := len(nums)
    s := make([]int, n)   
    ans := make([]int, n)
    for i := range ans {
        ans[i] = -1
    }

    for i := 0; i < 2*n; i++ {
        i := i % n
        
        for top := len(s)-1; top >= 0 && nums[s[top]] < nums[i]; top-- {
            ans[s[top]] = nums[i]
            s = s[:top]
        }
        s = append(s, i)
    }

    return ans
}
