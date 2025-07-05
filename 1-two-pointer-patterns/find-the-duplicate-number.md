Here's the `.md` formatted solution for **LeetCode: Find the Duplicate Number**, using:

1. ✅ **Brute Force**
2. ✅ **Floyd’s Tortoise and Hare (Cycle Detection)** — the **Two Pointer** pattern optimized for this problem.

---

````markdown
# LeetCode Problem: Find the Duplicate Number

## Problem Statement

Given an array of integers `nums` containing `n + 1` integers where each integer is in the range `[1, n]` inclusive.

There is exactly **one duplicated number**, return it.

🚫 Constraints:
- Do **not** modify the input array.
- Use **only constant extra space**.
- Aim for **linear time complexity**.

---

### Example 1:
Input: `[1,3,4,2,2]`  
Output: `2`

### Example 2:
Input: `[3,1,3,4,2]`  
Output: `3`

### Example 3:
Input: `[3,3,3,3,3]`  
Output: `3`

---

## ✅ Brute Force Solution (Invalid for large constraints)

### Code:
```python
class Solution:
    def findDuplicate(self, nums):
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] == nums[j]:
                    return nums[i]
````

### Explanation:

* Compare every pair of elements.
* Return the first match found.

### Time Complexity:

* **O(n²)**

### Space Complexity:

* **O(1)**

### ❗ Not acceptable for large inputs or constraints from the prompt.

---

### 🔍 Brute Force Significance:

1. Naïve but builds initial understanding.
2. Violates performance and constraint requirements for this problem.

---

## ✅ Optimized Solution: Two Pointer Pattern (Floyd’s Cycle Detection)

### Code:

```python
class Solution:
    def findDuplicate(self, nums):
        # Phase 1: Find the intersection point
        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # Phase 2: Find entrance to cycle (duplicate number)
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow
```

### Explanation:

* Treat the array as a **linked list** where `next = nums[i]`.
* There is guaranteed to be a **cycle** due to the pigeonhole principle.
* Use **Floyd’s Tortoise and Hare algorithm** to detect the cycle start — which is the duplicate number.

### Time Complexity:

* **O(n)**

### Space Complexity:

* **O(1)**

---

### 🔍 Two Pointer (Cycle Detection) Significance:

1. Elegant use of pointer logic from cycle detection in linked lists.
2. Meets all constraints: no modification, constant space, linear time.
3. Leverages the mathematical guarantee of a cycle due to duplicate.

---

## ✅ Follow-up: Why must a duplicate exist?

* The array contains `n+1` values in range `[1, n]`.
* Only `n` distinct values possible → at least **one must repeat** (Pigeonhole Principle).

