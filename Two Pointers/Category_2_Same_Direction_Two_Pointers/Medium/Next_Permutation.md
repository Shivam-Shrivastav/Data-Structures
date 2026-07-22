# Next Permutation (LeetCode 31)

**Pattern:** Array Traversal + Greedy + Two Pointers (Reverse Suffix)

---

# 1. Problem Statement

Implement the **next lexicographically greater permutation** of an array of integers.

If such a permutation is not possible (i.e., the array is the largest permutation), rearrange it into the **smallest possible order** (ascending order).

The modification must be **in-place** using **O(1)** extra space.

### Constraints

* `1 <= nums.length <= 100`
* `0 <= nums[i] <= 100`
* Must modify the array in-place.
* Extra space: **O(1)**.

---

# 2. Diagram

Example

```text
nums = [1,2,3,6,5,4]

Step 1: Find Pivot

1 2 3 6 5 4
      ^
     Pivot (3)

Everything after pivot is decreasing.

----------------------------

Step 2: Find next larger element

1 2 3 6 5 4
          ^
          4

Swap

1 2 4 6 5 3

----------------------------

Step 3: Reverse suffix

1 2 4 | 6 5 3

↓

1 2 4 | 3 5 6
```

---

# 3. Example I/O

### Example 1

```text
Input:
nums = [1,2,3]

Output:
[1,3,2]
```

Explanation

Next permutation after `123` is `132`.

---

### Example 2

```text
Input:
nums = [3,2,1]

Output:
[1,2,3]
```

Explanation

Already the largest permutation, so return the smallest.

---

### Example 3

```text
Input:
nums = [1,1,5]

Output:
[1,5,1]
```

---

### Edge Case

```text
Input:
nums = [1]

Output:
[1]
```

---

# 4. Intuition & Pattern Recognition

### Signals

Whenever you see:

* Next greater arrangement
* Lexicographical order
* In-place
* O(1) space

Think:

> **Greedy + Reverse Suffix**

### Key Observation

The **longest decreasing suffix** is already the **largest possible arrangement**.

To get the next permutation:

1. Increase the number **slightly**.
2. Keep the remaining part **as small as possible**.

### Interview Thinking

Tell yourself:

```text
The suffix is already the biggest.

I need to increase the number
at the earliest possible position.

Swap with the next larger value.

Then make everything after it
as small as possible by reversing.
```

---

# 5. Simpler Version

## Simpler Question 1

### Reverse an Array

Reverse a portion of an array using two pointers.

Introduces:

```text
Left++

Right--
```

---

## Simpler Question 2

### Find First Increasing Pair from Right

```text
while nums[i] >= nums[i+1]:
    i--
```

Find where the decreasing suffix begins.

---

## Simpler Question 3

### Find Next Greater Element

From the right,

find the first number larger than the pivot.

---

## Current Question

Combine all three:

```text
Find Pivot

↓

Find Next Larger

↓

Swap

↓

Reverse Remaining Part
```

---

### Thinking Progression

```text
Reverse Array

↓

Find Break Point

↓

Swap with Next Greater

↓

Reverse Suffix

↓

Next Permutation
```

---

# 6. Brute Force

Generate all permutations.

Sort them.

Find the current permutation.

Return the next one.

### Complexity

```text
Time  : O(N! × N)

Space : O(N!)
```

Completely impractical.

---

# 7. Optimal Solution

### Algorithm

### Step 1

Find the first index from the right where

```text
nums[i] < nums[i+1]
```

This is the **pivot**.

---

### Step 2

If pivot exists,

find the first element from the right greater than the pivot.

Swap them.

---

### Step 3

Reverse everything after the pivot.

---

### Why Reverse?

The suffix is already in **descending order**.

Reversing makes it **ascending**, giving the smallest possible suffix.

---

### Python

```python
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:

        n = len(nums)

        # Step 1: Find pivot
        pivot = n - 2
        while pivot >= 0 and nums[pivot] >= nums[pivot + 1]:
            pivot -= 1

        # Step 2: Find next larger element
        if pivot >= 0:
            j = n - 1
            while nums[j] <= nums[pivot]:
                j -= 1

            nums[pivot], nums[j] = nums[j], nums[pivot]

        # Step 3: Reverse suffix
        left = pivot + 1
        right = n - 1

        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
```

### Complexity

```text
Time  : O(N)

Space : O(1)
```

---

# 8. Step-by-Step Trace

Example

```text
nums = [1,2,3,6,5,4]
```

### Step 1

Find pivot

| Index | Value     |
| ----- | --------- |
| 5     | 4         |
| 4     | 5         |
| 3     | 6         |
| 2     | 3 ← Pivot |

Because

```text
3 < 6
```

---

### Step 2

Find first larger element from right

```text
4 > 3

Swap

[1,2,4,6,5,3]
```

---

### Step 3

Reverse suffix

```text
Before

6 5 3

↓

After

3 5 6
```

Final

```text
[1,2,4,3,5,6]
```

---

# 9. Related Problems

| Problem                           | Connection                                                                               |
| --------------------------------- | ---------------------------------------------------------------------------------------- |
| **344. Reverse String**           | Introduces in-place reversal using two pointers.                                         |
| **556. Next Greater Element III** | Applies the exact same next permutation logic to digits of an integer.                   |
| **670. Maximum Swap**             | Greedy swapping to maximize a number; similar idea of choosing the best swap.            |
| **46. Permutations**              | Generates all permutations using backtracking (contrast with finding only the next one). |
| **60. Permutation Sequence**      | Computes the k-th permutation directly using factorial number system.                    |

---

# Key Interview Takeaways

* **Pattern:** Greedy + Two Pointers.
* **Core Insight:** The longest decreasing suffix is already the largest possible arrangement.
* **Algorithm:**

  1. Find the first decreasing element from the right (**pivot**).
  2. Swap it with the smallest element greater than it on the right.
  3. Reverse the suffix to obtain the smallest possible tail.
* **Critical Observation:** The suffix is always in **descending order**, so a simple reversal sorts it in ascending order.
* **Complexity:** **O(N)** time and **O(1)** space.

Reference style followed from your sliding window revision notes. 
