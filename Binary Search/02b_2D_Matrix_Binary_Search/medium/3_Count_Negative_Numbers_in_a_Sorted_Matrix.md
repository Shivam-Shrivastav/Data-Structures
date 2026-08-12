# **1351. Count Negative Numbers in a Sorted Matrix**

---

# 1. Problem Statement

Given an `m x n` matrix `grid` where:

* Each **row** is sorted in **non-increasing** order (left → right decreases).
* Each **column** is sorted in **non-increasing** order (top → bottom decreases).

Return the **total number of negative numbers** in the matrix.

### Constraints

* `1 <= m, n <= 100`
* `-100 <= grid[i][j] <= 100`

---

# 2. Diagram

The matrix is sorted in decreasing order.

```text
[
 [10,  5,  0, -3],
 [ 8,  2, -1, -5],
 [ 4, -2, -3, -7],
 [ 1, -4, -6, -9]
]
```

Start from **Bottom Left**

```text
[
 [10,  5,  0, -3],
 [ 8,  2, -1, -5],
 [ 4, -2, -3, -7],
 [👉1, -4, -6, -9]
]
```

At Bottom Left:

```text
Right → Smaller

↑
Larger
```

This lets us eliminate an entire **row** or **column** in one comparison.

---

# 3. Example I/O

### Example 1

**Input**

```text
grid =
[
 [4,3,2,-1],
 [3,2,1,-1],
 [1,1,-1,-2],
 [-1,-1,-2,-3]
]
```

**Output**

```text
8
```

Explanation

```text
Negative numbers:

-1
-1
-1
-2
-1
-1
-2
-3

Total = 8
```

---

### Example 2

**Input**

```text
grid =
[
 [3,2],
 [1,0]
]
```

Output

```text
0
```

---

### Edge Case

```text
grid =
[
 [-1]
]

Output

1
```

---

# 4. Intuition & Pattern Recognition

This is almost the **same idea as Search a 2D Matrix II (240).**

Difference:

Instead of **finding one target**, we're **counting all negatives**.

---

## Key Observation

At Bottom Left

```text
      ↑ Larger

Current

→ Smaller
```

Suppose

```text
Current = -2
```

Everything to the **right** is also negative.

```text
-2  -3  -7
```

So instead of counting one-by-one,

Count them all together.

```text
count += cols - current_col
```

Move **up**.

---

If current is positive

```text
Current = 3
```

Numbers on the right may become negative.

Move right.

---

## Interview Recognition

Whenever you see

* Row sorted
* Column sorted
* Need total count

Think

> Traverse once while eliminating rows or columns.

---

# 5. Simpler Version

## Simpler Problem

Count negatives in one sorted row.

```text
5 4 2 1 -1 -3 -5
```

Once first negative is found,

everything after it is also negative.

Count directly.

---

Now extend to matrix.

Instead of binary searching every row (`O(m log n)`),

reuse information from previous rows.

---

### Simpler Question Chain

### 1. Binary Search in Sorted Array

Find first negative.

---

### 2. Count negatives in one row

Count remaining elements.

---

### 3. Search Matrix II (240)

Learn directional elimination.

---

### 4. Count Negative Numbers (1351)

Same traversal as 240 + count remaining negatives.

---

Thinking progression

```text
Sorted row

↓

Count suffix

↓

Sorted rows

↓

Reuse previous work

↓

Bottom-left traversal
```

---

# 6. Brute Force

Visit every cell.

```python
class Solution:
    def countNegatives(self, grid):
        count = 0

        for row in grid:
            for num in row:
                if num < 0:
                    count += 1

        return count
```

### Complexity

Time

```text
O(m*n)
```

Space

```text
O(1)
```

---

# 7. Better Solution (Binary Search Per Row)

Each row is sorted.

Find the first negative using binary search.

```python
class Solution:
    def countNegatives(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        count = 0

        for row in grid:
            left = 0
            right = cols - 1

            while left <= right:
                mid = (left + right) // 2

                if row[mid] < 0:
                    right = mid - 1
                else:
                    left = mid + 1

            count += cols - left

        return count
```

### Complexity

Time

```text
O(m log n)
```

Space

```text
O(1)
```

---

# 8. Optimal Solution (Bottom Left Traversal)

```python
class Solution:
    def countNegatives(self, grid):
        rows = len(grid)
        cols = len(grid[0])

        row = rows - 1          # Start from bottom-left
        col = 0
        count = 0

        while row >= 0 and col < cols:

            if grid[row][col] < 0:
                # Everything to the right is also negative
                count += cols - col
                row -= 1
            else:
                # Need to move right to find negatives
                col += 1

        return count
```

---

## Why does this work?

If

```text
grid[row][col] = -2
```

then

```text
-2  -3  -8
```

must also be negative because rows are sorted decreasingly.

So count them all at once.

---

## Complexity

Time

```text
O(m+n)
```

Space

```text
O(1)
```

---

# 9. Step-by-Step Trace

```text
[
 [4,3,2,-1],
 [3,2,1,-1],
 [1,1,-1,-2],
 [-1,-1,-2,-3]
]
```

Start

```text
row = 3
col = 0
count = 0
```

| Row | Col | Value | Action                | Count |
| --- | --- | ----- | --------------------- | ----- |
| 3   | 0   | -1    | Count 4 numbers (4-0) | 4     |
| 2   | 0   | 1     | Move Right            | 4     |
| 2   | 1   | 1     | Move Right            | 4     |
| 2   | 2   | -1    | Count 2 numbers (4-2) | 6     |
| 1   | 2   | 1     | Move Right            | 6     |
| 1   | 3   | -1    | Count 1 number        | 7     |
| 0   | 3   | -1    | Count 1 number        | 8     |

Return

```text
8
```

---

# 10. Related Problems

### 1. **704. Binary Search**

Binary search fundamentals.

---

### 2. **74. Search a 2D Matrix**

Treat matrix as a virtual sorted array.

---

### 3. **240. Search a 2D Matrix II**

Same row/column elimination technique.

---

### 4. **1351. Count Negative Numbers in a Sorted Matrix**

Use elimination + count suffixes.

---

### 5. **378. Kth Smallest Element in a Sorted Matrix**

Uses the same row-column sorted property with a different search strategy.

---

# ⭐ Relation with 240

| Feature        | 240 Search Matrix II | 1351 Count Negatives           |
| -------------- | -------------------- | ------------------------------ |
| Rows Sorted    | ✅                    | ✅ (decreasing)                 |
| Columns Sorted | ✅                    | ✅ (decreasing)                 |
| Goal           | Find target          | Count negatives                |
| Traversal      | Top-right            | Bottom-left                    |
| Why?           | Eliminate row/column | Count whole suffix + eliminate |
| Time           | `O(m+n)`             | `O(m+n)`                       |

---

# ⭐ Interview Cheat Sheet

### Pattern

```text
Rows sorted decreasing

Columns sorted decreasing
```

### Start Position

```text
Bottom Left
```

### Rules

```text
Current < 0

Count += cols - col

Move Up
```

```text
Current >= 0

Move Right
```

### Complexity

```text
Time  : O(m+n)

Space : O(1)
```

### Recognition Cue

> **Whenever a matrix is sorted in both rows and columns and you need to count (rather than search), look for a traversal that lets you eliminate an entire row or column. Here, starting from the bottom-left lets you count all negatives to the right in one step, yielding an `O(m+n)` solution.**
