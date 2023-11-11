class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        s = []
        ans = [0] * len(t)
        
        for i in range(len(t)):
            while s and t[s[-1]] < t[i]:
                idx = s.pop()
                ans[idx] = i - idx
            s.append(i)

        return ans
