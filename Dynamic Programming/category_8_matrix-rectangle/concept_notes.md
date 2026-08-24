# Matrix Rectangle — DP

This pattern usually means **finding the largest rectangle / square-like region in a matrix using DP**. There are two important problems to distinguish:

* **Maximal Square** → largest all-1s **square**
* **Maximal Rectangle** → largest all-1s **rectangle** → usually solved as **Histogram + Monotonic Stack**, not pure DP.

For **DP revision**, the key one is **Maximal Square**.

---

## 1. Pattern in One Minute

### Core idea

For every cell `(i, j)`, ask:

> **If this cell is the bottom-right corner of a square, how large can that square be?**

Define:

```python
dp[i][j] = largest all-1 square ending at (i, j)
```

If `matrix[i][j] == "1"`:

```text
dp[i][j] = 1 + min(
    dp[i-1][j],      # top
    dp[i][j-1],      # left
    dp[i-1][j-1]     # diagonal
)
```

Why `min`?

Because a square can only expand as far as its **smallest neighboring square** allows.

### Immediately think of it when:

> Matrix + contiguous region + all cells satisfy a condition + maximize square/rectangle.

---

# 2. Recognition Signals

### Strong clues

* Binary matrix (`0/1`)
* "largest square"
* "largest area of square"
* "all 1s"
* contiguous cells
* submatrix/subgrid
* each cell has a local dependency on **top, left, diagonal**

### Example

```text
1 1 1
1 1 1
1 1 1
```

At bottom-right:

```text
dp = 1 + min(top, left, diagonal)
```

So it becomes `3`.

### Don't use this DP for:

**Largest rectangle of 1s.**

Example:

```text
1 1 1 1
1 1 1 1
```

The answer is `8`, which is a rectangle, not a square.

For that → **Histogram + Monotonic Stack**.

---

# 3. Mental Model

Remember:

> **"Bottom-right corner tells me the square size."**

1. Every `1` can form at least a `1 × 1` square.
2. Look upward → how big a square exists there?
3. Look left → how big a square exists there?
4. Look diagonally → how big a square exists there?
5. The smallest of those three limits expansion.
6. Add `1` for the current cell.
7. Track the largest `dp` value.
8. Convert side length → area using `side²`.

### Mnemonic

**TOP + LEFT + DIAGONAL → MIN + 1**

```text
      TOP
       ↓
LEFT → X
       ↘
      DIAGONAL
```

---

# 4. Boilerplate Template

```python
def maximalSquare(matrix):
    m, n = len(matrix), len(matrix[0])

    dp = [[0] * (n + 1) for _ in range(m + 1)]

    max_side = 0

    for i in range(1, m + 1):
        for j in range(1, n + 1):

            if matrix[i-1][j-1] == "1":
                dp[i][j] = 1 + min(
                    dp[i-1][j],     # top
                    dp[i][j-1],     # left
                    dp[i-1][j-1]    # diagonal
                )

                max_side = max(max_side, dp[i][j])

    return max_side * max_side
```

### Why `m + 1`, `n + 1`?

The extra row/column gives us automatic `0`s for the matrix boundaries.

So we don't need:

```python
if i > 0 and j > 0:
```

This is the same **padding/sentinel DP trick** you've seen in other DP patterns.

---

# 5. Variations

### A. Maximal Square

```text
dp[i][j] = 1 + min(top, left, diagonal)
```

Return:

```python
max_side ** 2
```

**Top 3 revision problem:** LeetCode 221 — Maximal Square

---

### B. Count Square Submatrices With All Ones

Instead of only tracking maximum:

```python
ans += dp[i][j]
```

Because if:

```text
dp[i][j] = 3
```

then this cell is the bottom-right corner of:

```text
1x1
2x2
3x3
```

So it contributes **3 squares**.

LeetCode 1277.

---

### C. Maximal Rectangle

Different pattern:

```text
Matrix
  ↓
Convert each row into histogram heights
  ↓
Largest Rectangle in Histogram
  ↓
Monotonic Stack
```

This is **not** the `min(top,left,diagonal)` DP.

---

# 6. Common Pitfalls

### ❌ Using `max()` instead of `min()`

Wrong:

```python
1 + max(top, left, diagonal)
```

A square requires **all three directions** to support its expansion.

Therefore:

```python
1 + min(...)
```

---

### ❌ Forgetting area conversion

`dp[i][j]` represents:

```text
SIDE LENGTH
```

Not area.

So:

```python
area = max_side * max_side
```

---

### ❌ Confusing rectangle with square

If the question asks:

> largest rectangle of 1s

don't automatically use this DP.

Think:

**Matrix → Histogram → Monotonic Stack**

---

### ❌ Mixing matrix indices with DP indices

With padded DP:

```python
matrix[i-1][j-1]
```

but:

```python
dp[i][j]
```

---

# 7. Interview Checklist

✓ Matrix contains `0/1`
✓ Need a contiguous **square**
✓ All cells must satisfy a condition
✓ Current cell can be viewed as bottom-right corner
✓ Need information from **top + left + diagonal**

→ **2D DP**

```text
dp[i][j]
   =
1 + min(top, left, diagonal)
```

If they say:

> "largest rectangle"

→ **Histogram + Monotonic Stack**

If they say:

> "count all squares"

→ **same DP, but SUM all dp values**

---

# 8. Must-Do Problems

### 🟢 Easy

**Top 3 foundational**

1. ⭐ **LeetCode 1277 — Count Square Submatrices with All Ones**
2. ⭐ **LeetCode 221 — Maximal Square**
3. **LeetCode 85 — Maximal Rectangle** — important variation, but switch to Histogram + Stack

There aren't many truly useful easy problems here; these are the high-ROI ones.

### 🟡 Medium

* ⭐ **221 — Maximal Square**
* **1277 — Count Square Submatrices with All Ones**
* **85 — Maximal Rectangle**

### 🔴 Hard

No need to force a hard problem specifically for this pattern. Mastering **221 + 1277 + 85** gives you the important interview recognition.

---

# 9. 30-Second Cheat Sheet

```text
MATRIX + ALL 1s + LARGEST SQUARE
                ↓
              2D DP

dp[i][j] = largest square ending at (i,j)

if matrix[i][j] == 1:

    dp[i][j] = 1 + min(
        TOP,
        LEFT,
        DIAGONAL
    )

answer = max(dp)^2


KEY MNEMONIC:
TOP + LEFT + DIAGONAL
          ↓
         MIN
          ↓
        + 1


VARIATIONS:
Max Square       → max(dp)^2
Count Squares    → sum(dp)
Max Rectangle    → Histogram + Monotonic Stack

COMPLEXITY:
Time  → O(m × n)
Space → O(m × n)
```

**The one thing to burn into memory:**

> **For a square ending at `(i,j)`: `1 + MIN(top, left, diagonal)`.**
