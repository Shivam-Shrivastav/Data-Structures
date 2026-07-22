# **85. Maximal Rectangle**

---

# 1. Problem Statement

You are given a binary matrix containing only `'0'`s and `'1'`s.

Find the **largest rectangle containing only 1's** and return its area.

### Example

```text
Input:

[
 ["1","0","1","0","0"],
 ["1","0","1","1","1"],
 ["1","1","1","1","1"],
 ["1","0","0","1","0"]
]

Output:
6
```

Explanation

Largest rectangle:

```text
1 0 1 0 0
1 0 █ █ █
1 1 █ █ █
1 0 0 1 0

Area = 2 × 3 = 6
```

---

### Constraints

* `1 <= rows, cols <= 200`
* Matrix contains only `'0'` and `'1'`

---

# 2. Diagram

The biggest realization is:

> **Every row becomes a Histogram.**

Suppose the matrix is

```text
1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
```

Convert row by row into histogram heights.

### Row 1

```text
1 0 1 0 0

Histogram

1 0 1 0 0
```

---

### Row 2

Current row:

```text
1 0 1 1 1
```

Add consecutive ones vertically

```text
2 0 2 1 1
```

Histogram

```text
█   █
█   █ █ █
---------
2 0 2 1 1
```

---

### Row 3

```text
3 1 3 2 2
```

Histogram

```text
█
█   █
█   █ █ █
█ █ █ █ █
---------
3 1 3 2 2
```

Largest Histogram Rectangle = **6**

---

### Row 4

```text
4 0 0 3 0
```

Again compute histogram.

Overall answer = maximum among all histograms.

---

# 3. Example I/O

## Example 1

```text
Input:

[
["1","0","1","0","0"],
["1","0","1","1","1"],
["1","1","1","1","1"],
["1","0","0","1","0"]
]

Output:
6
```

---

## Example 2 (Edge Case)

```text
Input:

[
["0"]
]

Output:
0
```

---

Another edge case

```text
Input:

[
["1"]
]

Output:
1
```

---

# 4. Intuition & Pattern Recognition

## Interview Signal

Whenever you see

* largest rectangle of 1s
* binary matrix
* rectangle
* consecutive rows

Think

> **Convert every row into Histogram**

and solve

> **Largest Rectangle in Histogram**

---

### Why does this work?

Imagine standing on one row.

Each column stores

> "How many consecutive 1's have appeared vertically?"

That is exactly a histogram.

Example

```text
Matrix

1
1
1

↓

Histogram height =3
```

Instead of solving a 2D problem,

we solve **m histogram problems**.

---

### Interview Thinking

Whenever you solve one histogram,

you're finding

> Largest rectangle whose bottom is the current row.

Checking every row guarantees the global maximum.

---

# 5. Simpler Version

## Simplest Question

Largest Rectangle in Histogram

```
2 1 5 6 2 3
```

Already solved using Monotonic Stack.

---

### Current Question

Instead of one histogram,

you are given many histograms hidden inside the matrix.

```text
Row 1

1 0 1 0 0

↓

Histogram

1 0 1 0 0

-------------------

Row 2

↓

2 0 2 1 1

-------------------

Row 3

↓

3 1 3 2 2

-------------------

Each histogram

↓

Largest Rectangle
```

Take maximum.

---

### Thinking Progression

```text
Largest Rectangle in Histogram
           ↓
Build histogram
           ↓
Every row becomes histogram
           ↓
Run histogram algorithm
           ↓
Take maximum
```

---

### Related Simpler Questions

1. Largest Rectangle in Histogram ⭐⭐⭐⭐⭐
2. Maximal Square
3. Count Square Submatrices With All Ones

This problem is simply an extension of Histogram.

---

# 6. Brute Force

For every cell

Try every possible rectangle

Verify every element

```text
Top-left

↓

Bottom-right

↓

Check if all are 1
```

### Complexity

Time

