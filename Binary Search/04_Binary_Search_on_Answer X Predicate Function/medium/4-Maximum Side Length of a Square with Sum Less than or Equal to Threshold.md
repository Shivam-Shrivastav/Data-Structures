# **1292. Maximum Side Length of a Square with Sum Less than or Equal to Threshold (Binary Search + Prefix Sum)**

> **Pattern:** Binary Search on Answer + 2D Prefix Sum

---

# 1. Problem Statement

You are given an `m × n` matrix `mat` and an integer `threshold`.

Find the **maximum side length** of a square such that the **sum of all elements inside the square** is **less than or equal to** `threshold`.

Return the side length of that square.

---

### Constraints

* `1 <= m, n <= 300`
* `0 <= mat[i][j] <= 10⁴`
* `0 <= threshold <= 10⁵`

Since there are many possible squares, checking each one repeatedly would be too slow.

---

## Example

```text
Input:

mat =
[
 [1,1,3,2,4,3,2],
 [1,1,3,2,4,3,2],
 [1,1,3,2,4,3,2]
]

threshold = 4

Output:
2
```

Explanation

A 2×2 square

```text
1 1
1 1
```

has sum = 4.

No 3×3 square satisfies the threshold.

---

# 2. Diagram

Suppose

```text
1 2 3
4 5 6
7 8 9
```

Need to check

```text
□
□□
□□□
```

Possible Side Lengths

```text
1    2    3
|----|----|

Valid?

Yes
Yes
No
```

```text
True True False
```

We're searching for the **largest valid side length**.

This is Binary Search on Answer.

---

# 3. Example I/O

## Example 1

```text
Input

mat =
[
 [1,1,3],
 [1,1,3],
 [1,1,3]
]

threshold =4

Output

2
```

Explanation

```text
1 1
1 1

Sum =4
```

3×3 sum =15

Too large.

---

## Example 2 (Edge Case)

```text
Input

mat = [[10]]

threshold =5

Output

0
```

Even the smallest square exceeds the threshold.

---

# 4. Intuition & Pattern Recognition

### Signal 1

Question asks

> Maximum possible side length.

Immediately think Binary Search on Answer.

---

### Signal 2

Suppose

```text
Side Length =5
```

works.

Then

```text
4
3
2
1
```

must also work.

If a large square satisfies the threshold,

every smaller square also satisfies it.

Monotonic.

```text
True True True False False
```

(or viewed from smallest to largest: `True True ... False False`)

---

### Signal 3

Need to repeatedly calculate

```text
Square Sum
```

Doing that naively costs

```text
O(side²)
```

Too slow.

Need

```text
2D Prefix Sum
```

to compute every square sum in O(1).

---

### Interview Thinking

Ask:

> Can I guess a side length?

Yes.

> Can I verify it?

Yes.

Check every square of that size using Prefix Sum.

Hence

Binary Search.

---

# 5. Simpler Version

## Simpler Problem

Suppose

Need sum of

```text
2×2
```

square.

Without Prefix Sum

```text
Add 4 numbers
```

Easy.

Now imagine

300×300 matrix.

Need thousands of square sums.

Repeated addition is expensive.

---

Use Prefix Sum.

Then every square sum becomes

```text
O(1)
```

Now Binary Search becomes possible.

---

## Simpler LeetCode Problems

### 1. **303. Range Sum Query - Immutable**

1D Prefix Sum.

---

### 2. **304. Range Sum Query 2D - Immutable**

2D Prefix Sum.

---

### 3. **1314. Matrix Block Sum**

Practice Prefix Sum.

---

### Thinking Progression

```text
1D Prefix Sum
      ↓
2D Prefix Sum
      ↓
Fast Square Sum
      ↓
Binary Search Side Length
```

---

# 6. Brute Force

Try every side length.

For every square,

compute its sum manually.

### Python

```python
class Solution:
    def maxSideLength(self, mat, threshold):

        m = len(mat)
        n = len(mat[0])

        ans = 0

        for size in range(1, min(m, n) + 1):

            for i in range(m - size + 1):

                for j in range(n - size + 1):

                    total = 0

                    for r in range(i, i + size):
                        for c in range(j, j + size):
                            total += mat[r][c]

                    if total <= threshold:
                        ans = size

        return ans
```

### Complexity

```text
O(m*n*size²)
```

Too slow.

---

# 7. Optimal Solution

## Step 1

