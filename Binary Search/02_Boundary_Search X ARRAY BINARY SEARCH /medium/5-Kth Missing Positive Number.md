# **1539. Kth Missing Positive Number (Binary Search)**

---

# 1. Problem Statement

You are given a **strictly increasing** array of positive integers `arr` and a positive integer `k`.

Return the **k-th missing positive integer**.

A missing positive integer is a positive integer that does **not** appear in `arr`.

### Constraints

* `1 <= arr.length <= 1000`
* `1 <= arr[i] <= 1000`
* `1 <= k <= 1000`

---

# 2. Diagram

Suppose

```text
arr = [2,3,4,7,11]
k = 5
```

Numbers:

```text
1 2 3 4 5 6 7 8 9 10 11

M ✓ ✓ ✓ M M ✓ M M M ✓

Missing:
1, 5, 6, 8, 9, 10, ...

5th Missing = 9
```

---

## Key Observation

For every index, calculate how many numbers are missing **before it**.

```text
Index : 0  1  2  3  4

Value : 2  3  4  7 11

Missing before each element:

2 -> 1

3 -> 1

4 -> 1

7 -> 3

11 -> 6
```

Formula:

```text
Missing = arr[i] - (i + 1)
```

Why?

```text
Expected value at index i

1 2 3 4 5

Actual

2 3 4 7 11

Difference = Missing numbers
```

---

# 3. Example I/O

### Example 1

Input

```text
arr = [2,3,4,7,11]
k = 5
```

Output

```text
9
```

Explanation

```text
Missing numbers

1,5,6,8,9,...

5th missing = 9
```

---

### Example 2

Input

```text
arr = [1,2,3,4]

k = 2
```

Output

```text
6
```

Explanation

```text
Missing numbers

5,6,...

2nd missing = 6
```

---

### Edge Case

```text
arr = [2]

k = 1

Output = 1
```

---

# 4. Intuition & Pattern Recognition

The difficult part is **finding where the k-th missing number lies.**

Instead of checking every number,

ask:

> **How many numbers are already missing before arr[mid]?**

That value is

```text
missing = arr[mid] - (mid + 1)
```

If

```text
missing < k
```

then the answer must be **after** `mid`.

Otherwise,

the answer is **before or at** `mid`.

This makes the missing-count array monotonic, which is exactly what Binary Search needs.

---

## Interview Recognition

Whenever you see

* Sorted array
* Need k-th missing / first position
* A monotonic count function

Think:

> Binary Search on the missing-count function.

---

# 5. Simpler Version

## Step 1

Find the missing numbers by scanning.

```text
arr = [2,3,4,7,11]

Missing

1 5 6 8 9 10 ...
```

Works but is slow.

---

## Step 2

Notice

```text
arr = [2,3,4,7,11]

Missing counts

1
1
1
3
6
```

These counts never decrease.

So Binary Search can find the first index where

```text
missing >= k
```

---

### Simpler Question Chain

### 1. 704. Binary Search

Find an element.

---

### 2. First Bad Version (278)

Find first index satisfying a condition.

---

### 3. Search Insert Position (35)

Binary search on boundaries.

---

### 4. Kth Missing Positive Number

Binary search on a **derived monotonic function** (`missing count`).

---

Thinking progression

```text
Binary Search

↓

Need monotonic function

↓

Missing count

↓

Find first count ≥ k

↓

Compute answer
```

---

# 6. Brute Force

Generate missing numbers one by one.

```python
class Solution:
    def findKthPositive(self, arr, k):
        current = 1
        i = 0

        while k:
            if i < len(arr) and arr[i] == current:
                i += 1
            else:
                k -= 1
                if k == 0:
                    return current
            current += 1
```

### Complexity

Time

```text
O(arr[-1] + k)
```

Space

```text
O(1)
```

---

# 7. Optimal Solution (Binary Search)

## Key Formula

```text
Missing before arr[i]

= arr[i] - (i + 1)
```

### Code

```python
class Solution:
    def findKthPositive(self, arr, k):
        left = 0
        right = len(arr) - 1

        while left <= right:
            mid = (left + right) // 2

            # Missing numbers before arr[mid]
            missing = arr[mid] - (mid + 1)

            if missing < k:
                left = mid + 1
            else:
                right = mid - 1

        # left is the first index where missing >= k
        return left + k
```

---

## Why `left + k`?

After binary search:

```text
left = number of array elements before the answer
```

Among the first

```text
answer
```

positive numbers,

`left` numbers already exist in the array.

So

```text
answer - left = k

answer = left + k
```

This elegant relationship gives the final answer directly.

---

## Complexity

Time

```text
O(log n)
```

Space

```text
O(1)
```

---

# 8. Step-by-Step Trace

```text
arr = [2,3,4,7,11]

k = 5
```

| Left | Right | Mid | arr[mid] | Missing | Action               |
| ---- | ----- | --- | -------- | ------- | -------------------- |
| 0    | 4     | 2   | 4        | 1       | Need more → Left = 3 |
| 3    | 4     | 3   | 7        | 3       | Need more → Left = 4 |
| 4    | 4     | 4   | 11       | 6       | Enough → Right = 3   |

Loop ends.

```text
left = 4
```

Answer

```text
left + k

4 + 5 = 9
```

Correct.

---

# 9. Related Problems

### 1. **704. Binary Search**

Foundation of binary search.

---

### 2. **35. Search Insert Position**

Binary search for the first valid position.

---

### 3. **278. First Bad Version**

Find the first index satisfying a condition.

---

### 4. **1539. Kth Missing Positive Number**

Binary search on a monotonic missing-count function.

---

### 5. **1060. Missing Element in Sorted Array**

A harder version that uses the same missing-count idea but with arbitrary starting values instead of beginning at 1.

---

# ⭐ Interview Cheat Sheet

### Pattern

```text
Sorted array

↓

Monotonic missing-count function

↓

Binary Search
```

### Missing Count Formula

```python
missing = arr[i] - (i + 1)
```

### Binary Search Condition

```python
if missing < k:
    left = mid + 1
else:
    right = mid - 1
```

### Final Answer

```python
answer = left + k
```

### Complexity

```text
Time  : O(log n)

Space : O(1)
```

### Recognition Cue

> **If a sorted array lets you compute a monotonic "how many items are missing before this index?" value, binary search can find the boundary where that count reaches `k`. The formula `arr[i] - (i + 1)` is the key insight, and after the search the answer is simply `left + k`.**
