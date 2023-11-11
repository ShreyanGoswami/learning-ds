package main

func removeKdigits(num string, k int) string {
    s := make([]rune, 0)

    for _, r := range num {
        for top := len(s)-1; top >= 0 && k > 0 && s[top] > r; top-- {
            s = s[:top]
            k--
        }
        s = append(s, r)
    }

    if k > 0 {
        s = s[:len(s)-k]
    }

    for i := range s {
        if s[i] != '0' {
            return string(s[i:])
        }
    }

    return "0"
}
