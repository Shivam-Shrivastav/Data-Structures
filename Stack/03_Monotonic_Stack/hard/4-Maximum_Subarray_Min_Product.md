# **1856. Maximum Subarray Min-Product**

---

# 1. Problem Statement

You are given an integer array `nums`.

The **min-product** of a subarray is defined as:

```text
(minimum element in subarray) × (sum of all elements in subarray)
```

Return the **maximum min-product** among all non-empty subarrays.

Since the answer can be very large, return it **modulo (10⁹ + 7)**.

> **Important:** Apply the modulo **only after** finding the maximum min-product.

### Example

```text
Input:
nums = [1,2,3,2]

Output:
14
```

Explanation

Subarray:

```text
[2,3,2]

Minimum = 2
Sum = 7

Min-product = 2 × 7 = 14
```

---

### Constraints

* `1 <= nums.length <= 10^5`
* `1 <= nums[i] <= 10^7`

---

# 2. Diagram

The core idea is:

For every element, treat it as the **minimum** of the subarray.

Then find the **largest subarray** where it remains the minimum.

```text
nums = [1,2,3,2]

Index
0 1 2 3

Value
1 2 3 2

Consider value = 2 (index 1)

Previous Smaller = none
Next Smaller = none

Entire valid range

1 2 3 2
  ^^^^^^^

Sum = prefix[right]-prefix[left]

Product = 2 × sum
```

For another `2` (index 3):

```text
Previous Smaller = index0

Next Smaller = none

Valid range

1 2 3 2
    ^^^^^
```

Each element computes **its own best answer**.

---

# 3. Example I/O

### Example 1

```text
Input:
[1,2,3,2]

Output:
14
```

Explanation

```text
Subarray

2 3 2

Minimum =2
Sum =7

Answer =14
```

---

### Example 2

```text
Input:
[2,3,3,1,2]

Output:
18
```

Explanation

```text
Subarray

3 3

Minimum =3
Sum =6

Answer =18
```

---

# 4. Intuition & Pattern Recognition

## Interview Signal

Whenever the problem says

* minimum of subarray
* largest range
* previous smaller
* next smaller
* contribution of each element

Think

> **Monotonic Increasing Stack**

If it also asks for

* sum of subarray

Think

> **Prefix Sum**

---

### Why does it work?

Suppose current element is

```text
nums[i]=5
```

If 5 is the minimum,

then the subarray can extend until the first smaller element.

```text
Smaller   5   Smaller

|---------|
```

That gives the **largest possible sum** while keeping 5 as minimum.

Since

```text
Product = Minimum × Sum
```

Using the widest valid range maximizes the product for that minimum.

---

### Interview Thinking

> Every element wants to become the minimum.

Find

* Left boundary
* Right boundary

using a monotonic stack.

Compute subarray sum instantly using prefix sums.

---

# 5. Simpler Version

## Simplest Problem

Find Previous Smaller Element

```text
5 2 6 3
```

Solved using stack.

---

### Slightly Harder

Largest Rectangle in Histogram

Each bar is treated as the minimum.

Exactly the same thinking.

---

### Current Question

Instead of

```text
Height × Width
```

we compute

```text
Minimum × Subarray Sum
```

Width is replaced by

```text
Prefix Sum
```

---

### Thinking Progression

```text
Previous Smaller
        ↓

Next Smaller
        ↓

Largest Rectangle in Histogram
(height × width)
        ↓

Replace width
with subarray sum
        ↓

Maximum Subarray Min Product
```

---

### Related Simpler Questions

1. **84. Largest Rectangle in Histogram** ⭐⭐⭐⭐⭐ (same boundaries)
2. **907. Sum of Subarray Minimums** (same previous/next smaller logic)
3. **2104. Sum of Subarray Ranges** (next/previous greater & smaller)
4. **560. Subarray Sum Equals K** (prefix sums)

---

# 6. Brute Force

Generate every subarray.

For each

* find minimum
* find sum

Compute product.

```python
for i:
    for j:
        minimum = min(...)
        total = sum(...)
```

### Complexity

Time

```text
O(n²)
```

(or `O(n³)` if min/sum are recomputed each time)

Space

```text
O(1)
```

Too slow for `10⁵`.

---

