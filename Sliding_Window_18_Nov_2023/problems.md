Solve the following LC problems
- [x] https://leetcode.com/problems/longest-substring-without-repeating-characters/
- [x] https://leetcode.com/problems/maximum-erasure-value/
- [x] https://leetcode.com/problems/optimal-partition-of-string/
- [ ] https://leetcode.com/problems/count-complete-subarrays-in-an-array/
- [x] https://leetcode.com/problems/minimum-consecutive-cards-to-pick-up/
- [x] https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/
- [x] https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/

Watch the following videos on time complexity analysis
- [x] [1.5.1 Time Complexity #1](https://www.youtube.com/watch?v=9TlHvipP5yA)
- [x] [1.5.2 Time Complexity Example #2](https://www.youtube.com/watch?v=9SgLBjXqwd4)
- [x] [1.5.3 Time Complexity of While and if #3](https://www.youtube.com/watch?v=p1EnSvS3urU)
- [x] [1.8.1 Asymptotic Notations Big Oh - Omega - Theta #1](https://www.youtube.com/watch?v=A03oI0znAoc)
- [x] [1.8.2 Asymptotic Notations - Big Oh - Omega - Theta #2](https://www.youtube.com/watch?v=Nd0XDY-jVHs)

More LC problems
- [ ] https://leetcode.com/problems/min-stack/ 
- [ ] https://leetcode.com/problems/sort-colors/
- [ ] https://leetcode.com/problems/decode-string/
- [ ] https://leetcode.com/problems/car-fleet/
- [ ] Optional hard problem - https://leetcode.com/problems/maximal-rectangle/

## Theory problem

Till now we haven't formally talked about time complexity. After watching Abdul Bari's videos above I hope you get a better understanding.
Consider the code we had seen to generate all possible substring.
```python
def substrings(s):
    for i in range(len(s)):
        for j in range(i, len(s)):
            print(s[i, j+1])
```

As we have previously discussed, the time complexity of an algorithm is measured in terms of it's input size. If there's any computation in the function that's done irrespective of input size we don't consider it for the time complexity analysis or we say that it takes constant time O(1). For steps that do depend on input size, a basic way to analyze the time complixty is to just count the total number of steps/operation in terms of input size(n). 

For example, say we print all the characters of a string of length n -
```python
def print_chars(s):
    for c in s:
        print(c)
```

The time complexity of the above function is O(n) since we need to iterate over all n characters in a string. Apply the above logic to count the number of steps in the **substrings** function. Hint: Consider the number of steps in every iteration of the inner for loop.

#### Solution
- [ ] TODO
