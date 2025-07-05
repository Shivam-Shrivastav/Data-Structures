Here’s the `.md` formatted solution for **LeetCode: 4Sum**, using:

1. ✅ **Brute Force** (check all quadruplets)
2. ✅ **Optimized Two Pointer** (after sorting, similar to 2Sum/3Sum)

---

````markdown
# LeetCode Problem: 4Sum

## Problem Statement

Given an array `nums` of `n` integers, return all unique quadruplets `[nums[a], nums[b], nums[c], nums[d]]` such that:

- `a`, `b`, `c`, `d` are distinct indices
- `nums[a] + nums[b] + nums[c] + nums[d] == target`
- Return answer in any order (no duplicates).

---

### Example 1:
Input: `nums = [1,0,-1,0,-2,2]`, target = `0`  
Output: `[[-2,-1,1,2], [-2,0,0,2], [-1,0,0,1]]`

### Example 2:
Input: `nums = [2,2,2,2,2]`, target = `8`  
Output: `[[2,2,2,2]]`

---

## ✅ Brute Force Solution

### Code:
```python
from itertools import combinations

class Solution:
    def fourSum(self, nums, target):
        result = set()
        n = len(nums)

        for a in range(n):
            for b in range(a+1, n):
                for c in range(b+1, n):
                    for d in range(c+1, n):
                        if nums[a] + nums[b] + nums[c] + nums[d] == target:
                            quad = tuple(sorted([nums[a], nums[b], nums[c], nums[d]]))
                            result.add(quad)

        return list(result)
````

### Explanation:

* Check all combinations of 4 elements.
* Sort and store in a set to avoid duplicates.

### Time Complexity:

* **O(n⁴)**

### Space Complexity:

* **O(n)** for storing result

---

### 🔍 Brute Force Significance:

1. Guarantees correctness but not efficient.
2. Useful for understanding the problem and testing logic.

---

## ✅ Optimized Solution: Two Pointer (Sorting + Nested Loops)

### Code:

```python
class Solution:
    def fourSum(self, nums, target):
        nums.sort()
        n = len(nums)
        result = []

        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # Skip duplicates for i

            for j in range(i + 1, n):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue  # Skip duplicates for j

                left, right = j + 1, n - 1

                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]

                    if total == target:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1

                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1

                    elif total < target:
                        left += 1
                    else:
                        right -= 1

        return result
```

### Explanation:

* Sort the array to easily skip duplicates and apply the two-pointer technique.
* Fix two numbers with outer loops (`i`, `j`).
* Use `left` and `right` pointers for remaining two numbers.
* Adjust pointers based on sum comparison with target.
* Skip duplicates at every level.

### Time Complexity:

* **O(n³)** — due to 2 nested loops + 2-pointer traversal

### Space Complexity:

* **O(1)** extra (output list not counted)

---

### 🔍 Two Pointer Pattern Significance:

1. Great for k-sum type problems on **sorted arrays**.
2. Reduces brute-force complexity by smart traversal.
3. Handles duplicates efficiently using pointer adjustments.

---

## ✅ Final Notes:

* Sorting is critical to avoid duplicate quadruplets.
* This approach can be generalized to **k-Sum** using recursion.

```

Let me know the next problem and the pattern you'd like me to use!
```
