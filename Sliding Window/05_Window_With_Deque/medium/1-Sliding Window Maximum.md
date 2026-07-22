# Sliding Window Maximum (LeetCode 239)

**Pattern:** Monotonic Deque + Fixed Size Sliding Window

---

# 1. Problem Statement

Given an integer array `nums` and an integer `k`, return an array containing the **maximum element of every contiguous subarray (window) of size `k`**.

Instead of finding the maximum for one window, we need to efficiently compute it for **all** windows.

### Example

```text
nums = [1,3,-1,-3,5,3,6,7]
k = 3

Windows:

[1 3 -1] -3  5  3  6  7   -> 3
 1 [3 -1 -3] 5  3  6  7   -> 3
 1  3 [-1 -3 5] 3  6  7   -> 5
 1  3 -1 [-3 5 3] 6  7    -> 5
 1  3 -1 -3 [5 3 6] 7     -> 6
 1  3 -1 -3 5 [3 6 7]     -> 7

Output = [3,3,5,5,6,7]
```

### Constraints

* `1 <= nums.length <= 10^5`
* `-10^4 <= nums[i] <= 10^4`
* `1 <= k <= nums.length`
* Expected complexity: **O(N)**

---

# 2. Diagram

```text
nums = [1,3,-1,-3,5,3,6,7]
k = 3

Deque stores INDICES
(Values kept in decreasing order)

Index:  0 1 2 3 4 5 6 7
Value:  1 3 -1 -3 5 3 6 7

Process 1:
Deque = [0]

Process 3:
1 < 3
Remove 0

Deque = [1]

Process -1

Deque = [1,2]

Window:
[1,3,-1]

Front = index 1
Maximum = 3

-------------------------

Next element = -3

Deque = [1,2,3]

Maximum still 3

-------------------------

Next element = 5

Remove 3
Remove 2
Remove 1

Deque = [4]

Maximum becomes 5
```

The deque always keeps **possible maximum candidates**.

---

# 3. Example I/O

### Example 1

```text
Input:
nums = [1,3,-1,-3,5,3,6,7]
k = 3

Output:
[3,3,5,5,6,7]
```

Explanation

```text
Every window maximum is reported.
```

---

### Example 2 (Edge Case)

```text
Input:
nums = [1]
k = 1

Output:
[1]
```

---

### Example 3

```text
Input:
nums = [7,2,4]
k = 2

Output:
[7,4]
```

Explanation

```text
[7,2] -> 7
[2,4] -> 4
```

---

# 4. Intuition & Pattern Recognition

### Signals

Whenever you see

* Maximum/Minimum of every window
* Window size fixed
* Need O(N)

Think:

> **Monotonic Queue (Deque)**

### Why not recompute every time?

If every window scans all `k` elements,

```text
Time = O(N × K)
```

Too slow when

```text
N = 100000
```

Need to reuse previous work.

---

### Key Observation

Suppose deque currently stores

```text
8 6 5
```

New number arrives

```text
7
```

Now

```text
8 6 5 7
```

Can **5** ever become maximum later?

No.

7 is newer and larger.

So remove 5.

Similarly,

```text
8 6 7

Remove 6

Deque:

8 7
```

Only useful candidates remain.

---

### Interview Thinking

Tell yourself:

```text
Need maximum of every window.

Largest element should always stay
at the front.

Smaller elements behind a larger one
can never become maximum.

Remove them immediately.

Also remove indices that move
outside the window.
```

---

# 5. Simpler Version

## Simpler Question 1

### Maximum Element in an Array

```text
Scan once

Keep largest value.
```

---

## Simpler Question 2

### Maximum of One Window

```text
Given one window of size K

Loop through K elements.

Find maximum.
```

Complexity:

```text
O(K)
```

---

## Simpler Question 3

### Sliding Window Sum

```text
Remove left

Add right
```

Window changes efficiently.

---

## Current Question

Instead of updating a sum,

we must update the **maximum**.

Maximum cannot be updated by subtraction.

Need another structure.

That structure is

> **Monotonic Deque**

---

### Thinking Progression

```text
Maximum of one array

↓

Maximum of one window

↓

Sliding window

↓

Need fast maximum update

↓

Monotonic Queue

↓

Sliding Window Maximum
```

---

# 6. Brute Force

For every window

```text
Scan all K elements

Find maximum
```

```python
for i in range(n-k+1):
    ans.append(max(nums[i:i+k]))
```

### Complexity

```text
Time  : O(N × K)

Space : O(1)
```

---

# 7. Optimal Solution (Monotonic Deque)

### Idea

Deque stores **indices**, not values.

Rules:

1. Remove indices outside the window.
2. Remove smaller values from the back.
3. Add current index.
4. Front of deque = maximum.

### Python

```python
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums, k):

        dq = deque()      # Stores indices
        ans = []

        for i in range(len(nums)):

            # Remove indices outside current window
            while dq and dq[0] <= i - k:
                dq.popleft()

            # Remove smaller values
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            # Add current index
            dq.append(i)

            # Window formed
            if i >= k - 1:
                ans.append(nums[dq[0]])

        return ans
```

### Complexity

```text
Time  : O(N)

Space : O(K)
```

Each index enters and leaves the deque at most once.

---

# 8. Step-by-Step Trace

Example

```text
nums = [1,3,-1,-3,5,3,6,7]
k = 3
```

| i | Num | Deque (indices) | Deque (values) | Window Max |
| - | --- | --------------- | -------------- | ---------- |
| 0 | 1   | [0]             | [1]            | -          |
| 1 | 3   | [1]             | [3]            | -          |
| 2 | -1  | [1,2]           | [3,-1]         | 3          |
| 3 | -3  | [1,2,3]         | [3,-1,-3]      | 3          |
| 4 | 5   | [4]             | [5]            | 5          |
| 5 | 3   | [4,5]           | [5,3]          | 5          |
| 6 | 6   | [6]             | [6]            | 6          |
| 7 | 7   | [7]             | [7]            | 7          |

Final Output

```text
[3,3,5,5,6,7]
```

---

# 9. Related Problems

| Problem                                                          | Connection                                                                 |
| ---------------------------------------------------------------- | -------------------------------------------------------------------------- |
| **643. Maximum Average Subarray I**                              | Fixed-size sliding window using sums instead of maxima.                    |
| **346. Moving Average from Data Stream**                         | Maintains a fixed-size window efficiently.                                 |
| **862. Shortest Subarray with Sum at Least K**                   | Uses a monotonic deque for prefix sums, a more advanced deque application. |
| **1438. Longest Continuous Subarray With Absolute Diff ≤ Limit** | Uses two monotonic deques (one max, one min) to maintain window validity.  |
| **1696. Jump Game VI**                                           | Dynamic programming optimized with a monotonic deque.                      |

---

# Key Interview Takeaways

* **Pattern:** Fixed Size Sliding Window + Monotonic Deque.
* **Data Structure:** `deque` storing **indices**.
* **Invariant:** Values corresponding to indices in the deque are always in **decreasing order**.
* **Rule 1:** Remove indices that fall outside the current window.
* **Rule 2:** Remove smaller values from the back before inserting the current index.
* **Rule 3:** The front of the deque always points to the maximum element of the current window.
* **Complexity:** **O(N)** time and **O(K)** space because each index is pushed and popped at most once.

This follows the same quick-revision structure as your previous sliding window notes. It also builds naturally after **Longest Substring Without Repeating Characters**, progressing from a **HashSet-based sliding window** to the more advanced **Monotonic Deque** technique. 
