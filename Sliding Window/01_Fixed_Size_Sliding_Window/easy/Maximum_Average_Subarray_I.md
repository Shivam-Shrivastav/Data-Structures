
# Maximum Average Subarray I

## Pattern
Fixed Size Sliding Window

## Problem
Given an integer array `nums` and an integer `k`, find the **maximum average value** of any contiguous subarray of length `k`.

### Constraints
- Window size is fixed.
- Need the maximum average, not the subarray.

---

# Diagram

```
nums = [1,12,-5,-6,50,3], k = 4

[1 12 -5 -6]  -> sum = 2
   ↓ slide
[12 -5 -6 50] -> sum = 51
      ↓ slide
[-5 -6 50 3]  -> sum = 42
```

---

# Examples

### Example 1
Input:
```
nums = [1,12,-5,-6,50,3], k = 4
```

Output:
```
12.75
```

Explanation:
Maximum window sum = 51.

### Edge Case

Input:
```
nums = [5], k = 1
```

Output:
```
5.0
```

---

# Intuition

Whenever:
- window size is fixed
- every contiguous window must be checked

think **Sliding Window**.

Instead of recomputing every window sum:

```
new_sum = old_sum - outgoing + incoming
```

---

# Simpler Version

Brute-force:
Compute every window sum independently.

Time: O(nk)

Observation:
Only one element leaves and one enters.

Hence O(n).

---

# Brute Force

```python
for every window:
    calculate sum(window)
answer = maximum
```

Time: **O(nk)**

Space: **O(1)**

---

# Optimal Solution

```python
class Solution:
    def findMaxAverage(self, nums, k):
        window = sum(nums[:k])
        best = window

        for i in range(k, len(nums)):
            window += nums[i]
            window -= nums[i-k]
            best = max(best, window)

        return best / k
```

Time: **O(n)**

Space: **O(1)**

---

# Dry Run

Window = [1,12,-5,-6]

sum = 2

Slide:

```
2 -1 +50 = 51
best = 51
```

Slide:

```
51 -12 +3 = 42
```

Answer:

```
51/4 = 12.75
```

---

# Related Problems

- Sliding Window Maximum
- Grumpy Bookstore Owner
- Maximum Points You Can Obtain from Cards
