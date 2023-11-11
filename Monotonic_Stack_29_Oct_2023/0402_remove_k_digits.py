class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        ## e.g Say k = 1
        ## 4321 : when digits are decreasing, pop from left, get 321
        ## 1234 : when numbers are increasing, pop from right, get 123
        s = []
        for n in num:
            while s and k and s[-1] > n:
                s.pop()
                k -= 1

            if s or n is not '0':
                s.append(n)

        if k:
            s = s[0:-k]

        return ''.join(s) or '0'
