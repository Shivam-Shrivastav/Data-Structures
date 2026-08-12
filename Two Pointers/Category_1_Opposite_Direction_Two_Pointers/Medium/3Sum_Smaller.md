# 3Sum Smaller (LeetCode 259 - Premium)

**Pattern:** Sorting + Two Pointers + Counting

---

# 1. Problem Statement

Given an integer array `nums` and an integer `target`, **count the number of index triplets** `(i, j, k)` such that:

* `0 <= i < j < k < n`
* `nums[i] + nums[j] + nums[k] < target`

Return the **total number of valid triplets**.

### Constraints

* `3 <= nums.length <= 3500`
* `-100 <= nums[i] <= 100`
* `-100 <= target <= 100`
* Need better than **O(N³)**.

---

# 2. Diagram

Example

```text
nums = [-2, 0, 1, 3]
target = 2

After Sorting

-2    0    1    3
 ^
 i

      L         R

Sum = -2 + 0 + 3 = 1

1 < 2 ✓

Since array is sorted,

(-2,0,3)
(-2,0,1)

Both are valid.

Count += (R - L)

Move L →
```

Why?

```text
Current

L ------ R

If

nums[i] + nums[L] + nums[R] < target

Then every element

between L+1 ... R

is smaller than nums[R].

Therefore

nums[i] + nums[L] + anything_before_R

will also be < target.
```

This is the key optimization.

---

# 3. Example I/O

### Example 1

```text
Input:
nums = [-2,0,1,3]
target = 2

Output:
2
```

Explanation

```text
Triplets

(-2,0,1) = -1 ✓

(-2,0,3) = 1 ✓

(-2,1,3) = 2 ✗

(0,1,3) = 4 ✗

Answer = 2
```

---

### Example 2

```text
Input:
nums = [3,1,0,-2]
target = 4

Output:
3
```

Explanation

```text
Sorted

[-2,0,1,3]

Triplets

(-2,0,1)
(-2,0,3)
(-2,1,3)
```

---

### Example 3 (Edge Case)

```text
Input:
nums = [5,5,5]
target = 5

Output:
0
```

No valid triplet.

---

# 4. Intuition & Pattern Recognition

### Signals

Whenever you see

* Count triplets
* Sum < target
* Sorted array helps
* Need O(N²)

Think:

> **Sorting + Two Pointers + Counting**

### Key Observation

Suppose

```text
nums[i] + nums[left] + nums[right] < target
```

Since array is sorted,

```text
nums[left+1]

nums[left+2]

...

nums[right-1]

<= nums[right]
```

Therefore

every triplet between

```text
left+1

...

right
```

also works.

Instead of counting one,

count all at once.

### Interview Thinking

```text
This is not asking for one triplet.

It asks for ALL triplets.

Whenever the current sum is valid,

every element before right is also valid.

So instead of moving one-by-one,

count

(right-left)

triplets immediately.
```

---

# 5. Simpler Version

## Simpler Question 1

### Two Sum II

```text
Need one pair.

Move pointers.
```

---

## Simpler Question 2

### 3Sum

```text
Fix first element.

Find exact pair.
```

---

## Simpler Question 3

### 3Sum Closest

```text
Need closest sum.

Move pointers.
```

---

## Current Question

Instead of

```text
Find one answer
```

we need

```text
Count ALL answers
```

When sum is valid,

```text
Count += right-left
```

instead of

```text
Count += 1
```

This is the trick.

---

### Thinking Progression

```text
Two Sum II

↓

Fix first element

↓

3Sum

↓

Pointer Movement

↓

Need Count

↓

If current works

↓

Everything before right works

↓

Count += right-left
```

---

# 6. Brute Force

Generate every triplet.

```text
for i

    for j

        for k

            if sum < target

                count++
```

### Complexity

```text
Time : O(N³)

Space : O(1)
```

---

# 7. Optimal Solution (Sorting + Two Pointers)

### Idea

* Sort the array.
* Fix one element.
* Use two pointers.
* If the sum is less than the target:

  * All elements from `left+1` to `right` also form valid triplets.
  * Add `right - left` to the answer.
  * Move `left`.
* Otherwise move `right`.

### Python

```python
class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:

        nums.sort()
        n = len(nums)
        count = 0

        for i in range(n - 2):

            left = i + 1
            right = n - 1

            while left < right:

                curr = nums[i] + nums[left] + nums[right]

                if curr < target:

                    # Every index between left+1 and right also works
                    count += right - left

                    left += 1

                else:

                    right -= 1

        return count
```

### Complexity

```text
Sorting : O(N log N)

Two Pointer : O(N²)

Overall : O(N²)

Space : O(1)
```

---

# 8. Step-by-Step Trace

Example

```text
nums = [-2,0,1,3]
target = 2
```

Sorted

```text
[-2,0,1,3]
```

| i | Left | Right | Sum | Action              | Count |
| - | ---- | ----- | --- | ------------------- | ----- |
| 0 | 1    | 3     | 1   | Valid → Count +=2   | 2     |
| 0 | 2    | 3     | 2   | Too large → Right-- | 2     |
| 1 | 2    | 3     | 4   | Too large → Right-- | 2     |

Final Answer

```text
2
```

### Why `Count += 2`?

```text
Current

-2   0   1   3
 ^    L       R

Sum = 1

Valid

Triplets

(-2,0,3)

(-2,0,1)

Total =

R-L

= 3-1

= 2
```

No need to check them individually.

---

# 9. Related Problems

| Problem                                     | Connection                                                                      |
| ------------------------------------------- | ------------------------------------------------------------------------------- |
| **167. Two Sum II - Input Array Is Sorted** | Basic two-pointer technique on a sorted array.                                  |
| **15. 3Sum**                                | Finds exact triplets instead of counting.                                       |
| **16. 3Sum Closest**                        | Uses the same pointer movements to minimize the difference from a target.       |
| **18. 4Sum**                                | Extends the idea by fixing two numbers before applying two pointers.            |
| **611. Valid Triangle Number**              | Uses the same `count += right - left` optimization for counting valid triplets. |

---

# Key Interview Takeaways

* **Pattern:** Sorting + Two Pointers + Counting.
* **Key Insight:** When `nums[i] + nums[left] + nums[right] < target`, every index between `left+1` and `right` also forms a valid triplet because the array is sorted.
* **Counting Trick:** Instead of checking each triplet individually, add `right - left` in one step.
* **Pointer Rules:**

  * `sum < target` → `count += (right - left)` and move `left`.
  * `sum >= target` → move `right`.
* **Complexity:** **O(N²)** time and **O(1)** extra space (excluding sorting). 
