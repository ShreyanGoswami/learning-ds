pacakge main

func removeKdigits(num string, k int) string {
    s := make([]rune, 0)

    for _, r := range num {
        for len(s) > 0 && s[len(s)-1] > r && k > 0 {
            s = s[:len(s)-1]
            k--
        }
        s = append(s, r)
    }

    for k > 0 {
        s = s[:len(s)-1]
        k--
    }

    for i := range s {
        if s[i] != '0' {
            return string(s[i:])
        }
    }

    return "0"
}
