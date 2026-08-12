# Subarrays with K Different Integers (LeetCode 992)

## 1. Problem Statement

Given an integer array `nums` and an integer `k`, return the **number of good subarrays**.

A **good subarray** is a contiguous subarray that contains **exactly `k` distinct integers**.

Return the total number of such subarrays.

### Constraints

* `1 <= nums.length <= 2 * 10^4`
* `1 <= nums[i], k <= nums.length`

Since `n` can be `20,000`, an `O(n²)` solution will not pass.

---

## Example

```text
nums = [1,2,1,2,3]
k = 2

Output = 7
```

Valid subarrays:

```text
[1,2]
[2,1]
[1,2]
[2,3]
[1,2,1]
[2,1,2]
[1,2,1,2]
```

---

# 2. Diagram

```text
nums = [1,2,1,2,3]
        L       R

Current Window

1 2 1 2

Distinct = 2 ✅

All these endings are valid.
```

When adding `3`

```text
1 2 1 2 3

Distinct = 3 ❌

Move left until

Distinct <= 2
```

Sliding window can easily maintain

```text
Distinct <= K
```

But counting

```text
Distinct == K
```

directly is difficult.

---

# 3. Example I/O

### Example 1

Input

```text
nums = [1,2,1,2,3]
k = 2
```

Output

```text
7
```

---

### Example 2 (Edge)

Input

```text
nums = [1,1,1]
k = 1
```

Output

```text
6
```

Subarrays

```text
[1]
[1]
[1]
[1,1]
[1,1]
[1,1,1]
```

Every subarray contains exactly one distinct element.

---

# 4. Intuition & Pattern Recognition

## Observation

The problem asks

> Count subarrays having **exactly K distinct elements**

Exactly is difficult.

At a fixed `right`, there may be many valid left positions.

---

## Key Trick

Instead count

```text
AtMost(K)
```

and

```text
AtMost(K-1)
```

Then

```text
Exactly(K)

=

AtMost(K)

-

AtMost(K-1)
```

---

### Why?

Suppose

```text
Distinct count

0
1
2
3
```

AtMost(2)

contains

```text
0
1
2
```

AtMost(1)

contains

```text
0
1
```

Subtract

↓

Only

```text
2
```

Exactly K remains.

---

## Interview Recognition

Whenever you hear

* Count subarrays
* Exactly K distinct
* Positive/expandable window

Think

> Exactly = AtMost(K) − AtMost(K−1)

This is one of the most common interview tricks.

---

# 5. Simpler Version

## Simpler Problem

### Count subarrays having **at most K distinct numbers**

This is much easier.

Maintain

* Frequency map
* Distinct count

Whenever distinct exceeds K

Shrink window.

Every valid window contributes

```text
right - left + 1
```

---

## Related simpler questions

### 3. Longest Substring Without Repeating Characters

Maintain frequency map.

Window always contains unique characters.

---

### 340. Longest Substring with At Most K Distinct Characters

Maintain

```text
Distinct <= K
```

Almost identical.

---

### Progression

```text
Longest unique substring

↓

Longest at most K distinct

↓

Count at most K distinct

↓

Exactly K distinct

=

AtMost(K)-AtMost(K-1)
```

---

# 6. Brute Force

Generate every subarray.

Maintain a set.

```python
answer = 0

for i in range(n):
    s = set()

    for j in range(i, n):
        s.add(nums[j])

        if len(s) == k:
            answer += 1

        elif len(s) > k:
            break
```

---

### Complexity

Time

```text
O(n²)
```

Space

```text
O(K)
```

---

# 7. Optimal Solution

## Idea

Helper function

```text
countAtMost(k)
```

returns number of subarrays having at most `k` distinct integers.

Answer

```text
countAtMost(k) - countAtMost(k-1)
```

---

### Python

```python
from collections import defaultdict

class Solution:
    def subarraysWithKDistinct(self, nums, k):

        def atMost(k):
            if k < 0:
                return 0

            freq = defaultdict(int)
            left = 0
            count = 0

            for right in range(len(nums)):

                # New distinct element enters the window
                if freq[nums[right]] == 0:
                    k -= 1

                freq[nums[right]] += 1

                # Too many distinct elements
                while k < 0:
                    freq[nums[left]] -= 1

                    # One distinct element removed completely
                    if freq[nums[left]] == 0:
                        k += 1

                    left += 1

                # Every subarray ending at right
                # and starting from left...right is valid
                count += right - left + 1

            return count

        return atMost(k) - atMost(k - 1)
```

---

### Complexity

Time

```text
O(n)
```

Each element enters and leaves the window once.

Space

```text
O(K)
```

Frequency map.

---

# 8. Step-by-Step Trace

Example

```text
nums = [1,2,1]
k = 2
```

Compute

```text
AtMost(2)
```

| Right | Value | Window  | Distinct | Left | New Windows | Count |
| ----- | ----- | ------- | -------- | ---- | ----------- | ----- |
| 0     | 1     | [1]     | 1        | 0    | 1           | 1     |
| 1     | 2     | [1,2]   | 2        | 0    | 2           | 3     |
| 2     | 1     | [1,2,1] | 2        | 0    | 3           | 6     |

```text
AtMost(2)=6
```

Now compute

```text
AtMost(1)
```

| Right | Value | Window     | Distinct | Left | New Windows | Count |
| ----- | ----- | ---------- | -------- | ---- | ----------- | ----- |
| 0     | 1     | [1]        | 1        | 0    | 1           | 1     |
| 1     | 2     | Shrink→[2] | 1        | 1    | 1           | 2     |
| 2     | 1     | Shrink→[1] | 1        | 2    | 1           | 3     |

```text
AtMost(1)=3
```

Final

```text
6 - 3 = 3
```

Exactly three subarrays have exactly two distinct integers.

---

# 9. Related Problems (Increasing Difficulty)

| Problem                                                                 | Connection                                                                                                    |
| ----------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| **3. Longest Substring Without Repeating Characters**                   | Sliding window with a frequency map; maintain a valid window of unique elements.                              |
| **340. Longest Substring with At Most K Distinct Characters (Premium)** | Directly maintains `distinct <= K`; the foundation for this problem.                                          |
| **930. Binary Subarrays With Sum**                                      | Uses the same **Exactly = AtMost(K) − AtMost(K−1)** trick, but with subarray sums instead of distinct counts. |
| **1248. Count Number of Nice Subarrays**                                | Counts subarrays with exactly `K` odd numbers using the same AtMost difference technique.                     |
| **992. Subarrays with K Different Integers**                            | Classic interview problem combining a frequency map with the AtMost trick.                                    |

---

# Interview Cheat Sheet

### Pattern

* Variable Size Sliding Window
* Frequency Map
* Count Subarrays
* **Exactly = AtMost(K) − AtMost(K−1)**

### Recognition Signals

* Count subarrays
* Exactly `K`
* Distinct elements
* Window can expand/shrink while maintaining `≤ K`

### Formula

```text
Exactly(K)
=
AtMost(K)
-
AtMost(K-1)
```

### Sliding Window Rules

* Expand `right`.
* Track frequencies of elements.
* If a new distinct element enters, decrease remaining distinct allowance.
* While distinct elements exceed `K`, move `left`.
* At every `right`, add:

```text
right - left + 1
```

because every starting index from `left` to `right` forms a valid subarray ending at `right`.

### Complexity

* **Time:** `O(n)`
* **Space:** `O(K)` (frequency map)
