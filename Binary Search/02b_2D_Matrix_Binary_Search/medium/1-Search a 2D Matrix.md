# **74. Search a 2D Matrix**

## 1. Problem Statement

You are given an `m x n` integer matrix with the following properties:

* Each row is sorted in **ascending order**.
* The **first integer of each row is greater than the last integer of the previous row**.

Given an integer `target`, return **true** if the target exists in the matrix, otherwise return **false**.

### Constraints

* `1 <= m, n <= 100`
* `-10^4 <= matrix[i][j], target <= 10^4`

The important observation is that the matrix behaves exactly like a **single sorted 1D array**.

---

## 2. Diagram

```
Matrix

[
 [ 1,  3,  5,  7],
 [10, 11, 16, 20],
 [23, 30, 34, 60]
]

Can be viewed as

Index:
0   1   2   3   4   5   6   7   8    9   10  11

Value:
1   3   5   7  10  11  16  20  23   30   34  60


mid = 5
↓

11

Convert back

row = mid // cols = 5 // 4 = 1
col = mid % cols = 5 % 4 = 1

matrix[1][1] = 11
```

Think of the matrix as one continuous sorted array.

---

# 3. Example I/O

### Example 1

**Input**

```
matrix =
[
 [1,3,5,7],
 [10,11,16,20],
 [23,30,34,60]
]

target = 3
```

**Output**

```
true
```

Explanation

```
3 exists at matrix[0][1].
```

---

### Example 2

**Input**

```
matrix =
[
 [1,3,5],
 [7,9,11]
]

target = 8
```

**Output**

```
false
```

---

### Edge Case

```
matrix = [[5]]

target = 5

Output = true
```

---

# 4. Intuition & Pattern Recognition

### Clues

* Every row is sorted.
* Every next row starts after the previous row ends.

This means

```
1 3 5 7
10 11 16 20
23 30 34 60

↓

1 3 5 7 10 11 16 20 23 30 34 60
```

The entire matrix is globally sorted.

So instead of searching row-by-row, perform **Binary Search** over all `m*n` elements.

### Interview Thought Process

> "Since the first element of each row is greater than the previous row's last element, flattening the matrix still gives a sorted array. Binary Search can directly work."

Pattern:

* Binary Search on Answer ❌
* Binary Search on Virtual Array ✅

---

# 5. Simpler Version

## Step 1

### LeetCode 704 — Binary Search

```
nums = [1,3,5,7,9]
```

Search normally.

---

## Step 2

Imagine the array split into rows

```
1 3 5
7 9 11
13 15 17
```

Nothing changed.

It is still

```
1 3 5 7 9 11 13 15 17
```

The only challenge is converting

```
1D index

↓

(row,col)
```

using

```
row = idx // cols
col = idx % cols
```

That's literally the entire problem.

### Simpler Question Chain

1. **704. Binary Search**

   * Learn standard binary search.

2. **35. Search Insert Position**

   * Learn boundary movement.

3. **74. Search a 2D Matrix**

   * Same binary search, but convert index into `(row, col)`.

Thinking progression:

```
Binary Search

↓

Binary Search on virtual array

↓

Convert index → row,col

↓

Done
```

---

# 6. Brute Force

Search every element.

```python
class Solution:
    def searchMatrix(self, matrix, target):
        for row in matrix:
            for num in row:
                if num == target:
                    return True
        return False
```

### Complexity

Time

```
O(m*n)
```

Space

```
O(1)
```

---

# 7. Optimal Solution (Binary Search)

```python
class Solution:
    def searchMatrix(self, matrix, target):
        rows = len(matrix)
        cols = len(matrix[0])

        left = 0
        right = rows * cols - 1

        while left <= right:
            mid = (left + right) // 2

            # Convert virtual index into row and column
            row = mid // cols
            col = mid % cols

            value = matrix[row][col]

            if value == target:
                return True
            elif value < target:
                left = mid + 1
            else:
                right = mid - 1

        return False
```

### Complexity

Time

```
O(log(m*n))
```

Equivalent to

```
O(log m + log n)
```

Space

```
O(1)
```

---

# 8. Step-by-Step Trace

Matrix

```
[
 [1,3,5,7],
 [10,11,16,20],
 [23,30,34,60]
]

target = 16
```

Rows = 3

Cols = 4

Total elements = 12

| left | right | mid | row | col | value | Action              |
| ---- | ----- | --- | --- | --- | ----- | ------------------- |
| 0    | 11    | 5   | 1   | 1   | 11    | 11 < 16 → left = 6  |
| 6    | 11    | 8   | 2   | 0   | 23    | 23 > 16 → right = 7 |
| 6    | 7     | 6   | 1   | 2   | 16    | Found               |

Return

```
True
```

---

# 9. Related Problems

1. **704. Binary Search**

   * Pure binary search foundation.

2. **35. Search Insert Position**

   * Same binary search boundary logic.

3. **74. Search a 2D Matrix**

   * Binary search on a virtual flattened array.

4. **240. Search a 2D Matrix II**

   * Rows and columns are sorted independently; virtual flattening no longer works. Use the top-right corner search (`O(m+n)`).

5. **33. Search in Rotated Sorted Array**

   * Binary search on a modified sorted structure with additional conditions.

---

# ⭐ Interview Cheat Sheet

### Pattern

```
Matrix behaves like one sorted array.
```

### Index Conversion

```python
row = mid // cols
col = mid % cols
```

### Binary Search

```python
left = 0
right = rows * cols - 1
```

### Time

```
O(log(m*n))
```

### Space

```
O(1)
```

### Recognition Cue

> **Whenever every row starts after the previous row ends, treat the 2D matrix as one sorted 1D array and perform binary search using index-to-(row, col) conversion.**
