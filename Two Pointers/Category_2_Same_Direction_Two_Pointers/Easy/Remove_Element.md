# Remove Element (LeetCode 27)

**Pattern:** Two Pointers (Overwrite / In-place Array Modification)

---

# 1. Problem Statement

Given an integer array `nums` and an integer `val`, remove **all occurrences** of `val` **in-place**.

Return the number of elements that are **not equal** to `val`.

The first `k` elements of `nums` should contain the remaining elements (order may or may not matter depending on the approach). Anything beyond `k` is ignored.

### Constraints

* `0 <= nums.length <= 100`
* `0 <= nums[i] <= 50`
* `0 <= val <= 100`
* Must modify the array **in-place**.
* Extra space should be **O(1)**.

---

# 2. Diagram

Example

```text
nums = [3,2,2,3]
val = 3

Read Pointer (i)
↓

3  2  2  3
↑
Write Pointer (k)

3 == val
Skip

--------------------------

i↓

3  2  2  3
   ↑
k

2 != val

Write at index k

2  2  2  3
   ↑
   k=1

--------------------------

Next

2 != val

2  2  2  3
      ↑
      k=2

--------------------------

3 == val

Skip

Final valid array:

[2,2]
```

Think of it as:

```text
Read everything

↓

Copy only useful elements

↓

Return count
```

---

# 3. Example I/O

### Example 1

```text
Input:
nums = [3,2,2,3]
val = 3

Output:
2

nums becomes:
[2,2,_,_]
```

Explanation

Only two elements are not equal to 3.

---

### Example 2

```text
Input:
nums = [0,1,2,2,3,0,4,2]
val = 2

Output:
5

nums becomes:
[0,1,3,0,4,_,_,_]
```

---

### Edge Case

```text
Input:
nums = []
val = 1

Output:
0
```

---

# 4. Intuition & Pattern Recognition

### Signals

Whenever you see:

* Remove elements
* Modify array in-place
* O(1) extra space
* Preserve remaining elements

Think:

> **Two Pointers**

One pointer reads every element.

Another pointer writes only the elements we want to keep.

### Interview Thinking

Tell yourself:

```text
I don't actually need to delete elements.

I only need to keep the good ones together.

So,

Scan the array.

Whenever an element is valid,
copy it to the next available position.

The write pointer tells me
where the next valid element goes.
```

---

# 5. Simpler Version

## Simpler Question 1

### Copy all elements of one array into another

```text
for num in nums:
    new.append(num)
```

No filtering.

---

## Simpler Question 2

### Copy only even numbers

```text
for num in nums:
    if num % 2 == 0:
        new.append(num)
```

Introduces filtering.

---

## Current Question

Now,

Instead of another array,

copy back into the **same array**.

```text
Read

↓

If valid

↓

Write into same array

↓

Move write pointer
```

No extra memory.

---

### Thinking Progression

```text
Copy array

↓

Filter elements

↓

Need O(1) space

↓

Overwrite original array

↓

Remove Element
```

---

# 6. Brute Force

Create a new array.

Copy every element except `val`.

Replace original array if needed.

```python
result = []

for num in nums:
    if num != val:
        result.append(num)

return len(result)
```

### Complexity

```text
Time  : O(N)

Space : O(N)
```

Not allowed because the problem requires **O(1)** extra space.

---

# 7. Optimal Solution (Two Pointers)

### Idea

Maintain:

* `i` → reads every element.
* `k` → next position to write a valid element.

Whenever `nums[i] != val`:

* Copy it to `nums[k]`.
* Increment `k`.

At the end, `k` is the answer.

### Python

```python
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        k = 0

        for i in range(len(nums)):

            # Keep only valid elements
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        return k
```

### Complexity

```text
Time  : O(N)

Space : O(1)
```

---

## Alternate Approach (Order Doesn't Matter)

If preserving order isn't required, use two pointers from both ends.

```python
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        left = 0
        right = len(nums)

        while left < right:

            if nums[left] == val:
                nums[left] = nums[right - 1]
                right -= 1
            else:
                left += 1

        return right
```

### Complexity

```text
Time  : O(N)

Space : O(1)
```

Useful when many removals exist because it minimizes writes.

---

# 8. Step-by-Step Trace

Example

```text
nums = [0,1,2,2,3,0,4,2]
val = 2
```

| i | nums[i] | Action | k | Array (valid part) |
| - | ------- | ------ | - | ------------------ |
| 0 | 0       | Write  | 1 | [0]                |
| 1 | 1       | Write  | 2 | [0,1]              |
| 2 | 2       | Skip   | 2 | [0,1]              |
| 3 | 2       | Skip   | 2 | [0,1]              |
| 4 | 3       | Write  | 3 | [0,1,3]            |
| 5 | 0       | Write  | 4 | [0,1,3,0]          |
| 6 | 4       | Write  | 5 | [0,1,3,0,4]        |
| 7 | 2       | Skip   | 5 | [0,1,3,0,4]        |

Final

```text
k = 5

nums = [0,1,3,0,4,_,_,_]
```

Return:

```text
5
```

---

# 9. Related Problems

| Problem                                        | Connection                                                                                        |
| ---------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| **26. Remove Duplicates from Sorted Array**    | Same overwrite technique, but keeps only one copy of each value.                                  |
| **80. Remove Duplicates from Sorted Array II** | Generalizes the overwrite idea to allow at most two occurrences.                                  |
| **283. Move Zeroes**                           | Move selected elements forward while preserving order using the same read/write pointer approach. |
| **905. Sort Array By Parity**                  | Two pointers partition elements based on a condition.                                             |
| **75. Sort Colors**                            | Advanced in-place partitioning using multiple pointers (Dutch National Flag).                     |

---

# Key Interview Takeaways

* **Pattern:** Two Pointers (Read/Write Pointer).
* **Invariant:** Elements before `k` are always the valid elements kept so far.
* **Rule:** Read every element once, write only those that should remain.
* **When to use:** In-place filtering, removing elements, compacting arrays, and moving selected elements while preserving order.
* **Complexity:** **O(N)** time and **O(1)** extra space.

Reference style followed from your sliding window revision notes. 
