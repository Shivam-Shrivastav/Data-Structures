Here's the `.md` formatted solution for **LeetCode: Shortest Unsorted Continuous Subarray**, using:

1. ✅ **Brute Force**
2. ✅ **Optimized Two Pointer Approach** (O(n) time)

---

````markdown
# LeetCode Problem: Shortest Unsorted Continuous Subarray

## Problem Statement

Given an integer array `nums`, return the length of the **shortest continuous subarray** such that if you **sort only this subarray**, the whole array becomes sorted in non-decreasing order.

---

### Example 1:
Input: `nums = [2,6,4,8,10,9,15]`  
Output: `5`  
Explanation: Sorting subarray `[6,4,8,10,9]` results in full array being sorted.

### Example 2:
Input: `nums = [1,2,3,4]`  
Output: `0`

### Example 3:
Input: `nums = [1]`  
Output: `0`

---

## ✅ Brute Force Solution (Compare with Sorted Copy)

### Code:
```python
class Solution:
    def findUnsortedSubarray(self, nums):
        sorted_nums = sorted(nums)
        start, end = 0, len(nums) - 1

        # Find first mismatch from left
        while start < len(nums) and nums[start] == sorted_nums[start]:
            start += 1

        # Find first mismatch from right
        while end > start and nums[end] == sorted_nums[end]:
            end -= 1

        return end - start + 1 if end > start else 0
````

### Explanation:

* Sort a copy of the array.
* Compare original vs sorted from both ends to find mismatch bounds.

### Time Complexity:

* **O(n log n)** — due to sorting

### Space Complexity:

* **O(n)** — for sorted copy

---

### 🔍 Brute Force Significance:

1. Simple and reliable.
2. Doesn't meet the O(n) requirement.

---

## ✅ Optimized Solution: Two Pointer + Min/Max Scan (O(n) Time)

### Code:

```python
class Solution:
    def findUnsortedSubarray(self, nums):
        n = len(nums)
        start, end = -1, -2  # So end - start + 1 == 0 if already sorted
        max_seen, min_seen = nums[0], nums[-1]

        # Left to Right: track max and detect disorder
        for i in range(1, n):
            if nums[i] < max_seen:
                end = i
            else:
                max_seen = nums[i]

        # Right to Left: track min and detect disorder
        for i in range(n - 2, -1, -1):
            if nums[i] > min_seen:
                start = i
            else:
                min_seen = nums[i]

        return end - start + 1
```

### Explanation:

* **First Pass (L → R):** Track `max_seen`; if `nums[i] < max_seen`, `i` might be in the unsorted part.
* **Second Pass (R → L):** Track `min_seen`; if `nums[i] > min_seen`, `i` might be in the unsorted part.
* Final window `[start, end]` is the minimal subarray needing sorting.

### Time Complexity:

* **O(n)**

### Space Complexity:

* **O(1)**

---

### 🔍 Two Pointer Pattern Significance:

1. Uses forward/backward traversal to detect out-of-order elements.
2. Avoids sorting, saving time.
3. Great example of prefix/suffix-based comparison.