Build a

```text
2D Prefix Sum
```

where

```text
prefix[i][j]

=

sum of rectangle

(0,0)

↓

(i-1,j-1)
```

---

## Step 2

Binary Search

```text
1

↓

min(m,n)
```

---

## Step 3

Check Function

For every possible square

calculate

```text
sum =
prefix[r2][c2]
-prefix[r1][c2]
-prefix[r2][c1]
+prefix[r1][c1]
```

If **any** square satisfies the threshold,

that side length works.

---

## Python

```python
class Solution:
    def maxSideLength(self, mat, threshold):

        m = len(mat)
        n = len(mat[0])

        # Build 2D prefix sum
        prefix = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m):
            for j in range(n):
                prefix[i + 1][j + 1] = (
                    mat[i][j]
                    + prefix[i][j + 1]
                    + prefix[i + 1][j]
                    - prefix[i][j]
                )

        # Check whether a square of given size exists
        def can(size):

            for i in range(size, m + 1):
                for j in range(size, n + 1):

                    total = (
                        prefix[i][j]
                        - prefix[i - size][j]
                        - prefix[i][j - size]
                        + prefix[i - size][j - size]
                    )

                    if total <= threshold:
                        return True

            return False

        left = 0
        right = min(m, n)

        while left <= right:

            mid = (left + right) // 2

            if can(mid):
                left = mid + 1
            else:
                right = mid - 1

        return right
```

---

## Complexity

Building Prefix

```text
O(mn)
```

Each check

```text
O(mn)
```

Binary Search

```text
O(log(min(m,n)))
```

Overall

```text
O(mn log(min(m,n)))
```

Space

```text
O(mn)
```

---

# 8. Step-by-Step Trace

Example

```text
1 1
1 1

threshold =4
```

Search Space

```text
0

↓

2
```

---

### Iteration 1

```text
mid=1
```

Every 1×1 square

≤4

Works.

```text
left=2
```

---

### Iteration 2

```text
mid=2
```

Square

```text
1 1
1 1
```

Sum

```text
4
```

Works.

```text
left=3
```

Loop ends.

Answer

```text
2
```

---

## Dry Run Table

| Left | Right | Mid | Exists? | Decision     |
| ---: | ----: | --: | ------- | ------------ |
|    0 |     2 |   1 | Yes     | Left = 2     |
|    2 |     2 |   2 | Yes     | Left = 3     |
| Stop |       |     |         | Return **2** |

---

# 9. Related Problems (Increasing Difficulty)

1. Range Sum Query 2D - Immutable – Learn how to build and query a 2D prefix sum table.

2. Matrix Block Sum – Uses 2D prefix sums to compute many submatrix sums efficiently.

3. Maximum Side Length of a Square with Sum Less than or Equal to Threshold – Combines 2D prefix sums with Binary Search on the answer.

4. Max Sum of Rectangle No Larger Than K – A harder submatrix-sum problem using prefix sums and balanced search trees.

5. Largest Rectangle in Histogram – Another classic "largest valid area" problem requiring a different optimization technique (monotonic stack).

---

# Binary Search on Answer Cheat Sheet

| Problem                                 | Search Space                  | Check Function                                                                |
| --------------------------------------- | ----------------------------- | ----------------------------------------------------------------------------- |
| **875. Koko Eating Bananas**            | `1 → max(piles)`              | Compute total hours                                                           |
| **1011. Capacity To Ship Packages**     | `max(weights) → sum(weights)` | Compute required days                                                         |
| **1283. Smallest Divisor**              | `1 → max(nums)`               | Compute `Σ ceil(num/divisor)`                                                 |
| **1292. Maximum Side Length of Square** | `0 → min(rows, cols)`         | Check if **any** square of that size has sum ≤ threshold using 2D prefix sums |
| **410. Split Array Largest Sum**        | `max(nums) → sum(nums)`       | Compute required partitions                                                   |

## Interview Recognition

When you see:

* ✅ Find the **maximum/minimum possible value**
* ✅ You can **guess** an answer (here, the side length)
* ✅ You can **verify** that guess efficiently (using a 2D prefix sum)
* ✅ Valid answers are monotonic (`True True ... False False`)

Think:

> **Binary Search on Answer + an efficient check function**.

For this problem, the key insight is that **Binary Search alone is not enough**—you first need **2D Prefix Sums** so that checking a candidate side length is fast enough.
