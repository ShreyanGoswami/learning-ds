class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        n = len(heights)
        s = [-1]
        area = 0
        for i in range(n):
            while heights[s[-1]] > heights[i]:
                h = heights[s.pop()]
                w = i - s[-1] - 1
                area = max(area, h * w)
            s.append(i)
        return area
