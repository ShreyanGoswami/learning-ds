def longest_distance(blocks):
    n = len(blocks)
    left = {i: i for i in range(n)}
    right = {i: i for i in range(n)}
    for i in range(1, n):
        if blocks[i] >= blocks[i - 1]:
            left[i] = left[i - 1]
    for i in range(n - 2, -1, -1):
        if blocks[i] >= blocks[i + 1]:
            right[i] = right[i + 1]
    max_distance = 0
    for i in range(n):
        max_distance = max(max_distance, right[i] - left[i] + 1)
    return max_distance
