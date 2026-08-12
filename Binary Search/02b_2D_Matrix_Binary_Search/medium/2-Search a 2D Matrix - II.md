# **240. Search a 2D Matrix II**

---

# 1. Problem Statement

You are given an `m x n` integer matrix where:

* Integers in **each row** are sorted in ascending order.
* Integers in **each column** are sorted in ascending order.

Given an integer `target`, return **true** if the target exists in the matrix, otherwise return **false**.

Unlike **LeetCode 74**, the rows are **not connected**.

### Constraints

* `m == matrix.length`
* `n == matrix[i].length`
* `1 <= m, n <= 300`
* `-10^9 <= matrix[i][j] <= 10^9`

---

# 2. Diagram

```
Matrix

[
 [ 1,  4,  7, 11, 15],
 [ 2,  5,  8, 12, 19],
 [ 3,  6,  9, 16, 22],
 [10, 13, 14, 17, 24],
 [18, 21, 23, 26, 30]
]

Start Here
          ↓
[ 1,  4,  7, 11, 15]
[ 2,  5,  8, 12, 19]
[ 3,  6,  9, 16, 22]
[10, 13, 14, 17, 24]
[18, 21, 23, 26, 30]

Top Right Corner
```

Why Top Right?

```
Left  → Smaller
Down  → Larger
```

So every comparison removes **one entire row or column**.

---

# 3. Example I/O

### Example 1

Input

```text
matrix =
[
 [1,4,7,11,15],
 [2,5,8,12,19],
 [3,6,9,16,22],
 [10,13,14,17,24],
 [18,21,23,26,30]
]

target = 5
```

Output

```text
true
```

---

### Example 2

Input

```text
target = 20
```

Output

```text
false
```

---

### Edge Case

```text
matrix = [[1]]

target = 2

Output = false
```

---

# 4. Intuition & Pattern Recognition

## Why can't we use Binary Search like Question 74?

Question 74 property:

```
1 3 5
7 9 11
13 15 17
```

Flattening gives

```
1 3 5 7 9 11 13 15 17
```

Still sorted.

---

But here

```
1 4 7
2 5 8
3 6 9
```

Flattening gives

```
1 4 7 2 5 8 3 6 9
```

❌ Not sorted anymore.

So Binary Search **doesn't work**.

---

## Key Observation

Top-right corner has a unique property.

Suppose current value = **15**

```
      15
← smaller

↓

larger
```

If

```
15 > target
```

Entire column can be removed.

If

```
15 < target
```

Entire row can be removed.

Each comparison removes **O(n)** elements at once.

---

## Interview Recognition

Whenever you see

* Rows sorted
* Columns sorted

Think immediately

> **Start from top-right (or bottom-left).**

---

# 5. Simpler Version

## Simpler Question

Imagine

```
1 2 3

4 5 6

7 8 9
```

Need to search 5.

Start

```
3
```

3 < 5

↓

Go Down

```
6
```

6 > 5

←

Go Left

```
5
```

Found.

---

## Simpler Problems

### 1. Binary Search (704)

Learn eliminating half.

---

### 2. Search Matrix (74)

Whole matrix globally sorted.

Binary Search.

---

### 3. Search Matrix II (240)

Matrix isn't globally sorted.

Need directional elimination.

---

Thinking Progression

```
Binary Search

↓

Matrix behaves like array

↓

Oops not sorted

↓

Need another elimination strategy

↓

Top Right Search
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

# 7. Optimal Solution

```python
class Solution:
    def searchMatrix(self, matrix, target):
        rows = len(matrix)
        cols = len(matrix[0])

        # Start from top-right corner
        row = 0
        col = cols - 1

        while row < rows and col >= 0:

            if matrix[row][col] == target:
                return True

            elif matrix[row][col] > target:
                # Everything below is larger,
                # so move left.
                col -= 1

            else:
                # Everything left is smaller,
                # so move down.
                row += 1

        return False
```

---

## Complexity

Time

```
O(m+n)
```

Each move either

* goes left
* goes down

Maximum

```
m+n
```

moves.

Space

```
O(1)
```

---

# 8. Step-by-Step Trace

Target = **14**

```
[
 [1,4,7,11,15],
 [2,5,8,12,19],
 [3,6,9,16,22],
 [10,13,14,17,24],
 [18,21,23,26,30]
]
```

| Row | Col | Value | Action         |
| --- | --- | ----- | -------------- |
| 0   | 4   | 15    | 15 > 14 → Left |
| 0   | 3   | 11    | 11 < 14 → Down |
| 1   | 3   | 12    | 12 < 14 → Down |
| 2   | 3   | 16    | 16 > 14 → Left |
| 2   | 2   | 9     | 9 < 14 → Down  |
| 3   | 2   | 14    | Found          |

Return

```
True
```

---

# 9. Related Problems

### 1. **704. Binary Search**

Foundation of searching sorted structures.

---

### 2. **74. Search a 2D Matrix**

Whole matrix is globally sorted.

Binary Search on virtual array.

---

### 3. **240. Search a 2D Matrix II**

Rows and columns sorted independently.

Top-right elimination.

---

### 4. **378. Kth Smallest Element in a Sorted Matrix**

Uses row-column sorted property with binary search on value.

---

### 5. **1351. Count Negative Numbers in a Sorted Matrix**

Exactly the same top-right (or bottom-left) traversal pattern.

---

# ⭐ Difference Between 74 and 240

| Feature            | 74                          | 240                       |
| ------------------ | --------------------------- | ------------------------- |
| Rows sorted        | ✅                           | ✅                         |
| Columns sorted     | ❌                           | ✅                         |
| Rows connected?    | ✅ Yes                       | ❌ No                      |
| Can flatten to 1D? | ✅ Yes                       | ❌ No                      |
| Binary Search?     | ✅ Yes                       | ❌ No                      |
| Optimal            | Binary Search `O(log(m*n))` | Top-right Search `O(m+n)` |

---

# ⭐ Interview Cheat Sheet

### Pattern

```
Rows sorted + Columns sorted
```

### Start Position

```
Top Right
```

### Why?

```
Left  -> Smaller
Down  -> Larger
```

### Rules

```
current > target
    ← Left

current < target
    ↓ Down

current == target
    Return True
```

### Complexity

```
Time : O(m+n)

Space : O(1)
```

### Recognition Cue

> **If each row and each column is sorted independently (but the matrix is not globally sorted), start from the top-right corner. Each comparison lets you eliminate an entire row or an entire column, giving an `O(m+n)` solution.**
