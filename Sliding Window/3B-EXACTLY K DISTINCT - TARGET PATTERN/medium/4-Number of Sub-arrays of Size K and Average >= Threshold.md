# **1343. Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold**

## 1. Problem Statement

You are given:

* An integer array `arr`
* An integer `k`
* An integer `threshold`

Find the **number of contiguous subarrays of length exactly `k`** whose **average** is **greater than or equal to `threshold`**.

Return that count.

### Constraints

* `1 <= arr.length <= 10^5`
* `1 <= arr[i] <= 10^4`
* `1 <= k <= arr.length`
* `0 <= threshold <= 10^4`

Since `n` can be **100,000**, checking every subarray repeatedly is too slow.

---

## 2. Diagram

Suppose

```
arr = [2,2,2,2,5,5,5,8]
k = 3
threshold = 4
```

Sliding window:

```
Window 1
[2 2 2] 2 5 5 5 8
 sum = 6

Shift →

2 [2 2 2] 5 5 5 8
 sum = 6

Shift →

2 2 [2 2 5] 5 5 8
 sum = 9

Shift →

2 2 2 [2 5 5] 5 8
 sum =12 ✓

Shift →

2 2 2 2 [5 5 5] 8
 sum =15 ✓

Shift →

2 2 2 2 5 [5 5 8]
 sum =18 ✓
```

Instead of recomputing every window's sum:

```
newSum = oldSum
         - outgoing element
         + incoming element
```

---

# 3. Example I/O

### Example 1

**Input**

```
arr = [2,2,2,2,5,5,5,8]
k = 3
threshold = 4
```

**Output**

```
3
```

Explanation

Average required:

```
>=4
```

Equivalent sum:

```
>=4×3
>=12
```

Valid windows

```
[2,5,5] =12
[5,5,5] =15
[5,5,8] =18
```

Answer = **3**

---

### Example 2 (Edge Case)

```
arr = [5]
k = 1
threshold = 5
```

Output

```
1
```

Average = 5

Valid.

---

## 4. Intuition & Pattern Recognition

### Signals

Whenever you see

* Fixed window size
* Every subarray of length exactly K
* Need sum/average/max/min

Think immediately:

> **Fixed Size Sliding Window**

---

### Key Observation

Average comparison

```
sum / k >= threshold
```

Multiply both sides by k

```
sum >= threshold × k
```

Now we don't even calculate averages.

Only maintain window sum.

---

### Interview Thought Process

> "Window size never changes."

So,

* build first window
* move one step
* subtract left
* add right

Classic fixed-size sliding window.

---

# 5. Simpler Version

## Simpler Question

**Maximum Sum Subarray of Size K**

You only maintain window sum.

```
sum += incoming
sum -= outgoing
```

This problem is exactly the same.

Instead of

```
maximize sum
```

we simply check

```
sum >= threshold*k
```

and count.

---

### Thinking Progression

```
Maximum Sum Window
        ↓
Maintain running sum
        ↓
Compare each window
        ↓
Count qualifying windows
```

---

### Related Simpler Problems

* Maximum Sum Subarray of Size K
* Maximum Average Subarray I
* Find All Anagrams in a String (fixed window)
* Defuse the Bomb
* K Radius Subarray Averages

---

# 6. Brute Force

For every starting index

Compute sum of next K elements.

```
count = 0

for every i
      sum = 0
      for j=i to i+k-1
             sum += arr[j]

      if sum/k >= threshold
             count++
```

### Time Complexity

```
O(n*k)
```

### Space

```
O(1)
```

Too slow for

```
n = 100000
```

---

# 7. Optimal Solution (Sliding Window)

### Idea

Maintain

```
windowSum
```

Whenever window reaches size K

```
if windowSum >= threshold*k
      answer++

Remove left element
Continue
```

### Python

```python
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int):
        required = threshold * k
        window_sum = 0
        count = 0

        # Build the first window
        for i in range(k):
            window_sum += arr[i]

        if window_sum >= required:
            count += 1

        # Slide the window
        for i in range(k, len(arr)):
            window_sum += arr[i]          # Add incoming element
            window_sum -= arr[i - k]      # Remove outgoing element

            if window_sum >= required:
                count += 1

        return count
```

### Time Complexity

```
O(n)
```

Every element enters and leaves the window once.

### Space Complexity

```
O(1)
```

---

# 8. Step-by-Step Trace

```
arr = [2,2,2,2,5,5,5,8]
k = 3
threshold = 4

requiredSum = 12
```

| Window  | Window Sum | ≥12? | Count |
| ------- | ---------: | :--: | ----: |
| [2,2,2] |          6 |   ❌  |     0 |
| [2,2,2] |          6 |   ❌  |     0 |
| [2,2,5] |          9 |   ❌  |     0 |
| [2,5,5] |         12 |   ✅  |     1 |
| [5,5,5] |         15 |   ✅  |     2 |
| [5,5,8] |         18 |   ✅  |     3 |

Final answer

```
3
```

---

# 9. Related Problems

### 1. Maximum Sum Subarray of Size K (Easy)

The fundamental fixed-size sliding window problem. Maintain a running sum for a window of size `k`.

---

### 2. Maximum Average Subarray I (Easy)

Uses the exact same window-sum technique, but keeps track of the maximum average instead of counting windows.

---

### 3. Defuse the Bomb (Easy)

Computes sums over fixed-size circular windows using sliding window logic.

---

### 4. Find All Anagrams in a String (Medium)

Maintains a fixed-size window, but tracks character frequencies instead of sums.

---

### 5. Sliding Window Maximum (Hard)

A more advanced fixed-window problem where a monotonic deque is used to maintain the maximum efficiently.

---

# Pattern Summary

| Clue in Problem                    | Pattern                           |
| ---------------------------------- | --------------------------------- |
| Subarray of **exactly K** elements | Fixed Size Sliding Window         |
| Need sum/average of every window   | Maintain running sum              |
| Average comparison                 | Convert to `sum >= threshold × k` |
| Move window                        | Add incoming, remove outgoing     |
| Complexity                         | **O(n)** time, **O(1)** space     |

### Interview takeaway

Whenever you see **"every subarray of length exactly `k`"**, your first thought should be:

> **Fixed-size Sliding Window → Maintain one running value (sum/frequency/etc.) → Update in O(1) while sliding.**
