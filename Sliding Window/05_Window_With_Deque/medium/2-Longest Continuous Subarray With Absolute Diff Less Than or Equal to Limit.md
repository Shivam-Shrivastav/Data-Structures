# Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit (LeetCode 1438)

**Pattern:** Variable Size Sliding Window + Two Monotonic Deques

---

# 1. Problem Statement

Given an integer array `nums` and an integer `limit`, return the **length of the longest contiguous subarray** such that:

```text
max(nums in window) - min(nums in window) <= limit
```

The window is valid only if the difference between its **maximum** and **minimum** elements is at most `limit`.

### Constraints

* `1 <= nums.length <= 10^5`
* `1 <= nums[i] <= 10^9`
* `0 <= limit <= 10^9`
* Need an **O(N)** solution.

---

# 2. Diagram

```text
nums = [8,2,4,7]
limit = 4

Window:

[8]

Max = 8
Min = 8
Diff = 0 ✓

-----------------------

[8,2]

Max = 8
Min = 2
Diff = 6 ✗

Shrink

[2]

-----------------------

[2,4]

Max = 4
Min = 2
Diff = 2 ✓

-----------------------

[2,4,7]

Max = 7
Min = 2
Diff = 5 ✗

Shrink

[4,7]

Diff = 3 ✓
```

We must know the **maximum** and **minimum** of the current window at all times.

---

# 3. Example I/O

### Example 1

```text
Input:
nums = [8,2,4,7]
limit = 4

Output:
2
```

Explanation

```text
Valid longest windows:

[2,4]
[4,7]

Length = 2
```

---

### Example 2

```text
Input:
nums = [10,1,2,4,7,2]
limit = 5

Output:
4
```

Explanation

```text
Longest window:

[2,4,7,2]

Max = 7
Min = 2

Difference = 5
```

---

### Example 3 (Edge Case)

```text
Input:
nums = [5]
limit = 0

Output:
1
```

---

# 4. Intuition & Pattern Recognition

### Signals

Whenever you see

* Longest subarray
* Window must satisfy a condition
* Need maximum and minimum continuously
* Constraint = 100000

Think:

> **Variable Sliding Window + Two Monotonic Deques**

---

### Why two deques?

Need

```text
Maximum

AND

Minimum
```

efficiently.

One deque cannot maintain both.

Use

```text
MaxDeque

(decreasing)

------------------

MinDeque

(increasing)
```

---

### Interview Thinking

Tell yourself:

```text
Window becomes invalid when

max - min > limit

Need maximum instantly.

Need minimum instantly.

Maintain both using
monotonic queues.

Expand right.

If invalid,

shrink left until valid again.
```

---

# 5. Simpler Version

## Simpler Question 1

### Sliding Window Maximum (239)

Maintain only

```text
Maximum
```

using one deque.

---

## Simpler Question 2

### Sliding Window Minimum

Exactly same idea

but increasing deque.

---

## Current Question

Need both simultaneously.

```text
Maximum

AND

Minimum
```

Then

```text
if max-min > limit

Shrink
```

---

### Thinking Progression

```text
Sliding Window Maximum

↓

Sliding Window Minimum

↓

Maintain both

↓

Variable Window

↓

Longest Continuous Subarray
```

---

# 6. Brute Force

For every starting index

Expand right

Compute

```text
Maximum

Minimum
```

each time.

```python
for i:
    mx = mn = nums[i]

    for j:
        mx = max(mx, nums[j])
        mn = min(mn, nums[j])

        if mx-mn <= limit:
            answer = max(answer, j-i+1)
```

### Complexity

```text
Time : O(N²)

Space : O(1)
```

---

# 7. Optimal Solution (Two Monotonic Deques)

### Idea

Maintain

```text
maxDeque

↓

largest at front

----------------

minDeque

↓

smallest at front
```

Whenever

```text
max-min > limit
```

move left pointer until valid.

### Python

```python
from collections import deque

class Solution:
    def longestSubarray(self, nums, limit):

        maxDeque = deque()
        minDeque = deque()

        left = 0
        ans = 0

        for right in range(len(nums)):

            # Maintain decreasing deque (maximum)
            while maxDeque and nums[maxDeque[-1]] < nums[right]:
                maxDeque.pop()

            maxDeque.append(right)

            # Maintain increasing deque (minimum)
            while minDeque and nums[minDeque[-1]] > nums[right]:
                minDeque.pop()

            minDeque.append(right)

            # Shrink until valid
            while nums[maxDeque[0]] - nums[minDeque[0]] > limit:

                if maxDeque[0] == left:
                    maxDeque.popleft()

                if minDeque[0] == left:
                    minDeque.popleft()

                left += 1

            ans = max(ans, right - left + 1)

        return ans
```

### Complexity

```text
Time  : O(N)

Space : O(N)
```

Each index enters and leaves each deque at most once.

---

# 8. Step-by-Step Trace

Example

```text
nums = [10,1,2,4,7,2]
limit = 5
```

| Right | Num | MaxDeque (values) | MinDeque (values) | Left | Window    | Max Len |
| ----- | --- | ----------------- | ----------------- | ---- | --------- | ------- |
| 0     | 10  | [10]              | [10]              | 0    | [10]      | 1       |
| 1     | 1   | [10,1]            | [1]               | 1    | [1]       | 1       |
| 2     | 2   | [2]               | [1,2]             | 1    | [1,2]     | 2       |
| 3     | 4   | [4]               | [1,2,4]           | 1    | [1,2,4]   | 3       |
| 4     | 7   | [7]               | [1,2,4,7]         | 2    | [2,4,7]   | 3       |
| 5     | 2   | [7,2]             | [2,2]             | 2    | [2,4,7,2] | 4       |

Final Answer

```text
4
```

---

### Window Shrinking Example

At

```text
Window = [10,1]

Max = 10

Min = 1

Difference = 9

> 5
```

Shrink

```text
Remove 10

Window = [1]

Difference = 0

Valid again.
```

---

# 9. Related Problems

| Problem                                        | Connection                                                                                   |
| ---------------------------------------------- | -------------------------------------------------------------------------------------------- |
| **239. Sliding Window Maximum**                | Uses a single monotonic deque to maintain the maximum.                                       |
| **480. Sliding Window Median**                 | Generalizes sliding-window statistics using balanced data structures.                        |
| **862. Shortest Subarray with Sum at Least K** | Uses a monotonic deque with prefix sums.                                                     |
| **1696. Jump Game VI**                         | Dynamic programming optimized with a monotonic deque.                                        |
| **2762. Continuous Subarrays**                 | Same idea of maintaining max and min with two monotonic deques while counting valid windows. |

---

# Key Interview Takeaways

* **Pattern:** Variable Size Sliding Window + Two Monotonic Deques.
* **Data Structures:**

  * `maxDeque` → decreasing values (front = maximum).
  * `minDeque` → increasing values (front = minimum).
* **Invariant:** The current window is valid only if `max - min <= limit`.
* **Rule:** Expand the `right` pointer, update both deques, and shrink from the `left` whenever the condition is violated.
* **Complexity:** **O(N)** time because each index is inserted and removed from each deque at most once, with **O(N)** auxiliary space in the worst case.
