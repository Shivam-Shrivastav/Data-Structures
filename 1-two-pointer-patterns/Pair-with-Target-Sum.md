Here’s the solution to **LeetCode: Two Sum** — first using the **brute force** approach, then using the **two pointer** pattern (on a sorted array).

---

````markdown
# LeetCode Problem: Two Sum

## Problem Statement

Given an array of integers `nums` and an integer `target`, return **indices** of the two numbers such that they add up to `target`.

You may assume that each input would have **exactly one solution**, and you **may not use the same element twice**.

Return the answer in **any order**.

---

### Example 1:
Input: `nums = [2,7,11,15]`, target = `9`  
Output: `[0,1]`

---

## ✅ Brute Force Solution

### Code:
```python
def two_sum_brute_force(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
````

### Explanation:

* We loop through all pairs `(i, j)` where `i < j`.
* For each pair, check if `nums[i] + nums[j] == target`.
* If so, return the indices.

### Time Complexity:

* **O(n²)** — Two nested loops over the array.

### Space Complexity:

* **O(1)** — No extra space used.

---

### 🔍 Brute Force Significance:

1. Tries all possible pairs without optimization — good for understanding basic logic.
2. Easy to implement but not scalable for large inputs.

---

## ✅ Optimized Solution using Two Pointers Pattern

⚠️ **Note:** The two pointer approach requires the array to be **sorted**, but the problem needs **original indices**. So we must:

* **Sort** a copy of the array **with indices**
* Use **two pointers** to find the elements
* Map back to original indices

### Code:

```python
def two_sum_two_pointers(nums, target):
    # Keep track of original indices
    indexed_nums = list(enumerate(nums))
    # Sort by value
    indexed_nums.sort(key=lambda x: x[1])

    left = 0
    right = len(nums) - 1

    while left < right:
        current_sum = indexed_nums[left][1] + indexed_nums[right][1]
        if current_sum == target:
            return [indexed_nums[left][0], indexed_nums[right][0]]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
```

### Explanation:

* We pair each element with its index using `enumerate`.
* Sort the list by values.
* Use two pointers: one from start, one from end.
* Move pointers inward depending on whether the sum is smaller or larger than the target.

### Time Complexity:

* **O(n log n)** for sorting
* **O(n)** for two-pointer scan
* **Total: O(n log n)**

### Space Complexity:

* **O(n)** for storing index-value pairs.

---

### 🔍 Two Pointer Pattern Significance:

1. Efficient for sorted arrays where we need to find two elements that meet a condition.
2. Reduces time complexity significantly compared to brute force.

---

✅ Both solutions return correct results, but **use brute force** when constraints are small and **two pointers** (or hashmap) for better performance in larger arrays.

```

Let me know the next problem and which pattern you want next!
```
