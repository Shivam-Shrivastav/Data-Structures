# 4Sum (LeetCode 18)

**Pattern:** Sorting + Two Pointers + Nested Loops

---

# 1. Problem Statement

Given an integer array `nums` and an integer `target`, return **all unique quadruplets** `[nums[a], nums[b], nums[c], nums[d]]` such that:

* `0 <= a < b < c < d < n`
* `nums[a] + nums[b] + nums[c] + nums[d] == target`

The solution must not contain duplicate quadruplets.

### Constraints

* `1 <= nums.length <= 200`
* `-10^9 <= nums[i] <= 10^9`
* `-10^9 <= target <= 10^9`

Since `N = 200`, an **O(N³)** solution is expected.

---

# 2. Diagram

Example:

```text
nums = [1,0,-1,0,-2,2], target = 0

Sort

[-2, -1, 0, 0, 1, 2]

        i
       -2

             j
            -1

                 L        R
                 0        2

Sum = -1

Move L →

[-2,-1,0,0,1,2]
          L     R

Sum = -1

Move L →

[-2,-1,0,0,1,2]
            L   R

Sum = 0 ✓

Quadruplet:
[-2,-1,1,2]

Continue skipping duplicates...
```

The first **two numbers are fixed**, while the remaining two are found using **Two Pointers**.

---

# 3. Example I/O

### Example 1

```text
Input:
nums = [1,0,-1,0,-2,2]
target = 0

Output:
[
 [-2,-1,1,2],
 [-2,0,0,2],
 [-1,0,0,1]
]
```

Explanation

```text
All unique quadruplets summing to 0.
```

---

### Example 2

```text
Input:
nums = [2,2,2,2,2]
target = 8

Output:
[[2,2,2,2]]
```

Duplicates are ignored.

---

### Example 3 (Edge Case)

```text
Input:
nums = [1,2,3]
target = 6

Output:
[]
```

Need at least 4 elements.

---

# 4. Intuition & Pattern Recognition

### Signals

Whenever you see

* Find all pairs/triplets/quadruplets
* Sum equals target
* Return unique combinations

Think:

> **Sort the array first**

Then ask:

How many numbers should I fix?

For:

* 2Sum → Fix 0 → Two pointers
* 3Sum → Fix 1 → Two pointers
* 4Sum → Fix 2 → Two pointers

---

### Interview Thinking

```text
I need four numbers.

Instead of checking all O(N⁴)
combinations,

I'll fix two numbers.

Now I only need to find
two remaining numbers whose
sum equals

target - nums[i] - nums[j]

That's exactly Two Sum on a
sorted array.
```

---

# 5. Simpler Version

## Simpler Question 1

### Two Sum II

Fix nothing.

Just use two pointers.

```text
L →

← R
```

---

## Simpler Question 2

### 3Sum

Fix one element.

Use two pointers for remaining two.

```text
for i

    Two Sum
```

Time = O(N²)

---

## Current Question

Now simply fix **two** numbers.

```text
for i

    for j

        Two Sum
```

Time becomes

```text
O(N³)
```

---

### Thinking Progression

```text
Two Sum

↓

Sorted Two Pointers

↓

3Sum

(Fix one)

↓

4Sum

(Fix two)

↓

K Sum
```

4Sum is the natural extension of 3Sum.

---

# 6. Brute Force

Try every possible quadruplet.

```text
for i
    for j
        for k
            for l
```

Check if the sum equals the target.

Use a set to remove duplicates.

### Complexity

```text
Time  : O(N⁴)

Space : O(number of answers)
```

---

# 7. Optimal Solution

### Idea

1. Sort the array.
2. Fix first number `i`.
3. Fix second number `j`.
4. Use two pointers (`left`, `right`) to find the remaining two numbers.
5. Skip duplicates at every level.

### Python

```python
class Solution:
    def fourSum(self, nums, target):
        nums.sort()
        n = len(nums)
        ans = []

        for i in range(n - 3):

            # Skip duplicate first numbers
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, n - 2):

                # Skip duplicate second numbers
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                left = j + 1
                right = n - 1

                while left < right:

                    total = nums[i] + nums[j] + nums[left] + nums[right]

                    if total == target:

                        ans.append([
                            nums[i],
                            nums[j],
                            nums[left],
                            nums[right]
                        ])

                        left += 1
                        right -= 1

                        # Skip duplicate third numbers
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1

                        # Skip duplicate fourth numbers
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1

                    elif total < target:
                        left += 1

                    else:
                        right -= 1

        return ans
```

### Complexity

```text
Time  : O(N³)

Space : O(1)
```

(Not counting the output list.)

---

# 8. Step-by-Step Trace

Example

```text
nums = [1,0,-1,0,-2,2]
target = 0
```

Sorted:

```text
[-2,-1,0,0,1,2]
```

| i     | j     | Left | Right | Sum | Action          |
| ----- | ----- | ---- | ----- | --- | --------------- |
| 0(-2) | 1(-1) | 2    | 5     | -1  | Left++          |
| 0     | 1     | 3    | 5     | -1  | Left++          |
| 0     | 1     | 4    | 5     | 0   | Add [-2,-1,1,2] |
| 0(-2) | 2(0)  | 3    | 5     | 0   | Add [-2,0,0,2]  |
| 1(-1) | 2(0)  | 3    | 5     | 1   | Right--         |
| 1     | 2     | 3    | 4     | 0   | Add [-1,0,0,1]  |

Answer

```text
[
[-2,-1,1,2],
[-2,0,0,2],
[-1,0,0,1]
]
```

---

# 9. Related Problems

| Problem                                     | Connection                                                                     |
| ------------------------------------------- | ------------------------------------------------------------------------------ |
| **1. Two Sum**                              | Foundation of all K-Sum problems.                                              |
| **167. Two Sum II - Input Array Is Sorted** | Introduces the two-pointer technique on a sorted array.                        |
| **15. 3Sum**                                | Fix one element, solve the remaining two with two pointers.                    |
| **16. 3Sum Closest**                        | Same structure as 3Sum, but optimize for closest sum instead of exact matches. |
| **18. 4Sum II**                             | Different approach using hash maps to combine pair sums in O(N²).              |

---

# Key Interview Takeaways

* **Pattern:** Sorting + Two Pointers.
* **Observation:** 4Sum is simply **3Sum with one extra fixed loop**.
* **Formula:** After fixing two numbers, solve a **Two Sum** problem on the remaining sorted subarray.
* **Duplicates:** Skip duplicates for `i`, `j`, `left`, and `right` to avoid repeated quadruplets.
* **General Rule:**

  * **2Sum** → Fix 0 elements.
  * **3Sum** → Fix 1 element.
  * **4Sum** → Fix 2 elements.
  * **K-Sum** → Fix `K-2` elements, then solve with two pointers.

This follows the same interview progression as **Two Sum → 3Sum → 4Sum**, making it an essential K-Sum pattern to master. 
