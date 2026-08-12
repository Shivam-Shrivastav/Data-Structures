# 209. Minimum Size Subarray Sum

**Pattern:** Variable Size Sliding Window

---

# 1. Problem Statement

Given an array of **positive integers** `nums` and an integer `target`, return the **minimum length** of a contiguous subarray whose sum is **greater than or equal to** `target`.

If no such subarray exists, return `0`.

### Constraints

* `1 <= nums.length <= 10^5`
* `1 <= nums[i] <= 10^4` (**Important: All numbers are positive**)
* `1 <= target <= 10^9`
* Expected solution: **O(N)**

---

# 2. Diagram

Example

```text
target = 7

nums = [2,3,1,2,4,3]

L
R
2

sum = 2

----------------------------

L
    R
2 3 1 2

sum = 8  ✔ Valid

Need MINIMUM length

Shrink Left

3 1 2

sum = 6 ❌

Expand Again

3 1 2 4

sum = 10 ✔

Shrink Again...
```

Unlike previous problems, **once the window becomes valid, we immediately try to shrink it** because we want the **smallest** valid window.

---

# 3. Example I/O

### Example 1

```text
Input:
target = 7
nums = [2,3,1,2,4,3]

Output:
2
```

Explanation

```text
Subarray = [4,3]

Length = 2
```

---

### Example 2

```text
Input:
target = 4
nums = [1,4,4]

Output:
1
```

Single element satisfies the target.

---

### Example 3

```text
Input:
target = 11
nums = [1,1,1,1]

Output:
0
```

No valid subarray exists.

---

# 4. Intuition & Pattern Recognition

## How to recognize this pattern

Whenever you see:

* Minimum length
* Contiguous subarray
* Sum condition (`>= target`)
* Positive numbers
* O(N)

Think immediately:

> **Variable Size Sliding Window**

### Why does positivity matter?

Because all numbers are **positive**:

* Expanding the window **always increases** the sum.
* Shrinking the window **always decreases** the sum.

This monotonic behavior makes Sliding Window possible.

If negative numbers were allowed:

```text
Expand

↓

Sum may decrease ❌

Shrink

↓

Sum may increase ❌
```

Sliding Window no longer works.

---

## Interview Thinking

> I don't know the window size.

Expand until the window becomes valid.

```text
Expand Right

↓

sum >= target ?

↓

YES

↓

Update minimum

↓

Shrink Left

↓

Still valid?

↓

Keep shrinking
```

The key difference from LeetCode 3 is:

* **Longest problems:** shrink only until valid.
* **Minimum problems:** once valid, keep shrinking as much as possible.

---

# 5. Simpler Version

## Simpler Question 1

### Maximum Number of Vowels in a Substring of Given Length

Fixed-size window.

Window never changes.

Learns:

* Sliding Window basics

---

## Simpler Question 2

### Longest Substring Without Repeating Characters

Variable window.

```text
Expand

↓

Invalid?

↓

Shrink
```

Learns:

* Dynamic window

---

## Current Question

Now the window validity depends on **sum**, not duplicates.

```text
Expand

↓

sum >= target ?

↓

Shrink

↓

Record minimum
```

---

### Thinking Progression

```text
Fixed Window

↓

Variable Window

↓

Maintain Sum

↓

Shrink While Valid

↓

Minimum Size Subarray Sum
```

---

# 6. Brute Force

Generate every subarray.

Compute its sum.

Return the minimum valid length.

```python
ans = float("inf")

for i in range(len(nums)):
    total = 0

    for j in range(i, len(nums)):
        total += nums[j]

        if total >= target:
            ans = min(ans, j - i + 1)

return 0 if ans == float("inf") else ans
```

### Complexity

```text
Time : O(N²)

Space : O(1)
```

---

# 7. Optimal Solution

```python
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        left = 0
        total = 0
        ans = float("inf")

        for right in range(len(nums)):

            # Expand window
            total += nums[right]

            # Window is valid
            while total >= target:

                # Update minimum length
                ans = min(ans, right - left + 1)

                # Shrink window
                total -= nums[left]
                left += 1

        return 0 if ans == float("inf") else ans
```

---

### Complexity

```text
Time : O(N)

Space : O(1)
```

Each element:

* Added once
* Removed once

Hence total work = **2N = O(N)**

---

# 8. Step-by-Step Trace

Example

```text
target = 7

nums = [2,3,1,2,4,3]
```

| Right | Add | Sum | Valid? | Action          | Left |   Min |
| ----: | --: | --: | ------ | --------------- | ---: | ----: |
|     0 |   2 |   2 | ❌      | Expand          |    0 |     ∞ |
|     1 |   3 |   5 | ❌      | Expand          |    0 |     ∞ |
|     2 |   1 |   6 | ❌      | Expand          |    0 |     ∞ |
|     3 |   2 |   8 | ✔      | Min=4, Remove 2 |    1 |     4 |
|     4 |   4 |  10 | ✔      | Min=4, Remove 3 |    2 |     4 |
|       |     |   7 | ✔      | Min=3, Remove1  |    3 |     3 |
|     5 |   3 |   9 | ✔      | Min=3, Remove2  |    4 |     3 |
|       |     |   7 | ✔      | Min=2, Remove4  |    5 | **2** |

Final Answer

```text
2
```

Subarray

```text
[4,3]
```

---

# 9. Related Problems

| Problem                                                 | Connection                                                                    |
| ------------------------------------------------------- | ----------------------------------------------------------------------------- |
| Maximum Number of Vowels in a Substring of Given Length | Fixed-size sliding window.                                                    |
| Longest Substring Without Repeating Characters          | Variable-size window based on uniqueness.                                     |
| Minimum Window Substring                                | Same expand-then-shrink idea, but with character frequencies instead of sums. |
| Binary Subarrays With Sum                               | Counting subarrays using sliding window/prefix sums.                          |
| Subarray Product Less Than K                            | Same pattern, but maintain a running product instead of a sum.                |

---

# 🎯 Interview Cheat Sheet

## Pattern Recognition

```text
Minimum

+

Contiguous Subarray

+

Positive Numbers

+

Sum Condition

↓

Variable Size Sliding Window
```

---

## Window Invariant

```text
Current window sum = total

Expand until total >= target

Then shrink while still valid.
```

---

## Core Template

```python
left = 0
total = 0

for right in range(len(nums)):

    total += nums[right]

    while total >= target:

        update_answer()

        total -= nums[left]
        left += 1
```

---

## Common Mistakes

* ❌ Using `if` instead of `while` when `total >= target` (you may miss a smaller valid window).
* ❌ Forgetting that this solution **only works because all numbers are positive**.
* ❌ Returning `inf` instead of `0` when no valid subarray exists.

---

# 🧠 Pattern Connection

This problem is one of the most important transitions in Sliding Window:

```text
Maximum Average Subarray I (Fixed Window)
            ↓
Maximum Number of Vowels (Fixed Window)
            ↓
Longest Substring Without Repeating Characters
            ↓
Minimum Size Subarray Sum   ⭐
            ↓
Minimum Window Substring
```

## The Key Insight

Notice the difference in goals:

| Problem Type           | Strategy                                                                 |
| ---------------------- | ------------------------------------------------------------------------ |
| **Maximum / Longest**  | Expand as much as possible; shrink only when invalid.                    |
| **Minimum / Shortest** | Expand until valid; then shrink as much as possible while staying valid. |

This "expand until valid → shrink while valid" template appears repeatedly in advanced sliding window problems such as **Minimum Window Substring**, **Subarray Product Less Than K**, and **Smallest Range Covering Elements from K Lists**.