# 7. Optimal Solution

## Idea

1. Compute prefix sums.
2. Find previous smaller for every index.
3. Find next smaller for every index.
4. Compute

```text
Sum of valid range
×

Current minimum
```

---

## Why Different Comparisons (`>=` vs `>`)

To correctly handle duplicates:

* **Previous Smaller:** pop while `>=`
* **Next Smaller:** pop while `>`

This ensures equal elements are assigned to exactly one side and prevents double-counting or overlapping ranges.

---

## Python Solution

```python
class Solution:
    def maxSumMinProduct(self, nums):
        MOD = 10**9 + 7
        n = len(nums)

        # Prefix sum
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        left = [-1] * n
        stack = []

        # Previous Smaller
        for i in range(n):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()

            left[i] = stack[-1] if stack else -1
            stack.append(i)

        right = [n] * n
        stack = []

        # Next Smaller
        for i in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] > nums[i]:
                stack.pop()

            right[i] = stack[-1] if stack else n
            stack.append(i)

        ans = 0

        for i in range(n):

            total = prefix[right[i]] - prefix[left[i] + 1]

            ans = max(ans, total * nums[i])

        return ans % MOD
```

---

## Time Complexity

```text
O(n)
```

* Prefix sum → `O(n)`
* Previous smaller → `O(n)`
* Next smaller → `O(n)`

---

## Space Complexity

```text
O(n)
```

---

# 8. Step-by-Step Trace

Example

```text
nums = [1,2,3,2]
```

---

## Prefix Sum

```text
Index : 0 1 2 3

Nums  : 1 2 3 2

Prefix

0 1 3 6 8
```

---

## Previous Smaller

| Index | Value | Previous Smaller |
| ----- | ----- | ---------------- |
| 0     | 1     | -1               |
| 1     | 2     | 0                |
| 2     | 3     | 1                |
| 3     | 2     | 0                |

---

## Next Smaller

| Index | Value | Next Smaller |
| ----- | ----- | ------------ |
| 0     | 1     | 4            |
| 1     | 2     | 4            |
| 2     | 3     | 3            |
| 3     | 2     | 4            |

---

## Compute Products

### Index 0

```text
Range

1 2 3 2

Sum =8

1 ×8 =8
```

---

### Index 1

```text
Range

2 3 2

Sum =7

2 ×7 =14
```

Best so far.

---

### Index 2

```text
Range

3

3 ×3 =9
```

---

### Index 3

```text
Range

2 3 2

2 ×7 =14
```

Maximum

```text
14
```

---

# 9. Related Problems

### 1. **84. Largest Rectangle in Histogram** ⭐⭐⭐⭐

Each bar expands until a smaller bar is found. Replace **width** with **subarray sum** to get this problem.

---

### 2. **907. Sum of Subarray Minimums** ⭐⭐⭐⭐

Uses the same previous/next smaller element boundaries, but computes each element's contribution to the total sum.

---

### 3. **2104. Sum of Subarray Ranges** ⭐⭐⭐⭐⭐

Extends the monotonic stack idea by computing both minimum and maximum contributions for every element.

---

### 4. **560. Subarray Sum Equals K** ⭐⭐⭐

Introduces prefix sums, which are used here to compute subarray sums in `O(1)` after boundaries are known.

---

### 5. **85. Maximal Rectangle** ⭐⭐⭐⭐⭐

Another advanced monotonic stack problem built on the **Largest Rectangle in Histogram** technique.

---

# Interview Cheat Sheet

### Pattern

**Monotonic Increasing Stack + Prefix Sum**

### Key Observation

* Treat every element as the **minimum**.
* Expand left and right until a **smaller** element.
* Use prefix sums to get the **sum of the largest valid subarray** in `O(1)`.
* Compute:

```text
min-product = nums[i] × subarray_sum
```

### Duplicate Handling

* Previous Smaller → pop while `>=`
* Next Smaller → pop while `>`

This guarantees each duplicate value owns a unique maximal range.

### Complexity

* **Time:** `O(n)`
* **Space:** `O(n)`

### One-Line Interview Summary

> Find the maximum range where each element is the minimum using a monotonic increasing stack, compute that range's sum with prefix sums, and maximize `minimum × subarray_sum`.
