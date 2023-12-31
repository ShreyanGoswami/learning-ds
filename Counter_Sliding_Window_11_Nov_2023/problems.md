# Bucket Sort

1. The counter variable is inspired from the Valid Anagrams problem in leetcode. We discussed how we can use a counter to sort strings in linear time given certain constraints such as every character is lowercase. Here's the code for reference:

```python
s = "cccaaabbbddd"
counter = [0] * 26
for x in s:
    counter[ord(x)-ord('a')] += 1

res = ""
for i in range(26):
    char = chr(i+97) # this will convert the ith index to the corresponding character i=0 output='a', i =1, output = b
    res += char * counter[i]

print(res)
```

One can argue that we can use a dictionary instead of a counter variable for Valid Anagrams. However, it's not possible to substitute the counter variable for a python dictionary. Explain why it's not possible to do so. Hint: rewrite the above code using a dictionary and see the output. 

# The Sliding Window Technique

2. We discussed about the general structure of sliding window problems and saw a toy problem.

Given a list of positive numbers, find the largest sum of subarray of size 4. The solution we discussed -

```python
def max_sum(input, k=4):
    start = 0
    end = k - 1
    res = 0
    while end < len(input):
        # find the sum between start and end inclusive
        sum = 0
        for i in range(start, end+1):
            sum += input[i]
            res = max(res, sum)
        # Move the window forward
        start += 1
        end += 1
    return res
```

We analyzed the time complexity to figure out that this runs in linear time even though there's an internal for loop. Can you rewrite this algorithm to not have a for loop, list comprehension and without using in built python functions

## Solution

```python
def max_sum(input, k):
    start = 0
    end = k-1
    sub_sum = 0

    for i in range(k):
        sub_sum += input[i]

    res = sub_sum

    # Move the window forward
    while end < len(input) - 1:
        sub_sum += input[end+1] - input[start]
        start += 1
        end += 1
        res = max(res, sub_sum)
    return res
```

# Leetcode Problems

3. Solve https://leetcode.com/problems/maximum-average-subarray-i/
4. Solve https://leetcode.com/problems/contains-duplicate-ii/
5. Bonus monotonic stack problem (optional) https://leetcode.com/problems/largest-rectangle-in-histogram/
