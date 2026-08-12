# **154. Find Minimum in Rotated Sorted Array II (Binary Search with Duplicates)**

---

# 1. Problem Statement

You are given an array that was originally sorted in ascending order and then rotated at some pivot. **Unlike the previous problem, the array may contain duplicate values.**

Return the **minimum element**.

The goal is to use binary search as much as possible, although **duplicates may force the algorithm to degrade to O(n)** in the worst case.

### Example

```text
Original:
[0,1,2,4,5,6,7]

Rotated:
[4,5,6,7,0,1,2]

Now with duplicates:

[4,5,5,6,7,0,1,2,2]
```

Minimum = **0**

---

## Constraints

* `1 <= nums.length <= 5000`
* `-5000 <= nums[i] <= 5000`
* Array may contain duplicates.

---

# 2. Diagram

Example:

```text
nums = [2,2,2,0,1,2]

             Pivot
               ↓

2   2   2   0   1   2
-----------------------
```

Now notice:

```text
nums[mid] == nums[right]
```

We **cannot determine** which side contains the minimum.

That is the only difference from Problem 153.

---

# 3. Example I/O

## Example 1

```text
Input:
nums = [2,2,2,0,1]

Output:
0
```

Explanation

```text
2 2 2 | 0 1
```

---

## Example 2

```text
Input:
nums = [1,3,5]

Output:
1
```

Already sorted.

---

## Example 3 (Important)

```text
Input:
nums = [1,1,1,1,0,1]
```

Output

```text
0
```

---

## Example 4 (Worst Case)

```text
Input:
[1,1,1,1,1]
```

Output

```text
1
```

Binary search cannot eliminate half.

---

# 4. Intuition & Pattern Recognition

## First Thought

This is **exactly Problem 153...**

until duplicates appear.

---

In Problem 153 we relied on

```text
nums[mid] > nums[right]
```

or

```text
nums[mid] < nums[right]
```

to decide the side.

---

But now suppose

```text
nums = [2,2,2,0,2]
```

```text
left              right
 ↓                  ↓

2 2 2 0 2
    ↑
   mid
```

Here

```text
nums[mid] == nums[right]
```

Both are **2**.

Question:

Is minimum on left?

Or right?

Impossible to know.

---

## What do we do?

Simply discard one duplicate.

```text
right -= 1
```

Why is this safe?

Because

```text
nums[mid] == nums[right]
```

Removing one copy of that value **cannot remove the unique minimum** if it exists elsewhere. If that value itself is the minimum, another identical copy still exists at `mid`.

---

### Interview Recognition

If you already solved Problem 153 and the interviewer says:

> "Now duplicates are allowed."

Immediately think:

> "My binary search breaks only when `nums[mid] == nums[right]`. In that case, I'll shrink the search space by one."

---

# 5. Simpler Version

## Level 1

Find minimum in sorted array

```text
[1,2,3,4]

Answer = first element
```

↓

## Level 2

Find minimum in rotated array (unique)

LeetCode 153

Key observation:

```text
Compare mid with right.
```

↓

## Level 3

Duplicates appear

```text
2 2 2 0 2
```

Comparison becomes ambiguous.

Need an extra case.

---

## Simpler Questions Leading Here

### 704. Binary Search

Learn binary search basics.

↓

### 69. Sqrt(x)

Binary search over answer space.

↓

### 153. Find Minimum in Rotated Sorted Array

Learn how to identify the pivot using `nums[mid]` vs `nums[right]`.

↓

### **154. Find Minimum in Rotated Sorted Array II**

Handle the ambiguity caused by duplicates by shrinking the search window.

---

# 6. Brute Force

Simply scan the array.

```python
class Solution:
    def findMin(self, nums):
        ans = nums[0]

        for num in nums:
            ans = min(ans, num)

        return ans
```

### Complexity

Time

```text
O(n)
```

Space

```text
O(1)
```

---

# 7. Optimal Solution

## Three Cases

### Case 1

```text
nums[mid] > nums[right]
```

```text
4 5 6 7 | 0 1 2
      ↑
```

Minimum is on the right.

```python
left = mid + 1
```

---

### Case 2

```text
nums[mid] < nums[right]
```

```text
0 1 2 4 5
    ↑
```

Minimum is on the left (including `mid`).

```python
right = mid
```

---

### Case 3 (New)

```text
nums[mid] == nums[right]
```

Example

```text
2 2 2 0 2
    ↑   ↑
```

Cannot decide.

Shrink:

```python
right -= 1
```

---

## Python Code

```python
class Solution:
    def findMin(self, nums):
        left = 0
        right = len(nums) - 1

        while left < right:

            mid = (left + right) // 2

            # Minimum lies to the right
            if nums[mid] > nums[right]:
                left = mid + 1

            # Minimum is at mid or to the left
            elif nums[mid] < nums[right]:
                right = mid

            # Duplicate values: cannot determine the side
            else:
                right -= 1

        return nums[left]
```

---

## Complexity

### Average

```text
O(log n)
```

### Worst Case

```text
O(n)
```

Example

```text
1 1 1 1 1 1 1
```

Every iteration removes only one element.

---

Space

```text
O(1)
```

---

# 8. Step-by-Step Trace

Example

```text
nums = [2,2,2,0,1]
```

| Left | Right | Mid | nums[mid] | nums[right] | Action        |
| ---- | ----- | --- | --------- | ----------- | ------------- |
| 0    | 4     | 2   | 2         | 1           | 2>1 → left=3  |
| 3    | 4     | 3   | 0         | 1           | 0<1 → right=3 |

Stop.

Answer

```text
nums[3] = 0
```

---

### Duplicate Example

```text
nums = [2,2,2,0,2]
```

| Left | Right | Mid | nums[mid] | nums[right] | Action       |
| ---- | ----- | --- | --------- | ----------- | ------------ |
| 0    | 4     | 2   | 2         | 2           | right--      |
| 0    | 3     | 1   | 2         | 0           | 2>0 → left=2 |
| 2    | 3     | 2   | 2         | 0           | 2>0 → left=3 |

Answer

```text
0
```

---

### Worst Case

```text
nums = [1,1,1,1,1]
```

| Iteration | Action  |
| --------- | ------- |
| 1         | right-- |
| 2         | right-- |
| 3         | right-- |
| 4         | right-- |

Becomes linear.

---

# 9. Related Problems

1. **704. Binary Search**
   The foundation of binary search on sorted arrays.

2. **69. Sqrt(x)**
   Reinforces binary search on a monotonic search space.

3. **153. Find Minimum in Rotated Sorted Array**
   The same problem without duplicates, where every iteration discards half the search space.

4. **33. Search in Rotated Sorted Array**
   Uses similar pivot logic to locate a target value instead of the minimum.

5. **81. Search in Rotated Sorted Array II**
   Extends the rotated-array search to allow duplicates, requiring the same `right -= 1` strategy when `nums[mid] == nums[right]`.

---

# ⭐ Interview Memory Trick

Think of this as **Problem 153 + One Extra Case**.

```text
if nums[mid] > nums[right]:
    left = mid + 1

elif nums[mid] < nums[right]:
    right = mid

else:
    right -= 1    # <-- only new line
```

**Why only `right -= 1`?**

* `nums[mid] == nums[right]` gives **no information** about which half contains the minimum.
* Removing one duplicate from the right does not eliminate a unique minimum, so it's safe.
* This ambiguity is exactly why the worst-case complexity degrades from **O(log n)** to **O(n)**.
