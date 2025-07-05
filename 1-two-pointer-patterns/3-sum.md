Here’s the `.md` formatted solution for **LeetCode: 3Sum** using:

1. ✅ **Brute force**
2. ✅ **Two Pointer** pattern (after sorting the array)

---

````markdown
# LeetCode Problem: 3Sum

## Problem Statement

Given an integer array `nums`, return all the triplets `[nums[i], nums[j], nums[k]]` such that:

- `i != j`, `i != k`, and `j != k`
- `nums[i] + nums[j] + nums[k] == 0`
- No duplicate triplets allowed in the result.

---

### Example 1:
Input: `[-1,0,1,2,-1,-4]`  
Output: `[[-1,-1,2], [-1,0,1]]`

---

## ✅ Brute Force Solution

### Code:
```python
class Solution:
    def threeSum(self, nums):
        n = len(nums)
        result = set()  # use set to avoid duplicates

        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        triplet = tuple(sorted([nums[i], nums[j], nums[k]]))
                        result.add(triplet)

        return list(result)
````

### Explanation:

* Try every triplet `(i, j, k)` where `i < j < k`.
* If the sum is 0, sort and store it as a tuple to handle duplicates.
* Convert the set to a list before returning.

### Time Complexity:

* **O(n³)** — Triple nested loops.

### Space Complexity:

* **O(n)** for storing results in a set.

---

### 🔍 Brute Force Significance:

1. Checks all combinations — guarantees correctness.
2. Helps visualize the problem but inefficient on large arrays.

---

## ✅ Optimized Solution using Two Pointer Pattern

### Code:

```python
class Solution:
    def threeSum(self, nums):
        nums.sort()
        result = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # skip duplicates for i

            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    # Skip duplicates for left and right
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

        return result
```

### Explanation:

* Sort the array to use two pointers effectively.
* Fix one number `nums[i]`, and find two numbers using `left` and `right` pointers such that their sum is `-nums[i]`.
* Skip duplicates for all three positions (`i`, `left`, `right`).

### Time Complexity:

* **O(n²)** — One loop + two pointer scan.

### Space Complexity:

* **O(1)** (ignoring output list).

---

### 🔍 Two Pointer Pattern Significance:

1. Efficient for finding triplets or pairs with a target sum in a sorted array.
2. Skipping duplicates ensures correct and minimal result set.

