# 81. Search in Rotated Sorted Array II (Modified Binary Search with Duplicates)

## 1. Problem Statement

You are given an integer array `nums` sorted in ascending order, but it may have been **rotated** at some unknown pivot. **Unlike the previous problem, duplicates are allowed.**

Return `true` if `target` exists in the array, otherwise return `false`.

You must minimize the number of operations as much as possible.

### Example

```text
Original:
[0,1,2,4,4,4,5,6]

Rotate →

[4,5,6,0,1,2,4,4]
```

Find whether a given `target` exists.

### Constraints

* `1 <= nums.length <= 5000`
* `-10^4 <= nums[i], target <= 10^4`
* Duplicates are allowed.

> **Important:** Because of duplicates, the worst-case complexity cannot always remain `O(log n)`.

---

# 2. Diagram

### Without Duplicates (Problem 33)

```text
4 5 6 7 0 1 2
      ↑
     mid

Left half is clearly sorted.
```

Easy to determine.

---

### With Duplicates

```text
1 1 1 1 3 1
↑         ↑
l         r
      ↑
     mid

nums[left] = nums[mid] = nums[right] = 1
```

Now we **cannot tell** which half is sorted.

This is the only difficulty introduced by duplicates.

---

# 3. Example I/O

### Example 1

```text
Input:
nums = [2,5,6,0,0,1,2]
target = 0

Output:
true
```

---

### Example 2

```text
Input:
nums = [2,5,6,0,0,1,2]
target = 3

Output:
false
```

---

### Edge Case

```text
nums = [1,1,1,1,1]
target = 1

Output:
true
```

---

### Worst Case

```text
nums = [1,1,1,1,1,3,1]
target = 3
```

Need to remove duplicates one by one.

---

# 4. Intuition & Pattern Recognition

If you've solved **LeetCode 33**, you already know:

> At least one half is sorted.

That works because all values are distinct.

---

Now imagine

```text
1 1 1 1 1
```

Binary search asks

```text
Is left half sorted?

nums[left] <= nums[mid]

1 <= 1 ✓
```

Looks sorted.

But

```text
Right half

1 1
```

Also looks sorted!

You cannot decide.

---

## Key Observation

Whenever

```text
nums[left] == nums[mid] == nums[right]
```

Both halves look identical.

So simply shrink the search space:

```text
left += 1
right -= 1
```

Eventually the ambiguity disappears.

---

### Interview Signal

If you hear

* Rotated sorted array
* Duplicates

Immediately think

> "Same as Problem 33 + remove duplicate ambiguity."

---

# 5. Simpler Version

## Step 1

### LeetCode 704

Binary Search

↓

---

## Step 2

### LeetCode 33

Rotated Binary Search

↓

Find sorted half.

---

## Step 3

### Current Problem

Duplicates hide which half is sorted.

Need one extra step:

```text
nums[left] == nums[mid] == nums[right]

↓

Skip duplicates

↓

Continue binary search
```

---

### Thinking Evolution

```text
Binary Search

↓

Rotated Array

↓

Find Sorted Half

↓

Duplicates?

↓

Shrink boundaries

↓

Continue
```

---

# 6. Brute Force

```python
class Solution:
    def search(self, nums, target):

        for num in nums:
            if num == target:
                return True

        return False
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

```python
class Solution:
    def search(self, nums, target):

        left = 0
        right = len(nums) - 1

        while left <= right:

            mid = (left + right) // 2

            # Target found
            if nums[mid] == target:
                return True

            # Cannot determine sorted half due to duplicates
            if nums[left] == nums[mid] == nums[right]:
                left += 1
                right -= 1

            # Left half is sorted
            elif nums[left] <= nums[mid]:

                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            # Right half is sorted
            else:

                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return False
```

---

## Time Complexity

### Average

```text
O(log n)
```

### Worst Case

```text
O(n)
```

Example:

```text
1 1 1 1 1 1 1 1 1 1 3 1
```

Every iteration removes only one element from each end.

---

## Space

```text
O(1)
```

---

# 8. Step-by-Step Trace

Example

```text
nums = [1,1,1,3,1]
target = 3
```

| left | mid | right | nums[mid] | Action                                   |
| ---- | --- | ----- | --------- | ---------------------------------------- |
| 0    | 2   | 4     | 1         | All equal → shrink (`left=1`, `right=3`) |
| 1    | 2   | 3     | 1         | Left half sorted                         |
| 1    | 2   | 3     |           | Target not in left → search right        |
| 3    | 3   | 3     | 3         | Found                                    |

Answer

```text
True
```

---

# 9. Related Problems

### Easy

**704. Binary Search**

* Learn the basic binary search template.

---

**35. Search Insert Position**

* Practice binary search boundary updates.

---

### Medium

**33. Search in Rotated Sorted Array**

* Same problem without duplicates. This is the direct prerequisite.

---

**153. Find Minimum in Rotated Sorted Array**

* Uses the rotated-array property to locate the pivot (minimum element) with distinct values.

---

**154. Find Minimum in Rotated Sorted Array II**

* The duplicate version of Problem 153. Like this problem, duplicates can force the algorithm to shrink boundaries, leading to a worst-case `O(n)` time complexity.

---

# Difference Between Problem 33 and Problem 81

| Feature                          | Problem 33 | Problem 81                                                    |
| -------------------------------- | ---------- | ------------------------------------------------------------- |
| Duplicates                       | ❌ No       | ✅ Yes                                                         |
| Can always identify sorted half? | ✅ Yes      | ❌ Not always                                                  |
| Extra step                       | None       | If `nums[left] == nums[mid] == nums[right]`, shrink both ends |
| Average Time                     | `O(log n)` | `O(log n)`                                                    |
| Worst Time                       | `O(log n)` | `O(n)`                                                        |

---

# Interview Cheat Sheet 🚀

### Pattern

```text
Rotated Sorted Array
+
Duplicates
=
Modified Binary Search
```

### Core Observation

```text
If

nums[left] == nums[mid] == nums[right]

↓

Cannot determine the sorted half

↓

left += 1
right -= 1
```

### Algorithm

```text
Find mid

↓

Target found?

↓

All three equal?

↓

Shrink boundaries

↓

Otherwise,
find the sorted half

↓

Check if target belongs there

↓

Discard the other half
```

### Memory Trick

> **Problem 81 = Problem 33 + "Skip duplicate ambiguity."**
