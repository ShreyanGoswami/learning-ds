package main

func nextGreaterElement(nums1 []int, nums2 []int) []int {
    next := make(map[int]int)
    s := make([]int, 0, len(nums2))

    for _, v := range nums2 {
        next[v] = -1

        for top := len(s)-1; top >= 0 && s[top] < v; top-- {
            next[s[top]] = v
            s = s[:top]
        }

        s = append(s, v)
    }

    for i, v := range nums1 {
        nums1[i] = next[v]
    }

    return nums1
}
