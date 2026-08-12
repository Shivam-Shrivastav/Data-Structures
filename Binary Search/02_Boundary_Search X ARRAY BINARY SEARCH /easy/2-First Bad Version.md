# **278. First Bad Version (Binary Search on Answer)**

---

# 1. Problem Statement

You are a product manager leading a software development team. There are `n` versions of a product numbered from `1` to `n`.

A version is **bad** if it fails quality checks. Once a version becomes bad, **all versions after it are also bad**.

You are given an API:

```python
isBadVersion(version)
```

which returns:

* `True` → version is bad
* `False` → version is good

Your task is to find the **first bad version** while minimizing API calls.

### Example

```text
Versions:

1    2    3    4    5
G    G    B    B    B

Answer = 3
```

---

## Constraints

* `1 <= bad <= n <= 2^31 - 1`
* Minimize the number of API calls.

---

# 2. Diagram

```text
Versions

1   2   3   4   5   6   7
G   G   G   B   B   B   B
            ↑
      First Bad Version
```

The array is conceptually divided into:

```text
False False False True True True True
```

This is a **monotonic** sequence.

Binary search works whenever answers change only once.

---

# 3. Example I/O

## Example 1

```text
Input:
n = 5
bad = 4

Output:
4
```

Explanation

```text
Version

1 → Good

2 → Good

3 → Good

4 → Bad ← First

5 → Bad
```

---

## Example 2

```text
Input:
n = 1
bad = 1

Output:
1
```

---

## Example 3

```text
Input:
n = 10
bad = 7

Output:
7
```

---

# 4. Intuition & Pattern Recognition

## First Observation

We are **not** searching an array.

We're searching the **answer**.

Think of versions as

```text
1 2 3 4 5 6 7

F F F T T T T
```

where

* Good → False
* Bad → True

There is exactly **one transition**.

---

## Binary Search Signal

Whenever the question says

> Find the **first** element satisfying a condition

or

> Find the boundary

Think

> Binary Search on Answer.

---

## What happens?

Suppose

```text
bad = 6

1 2 3 4 5 6 7 8

F F F F F T T T
```

Check middle.

If middle is bad

```text
mid = 6

True
```

The first bad version could be

* version 6
* or earlier

Search left.

---

If middle is good

```text
mid = 4

False
```

Then

Everything before 4 is also good.

Search right.

---

### Interview Thought Process

> "The versions form a monotonic boolean sequence: `False...False True...True`. I need the first `True`, which is a classic binary search boundary problem."

---

# 5. Simpler Version

## Simplest Problem

Find the first `True` in

```text
F F F F T T T
```

Answer

```text
First True
```

---

## Another View

Imagine

```text
0 0 0 1 1 1
```

Find first 1.

Exactly the same problem.

---

## Simpler Questions Leading Here

### 704. Binary Search

Find target.

↓

### 35. Search Insert Position

Find first position where target could exist.

↓

### 69. Sqrt(x)

Binary search on answer space.

↓

### **278. First Bad Version**

Binary search over versions using an API.

---

# 6. Brute Force

Check every version.

```python
class Solution:
    def firstBadVersion(self, n):

        for version in range(1, n + 1):
            if isBadVersion(version):
                return version
```

---

### Complexity

Time

```text
O(n)
```

Space

```text
O(1)
```

---

# 7. Optimal Solution

## Binary Search

Maintain

```text
left = 1

right = n
```

At each step

### Case 1

```text
isBadVersion(mid) == True
```

Then

```text
mid may be the answer.
```

Keep it.

Search left.

```python
right = mid
```

---

### Case 2

```text
isBadVersion(mid) == False
```

Everything before mid is good.

Search right.

```python
left = mid + 1
```

---

## Python Code

```python
# The isBadVersion API is already defined.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n):

        left = 1
        right = n

        while left < right:

            mid = left + (right - left) // 2

            # mid is bad, so first bad could be mid or earlier
            if isBadVersion(mid):
                right = mid

            # mid is good, so first bad must be after mid
            else:
                left = mid + 1

        return left
```

---

## Why `right = mid` instead of `mid - 1`?

Suppose

```text
1 2 3 4 5

Good Good Bad Bad Bad
```

If

```text
mid = 3
```

Version 3 itself **might** be the first bad.

Removing it would lose the answer.

Hence

```python
right = mid
```

---

## Complexity

Time

```text
O(log n)
```

API Calls

```text
O(log n)
```

Space

```text
O(1)
```

---

# 8. Step-by-Step Trace

Example

```text
n = 8

bad = 6
```

Versions

```text
1 2 3 4 5 6 7 8

G G G G G B B B
```

| Left | Right | Mid | isBad(mid) | Action    |
| ---- | ----- | --- | ---------- | --------- |
| 1    | 8     | 4   | False      | left = 5  |
| 5    | 8     | 6   | True       | right = 6 |
| 5    | 6     | 5   | False      | left = 6  |

Now

```text
left == right == 6
```

Answer

```text
6
```

---

# 9. Related Problems

1. **704. Binary Search**
   Learn the basic binary search template.

2. **35. Search Insert Position**
   Find the leftmost valid position (lower bound), similar to finding the first bad version.

3. **69. Sqrt(x)**
   Binary search on a monotonic answer space rather than an array.

4. **540. Single Element in a Sorted Array**
   Uses binary search on a sorted array with a different monotonic property.

5. **875. Koko Eating Bananas**
   A classic "binary search on answer" problem where you search for the minimum feasible eating speed.

---

# ⭐ Interview Memory Trick

This is a **Left Boundary Binary Search**.

Whenever the question asks for:

* First bad version
* First true
* First valid answer
* Lower bound
* Earliest position satisfying a condition

Use this template:

```python
while left < right:
    mid = left + (right - left) // 2

    if condition(mid):
        right = mid      # keep mid
    else:
        left = mid + 1

return left
```

### Key Insight

* **Condition is False** → answer must be to the **right**.
* **Condition is True** → `mid` could already be the answer, so **keep it** by setting `right = mid`.
