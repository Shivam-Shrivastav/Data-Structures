# Wiggle Sort (LeetCode 280)

**Pattern:** Sorting / Greedy (Easy)

---

# 1. Problem Statement

Given an integer array `nums`, **rearrange it in-place** so that it satisfies the following condition:

```text
nums[0] <= nums[1] >= nums[2] <= nums[3] >= nums[4] ...
```

This is called a **wiggle sequence**.

You may return **any valid arrangement**.

### Constraints

* `1 <= nums.length <= 5 * 10^4`
* `0 <= nums[i] <= 10^4`
* Rearrange **in-place**.
* Multiple valid answers are allowed.

---

# 2. Diagram

Example:

```text
Input:
[3,5,2,1,6,4]

Goal:

3 <= 5 >= 2 <= 6 >= 1 <= 4

Index:
0   1   2   3   4   5

Pattern:

↓   ↑   ↓   ↑   ↓
<=  >=  <=  >=
```

Think of every adjacent pair:

```text
Even index:
nums[i] <= nums[i+1]

Odd index:
nums[i] >= nums[i+1]
```

---

# 3. Example I/O

### Example 1

```text
Input:
nums = [3,5,2,1,6,4]

Output:
[3,5,1,6,2,4]
```

Explanation

```text
3 <= 5
5 >= 1
1 <= 6
6 >= 2
2 <= 4
```

---

### Example 2

```text
Input:
nums = [1,2,3]

Output:
[1,3,2]
```

or

```text
[1,2,3]
```

Both satisfy the wiggle property.

---

### Edge Case

```text
Input:
nums = [2,2,2,2]

Output:
[2,2,2,2]
```

Equal elements are allowed because the condition uses `<=` and `>=`.

---

# 4. Intuition & Pattern Recognition

### Signals

Whenever you see:

* Rearrange array
* Adjacent relationship
* In-place
* No need for lexicographically smallest answer

Think:

> Can I fix the array **locally**?

Notice that each adjacent pair can be corrected independently.

---

### Interview Thinking

Tell yourself:

```text
At every index I only care about the relation
between nums[i] and nums[i+1].

If the relation is wrong,
swap them.

After swapping,
previous relations remain valid.
```

This is a **Greedy Local Swap** pattern.

---

# 5. Simpler Version

## Simpler Question 1

### Sort an Array

```text
Sort everything.

No alternating condition.
```

---

## Simpler Question 2

### Swap Adjacent Elements

```text
If two neighboring elements are wrong,
swap them.
```

---

## Current Question

Instead of fully sorting,

only ensure

```text
Even index:
small <= large

Odd index:
large >= small
```

Only local fixes are needed.

---

### Thinking Progression

```text
Sorting

↓

Adjacent comparison

↓

Swap if incorrect

↓

Alternate inequalities

↓

Wiggle Sort
```

---

# 6. Brute Force

### Method

Sort the array first.

Then swap every adjacent pair starting from index `1`.

Example:

```text
Sorted:

1 2 3 4 5 6

Swap

2↔3

4↔5

Result

1 3 2 5 4 6
```

### Python

```python
class Solution:
    def wiggleSort(self, nums):

        nums.sort()

        for i in range(1, len(nums)-1, 2):
            nums[i], nums[i+1] = nums[i+1], nums[i]
```

### Complexity

```text
Time  : O(N log N)

Space : O(1)
```

---

# 7. Optimal Solution (Greedy)

### Idea

Traverse once.

For every adjacent pair:

* If index is even, ensure

```text
nums[i] <= nums[i+1]
```

Otherwise ensure

```text
nums[i] >= nums[i+1]
```

If not,

swap.

---

### Why does this work?

Suppose

```text
... a b c
```

When fixing `(b,c)`,

the relation `(a,b)` is already valid.

Swapping `b` and `c` cannot violate the previous condition because of the alternating inequality pattern.

Thus one pass is sufficient.

---

### Python

```python
class Solution:
    def wiggleSort(self, nums):

        for i in range(len(nums)-1):

            # Even index should be <= next
            if i % 2 == 0:

                if nums[i] > nums[i+1]:
                    nums[i], nums[i+1] = nums[i+1], nums[i]

            # Odd index should be >= next
            else:

                if nums[i] < nums[i+1]:
                    nums[i], nums[i+1] = nums[i+1], nums[i]
```

---

### Complexity

```text
Time  : O(N)

Space : O(1)
```

---

# 8. Step-by-Step Trace

Example

```text
nums = [3,5,2,1,6,4]
```

| i | Condition | Action | Array         |
| - | --------- | ------ | ------------- |
| 0 | 3 ≤ 5     | OK     | [3,5,2,1,6,4] |
| 1 | 5 ≥ 2     | OK     | [3,5,2,1,6,4] |
| 2 | 2 ≤ 1     | Swap   | [3,5,1,2,6,4] |
| 3 | 2 ≥ 6     | Swap   | [3,5,1,6,2,4] |
| 4 | 2 ≤ 4     | OK     | [3,5,1,6,2,4] |

Final Answer

```text
[3,5,1,6,2,4]
```

Check:

```text
3 <= 5 ✓

5 >= 1 ✓

1 <= 6 ✓

6 >= 2 ✓

2 <= 4 ✓
```

---

# 9. Related Problems

| Problem                          | Connection                                                                                    |
| -------------------------------- | --------------------------------------------------------------------------------------------- |
| **75. Sort Colors**              | One-pass in-place array rearrangement using local swaps.                                      |
| **905. Sort Array By Parity**    | Rearrange elements in-place based on a condition.                                             |
| **922. Sort Array By Parity II** | Place elements at alternating positions while maintaining a pattern.                          |
| **324. Wiggle Sort II**          | Hard version requiring `nums[0] < nums[1] > nums[2] < ...` with duplicates handled carefully. |
| **31. Next Permutation**         | In-place array transformation based on ordering constraints.                                  |

---

# Key Interview Takeaways

* **Pattern:** Greedy + Local Swaps.
* **Observation:** Only adjacent relationships matter.
* **Invariant:**

  * Even index → `nums[i] <= nums[i+1]`
  * Odd index → `nums[i] >= nums[i+1]`
* **Rule:** Traverse once and swap whenever the current adjacent pair violates the expected relation.
* **Complexity:** **O(N)** time and **O(1)** extra space.

*Reference style based on your sliding-window revision notes.* 
