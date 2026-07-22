# Move Zeroes (LeetCode 283)

**Pattern:** Two Pointers (Fast & Slow)

---

# 1. Problem Statement

Given an integer array `nums`, **move all `0`s to the end** while maintaining the **relative order of the non-zero elements**.

You **must do this in-place**, meaning you cannot create another array.

### Constraints

* `1 <= nums.length <= 10^4`
* `-2^31 <= nums[i] <= 2^31 - 1`
* Solve in **O(N)** time.
* Extra space should be **O(1)**.

---

# 2. Diagram

Example:

```text
nums = [0,1,0,3,12]

Initial

0   1   0   3   12
S
F

-------------------------

Fast finds non-zero (1)

0   1   0   3   12
S   F

Swap

1   0   0   3   12
    S
    F

-------------------------

Fast continues

1   0   0   3   12
    S       F

Swap

1   3   0   0   12
        S       F

-------------------------

Fast continues

1   3   0   0   12
        S           F

Swap

1   3   12  0   0

Done
```

**Idea:**

* **Fast pointer** scans every element.
* **Slow pointer** points to where the next non-zero should be placed.

---

# 3. Example I/O

### Example 1

```text
Input:
nums = [0,1,0,3,12]

Output:
[1,3,12,0,0]
```

Explanation

```text
All non-zero elements keep their order.

1 → 3 → 12

Zeros move to the end.
```

---

### Example 2

```text
Input:
nums = [0]

Output:
[0]
```

---

### Example 3 (Already Sorted)

```text
Input:
nums = [1,2,3]

Output:
[1,2,3]
```

Nothing changes.

---

### Example 4 (All Zeros)

```text
Input:
nums = [0,0,0]

Output:
[0,0,0]
```

---

# 4. Intuition & Pattern Recognition

### Signals

Whenever you see:

* Move elements
* Preserve relative order
* In-place
* Constant extra space

Think:

> **Two Pointers**

Specifically,

One pointer reads the array.

Another pointer writes the correct position.

### Interview Thinking

Tell yourself:

```text
I only care about non-zero numbers.

Whenever I see one,

place it at the earliest available position.

Everything after that automatically becomes zeros through swapping.
```

---

# 5. Simpler Version

## Simpler Question 1

### Remove Element (LeetCode 27)

Keep only elements that are **not equal** to a target value.

```text
Read pointer

↓

Write valid elements

↓

Return new length
```

---

## Simpler Question 2

### Remove Duplicates from Sorted Array (LeetCode 26)

Keep only unique elements.

Uses the exact same **read/write pointer** idea.

---

## Current Question

Instead of removing values,

we move all non-zero values forward.

```text
Read every number

↓

If non-zero

↓

Swap/write to front

↓

Zeros naturally move back
```

---

### Thinking Progression

```text
Copy valid elements

↓

Write pointer

↓

Read + Write pointers

↓

Swap in-place

↓

Move Zeroes
```

---

# 6. Brute Force

Create another array.

1. Store all non-zero numbers.
2. Count zeros.
3. Append zeros at the end.
4. Copy back.

```python
temp = []

for num in nums:
    if num != 0:
        temp.append(num)

while len(temp) < len(nums):
    temp.append(0)

nums[:] = temp
```

### Complexity

```text
Time  : O(N)

Space : O(N)
```

---

# 7. Optimal Solution (Two Pointers)

### Idea

* `fast` scans every element.
* `slow` points to the next position where a non-zero should go.
* Whenever `nums[fast] != 0`, swap it with `nums[slow]`, then increment `slow`.

### Python

```python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:

        slow = 0

        for fast in range(len(nums)):

            # Found a non-zero element
            if nums[fast] != 0:

                # Place it at the earliest available position
                nums[slow], nums[fast] = nums[fast], nums[slow]

                # Next non-zero should go here
                slow += 1
```

### Complexity

```text
Time  : O(N)

Space : O(1)
```

Every element is visited exactly once.

---

# 8. Step-by-Step Trace

Example

```text
nums = [0,1,0,3,12]
```

| Fast | Slow | Array        | Action      |
| ---- | ---- | ------------ | ----------- |
| 0    | 0    | [0,1,0,3,12] | Zero → Skip |
| 1    | 0    | [1,0,0,3,12] | Swap(1,0)   |
| 2    | 1    | [1,0,0,3,12] | Zero → Skip |
| 3    | 1    | [1,3,0,0,12] | Swap(3,0)   |
| 4    | 2    | [1,3,12,0,0] | Swap(12,0)  |

Final Answer

```text
[1,3,12,0,0]
```

---

# 9. Related Problems

| Problem                                     | Connection                                                           |
| ------------------------------------------- | -------------------------------------------------------------------- |
| **27. Remove Element**                      | Same read/write pointer approach to overwrite unwanted values.       |
| **26. Remove Duplicates from Sorted Array** | Uses slow and fast pointers to keep only unique elements.            |
| **75. Sort Colors**                         | Extends the partitioning idea to three groups using pointers.        |
| **905. Sort Array By Parity**               | Rearranges elements based on a condition using two pointers.         |
| **88. Merge Sorted Array**                  | In-place array modification using pointer manipulation from the end. |

---

# Key Interview Takeaways

* **Pattern:** Two Pointers (Fast & Slow).
* **Invariant:** Elements before `slow` are always the processed non-zero elements in their original order.
* **Rule:** Scan with `fast`; whenever you find a non-zero, place it at `slow` and advance `slow`.
* **Why swapping works:** If `slow == fast`, it's effectively a no-op. Otherwise, the swap moves the non-zero forward and pushes a zero (or already-processed value) backward.
* **Complexity:** **O(N)** time and **O(1)** extra space. 
