package main

func largestRectangleArea(heights []int) int {
    heights = append(heights, 0)
    n := len(heights)
    s := []int{-1}
    ans := 0

    for i := 0; i < n; i++ {
        for len(s) > 1 && heights[i] < heights[s[len(s)-1]] {
            h := heights[s[len(s)-1]]
            s = s[:len(s)-1]
            w := i - s[len(s)-1] - 1
            ans = max(ans, h * w)
        }
        s = append(s, i)
    }
    return ans
}
