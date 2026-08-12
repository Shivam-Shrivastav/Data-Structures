# 48. Rotate Image — LeetCode 48

**Pattern:** Array / Matrix Manipulation
**Difficulty:** Medium
**Core trick:** **Transpose → Reverse each row**

---

## 1. Problem Statement

You are given an `n x n` matrix representing an image.

Rotate the image **90° clockwise**.

The rotation must be done **in-place**, meaning you should modify the original matrix instead of creating another `n x n` matrix.

### Example

```text
Input:

1 2 3
4 5 6
7 8 9

Output:

7 4 1
8 5 2
9 6 3
```

### Constraints

```text
n == matrix.length == matrix[i].length
1 <= n <= 20
-1000 <= matrix[i][j] <= 1000
```

The important constraint is:

> **Modify the matrix in-place.**

So an extra `n x n` result matrix is not the intended solution.

---

# 2. Diagram

We need:

```text
Original                  90° Clockwise

1  2  3                    7  4  1
4  5  6        --->        8  5  2
7  8  9                    9  6  3
```

The easiest way to remember the transformation:

### Step 1: Transpose

Swap across the main diagonal:

```text
1  2  3                   1  4  7
4  5  6       --->        2  5  8
7  8  9                   3  6  9
```

That is:

```text
matrix[i][j] ↔ matrix[j][i]
```

### Step 2: Reverse every row

```text
1  4  7                   7  4  1
2  5  8       --->        8  5  2
3  6  9                   9  6  3
```

Done.

```text
CLOCKWISE ROTATION
        =
TRANSPOSE + REVERSE ROWS
```

---

# 3. Example I/O

### Example 1 — Typical

```text
Input:

matrix = [
 [1,2,3],
 [4,5,6],
 [7,8,9]
]

Output:

[
 [7,4,1],
 [8,5,2],
 [9,6,3]
]
```

The first column `[1,4,7]` becomes the first row in reverse order `[7,4,1]`.

### Example 2 — Edge Case

```text
Input:

matrix = [[1]]

Output:

[[1]]
```

A `1 x 1` matrix remains unchanged.

---

# 4. Intuition & Pattern Recognition

When you see:

> Rotate an `n x n` matrix 90° **in-place**

think:

```text
Matrix transformation
      ↓
Can rotation be decomposed?
      ↓
Transpose + Reverse
```

Why?

Look at the columns:

```text
Original:

1 2 3
4 5 6
7 8 9
```

After clockwise rotation:

```text
7 4 1    ← original first column reversed
8 5 2    ← original second column reversed
9 6 3    ← original third column reversed
```

We need to turn **columns into rows**.

That immediately suggests:

> **Transpose**

Transpose gives:

```text
1 4 7
2 5 8
3 6 9
```

The rows are correct but backwards.

So:

> **Reverse each row.**

### Interview recognition

Tell yourself:

```text
90° clockwise
= transpose
+ horizontal flip
```

A useful matrix-transformation cheat sheet:

```text
90° clockwise:
Transpose → Reverse rows

90° counter-clockwise:
Transpose → Reverse column order

180°:
Reverse rows → Reverse row order
```

---

# 5. Simpler Version

There isn't a direct LeetCode problem that is simply "transpose this square matrix in-place" that you need to solve first, but the closest foundation is **867. Transpose Matrix**.

## Simpler: 867. Transpose Matrix

Given:

```text
1 2 3
4 5 6
7 8 9
```

Produce:

```text
1 4 7
2 5 8
3 6 9
```

The fundamental operation is:

```python
matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
```

Once you understand transpose, Rotate Image becomes:

```text
Transpose Matrix
      ↓
1 4 7
2 5 8
3 6 9

Rows aren't oriented correctly
      ↓
Reverse every row
      ↓
7 4 1
8 5 2
9 6 3
```

### Simpler thinking → current thinking

```text
Array reversal
     ↓
Reverse elements in-place

Transpose Matrix
     ↓
Swap matrix[i][j] with matrix[j][i]

Combine them
     ↓
Transpose + reverse rows

     ↓

ROTATE IMAGE
```

