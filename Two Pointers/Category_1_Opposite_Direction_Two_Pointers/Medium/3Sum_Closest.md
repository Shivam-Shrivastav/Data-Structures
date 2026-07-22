# 3Sum Closest (LeetCode 16)

**Pattern:** Sorting + Two Pointers

---

# 1. Problem Statement

Given an integer array `nums` of length `n` and an integer `target`, find **three integers** in the array such that their sum is **closest** to `target`.

Return **the sum** of the three integers.

It is guaranteed that **exactly one solution exists**.

### Constraints

* `3 <= nums.length <= 500`
* `-1000 <= nums[i] <= 1000`
* `-10^4 <= target <= 10^4`
* An **O(N²)** solution is expected.

---

# 2. Diagram

Example:

```text
nums = [-4, -1, 1, 2]
target = 1

Sorted Array

-4   -1    1    2
 ^
 i

        L        R

Current Sum
= -4 + (-1) + 2
= -3

Too small → Move Left →

-------------------------

-4   -1    1    2
 ^
 i
             L    R

Current Sum
= -4 + 1 + 2
= -1

Still small → Move Left

-------------------------

Now

i = -1

-4   -1    1    2
      ^
          L    R

Sum = 2

Difference = |2-1| = 1
```

The closest sum encountered is returned.

---

# 3. Example I/O

### Example 1

```text
Input:
nums = [-1,2,1,-4]
target = 1

Output:
2
```

Explanation

```text
Possible sums

-4 + -1 + 2 = -3
-4 + 1 + 2 = -1
-1 + 1 + 2 = 2  ← Closest

|2-1| = 1
```

---

### Example 2

```text
Input:
nums = [0,0,0]
target = 1

Output:
0
```

Explanation

Only possible sum is 0.

---

### Example 3 (Edge Case)

```text
Input:
nums = [1,1,1]
target = 100

Output:
3
```

Only one possible triplet.

---

# 4. Intuition & Pattern Recognition

### Signals

Whenever you see

* Three numbers
* Sum closest to target
* Return best possible answer
* Constraints around 500

Think:

> **Sort + Two Pointers**

### Why?

After sorting,

* Larger sum → move right pointer left.
* Smaller sum → move left pointer right.

Instead of checking all O(N³) triplets, we intelligently eliminate impossible combinations.

### Interview Thinking

Tell yourself:

```text
This looks like 3Sum.

Instead of searching for an exact target,

I only need the closest one.

Sort the array.

Fix one element.

Use two pointers to approach target.

Whenever current sum is closer,
update the answer.
```

---

# 5. Simpler Version

## Simpler Question 1

### Two Sum II (Sorted Array)

```text
Given a sorted array,
find two numbers equal to target.

Use

Left
Right
```

Introduces opposite-direction pointers.

---

## Simpler Question 2

### 3Sum

Find triplets whose sum equals zero.

```text
Fix one number

Run Two Sum
```

Introduces fixing one element.

---

## Current Question

Instead of checking

```text
sum == target
```

we check

```text
abs(sum - target)
```

and keep the closest answer.

---

### Thinking Progression

```text
Two Sum II

↓

Sort

↓

Two Pointers

↓

Fix one element

↓

3Sum

↓

Instead of exact match

↓

Minimum Difference

↓

3Sum Closest
```

---

# 6. Brute Force

Generate every triplet.

```text
for i

    for j

        for k

            compute sum

            compare difference
```

### Complexity

```text
Time  : O(N³)

Space : O(1)
```

---

# 7. Optimal Solution (Sorting + Two Pointers)

### Idea

1. Sort the array.
2. Fix one number.
3. Use two pointers for the remaining array.
4. Track the closest sum found.
5. Return immediately if exact target is found.

### Python

```python
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        nums.sort()
        n = len(nums)

        closest = nums[0] + nums[1] + nums[2]

        for i in range(n - 2):

            left = i + 1
            right = n - 1

            while left < right:

                curr = nums[i] + nums[left] + nums[right]

                # Update answer if current sum is closer
                if abs(curr - target) < abs(closest - target):
                    closest = curr

                # Exact answer found
                if curr == target:
                    return curr

                # Need a larger sum
                elif curr < target:
                    left += 1

                # Need a smaller sum
                else:
                    right -= 1

        return closest
```

### Complexity

```text
Sorting : O(N log N)

Two Pointer Scan : O(N²)

Overall : O(N²)

Space : O(1)
```

---

# 8. Step-by-Step Trace

Example

```text
nums = [-1,2,1,-4]
target = 1
```

Sorted:

```text
[-4,-1,1,2]
```

Initial

```text
closest = -4 + -1 + 1 = -4
```

| i | Left | Right | Sum | Closest | Action     |
| - | ---- | ----- | --- | ------- | ---------- |
| 0 | -1   | 2     | -3  | -3      | Move Left  |
| 0 | 1    | 2     | -1  | -1      | Move Left  |
| 1 | 1    | 2     | 2   | 2       | Move Right |

Comparison

```text
Target = 1

Difference

|-3-1| = 4

|-1-1| = 2

|2-1| = 1 ← Best
```

Final Answer

```text
2
```

---

# 9. Related Problems

| Problem                                     | Connection                                                                    |
| ------------------------------------------- | ----------------------------------------------------------------------------- |
| **167. Two Sum II - Input Array Is Sorted** | Learn the basic two-pointer technique on a sorted array.                      |
| **15. 3Sum**                                | Exact triplet sum problem using sorting and two pointers.                     |
| **18. 4Sum**                                | Extends the idea by fixing two elements before using two pointers.            |
| **611. Valid Triangle Number**              | Uses sorting and two pointers to count valid triplets.                        |
| **259. 3Sum Smaller** (Premium)             | Counts triplets with sum smaller than a target using the same movement logic. |

---

# Key Interview Takeaways

* **Pattern:** Sorting + Two Pointers.
* **Key Insight:** Fix one element and solve the remaining two-element problem with two pointers.
* **Invariant:** The array is sorted, so pointer movements predictably increase or decrease the sum.
* **Rule:**

  * `sum < target` → move `left` right to increase the sum.
  * `sum > target` → move `right` left to decrease the sum.
  * Update the answer whenever the current sum is closer to the target.
* **Complexity:** **O(N²)** time and **O(1)** extra space (excluding sorting). 
