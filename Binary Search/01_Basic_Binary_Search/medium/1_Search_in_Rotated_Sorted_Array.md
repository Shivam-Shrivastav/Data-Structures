# 33. Search in Rotated Sorted Array (Binary Search)

## 1. Problem Statement

You are given an array `nums` that was originally sorted in ascending order with **distinct** elements.

At some unknown index, the array was rotated.

Example:

```
Original: [0,1,2,4,5,6,7]
Rotate by 3
↓

[4,5,6,7,0,1,2]
```

Given a `target`, return its index if present, otherwise return `-1`.

### Constraints

* `1 <= nums.length <= 5000`
* `-10^4 <= nums[i], target <= 10^4`
* All values are distinct.
* **Required:** `O(log n)` time.

---

# 2. Diagram

Suppose

```
nums = [4,5,6,7,0,1,2]
target = 0
```

```
                mid
                 ↓
Index : 0 1 2 3 4 5 6
Value : 4 5 6 7 0 1 2

Notice:

Left Half
4 5 6 7
↑ Completely Sorted ↑

Right Half
0 1 2
↑ Completely Sorted ↑

At least ONE side is always sorted.
```

This observation is the entire solution.

---

# 3. Example I/O

### Example 1

```
Input:
nums = [4,5,6,7,0,1,2]
target = 0

Output:
4
```

Explanation:

```
0 exists at index 4.
```

---

### Example 2

```
Input:
nums = [4,5,6,7,0,1,2]
target = 3

Output:
-1
```

Explanation:

```
3 doesn't exist.
```

---

### Edge Case

```
nums = [1]
target = 1

Output:
0
```

---

# 4. Intuition & Pattern Recognition

## Normal Binary Search

Normally,

```
Array is sorted

1 3 5 7 9 11
```

We simply compare with `mid`.

---

But after rotation

```
4 5 6 7 0 1 2
```

Entire array isn't sorted.

However...

### HUGE Observation

For every Binary Search iteration

```
low -------- mid -------- high
```

**At least one half is guaranteed to be sorted.**

Either

```
low → mid
```

or

```
mid → high
```

must be sorted.

---

Interview signal:

Whenever you see

* Sorted array
* Rotated
* O(log n)

Think:

> "Modified Binary Search"

---

# 5. Simpler Version

## Simplest Question

### LeetCode 704 — Binary Search

```
1 3 5 7 9

Find target
```

Idea:

```
mid > target
Go Left

mid < target
Go Right
```

---

## Now Rotate

```
4 5 6 7 0 1 2
```

Now Binary Search doesn't know which direction.

So first ask

```
Which half is sorted?
```

Then ask

```
Does target lie inside that sorted half?
```

If Yes

```
Search there.
```

Otherwise

```
Search the other half.
```

---

### Thinking Evolution

```
Binary Search

↓

Rotated Binary Search

↓

Find Sorted Half

↓

Check if target belongs there

↓

Discard the other half
```

---

Related easier problems:

* **704. Binary Search**
* **35. Search Insert Position**
* **69. Sqrt(x)**
* **278. First Bad Version**

All teach boundary movement.

---

# 6. Brute Force

Simply scan every element.

```python
class Solution:
    def search(self, nums, target):
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1
```

### Complexity

Time

```
O(n)
```

Space

```
O(1)
```

Fails the required complexity.

---

# 7. Optimal Solution (Modified Binary Search)

```python
class Solution:
    def search(self, nums, target):

        left = 0
        right = len(nums) - 1

        while left <= right:

            mid = (left + right) // 2

            # Target found
            if nums[mid] == target:
                return mid

            # Left half is sorted
            if nums[left] <= nums[mid]:

                # Target lies inside left sorted half
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            # Right half is sorted
            else:

                # Target lies inside right sorted half
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1
```

---

### Time Complexity

```
O(log n)
```

### Space Complexity

```
O(1)
```

---

# 8. Step-by-Step Trace

Example

```
nums = [4,5,6,7,0,1,2]
target = 0
```

| left | mid | right | nums[mid] | Decision                               |
| ---- | --- | ----- | --------- | -------------------------------------- |
| 0    | 3   | 6     | 7         | Left half sorted                       |
| 0    | 3   | 6     |           | Target not in [4,5,6,7] → search right |
| 4    | 5   | 6     | 1         | Left half sorted                       |
| 4    | 5   | 6     |           | Target in [0,1] → go left              |
| 4    | 4   | 4     | 0         | Found                                  |

Answer

```
index = 4
```

---

# 9. Related Problems

### Easy

**704. Binary Search**

* Foundation of all binary search problems.

---

**35. Search Insert Position**

* Learn boundary updates when target may not exist.

---

**69. Sqrt(x)**

* Binary search on answer space instead of array.

---

### Medium

**81. Search in Rotated Sorted Array II**

* Same problem, but duplicates exist. Determining the sorted half becomes trickier because `nums[left] == nums[mid] == nums[right]` can make both halves appear sorted.

---

**153. Find Minimum in Rotated Sorted Array**

* Uses the same rotated-array property, but instead of searching for a target, you locate the pivot (minimum element). Understanding this problem makes the logic behind rotated binary search even clearer.

---

# Interview Cheat Sheet 🚀

### Pattern

```
Sorted Array
+
Rotation
+
O(log n)

→ Modified Binary Search
```

### Core Observation

```
Every iteration

One half is always sorted.
```

### Algorithm

```
Find mid

↓

Which half is sorted?

↓

Is target inside sorted half?

↓

YES → Search there

NO → Search other half
```

### Template

```python
if left half sorted:

    if target inside left:
        go left
    else:
        go right

else:

    if target inside right:
        go right
    else:
        go left
```

### Memory Trick

> **"Don't find the pivot first. Find the sorted half first."**
