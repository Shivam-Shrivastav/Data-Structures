# Remove Duplicates from Sorted Array II (LeetCode 80)

**Pattern:** Two Pointers (Fast & Slow)

---

# 1. Problem Statement

Given a **sorted** integer array `nums`, remove duplicates **in-place** such that **each unique element appears at most twice**.

The relative order of the elements must remain the same.

Return the new length `k`, where the first `k` elements contain the final result.

The elements beyond `k` do not matter.

### Constraints

* `1 <= nums.length <= 3 × 10^4`
* `-10^4 <= nums[i] <= 10^4`
* Array is sorted in non-decreasing order.
* Must use **O(1)** extra space.

---

# 2. Diagram

Example:

```text
nums = [1,1,1,2,2,3]

Initial

1  1  1  2  2  3
S
F

-------------------------

First two 1's are allowed

1  1  1  2  2  3
      F
      S

Result:
1  1

-------------------------

Third 1

Compare with nums[slow-2]

nums[0] = 1

Current = 1

Equal

Skip

-------------------------

Current = 2

Compare with nums[0]=1

Different

Write

1  1  2  2  2  3
         S

-------------------------

Current = 2

Compare with nums[1]=1

Different

Write

1  1  2  2

-------------------------

Current = 3

Compare with nums[2]=2

Different

Write

1 1 2 2 3
```

---

# 3. Example I/O

### Example 1

```text
Input:
nums = [1,1,1,2,2,3]

Output:
k = 5

nums = [1,1,2,2,3,_]
```

Explanation

```text
Three 1's become two 1's.

Everything else remains.
```

---

### Example 2

```text
Input:
nums = [0,0,1,1,1,1,2,3,3]

Output:
k = 7

nums = [0,0,1,1,2,3,3,_,_]
```

---

### Example 3 (Edge Case)

```text
Input:
nums = [1]

Output:
1
```

---

### Example 4

```text
Input:
nums = [1,1]

Output:
2
```

---

# 4. Intuition & Pattern Recognition

### Signals

Whenever you see:

* Sorted array
* Remove duplicates
* In-place
* Preserve order

Think:

> **Two Pointers**

Now ask:

How many duplicates are allowed?

Here,

**Maximum = 2**

Instead of checking the previous one,

compare with the element **two positions behind**.

### Interview Thinking

Tell yourself:

```text
Since the array is sorted,

duplicates come together.

The write pointer tells me where to place
the next valid number.

A new number is valid if it is different
from the number written two positions ago.
```

---

# 5. Simpler Version

## Simpler Question 1

### Remove Duplicates from Sorted Array (LeetCode 26)

Keep exactly one copy.

Condition:

```text
current != previous written element
```

---

## Simpler Question 2

### Move Zeroes

Introduces the read/write pointer technique.

---

## Current Question

Instead of allowing only one occurrence,

allow **two occurrences**.

The trick is:

```text
Compare with

nums[slow-2]

instead of

nums[slow-1]
```

---

### Thinking Progression

```text
Move valid elements

↓

Keep one duplicate

↓

Keep two duplicates

↓

Generalize to K duplicates
```

---

# 6. Brute Force

Traverse the array.

Count occurrences of each number.

Copy only the first two occurrences.

```python
temp = []

count = {}

for num in nums:
    count[num] = count.get(num, 0) + 1

    if count[num] <= 2:
        temp.append(num)

nums[:len(temp)] = temp
```

### Complexity

```text
Time  : O(N)

Space : O(N)
```

---

# 7. Optimal Solution (Two Pointers)

### Idea

The first two elements are always valid.

For every remaining element,

compare it with the element **two places behind the write pointer**.

If they are different,

keep it.

Otherwise,

skip it.

### Python

```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        n = len(nums)

        # Arrays of size 0,1,2 are already valid
        if n <= 2:
            return n

        slow = 2

        for fast in range(2, n):

            # If current number is different from the number
            # two places behind, we can safely keep it
            if nums[fast] != nums[slow - 2]:
                nums[slow] = nums[fast]
                slow += 1

        return slow
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
nums = [1,1,1,2,2,3]
```

Initial

```text
slow = 2
```

| Fast | nums[fast] | nums[slow-2] | Action | Array         | Slow |
| ---- | ---------- | ------------ | ------ | ------------- | ---- |
| 2    | 1          | 1            | Skip   | [1,1,1,2,2,3] | 2    |
| 3    | 2          | 1            | Write  | [1,1,2,2,2,3] | 3    |
| 4    | 2          | 1            | Write  | [1,1,2,2,2,3] | 4    |
| 5    | 3          | 2            | Write  | [1,1,2,2,3,3] | 5    |

Final Answer

```text
Length = 5

nums = [1,1,2,2,3]
```

---

# 9. Related Problems

| Problem                                       | Connection                                                                         |
| --------------------------------------------- | ---------------------------------------------------------------------------------- |
| **26. Remove Duplicates from Sorted Array**   | Same problem but only one occurrence is allowed.                                   |
| **27. Remove Element**                        | Uses the same fast/slow pointer overwrite technique.                               |
| **283. Move Zeroes**                          | Another classic read/write pointer problem for in-place modification.              |
| **88. Merge Sorted Array**                    | Uses pointer manipulation for in-place array updates.                              |
| **Generalization: Keep at Most K Duplicates** | Same logic extends by comparing with `nums[slow - K]` instead of `nums[slow - 2]`. |

---

# Key Interview Takeaways

* **Pattern:** Two Pointers (Fast & Slow).
* **Why `slow = 2`?** The first two elements are always valid because up to two duplicates are allowed.
* **Core Trick:** Compare the current element with `nums[slow - 2]`.

  * If they are **equal**, adding the current element would create a third duplicate → **skip**.
  * If they are **different**, it's safe to keep → **write and advance `slow`**.
* **General Rule:** To allow **at most `K` duplicates**, initialize `slow = K` and compare with `nums[slow - K]`.
* **Complexity:** **O(N)** time and **O(1)** extra space.
