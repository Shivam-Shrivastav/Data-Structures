# **162. Peak Index in a Mountain Array**

---

# 1. Problem Statement

A **peak element** is an element that is **strictly greater than its adjacent neighbors**.

Given a **0-indexed** integer array `nums`, return the **index of any peak element**.

If the array contains multiple peaks, you may return the index of **any** of them.

Assume:

* `nums[-1] = -∞`
* `nums[n] = -∞`

This means the first or last element can also be a peak.

Your algorithm must run in **O(log n)** time.

### Example

```text
nums = [1,2,3,1]

Output = 2

Because

3 > 2
3 > 1
```

---

## Constraints

* `1 <= nums.length <= 1000`
* `-2^31 <= nums[i] <= 2^31-1`
* `nums[i] != nums[i+1]`
* Required Time Complexity: **O(log n)**

---

# 2. Diagram

Example 1

```text
nums

1   2   3   1
        ▲
      Peak
```

Example 2

```text
nums

1   3   2   5   4

    ▲       ▲

Both are valid answers.
```

Think of every element as one of three possibilities.

```text
Left Neighbor Greater

5  3  1
   ↑
```

```text
Right Neighbor Greater

1  3  5
   ↑
```

```text
Current is Peak

2  8  3
   ↑
```

---

# 3. Example I/O

### Example 1

```text
Input:
nums = [1,2,3,1]

Output:
2
```

Explanation

```text
3 > 2

3 > 1
```

---

### Example 2

```text
Input:
nums = [1,2,1,3,5,6,4]

Output:
1 or 5
```

Both indices are valid.

---

### Example 3

```text
Input:
nums = [1]

Output:
0
```

Single element is always a peak.

---

# 4. Intuition & Pattern Recognition

Unlike Binary Search (704),

we are **not searching for a target value**.

We are searching for an index satisfying

```text
nums[i] > nums[i-1]

AND

nums[i] > nums[i+1]
```

Checking every element takes O(n).

Can we eliminate half the array?

Yes.

---

## Observation

Suppose

```text
5 4 3 2
  ↑
```

The **left neighbor is greater**.

That means a peak **must exist** somewhere on the left.

Why?

Because if we keep moving left,

either

* numbers keep increasing until the boundary

or

* we eventually reach a peak.

So we safely ignore the right half.

---

Similarly,

```text
2 4 5
  ↑
```

The **right neighbor is greater**.

A peak must exist on the right.

Discard the left half.

---

If neither neighbor is greater,

```text
2 8 3
  ↑
```

Current element itself is the peak.

Return immediately.

---

### Interview Thought Process

> "I'll compare the current element with its neighbors. If the left neighbor is larger, the peak must be on the left. If the right neighbor is larger, the peak must be on the right. Otherwise, I've found a peak."

This directly follows the definition of a peak, making it easy to explain.

---

# 5. Simpler Version

## Level 1

Find maximum element.

```text
1 4 2 6 5
```

Scan everything.

O(n).

↓

## Level 2

Realize we don't need the maximum.

We only need **one local maximum**.

↓

## Level 3

Use Binary Search.

Compare with neighbors.

Discard half of the array.

---

## Simpler Problems Leading Here

### 704. Binary Search

Learn binary search.

↓

### 69. Sqrt(x)

Binary search over answers.

↓

### 153. Find Minimum in Rotated Sorted Array

Binary search using local ordering.

↓

### 162. Find Peak Element

Binary search using neighboring elements.

---

# 6. Brute Force

Simply check every element.

```python
class Solution:
    def findPeakElement(self, nums):

        n = len(nums)

        for i in range(n):

            left = float("-inf") if i == 0 else nums[i - 1]
            right = float("-inf") if i == n - 1 else nums[i + 1]

            if nums[i] > left and nums[i] > right:
                return i
```

### Complexity

Time

```text
O(n)
```

Space

```text
O(1)
```

---

# 7. Optimal Solution

## Idea

At every midpoint, ask three questions.

### Case 1

```text
Left Neighbor Greater

5 3 1
  ↑
```

Peak must be on the left.

```python
right = mid - 1
```

---

### Case 2

```text
Right Neighbor Greater

1 3 5
  ↑
```

Peak must be on the right.

```python
left = mid + 1
```

---

### Case 3

```text
2 8 3
  ↑
```

Neither neighbor is larger.

Current element is already a peak.

Return it.

---

## Python Code (Easy to Understand)

```python
class Solution:
    def findPeakElement(self, nums):

        left, right = 0, len(nums) - 1

        while left <= right:

            mid = left + (right - left) // 2

            # Left neighbor is greater,
            # so peak lies on the left.
            if mid > 0 and nums[mid] < nums[mid - 1]:
                right = mid - 1

            # Right neighbor is greater,
            # so peak lies on the right.
            elif mid < len(nums) - 1 and nums[mid] < nums[mid + 1]:
                left = mid + 1

            # Current element is greater than both neighbors.
            else:
                return mid
```

---

## Why does this work?

Suppose

```text
9 7 5
  ↑
```

Since

```text
nums[mid] < nums[mid-1]
```

there must be a peak on the left.

---

Suppose

```text
2 4 6
  ↑
```

Since

```text
nums[mid] < nums[mid+1]
```

there must be a peak on the right.

---

Suppose

```text
2 8 3
  ↑
```

Current element is already greater than both neighbors.

Return it.

---

## Complexity

Time

```text
O(log n)
```

Space

```text
O(1)
```

---

# 8. Step-by-Step Trace

Example

```text
nums = [1,2,3,1]
```

| Left | Right | Mid | nums[mid] | Decision                                |
| ---- | ----- | --- | --------- | --------------------------------------- |
| 0    | 3     | 1   | 2         | Right neighbor (3) is larger → left = 2 |
| 2    | 3     | 2   | 3         | Neither neighbor larger → Return 2      |

Answer

```text
Index = 2
```

---

Another Example

```text
nums = [1,2,1,3,5,6,4]
```

| Left | Right | Mid | nums[mid] | Decision                                |
| ---- | ----- | --- | --------- | --------------------------------------- |
| 0    | 6     | 3   | 3         | Right neighbor (5) is larger → left = 4 |
| 4    | 6     | 5   | 6         | Neither neighbor larger → Return 5      |

Answer

```text
Index = 5
```

---

# 9. Related Problems

1. **704. Binary Search**
   Learn the standard binary search template.

2. **153. Find Minimum in Rotated Sorted Array**
   Uses binary search by analyzing local ordering instead of searching for a target.

3. **852. Peak Index in a Mountain Array**
   Easier version where there is exactly one peak.

4. **1095. Find in Mountain Array**
   First locate the peak, then perform binary search on both sides.

5. **1901. Find a Peak Element II**
   Extends the peak-finding idea to a 2D matrix.

---

# ⭐ Interview Memory Trick

Think only about the **neighbors**.

```text
Left Neighbor Greater?

YES → Search Left
```

```python
right = mid - 1
```

---

```text
Right Neighbor Greater?

YES → Search Right
```

```python
left = mid + 1
```

---

```text
Neither Neighbor Greater?
```

Current element is already a peak.

```python
return mid
```

### One-Line Rule

```text
Left bigger  → Go Left

Right bigger → Go Right

Neither bigger → Found Peak
```

This approach closely mirrors the problem's definition of a peak, making it one of the easiest solutions to derive and explain in an interview.
