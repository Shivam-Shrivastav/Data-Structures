Here’s the `.md` formatted solution for **LeetCode: Subarray Product Less Than K**, using:

1. ✅ **Brute Force**
2. ✅ **Two Pointer / Sliding Window** pattern (optimized O(n) approach)

---

````markdown
# LeetCode Problem: Subarray Product Less Than K

## Problem Statement

Given an array of positive integers `nums` and an integer `k`, return the **number of contiguous subarrays** where the **product** of all the elements is **strictly less than `k`**.

---

### Example 1:
Input: `nums = [10,5,2,6]`, `k = 100`  
Output: `8`

Valid subarrays:
- [10], [5], [2], [6]
- [10,5], [5,2], [2,6], [5,2,6]

---

### Example 2:
Input: `nums = [1,2,3]`, `k = 0`  
Output: `0`

---

## ✅ Brute Force Solution

### Code:
```python
class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        if k <= 1:
            return 0

        count = 0
        n = len(nums)

        for i in range(n):
            product = 1
            for j in range(i, n):
                product *= nums[j]
                if product < k:
                    count += 1
                else:
                    break  # stop early as product will only increase
        return count
````

### Explanation:

* Try every subarray starting at index `i`.
* Multiply elements one by one from `i` to `j`.
* Count the subarray if product `< k`.

### Time Complexity:

* **O(n²)**

### Space Complexity:

* **O(1)**

---

### 🔍 Brute Force Significance:

1. Works well for small inputs, easy to understand.
2. Breaks early to avoid full O(n²), but still not scalable for large arrays.

---

## ✅ Optimized Solution: Two Pointer / Sliding Window (O(n))

### Code:

```python
class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        if k <= 1:
            return 0

        prod = 1
        left = 0
        count = 0

        for right in range(len(nums)):
            prod *= nums[right]

            while prod >= k:
                prod //= nums[left]
                left += 1

            count += right - left + 1

        return count
```

### Explanation:

* Use a **sliding window** `[left, right]`:

  * Multiply the current `nums[right]` into the `prod`.
  * If `prod >= k`, shrink window from the left.
  * For each valid window, all subarrays ending at `right` and starting from `left` to `right` are valid.

    * Add `right - left + 1` to result.

### Time Complexity:

* **O(n)** — each element processed at most twice (once by right, once by left)

### Space Complexity:

* **O(1)**

---

### 🔍 Two Pointer / Sliding Window Significance:

1. Efficient for problems involving **contiguous subarrays** and **range-based conditions**.
2. Avoids redundant recalculations — builds on previous results.
3. Elegant and scalable for large input sizes.

---

## ✅ Edge Case Handling

* If `k <= 1`, then **no product of positive numbers** can be `< k`, so return `0` directly.
