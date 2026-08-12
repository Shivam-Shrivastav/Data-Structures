
# Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold

## Pattern
Fixed Size Sliding Window

## Problem

Count the number of contiguous subarrays of size `k` whose average is at least `threshold`.

Since:

```
average >= threshold
```

becomes

```
sum >= k * threshold
```

No division is required.

---

# Diagram

```
k = 3

[2 2 2]
 ↓
[2 5 5]
 ↓
[5 5 5]
```

---

# Examples

Input

```
arr=[2,2,2,2,5,5,5,8]
k=3
threshold=4
```

Output

```
3
```

---

# Intuition

Convert average comparison into sum comparison.

Maintain running window sum.

---

# Simpler Version

Brute force:
Calculate average of every window.

Time: O(nk)

Sliding window:
Update sum in O(1).

---

# Brute Force

```python
for each window:
    if sum(window)/k >= threshold:
        answer += 1
```

Time: O(nk)

---

# Optimal Solution

```python
class Solution:
    def numOfSubarrays(self, arr, k, threshold):
        target = k * threshold

        window = sum(arr[:k])
        ans = 1 if window >= target else 0

        for i in range(k, len(arr)):
            window += arr[i]
            window -= arr[i-k]

            if window >= target:
                ans += 1

        return ans
```

Time: **O(n)**

Space: **O(1)**

---

# Dry Run

Target = 12

Window sums:

```
6
9
12 ✔
15 ✔
18 ✔
```

Answer = 3

---

# Related Problems

- Maximum Average Subarray I
- Grumpy Bookstore Owner
