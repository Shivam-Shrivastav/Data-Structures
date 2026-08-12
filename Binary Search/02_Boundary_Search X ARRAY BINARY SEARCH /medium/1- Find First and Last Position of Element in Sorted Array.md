# **34. Find First and Last Position of Element in Sorted Array (Binary Search - Lower & Upper Bound)**

---

# 1. Problem Statement

Given a **sorted array** of integers `nums` (possibly containing duplicates) and an integer `target`, return the **starting and ending positions** of `target`.

If the target is not found, return `[-1, -1]`.

Your solution must run in **O(log n)** time.

### Example

```text
nums = [5,7,7,8,8,10]
target = 8

Output:
[3,4]
```

---

## Constraints

* `0 <= nums.length <= 10^5`
* Array is sorted in ascending order.
* `-10^9 <= nums[i], target <= 10^9`
* Required complexity: **O(log n)**

---

# 2. Diagram

```text
nums:

0  1  2  3  4  5
5  7  7  8  8 10
         |-----|
      First    Last
```

Instead of searching for **one occurrence**, we search for:

* Left Boundary (First Occurrence)
* Right Boundary (Last Occurrence)

---

# 3. Example I/O

## Example 1

```text
Input:
nums = [5,7,7,8,8,10]
target = 8

Output:
[3,4]
```

Explanation

```text
5 7 7 8 8 10
      ↑ ↑
```

---

## Example 2

```text
Input:
nums = [5,7,7,8,8,10]
target = 6

Output:
[-1,-1]
```

Target doesn't exist.

---

## Example 3

```text
Input:
nums = []

Output:
[-1,-1]
```

---

## Example 4

```text
Input:
nums = [2,2,2,2]

target = 2

Output:
[0,3]
```

---

# 4. Intuition & Pattern Recognition

This problem is **NOT** asking:

> Find any occurrence.

Instead it asks:

> Find the **leftmost** and **rightmost** occurrence.

That should immediately remind you of:

* First Bad Version
* Lower Bound
* Upper Bound

---

Suppose

```text
1 2 2 2 2 3
```

Searching for 2.

A normal binary search may return

```text
index = 2
```

But we need

```text
first = 1

last = 4
```

Need two boundary searches.

---

### Pattern Recognition

Whenever you hear

* First occurrence
* Last occurrence
* Left boundary
* Right boundary
* Lower bound
* Upper bound

Think

> Binary Search Boundary Problem.

---

# 5. Simpler Version

## Level 1

Binary Search (704)

```text
Find target.
```

↓

## Level 2

Search Insert Position (35)

```text
Find where target should be inserted.
```

↓

## Level 3

First Bad Version (278)

```text
Find first True.
```

↓

## Level 4

Find First Position

Lower Bound

↓

## Level 5

Find Last Position

Upper Bound

↓

Combine both.

---

## Simpler Problems Leading Here

### 704. Binary Search

Find any occurrence.

↓

### 35. Search Insert Position

Find left boundary.

↓

### 278. First Bad Version

Boundary binary search.

↓

### **34. Find First and Last Position**

Run boundary search twice.

---

# 6. Brute Force

Scan entire array.

```python
class Solution:
    def searchRange(self, nums, target):

        first = -1
        last = -1

        for i, num in enumerate(nums):

            if num == target:
                if first == -1:
                    first = i
                last = i

        return [first, last]
```

---

## Complexity

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

## Step 1

Find **left boundary**

If

```text
nums[mid] >= target
```

move left.

Why?

Because

`mid` could still be the first occurrence.

---

## Step 2

Find **right boundary**

If

```text
nums[mid] <= target
```

move right.

Because

`mid` could still be the last occurrence.

---

## Helper Function

```python
def lower_bound(target):
```

returns first index

```text
>= target
```

---

Then

```python
left = lower_bound(target)

right = lower_bound(target + 1) - 1
```

Why?

Because

```text
lower_bound(8)

returns

first 8
```

while

```text
lower_bound(9)

returns

first element > 8
```

Subtract one.

---

## Python Code (Recommended)

```python
class Solution:

    def lower_bound(self, nums, target):

        left = 0
        right = len(nums)

        while left < right:

            mid = (left + right) // 2

            # Target can still be at mid or to the left
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1

        return left

    def searchRange(self, nums, target):

        first = self.lower_bound(nums, target)

        # Target not found
        if first == len(nums) or nums[first] != target:
            return [-1, -1]

        last = self.lower_bound(nums, target + 1) - 1

        return [first, last]
```

---

## Alternative (Two Explicit Binary Searches)

```python
class Solution:
    def searchRange(self, nums, target):

        def findFirst():
            left, right = 0, len(nums) - 1
            ans = -1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    ans = mid
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return ans

        def findLast():
            left, right = 0, len(nums) - 1
            ans = -1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    ans = mid
                    left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return ans

        return [findFirst(), findLast()]
```

---

## Complexity

Time

```text
O(log n)
```

because binary search is executed twice.

Space

```text
O(1)
```

---

# 8. Step-by-Step Trace

Example

```text
nums = [5,7,7,8,8,10]

target = 8
```

### First Boundary

| Left | Right | Mid | nums[mid] | Action  |
| ---- | ----- | --- | --------- | ------- |
| 0    | 6     | 3   | 8         | right=3 |
| 0    | 3     | 1   | 7         | left=2  |
| 2    | 3     | 2   | 7         | left=3  |

Result

```text
first = 3
```

---

### Second Boundary

Search

```text
lower_bound(9)
```

| Left | Right | Mid | nums[mid] | Action  |
| ---- | ----- | --- | --------- | ------- |
| 0    | 6     | 3   | 8         | left=4  |
| 4    | 6     | 5   | 10        | right=5 |
| 4    | 5     | 4   | 8         | left=5  |

Result

```text
lower_bound(9)=5

last = 5-1 = 4
```

Answer

```text
[3,4]
```

---

# 9. Related Problems

1. **704. Binary Search**
   Basic binary search for finding a target.

2. **35. Search Insert Position**
   Finds the insertion point (lower bound), the core building block for this problem.

3. **278. First Bad Version**
   Uses the same left-boundary binary search template to find the first `True`.

4. **540. Single Element in a Sorted Array**
   Another binary search problem that relies on sorted array properties rather than searching for a specific value.

5. **300. Longest Increasing Subsequence**
   Uses `lower_bound` (binary search) repeatedly to maintain the smallest possible tail values.

---

# ⭐ Interview Memory Trick

This problem is simply:

> **Find two boundaries.**

### Left Boundary

```python
if nums[mid] >= target:
    right = mid
else:
    left = mid + 1
```

Finds the first index where `nums[i] >= target`.

---

### Right Boundary

Instead of writing another complex binary search:

```python
last = lower_bound(target + 1) - 1
```

This elegant trick works because:

```text
First 8     → lower_bound(8)
First > 8   → lower_bound(9)

Last 8 = First > 8 - 1
```

This "two lower_bound" approach is concise, reusable, and commonly used in C++ (`std::lower_bound`) and Java (`Arrays.binarySearch` patterns).
