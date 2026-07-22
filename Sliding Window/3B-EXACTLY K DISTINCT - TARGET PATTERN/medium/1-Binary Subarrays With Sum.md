# Binary Subarrays With Sum (LeetCode 930)

## 1. Problem Statement

You are given a **binary array** `nums` (contains only `0` and `1`) and an integer `goal`.

Return the **number of non-empty subarrays** whose sum equals `goal`.

A **subarray** is a contiguous part of the array.

### Constraints

* `1 <= nums.length <= 3 * 10^4`
* `nums[i]` is either `0` or `1`
* `0 <= goal <= nums.length`

These constraints rule out an `O(n²)` solution.

---

## Example

```
nums = [1,0,1,0,1]
goal = 2

Output: 4
```

Subarrays are:

```
[1,0,1]
[1,0,1,0]
[0,1,0,1]
[1,0,1]
```

---

# 2. Diagram

```
nums = [1,0,1,0,1]
         L       R

Current Window

1 + 0 + 1 = 2 ✔

Expand

1 + 0 + 1 + 0 = 2 ✔

Expand

1 + 0 + 1 + 0 + 1 = 3 ❌
Shrink left until <= goal
```

But...

Unlike "at most K distinct", when sum becomes exactly goal there may be **multiple valid left positions because of leading zeros**.

Example:

```
1 0 1

goal = 2

Both

[1 0 1]
  [0 1]

No!

Actually only first.

But

1 0 0 1

goal = 2

Valid:

1 0 0 1
  0 0 1

Leading zeros create multiple windows.
```

Counting them directly is difficult.

---

# 3. Example I/O

### Example 1

Input

```
nums = [1,0,1,0,1]
goal = 2
```

Output

```
4
```

Explanation

```
Four subarrays have sum exactly 2.
```

---

### Example 2 (Edge)

Input

```
nums = [0,0,0]
goal = 0
```

Output

```
6
```

Subarrays

```
[0]
[0]
[0]
[0,0]
[0,0]
[0,0,0]
```

This edge case makes direct sliding window difficult.

---

# 4. Intuition & Pattern Recognition

## First observation

They ask

> Count subarrays

Whenever you see

* count subarrays
* positive numbers
* sum constraint

Think

> Can I count **At Most** instead?

---

## Why exactly is difficult?

Suppose

```
1 0 1 0
```

When sum == goal

There can be many left boundaries.

Sliding window cannot count all easily.

---

## Key Trick

Instead compute

```
AtMost(goal)
```

This counts

```
sum <= goal
```

Then compute

```
AtMost(goal-1)
```

This counts

```
sum <= goal-1
```

Subtract.

```
Exactly(goal)

=

AtMost(goal)

-

AtMost(goal-1)
```

---

### Why?

Imagine

```
All subarrays

0
1
2
3
4
...
```

```
<= goal

contains

0
1
2
```

```
<= goal-1

contains

0
1
```

Subtract

↓

Only

```
2
```

Exactly goal remains.

---

## Interview Recognition

When you hear

* Binary array
* Positive numbers
* Count subarrays
* Exact sum

Immediately think

> Exact = AtMost(K) − AtMost(K−1)

This trick appears in many problems.

---

# 5. Simpler Version

## Simpler Problem

### Count subarrays whose sum ≤ K

This is easy.

Because binary numbers are non-negative.

If sum exceeds K

Move left.

Every valid window contributes

```
window length
```

---

### LeetCode relation

### 209. Minimum Size Subarray Sum

Uses

```
sum >= target
```

Sliding window.

---

### Binary Subarrays With Sum

New idea

Instead of

```
exact
```

convert into

```
at most
```

---

Thinking progression

```
Minimum window

↓

Count windows

↓

Count windows ≤ K

↓

Exactly K

=

AtMost(K)-AtMost(K-1)
```

---

# 6. Brute Force

Generate every subarray.

```
for i

    sum=0

    for j

        sum+=nums[j]

        if sum==goal

            answer++
```

---

### Complexity

Time

```
O(n²)
```

Space

```
O(1)
```

---

# 7. Optimal Solution

## Helper

```
Count subarrays having sum <= goal
```

If goal becomes negative

```
return 0
```

because impossible.

### Python

```python
class Solution:
    def numSubarraysWithSum(self, nums, goal):

        def atMost(goal):
            if goal < 0:
                return 0

            left = 0
            currSum = 0
            count = 0

            for right in range(len(nums)):

                currSum += nums[right]

                # Maintain window sum <= goal
                while currSum > goal:
                    currSum -= nums[left]
                    left += 1

                # Every subarray ending at right and starting
                # between left and right is valid
                count += right - left + 1

            return count

        return atMost(goal) - atMost(goal - 1)
```

---

### Complexity

Time

```
O(n)
```

Each index enters and leaves the window once.

Space

```
O(1)
```

---

# 8. Step-by-Step Trace

Example

```
nums = [1,0,1]
goal = 2
```

We compute

```
AtMost(2)
```

| Right | Value | Window Sum | Left | New Valid Windows | Count |
| ----- | ----- | ---------- | ---- | ----------------- | ----- |
| 0     | 1     | 1          | 0    | 1                 | 1     |
| 1     | 0     | 1          | 0    | 2                 | 3     |
| 2     | 1     | 2          | 0    | 3                 | 6     |

```
AtMost(2)=6
```

Now

```
AtMost(1)
```

| Right | Value | Window Sum | Left   | New Valid | Count |
| ----- | ----- | ---------- | ------ | --------- | ----- |
| 0     | 1     | 1          | 0      | 1         | 1     |
| 1     | 0     | 1          | 0      | 2         | 3     |
| 2     | 1     | 2          | Shrink | 1         | 4     |

```
AtMost(1)=4
```

Final

```
6-4 = 2
```

Exactly two subarrays have sum 2.

---

# 9. Related Problems

| Problem                                      | Connection                                                                           |
| -------------------------------------------- | ------------------------------------------------------------------------------------ |
| **209. Minimum Size Subarray Sum**           | Basic positive-number sliding window.                                                |
| **713. Subarray Product Less Than K**        | Uses the same "count all windows ending at right" idea.                              |
| **992. Subarrays with K Different Integers** | Uses **Exactly K = AtMost(K) − AtMost(K−1)** with distinct elements instead of sums. |
| **1248. Count Number of Nice Subarrays**     | Same exact trick, where "odd numbers" replace `1`s.                                  |
| **930. Binary Subarrays With Sum**           | Canonical problem for the AtMost difference technique.                               |

---

# Interview Cheat Sheet

### Pattern

* Variable-size Sliding Window
* Count Subarrays
* **Exactly = AtMost(K) − AtMost(K−1)**

### Recognition

* Binary/non-negative array
* Count subarrays
* Exact target
* Sliding window works for "≤ K"

### Formula

```
Exactly(K)
=
AtMost(K)
-
AtMost(K-1)
```

### Sliding Window Rule

* Expand `right`.
* While `sum > K`, move `left`.
* At each `right`, add:

  ```
  right - left + 1
  ```

  because every starting index from `left` to `right` forms a valid subarray ending at `right`.

### Complexity

* **Time:** `O(n)`
* **Space:** `O(1)`
