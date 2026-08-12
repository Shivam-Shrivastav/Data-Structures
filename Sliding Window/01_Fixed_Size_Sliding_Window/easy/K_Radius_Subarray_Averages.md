
# K Radius Subarray Averages

## Pattern
Fixed Size Sliding Window + Prefix Sum Idea

## Problem

For every index, compute the average of all elements within radius `k`.

Window size:

```
2*k + 1
```

If complete window cannot exist:

```
answer = -1
```

---

# Diagram

```
k = 1

1 3 2 6 4

   ^
window:

1 3 2

average = 2
```

---

# Example

Input

```
nums=[7,4,3,9,1,8,5,2,6]
k=3
```

Output

```
[-1,-1,-1,5,4,4,-1,-1,-1]
```

---

# Intuition

Every answer depends on a fixed-size window.

Window length never changes.

Slide once.

---

# Simpler Version

If only one query existed:

Compute sum directly.

Since every index needs one,

Sliding Window avoids repeated work.

---

# Brute Force

For every index:

```
calculate window sum
```

Time:

O(n × window)

---

# Optimal Solution

```python
class Solution:
    def getAverages(self, nums, k):
        n = len(nums)
        ans = [-1] * n

        length = 2 * k + 1
        if length > n:
            return ans

        window = sum(nums[:length])

        ans[k] = window // length

        for right in range(length, n):
            window += nums[right]
            window -= nums[right-length]
            ans[right-k] = window // length

        return ans
```

Time: **O(n)**

Space: **O(1)** (excluding output)

---

# Dry Run

Window length = 7

Compute first sum.

Each slide:

```
+incoming
-outgoing
```

Store average at window center.

---

# Related Problems

- Maximum Average Subarray I
- Moving Average from Data Stream
- Sliding Window Maximum
