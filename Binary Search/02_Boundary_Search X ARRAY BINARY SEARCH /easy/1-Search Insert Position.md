# 35. Search Insert Position

## 1. Problem Statement with Example

Given a **sorted array of distinct integers** `nums` and a target integer `target`, return:

* the **index** if the target is found
* otherwise, return the index where it would be inserted in order.

You must write an algorithm with **O(log n)** runtime complexity.

### Example

```text
Input:
nums = [1,3,5,6], target = 5

Output:
2
```

Because `5` exists at index `2`.

### Constraints

* `1 <= nums.length <= 10^4`
* `-10^4 <= nums[i] <= 10^4`
* `nums` is sorted in ascending order
* All values are distinct

---

# 2. Diagram

```text
nums = [1, 3, 5, 6]
index   0  1  2  3

target = 2

Binary Search:

L=0, R=3
          mid=1
             ↓
[1, 3, 5, 6]

target < nums[mid]
Move left

L=0, R=0
mid=0

target > nums[mid]
Move right

L=1, R=0  → stop

Insert at index 1
```

---

# 3. Example I/O

## Example 1 (Typical)

```text
Input:
nums = [1,3,5,6]
target = 5

Output:
2
```

Explanation:
`5` already exists at index `2`.

---

## Example 2 (Insertion)

```text
Input:
nums = [1,3,5,6]
target = 2

Output:
1
```

Explanation:
`2` should be inserted before `3`.

---

## Example 3 (Edge Case)

```text
Input:
nums = [1,3,5,6]
target = 7

Output:
4
```

Explanation:
`7` goes at the end.

---

# 4. Intuition & Pattern Recognition

This is a pure **Binary Search** problem.

### Signals that scream Binary Search

* Array is **sorted**
* Need **O(log n)**
* Need to find:

  * exact element
  * OR correct position

### Key Insight

Even if target does not exist:

* binary search eventually stops when:

```python
left > right
```

At that moment:

```python
left
```

is exactly the insertion position.

Why?

Because:

* everything before `left` is smaller
* everything from `left` onward is greater

---

### Interview Thinking

> “Sorted array + O(log n) → Binary Search immediately.”

Then ask:

* what should I return if not found?

Answer:

* return `left`

---

# 5. Simpler Version

## Simplest Problem

### "Find target in sorted array"

Classic Binary Search:

* return index if found
* else return `-1`

Example:

```text
704. Binary Search
```

---

## Transition to This Problem

Instead of returning `-1`,
we return the position where target should go.

### Important Observation

After binary search ends:

```python
left
```

naturally points to:

* first element greater than target
* OR array end

That is the insertion position.

---

## Related Simpler Questions

### 1. 

Learn:

* basic binary search template
* left/right movement

Difference:

* returns `-1` if absent

---

### 2. 

Learn:

* searching boundary
* first valid position

Connection:

* insertion index is also a boundary problem

---

### 3. 

Learn:

* lower bound / upper bound logic

Connection:

* this problem is essentially finding lower bound

---

# 6. Brute Force

## Idea

Traverse array linearly.

* if target found → return index
* if current element > target → return current index
* else insert at end

---

## Code

```python
class Solution:
    def searchInsert(self, nums, target):
        for i in range(len(nums)):

            # Found target
            if nums[i] == target:
                return i

            # Insert before bigger element
            if nums[i] > target:
                return i

        # Insert at end
        return len(nums)
```

---

## Complexity

### Time

```text
O(n)
```

### Space

```text
O(1)
```

---

# 7. Optimal Solution

## Binary Search

### Core Idea

Maintain:

```python
left, right
```

If:

* target bigger → search right
* target smaller → search left
* found → return mid

If loop ends:

```python
left
```

is insertion position.

---

## Code

```python
class Solution:
    def searchInsert(self, nums, target):

        left = 0
        right = len(nums) - 1

        while left <= right:

            # Prevent overflow
            mid = left + (right - left) // 2

            # Target found
            if nums[mid] == target:
                return mid

            # Search right half
            elif nums[mid] < target:
                left = mid + 1

            # Search left half
            else:
                right = mid - 1

        # Correct insertion position
        return left
```

---

## Complexity

### Time

```text
O(log n)
```

### Space

```text
O(1)
```

---

# 8. Step-by-Step Trace

## Example

```text
nums = [1,3,5,6]
target = 2
```

---

| Step | left | right | mid | nums[mid] | Action                  |
| ---- | ---- | ----- | --- | --------- | ----------------------- |
| 1    | 0    | 3     | 1   | 3         | target < 3 → move left  |
| 2    | 0    | 0     | 0   | 1         | target > 1 → move right |
| 3    | 1    | 0     | -   | -         | loop ends               |

---

Now:

```text
left = 1
```

So insertion position is:

```text
1
```

Final Answer:

```text
1
```

---

# 9. Related Problems

### 1. 

Pure binary search foundation.

---

### 2. 

Binary search on answer/boundary.

---

### 3. 

Lower bound + upper bound binary search.

---

### 4. 

Binary search on rotated arrays.

---

### 5. 

Binary search on answer space instead of indices.
