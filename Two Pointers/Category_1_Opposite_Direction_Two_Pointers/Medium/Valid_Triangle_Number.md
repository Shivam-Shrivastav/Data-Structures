# **Valid Triangle Number (LeetCode 611)**

**Pattern:** Sorting + Two Pointers

---

# 1. Problem Statement

You are given an integer array `nums`.

Return the **number of triplets** `(i, j, k)` such that:

* `0 <= i < j < k < n`
* `nums[i]`, `nums[j]`, and `nums[k]` can form a **valid triangle**.

A triangle is valid if the sum of **any two sides is greater than the third side**.

### Constraints

* `1 <= nums.length <= 1000`
* `0 <= nums[i] <= 1000`

Since `N = 1000`, an **O(N²)** solution is expected.

---

# 2. Diagram

Example:

```text
nums = [2,2,3,4]

After Sorting

2   2   3   4
            ↑ k = largest side

i           j
2 + 3 > 4 ✔

Since array is sorted,

Every value between i and j also satisfies.

Count += (j - i)

Move j ←
```

Another iteration:

```text
2   2   3
        ↑ k

i   j

2 + 2 > 3 ✔

Count += 1
```

---

# 3. Example I/O

### Example 1

```text
Input:
nums = [2,2,3,4]

Output:
3
```

Explanation

Valid triangles:

```text
(2,2,3)
(2,3,4)
(2,3,4)
```

Total = **3**

---

### Example 2

```text
Input:
nums = [4,2,3,4]

Output:
4
```

Explanation

Possible triangles:

```text
(2,3,4)
(2,4,4)
(3,4,4)
(2,3,4)   // using the other 4
```

---

### Edge Case

```text
Input:
nums = [1,1,3]

Output:
0
```

Explanation

```text
1 + 1 <= 3

Cannot form triangle.
```

---

# 4. Intuition & Pattern Recognition

## Observation 1

A triangle is valid when

```text
a + b > c
```

where `c` is the largest side.

Normally there are three inequalities:

```text
a+b>c
a+c>b
b+c>a
```

After sorting:

```text
a ≤ b ≤ c
```

The last two are **always true**.

Only check

```text
a + b > c
```

---

## Observation 2

Sorting gives:

```text
2 3 4 5 6
```

Suppose

```text
2 + 5 > 6 ✔
```

Then

```text
3 + 5 > 6 ✔
4 + 5 > 6 ✔
```

Everything between them also works.

Instead of counting one by one,

count all at once.

---

### Interview Thinking

Tell yourself:

```text
Largest side should be fixed.

Then find how many pairs
have sum greater than it.

Sorted array makes this
possible using two pointers.

Whenever nums[left] + nums[right] > nums[k],

every element between left and right
also satisfies.

Count them together.
```

---

# 5. Simpler Version

## Simpler Question 1

### Two Sum II

Find one pair.

```text
Sorted

left
right

Move pointers.
```

---

## Simpler Question 2

### 3Sum

Fix one element.

Use two pointers for remaining two.

---

## Current Question

Again fix one element.

But instead of searching for one answer,

count **all valid pairs**.

---

### Thinking Progression

```text
Two Sum

↓

Sorted + Two Pointers

↓

3Sum

↓

Fix one element

↓

Count all valid pairs

↓

Valid Triangle Number
```

---

# 6. Brute Force

Generate every triplet.

```python
for i
    for j
        for k
            check triangle
```

### Complexity

```text
Time  : O(N³)

Space : O(1)
```

---

# 7. Optimal Solution (Sorting + Two Pointers)

## Idea

Sort array.

For every largest side (`k`):

* `left = 0`
* `right = k-1`

If

```text
nums[left] + nums[right] > nums[k]
```

then

```text
left...
right

All pairs work.
```

Count

```text
right - left
```

Otherwise

```text
Need larger sum

Move left++
```

---

### Python

```python
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:

        nums.sort()
        count = 0
        n = len(nums)

        # Fix the largest side
        for k in range(n - 1, 1, -1):

            left = 0
            right = k - 1

            while left < right:

                # Triangle condition satisfied
                if nums[left] + nums[right] > nums[k]:

                    # Every index between left and right forms a triangle
                    count += right - left

                    # Try another pair
                    right -= 1

                else:
                    # Need a larger sum
                    left += 1

        return count
```

### Complexity

```text
Time  : O(N²)

Space : O(1)
```

Sorting costs **O(N log N)**, but the two-pointer traversal dominates with **O(N²)**.

---

# 8. Step-by-Step Trace

Example

```text
nums = [2,2,3,4]
```

After sorting

```text
[2,2,3,4]
```

---

### k = 3 (largest = 4)

| Left | Right | Sum | Condition | Count |
| ---- | ----- | --- | --------- | ----- |
| 0    | 2     | 5   | 5>4 ✔     | +2    |
| 0    | 1     | 4   | 4>4 ✖     | 2     |

Current answer = **2**

---

### k = 2 (largest = 3)

| Left | Right | Sum | Condition | Count |
| ---- | ----- | --- | --------- | ----- |
| 0    | 1     | 4   | 4>3 ✔     | +1    |

Final answer = **3**

---

### Why add `right - left`?

Current window:

```text
2   2   3   4
L       R   K
```

Since

```text
2 + 3 > 4
```

Then

```text
2 + 3 > 4   ✔
2 + 3 > 4   ✔
```

Both pairs work.

Instead of checking individually,

```text
Count += 2
```

This is the key optimization.

---

# 9. Related Problems

| Problem                         | Connection                                                                         |
| ------------------------------- | ---------------------------------------------------------------------------------- |
| **167. Two Sum II**             | Basic sorted two-pointer movement.                                                 |
| **15. 3Sum**                    | Fix one element and use two pointers on the remaining array.                       |
| **16. 3Sum Closest**            | Similar pointer movement while optimizing a target difference instead of counting. |
| **18. 4Sum**                    | Extension of 3Sum with one extra fixed element.                                    |
| **923. 3Sum With Multiplicity** | Counting triplets with duplicates, requiring careful combinatorics.                |

---

# Key Interview Takeaways

* **Pattern:** Sorting + Two Pointers.
* **Key Observation:** After sorting, only **`a + b > c`** needs to be checked because `c` is the largest side.
* **Optimization:** If `nums[left] + nums[right] > nums[k]`, then **every index from `left` to `right - 1` with `right` also forms a valid triangle**, so add `right - left` in one step.
* **Pointer Rule:**

  * Condition true → `count += right - left`, then `right--`.
  * Condition false → `left++`.
* **Complexity:** `O(N²)` time and `O(1)` extra space.
