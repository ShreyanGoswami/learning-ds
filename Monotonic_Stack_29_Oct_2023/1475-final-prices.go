package main

func finalPrices(prices []int) []int {
    s := make([]int, 0, len(prices))

    for i, p := range prices {
        for top := len(s)-1; top >= 0 && prices[s[top]] >= p; top-- {
            prices[s[top]] -= p
            s = s[:top]
        }
        s = append(s, i)
    }
    return prices
}
