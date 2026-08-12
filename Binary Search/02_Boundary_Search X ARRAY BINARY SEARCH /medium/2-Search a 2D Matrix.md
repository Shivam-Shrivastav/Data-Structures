# **74. Search a 2D Matrix (Binary Search on Flattened Matrix)**

---

# 1. Problem Statement

You are given an `m × n` integer matrix with the following properties:

1. Each row is sorted in **ascending order**.
2. The **first element of each row is greater than the last element of the previous row**.

Determine if a given `target` exists in the matrix.

You must solve it in **O(log(m × n))** time.

### Example

```text
matrix =

[
 [1,3,5,7],
 [10,11,16,20],
 [23,30,34,60]
]

target = 3

Output: True
```

---

## Constraints

* `m == matrix.length`
* `n == matrix[i].length`
* `1 <= m, n <= 100`
* Matrix satisfies the sorted properties.
* Required complexity: **O(log(mn))**

---

# 2. Diagram

Think of the matrix as **one sorted array**.

```text
Matrix

1   3   5   7
10 11 16 20
23 30 34 60
```

Flattened

```text
Index

0  1  2  3  4  5  6  7  8  9 10 11

Value

1  3  5  7 10 11 16 20 23 30 34 60
```

The trick is converting a **1D index** back into a matrix position.

```text
row = index // cols

col = index % cols
```

---

# 3. Example I/O

## Example 1

```text
Input:

matrix =
[
 [1,3,5,7],
 [10,11,16,20],
 [23,30,34,60]
]

target = 3

Output:
True
```

---

## Example 2

```text
Input:

target = 13

Output:
False
```

13 doesn't exist.

---

## Example 3

```text
Input:

matrix = [[1]]

target = 1

Output:
True
```

---

# 4. Intuition & Pattern Recognition

## Key Observation

Notice

```text
1  3  5  7
10 11 16 20
23 30 34 60
```

Every row starts after the previous row ends.

So the matrix is actually

```text
1 3 5 7 10 11 16 20 23 30 34 60
```

A single sorted array.

No need for two binary searches.

---

### How do we access elements?

Suppose

```text
cols = 4

mid = 6
```

Then

```text
row = 6 // 4 = 1

col = 6 % 4 = 2
```

Element

```text
matrix[1][2] = 16
```

That's the entire trick.

---

### Interview Thought Process

> "Since every row starts after the previous row ends, the whole matrix behaves like one sorted array. I'll binary search indices from `0` to `m*n-1` and map each index back to `(row, col)`."

---

# 5. Simpler Version

## Level 1

704. Binary Search

Search in

```text
1 3 5 7 10 11
```

↓

## Level 2

Search in Matrix

Instead of physically flattening

```text
matrix → array
```

we calculate

```text
index

↓

(row, col)
```

using division and modulo.

---

## Related Simpler Problems

### 704. Binary Search

Learn binary search.

↓

### 35. Search Insert Position

Binary search boundary.

↓

### 74. Search a 2D Matrix

Binary search over a virtual array.

---

# 6. Brute Force

Search every cell.

```python
class Solution:
    def searchMatrix(self, matrix, target):

        for row in matrix:
            for num in row:
                if num == target:
                    return True

        return False
```

---

## Complexity

Time

```text
O(mn)
```

Space

```text
O(1)
```

---

# 7. Optimal Solution

## Idea

Binary search over

```text
0 ...

m*n - 1
```

Convert

```text
mid
```

to

```text
row = mid // cols

col = mid % cols
```

Compare

```python
matrix[row][col]
```

with target.

---

## Python Code

```python
class Solution:
    def searchMatrix(self, matrix, target):

        rows = len(matrix)
        cols = len(matrix[0])

        left = 0
        right = rows * cols - 1

        while left <= right:

            mid = (left + right) // 2

            # Convert virtual index to matrix coordinates
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

---

## Why does the mapping work?

Suppose

```text
cols = 4

Matrix

1   3   5   7
10 11 16 20
23 30 34 60
```

Index = 9

```text
row = 9 // 4 = 2

col = 9 % 4 = 1
```

Access

```text
matrix[2][1]

= 30
```

Exactly the 10th element of the flattened array.

---

## Complexity

Time

```text
O(log(mn))
```

Space

```text
O(1)
```

---

# 8. Step-by-Step Trace

Example

```text
matrix =

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

| Left | Right | Mid | Row | Col | Value | Action  |
| ---- | ----- | --- | --- | --- | ----- | ------- |
| 0    | 11    | 5   | 1   | 1   | 11    | left=6  |
| 6    | 11    | 8   | 2   | 0   | 23    | right=7 |
| 6    | 7     | 6   | 1   | 2   | 16    | Found   |

Answer

```text
True
```

---

# 9. Related Problems

1. **704. Binary Search**
   The basic binary search template used to search a sorted array.

2. **35. Search Insert Position**
   Reinforces binary search on ordered data and finding positions.

3. **278. First Bad Version**
   Another binary search on a conceptual search space rather than a physical array.

4. **240. Search a 2D Matrix II**
   A different matrix-search problem where rows and columns are sorted independently. The flattening trick **does not work**.

5. **33. Search in Rotated Sorted Array**
   Extends binary search to arrays that are no longer globally sorted.

---

# ⭐ Interview Memory Trick

This problem is just **Binary Search (704)** with **index conversion**.

### Formula to Remember

```python
row = mid // cols
col = mid % cols
```

Think of the matrix as a **virtual sorted array**:

```text
Matrix

1  3  5  7
10 11 16 20
23 30 34 60

↓

Virtual Array

1 3 5 7 10 11 16 20 23 30 34 60
```

You never actually flatten the matrix—you simply translate the virtual index into `(row, col)` using integer division and modulo. This preserves the required **O(log(mn))** time and **O(1)** space.