```text
O((mn)^2)
```

or worse.

Space

```text
O(1)
```

Far too slow.

---

# 7. Optimal Solution

## Step 1

Maintain histogram heights

```python
if matrix[r][c] == "1":
    heights[c] += 1
else:
    heights[c] = 0
```

---

## Step 2

Run Largest Rectangle in Histogram.

Exactly same algorithm as previous problem.

---

## Python Solution

```python
class Solution:
    def maximalRectangle(self, matrix):
        if not matrix:
            return 0

        cols = len(matrix[0])
        heights = [0] * cols
        max_area = 0

        for row in matrix:

            # Build histogram
            for c in range(cols):
                if row[c] == "1":
                    heights[c] += 1
                else:
                    heights[c] = 0

            # Largest Rectangle in Histogram
            stack = []
            histogram = heights + [0]

            for i in range(len(histogram)):

                while stack and histogram[stack[-1]] > histogram[i]:

                    height = histogram[stack.pop()]

                    if stack:
                        width = i - stack[-1] - 1
                    else:
                        width = i

                    max_area = max(max_area, height * width)

                stack.append(i)

        return max_area
```

---

## Time Complexity

There are

* `m` rows
* Histogram takes `O(n)`

Overall

```text
O(m × n)
```

---

## Space Complexity

```text
O(n)
```

(Stack + Histogram)

---

# 8. Step-by-Step Trace

Matrix

```text
1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
```

---

### Row 1

Histogram

```text
1 0 1 0 0
```

Largest rectangle

```
1
```

Maximum = **1**

---

### Row 2

Histogram

```text
2 0 2 1 1
```

Largest rectangle

```
2
2
```

Area = **3**

Maximum = **3**

---

### Row 3

Histogram

```text
3 1 3 2 2
```

Histogram visualization

```text
█
█   █
█   █ █ █
█ █ █ █ █
---------
3 1 3 2 2
```

Largest rectangle

```text
█ █ █
█ █ █
```

Height = 2

Width = 3

Area = **6**

Maximum = **6**

---

### Row 4

Histogram

```text
4 0 0 3 0
```

Largest rectangle = 4

Overall maximum remains

```text
6
```

---

# 9. Related Problems

### 1. **84. Largest Rectangle in Histogram** ⭐⭐⭐⭐

The core subproblem. Master this first because every row in Maximal Rectangle is transformed into a histogram.

---

### 2. **221. Maximal Square** ⭐⭐⭐

Instead of the largest rectangle, find the largest square consisting entirely of `1`s. Uses Dynamic Programming rather than a monotonic stack.

---

### 3. **1277. Count Square Submatrices with All Ones** ⭐⭐⭐

Counts all possible square submatrices of `1`s using the same DP idea as Maximal Square.

---

### 4. **1504. Count Submatrices With All Ones** ⭐⭐⭐⭐⭐

A harder extension where you count all valid rectangles. It combines histogram heights with monotonic stack techniques.

---

### 5. **42. Trapping Rain Water** ⭐⭐⭐⭐

Another classic monotonic stack problem where boundaries are computed using stack operations instead of rectangle areas.

---

# Interview Cheat Sheet

### Pattern

**Monotonic Increasing Stack + Histogram Transformation**

### Key Observation

* Every row represents the **bottom** of a potential rectangle.
* Build a histogram of consecutive vertical `1`s.
* Solve **Largest Rectangle in Histogram** for each row.
* The largest rectangle across all rows is the answer.

### Steps

```text
For every row:
    Update histogram heights
        ↓
    Run Largest Rectangle in Histogram
        ↓
    Update global maximum
```

### Complexity

* **Time:** `O(rows × cols)`
* **Space:** `O(cols)`

### One-Line Interview Summary

> Convert each row into a histogram of consecutive `1`s and apply the **Largest Rectangle in Histogram** algorithm on every row. The maximum area among all histograms is the answer.
