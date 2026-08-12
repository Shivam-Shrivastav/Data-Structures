# 69. Sqrt(x) (Python)

## 1. Problem Statement

Given a non-negative integer `x`, return the **integer square root** of `x`.

The integer square root is the **largest integer `k`** such that:

```
k² ≤ x
```

Do **not** use any built-in square root or exponent functions.

### Constraints

* `0 <= x <= 2^31 - 1`
* Must run efficiently for very large numbers.

---

## Example

```
Input:  x = 8

Numbers:
0² = 0
1² = 1
2² = 4
3² = 9

Since:
4 ≤ 8 < 9

Answer = 2
```

---

# 2. Diagram

The answer lies in a sorted search space.

```
x = 26

Possible answers

0   1   2   3   4   5   6
|---|---|---|---|---|---|

Squares

0   1   4   9   16   25   36
                    ^
                   closest <=26

Answer = 5
```

Binary Search searches this answer space.

```
low                    high
0 ----------------------26

mid=13
13²=169 >26

Search left

0-----------12

mid=6
36>26

0------5

mid=2
4<26

3------5

mid=4
16<26

5------5

mid=5
25<26

Done
Answer=5
```

---

# 3. Example I/O

### Example 1

```
Input: 4
Output: 2
```

Explanation

```
2² = 4
```

---

### Example 2

```
Input: 8
Output: 2
```

Explanation

```
2² = 4
3² = 9

4 ≤ 8 < 9

Return 2.
```

---

### Edge Case

```
Input: 0

Output: 0
```

---

# 4. Intuition & Pattern Recognition

### Signal 1

You're looking for an integer answer between

```
0 ... x
```

---

### Signal 2

If

```
mid² > x
```

every larger number is also invalid.

---

If

```
mid² < x
```

every smaller number is also valid.

---

This monotonic property screams:

> **Binary Search on Answer**

### Interview Thinking

> "I'm not searching an array.
>
> I'm searching the answer itself.
>
> The condition `mid² <= x` is monotonic.
>
> Therefore Binary Search."

---

# 5. Simpler Version

## Simpler Question

Find a target inside a sorted array.

```
[1 3 5 7 9]
```

Binary Search works because everything left is smaller and everything right is larger.

---

Now remove the array.

Instead imagine the numbers

```
0 1 2 3 4 5 6 ...
```

Each number represents a possible answer.

Instead of checking

```
nums[mid]
```

we check

```
mid²
```

Exactly the same Binary Search.

---

## Related Simpler Problems

### 1. 704. Binary Search

Learn Binary Search.

↓

### 2. 35. Search Insert Position

Find boundary.

↓

### 3. 278. First Bad Version

Binary Search on Answer.

↓

### 4. 69. Sqrt(x)

Binary Search on mathematical values.

---

Thinking progression

```
Binary Search
      ↓
Binary Search Boundary
      ↓
Binary Search on Answer
      ↓
Sqrt(x)
```

---

# 6. Brute Force

Try every number.

```
i = 0

while i*i <= x:
    i += 1

return i-1
```

### Python

```python
class Solution:
    def mySqrt(self, x: int) -> int:
        i = 0

        while i * i <= x:
            i += 1

        return i - 1
```

### Complexity

Time

```
O(√x)
```

Space

```
O(1)
```

---

# 7. Optimal Solution (Binary Search)

### Idea

Maintain the last valid answer.

Whenever

```
mid² <= x
```

store

```
answer = mid
```

because maybe a larger valid answer exists.

---

### Python

```python
class Solution:
    def mySqrt(self, x: int) -> int:

        left = 0
        right = x
        ans = 0

        while left <= right:

            mid = left + (right - left) // 2

            square = mid * mid

            if square == x:
                return mid                  # Perfect square found

            elif square < x:
                ans = mid                   # Current best answer
                left = mid + 1              # Try for a larger square

            else:
                right = mid - 1             # Square is too large

        return ans
```

---

### Complexity

Time

```
O(log x)
```

Space

```
O(1)
```

---

# 8. Step-by-Step Trace

Example

```
x = 26
```

| left | right | mid | mid² | Action                | ans |
| ---- | ----- | --- | ---- | --------------------- | --- |
| 0    | 26    | 13  | 169  | Too big → right=12    | 0   |
| 0    | 12    | 6   | 36   | Too big → right=5     | 0   |
| 0    | 5     | 2   | 4    | Valid → ans=2, left=3 | 2   |
| 3    | 5     | 4   | 16   | Valid → ans=4, left=5 | 4   |
| 5    | 5     | 5   | 25   | Valid → ans=5, left=6 | 5   |

Loop stops because

```
left = 6
right = 5
```

Return

```
5
```

---

# 9. Related Problems

| Problem                        | Connection                                                                                         |
| ------------------------------ | -------------------------------------------------------------------------------------------------- |
| **704. Binary Search**         | Basic Binary Search implementation.                                                                |
| **35. Search Insert Position** | Find the boundary position in a sorted space.                                                      |
| **278. First Bad Version**     | Classic Binary Search on Answer (first valid index).                                               |
| **367. Valid Perfect Square**  | Uses the same `mid * mid` Binary Search idea to determine if a number is a perfect square.         |
| **875. Koko Eating Bananas**   | Advanced Binary Search on Answer, where the answer is a feasible speed rather than an array index. |

---

# Interview Cheat Sheet 📝

* **Pattern:** Binary Search on Answer
* **Search Space:** `0 ... x`
* **Monotonic Condition:** `mid² <= x`
* If `mid² <= x`:

  * Store `mid` as the current answer.
  * Search **right** for a potentially larger valid value.
* If `mid² > x`:

  * Search **left**.
* **Time:** `O(log x)`
* **Space:** `O(1)`
