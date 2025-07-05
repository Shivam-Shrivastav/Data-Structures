Here’s the `.md` formatted solution for **LeetCode: Squares of a Sorted Array**, using:

1. ✅ **Brute Force**
2. ✅ **Two Pointer Pattern** (O(n) optimized approach)

---

````markdown
# LeetCode Problem: Squares of a Sorted Array

## Problem Statement

Given an integer array `nums` **sorted in non-decreasing order**, return an array of the **squares of each number**, also sorted in non-decreasing order.

---

### Example 1:
Input: `[-4,-1,0,3,10]`  
Output: `[0,1,9,16,100]`

### Example 2:
Input: `[-7,-3,2,3,11]`  
Output: `[4,9,9,49,121]`

---

## ✅ Brute Force Solution (Square then Sort)

### Code:
```python
class Solution:
    def sortedSquares(self, nums):
        squared = [x * x for x in nums]
        squared.sort()
        return squared
````

### Explanation:

* Square each element.
* Sort the squared values.

### Time Complexity:

* **O(n log n)** due to sorting.

### Space Complexity:

* **O(n)** for the new array.

---

### 🔍 Brute Force Significance:

1. Easy to implement and understand.
2. Doesn't leverage the fact that the original array is already sorted.

---

## ✅ Optimized Solution: Two Pointer Approach (O(n) Time)

### Code:

```python
class Solution:
    def sortedSquares(self, nums):
        n = len(nums)
        result = [0] * n
        left, right = 0, n - 1
        pos = n - 1

        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                result[pos] = nums[left] ** 2
                left += 1
            else:
                result[pos] = nums[right] ** 2
                right -= 1
            pos -= 1

        return result
```

### Explanation:

* The array is sorted, but negative numbers can cause large squares on the left.
* Use **two pointers** (`left` and `right`).
* Compare absolute values at both ends:

  * Place the **larger square** at the **end** of the result array (`pos`), and move the corresponding pointer inward.
* Decrease `pos` after each placement.

### Time Complexity:

* **O(n)** — each element is processed once.

### Space Complexity:

* **O(n)** — result array.

---

### 🔍 Two Pointer Pattern Significance:

1. Efficiently leverages the input being **already sorted**.
2. Avoids the overhead of sorting — **linear time** solution.
3. Common technique when working with **sorted arrays from both ends** (especially when dealing with absolute values).

---

## ✅ Follow-Up Answer

> Can we do better than sorting squared values?

Yes — with the **two-pointer technique**, we achieve **O(n)** time without sorting, which is the optimal solution given the sorted nature of the original array.

```

Let me know the next question and the pattern you'd like me to use!
```
