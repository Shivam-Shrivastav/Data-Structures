# **153. Find Minimum in Rotated Sorted Array (Binary Search)**

## 1. Problem Statement

You are given a **sorted array of unique integers** that has been **rotated** between `1` and `n` times.

Find the **minimum element** in the array in **O(log n)** time.

### Example

```text
Original: [0,1,2,4,5,6,7]

Rotate at index 3

Result:   [4,5,6,7,0,1,2]

Minimum = 0
```

### Constraints

* `1 <= nums.length <= 5000`
* `-5000 <= nums[i] <= 5000`
* All elements are **unique**
* Array was originally sorted in ascending order.

---

# 2. Diagram

```
Example:

nums = [4,5,6,7,0,1,2]

          Pivot
            ↓
4   5   6   7   0   1   2
--------------------------
↑ Left Sorted   ↑ Right Sorted
```

Observe:

* Left part is sorted
* Right part is sorted
* Minimum always lies where the rotation happened.

---

# 3. Example I/O

### Example 1

```
Input:
nums = [3,4,5,1,2]

Output:
1
```

Explanation

```
Original:
1 2 3 4 5

Rotated:
3 4 5 1 2
      ↑
```

---

### Example 2 (Already Sorted)

```
Input:
nums = [1,2,3,4]

Output:
1
```

Explanation

No rotation.

---

### Example 3 (Edge)

```
Input:
nums = [2,1]

Output:
1
```

---

# 4. Intuition & Pattern Recognition

## Signal 1

Array is **sorted but rotated**.

Immediately think:

> Binary Search on two sorted halves.

---

## Signal 2

We're not searching for a value.

We're searching for the **rotation point**.

The smallest number is exactly where the rotation happened.

---

## Key Observation

For

```
[4,5,6,7,0,1,2]
```

Compare middle with the **rightmost** value.

```
mid = 7
right = 2

7 > 2

Minimum must be RIGHT.
```

Why?

Because

```
4 5 6 7 | 0 1 2
```

Everything before pivot is larger than last element.

---

Another example

```
0 1 2 4 5
```

mid = 2

right = 5

```
2 < 5
```

Middle belongs to sorted right-half.

Minimum could be **mid itself**.

So move left.

---

### Interview Thought Process

> "This isn't normal binary search. The array has two sorted regions. I can determine which region contains the minimum by comparing `nums[mid]` with `nums[right]`."

---

# 5. Simpler Version

## Simplest Question

**Find minimum in a sorted array.**

```
[1,2,3,4]

Answer = nums[0]
```

No work.

---

## Next Level

Find where order breaks.

```
4 5 6 7 0 1

Look for:

nums[i] > nums[i+1]
```

That's O(n).

---

## Better Thinking

Instead of checking every index...

Use binary search to identify which half contains the break.

---

### Related Simpler Problems

### 1. Binary Search (704)

Find target in sorted array.

Learn:

* Left/right pointers
* Mid calculation

↓

### 2. Sqrt(x)

Binary search on answer space.

↓

### 3. Search Insert Position

Binary search boundary.

↓

### 4. Search in Rotated Sorted Array

Binary search in rotated arrays.

↓

### 5. **Find Minimum in Rotated Sorted Array**

Instead of finding target,

find pivot.

---

# 6. Brute Force

Simply scan.

```python
class Solution:
    def findMin(self, nums):
        mn = nums[0]

        for num in nums:
            mn = min(mn, num)

        return mn
```

### Complexity

Time:

```
O(n)
```

Space:

```
O(1)
```

---

# 7. Optimal Solution (Binary Search)

## Idea

Compare

```
nums[mid]
```

with

```
nums[right]
```

### Case 1

```
nums[mid] > nums[right]
```

```
4 5 6 7 | 0 1 2
      ^
```

Minimum is right.

```
left = mid + 1
```

---

### Case 2

```
nums[mid] < nums[right]
```

```
0 1 2 4 5
    ^
```

Minimum is left including mid.

```
right = mid
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

            # Minimum lies on right side
            if nums[mid] > nums[right]:
                left = mid + 1

            # Minimum is mid or left side
            else:
                right = mid

        return nums[left]
```

### Complexity

Time

```
O(log n)
```

Space

```
O(1)
```

---

# 8. Step-by-Step Trace

Example

```
nums = [4,5,6,7,0,1,2]
```

| Left | Right | Mid | nums[mid] | nums[right] | Decision      |
| ---- | ----- | --- | --------- | ----------- | ------------- |
| 0    | 6     | 3   | 7         | 2           | 7>2 → left=4  |
| 4    | 6     | 5   | 1         | 2           | 1<2 → right=5 |
| 4    | 5     | 4   | 0         | 1           | 0<1 → right=4 |

Now

```
left == right == 4
```

Answer

```
nums[4] = 0
```

---

## Another Example

```
nums = [1,2,3,4,5]
```

| Left | Right | Mid | Decision |
| ---- | ----- | --- | -------- |
| 0    | 4     | 2   | right=2  |
| 0    | 2     | 1   | right=1  |
| 0    | 1     | 0   | right=0  |

Answer

```
1
```

Even though not rotated, algorithm works.

---

# 9. Related Problems

1. **704. Binary Search**
   The foundation of binary search on sorted arrays.

2. **69. Sqrt(x)**
   Uses binary search on the answer space instead of array indices.

3. **33. Search in Rotated Sorted Array**
   Builds on the same rotated-array property, but searches for a target instead of the pivot.

4. **81. Search in Rotated Sorted Array II**
   Introduces **duplicates**, making it harder to determine the sorted half and requiring extra handling.

5. **154. Find Minimum in Rotated Sorted Array II**
   The duplicate version of this problem, where equal values can force shrinking the search range by one, degrading the worst-case time complexity to **O(n)**.
