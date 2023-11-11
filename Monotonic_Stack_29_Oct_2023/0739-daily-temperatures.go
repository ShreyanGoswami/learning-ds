package main

func dailyTemperatures(T []int) []int {
	res := make([]int, len(T))
	s := make([]int, 0, len(T))

	for i, t := range T {
		for top := len(s)-1; top >= 0 && T[s[top]] < t; top-- {
			res[s[top]] = i - s[top]
			s = s[:top]
		}
		s = append(s, i)
	}

	return res
}