The difficulty isn't really the code. It is recognizing that **rotation can be decomposed into two simpler transformations**.

---

# 6. Brute Force

The straightforward approach is to create another matrix and directly place each element at its rotated position.

For an `n x n` matrix:

```text
Original position:
(row, col)

After 90° clockwise:
(col, n - 1 - row)
```

So:

```python
class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        n = len(matrix)

        rotated = [[0] * n for _ in range(n)]

        for row in range(n):
            for col in range(n):
                rotated[col][n - 1 - row] = matrix[row][col]

        # Copy result back into original matrix
        for row in range(n):
            for col in range(n):
                matrix[row][col] = rotated[row][col]
```

### Complexity

```text
Time:  O(N²)
Space: O(N²)
```

Time cannot really become better than `O(N²)` because there are `N²` cells.

The problem with brute force is **space**.

---

# 7. Optimal Solution

We keep the same `O(N²)` time but reduce extra space to `O(1)`.

```python
class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        n = len(matrix)

        # Step 1: Transpose across the main diagonal
        for row in range(n):
            for col in range(row + 1, n):
                matrix[row][col], matrix[col][row] = (
                    matrix[col][row],
                    matrix[row][col],
                )

        # Step 2: Reverse each row
        for row in matrix:
            row.reverse()
```

### Why `col = row + 1`?

This is important.

Suppose:

```text
1 2 3
4 5 6
7 8 9
```

We want swaps:

```text
2 ↔ 4
3 ↔ 7
6 ↔ 8
```

But not:

```text
1 ↔ 1
5 ↔ 5
9 ↔ 9
```

And definitely don't swap:

```text
2 ↔ 4

then later

4 ↔ 2
```

because that would undo the first swap.

So we process **only elements above the diagonal**:

```text
X  ✓  ✓
X  X  ✓
X  X  X
```

Hence:

```python
for col in range(row + 1, n):
```

### Complexity

```text
Time:  O(N²)
Space: O(1)
```

This is the cleanest interview solution.

---

# 8. Step-by-Step Trace

Input:

```text
matrix =

1 2 3
4 5 6
7 8 9
```

### Transpose

`row = 0, col = 1`

```text
swap 2 ↔ 4

1 4 3
2 5 6
7 8 9
```

`row = 0, col = 2`

```text
swap 3 ↔ 7

1 4 7
2 5 6
3 8 9
```

`row = 1, col = 2`

```text
swap 6 ↔ 8

1 4 7
2 5 8
3 6 9
```

Transpose complete.

### Reverse rows

```text
[1,4,7] → [7,4,1]

7 4 1
2 5 8
3 6 9
```

```text
[2,5,8] → [8,5,2]

7 4 1
8 5 2
3 6 9
```

```text
[3,6,9] → [9,6,3]

7 4 1
8 5 2
9 6 3
```

Final:

```text
[
 [7,4,1],
 [8,5,2],
 [9,6,3]
]
```

---

# 9. Related Problems

| Problem                   | Connection                                                                            |
| ------------------------- | ------------------------------------------------------------------------------------- |
| **344. Reverse String**   | Simplest in-place reversal; builds the reversal idea used after transpose.            |
| **867. Transpose Matrix** | Directly teaches the transpose transformation.                                        |
| **48. Rotate Image**      | Combines transpose + reversal while requiring `O(1)` extra space.                     |
| **73. Set Matrix Zeroes** | Another matrix problem where the challenge is performing the transformation in-place. |
| **54. Spiral Matrix**     | Builds matrix boundary/index manipulation skills.                                     |

## Quick Revision

```text
ROTATE IMAGE — 90° CLOCKWISE

Pattern:
Matrix / Array Manipulation

Key trick:

    TRANSPOSE
       ↓
  REVERSE ROWS
       ↓
  90° CLOCKWISE

Transpose:
matrix[i][j] ↔ matrix[j][i]

Only swap above diagonal:
j = i + 1 ... n-1

Time  = O(N²)
Space = O(1)
```

The key jump is **not memorizing the final rotated-index formula**. For the in-place solution, remember: **clockwise = transpose + reverse each row**. This follows the same quick-revision structure as your earlier sliding-window sheet. 
