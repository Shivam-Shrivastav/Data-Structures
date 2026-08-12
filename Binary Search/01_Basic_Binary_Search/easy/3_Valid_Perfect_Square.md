# Valid Perfect Square

You are given a positive integer `num`.
Return `true` if `num` is a **perfect square**, otherwise return `false`.

A perfect square is an integer that can be written as:

[
x \times x = num
]

You **cannot** use built-in square root functions like `sqrt()`.

---

## Constraints

* `1 <= num <= 2^31 - 1`

This constraint matters because:

* `mid * mid` can overflow in some languages.
* Binary Search is preferred over linear checking.

---

# Diagram

We search for a number whose square equals `num`.

Example: `num = 16`

```text
Search Space: [1 ... 16]

mid = 8  -> 64  > 16  -> move left
mid = 4  -> 16 == 16  -> found
```

Binary Search over numbers instead of array indices.

---

# Example I/O

## Example 1

Input:

```text
num = 16
```

Output:

```text
true
```

Explanation:

```text
4 * 4 = 16
```

---

## Example 2

Input:

```text
num = 14
```

Output:

```text
false
```

Explanation:

```text
No integer square gives 14
```

---

## Edge Case

Input:

```text
num = 1
```

Output:

```text
true
```

Because:

```text
1 * 1 = 1
```

---

# Intuition & Pattern Recognition

This is a classic **Binary Search on Answer** problem.

### Key signals

* We need to find a number satisfying a condition.
* The square function is monotonic:

[
1^2 < 2^2 < 3^2 < ...
]

So:

* if `mid² < num` → answer must be larger
* if `mid² > num` → answer must be smaller

That monotonic nature screams:

> “Binary Search”

---

# Simpler Version

## Simplest Problem

### Find if a number exists in a sorted array

```text
[1, 4, 9, 16, 25]
```

We binary search directly.

---

## Transition to This Problem

Instead of a sorted array:

```text
1², 2², 3², 4² ...
```

we generate values mathematically.

So we binary search over:

```text
1 → num
```

and compare:

```text
mid * mid
```

---

## Related Simpler Problems

1. **Binary Search**

   * Learn standard binary search template.

2. **Sqrt(x)**

   * Find floor of square root using binary search.
   * This problem is basically checking:

     ```text
     sqrt(num) is integer?
     ```

3. **Guess Number Higher or Lower**

   * Binary search on answer space.

---

# Brute Force

Try every number from `1` to `num`.

## Algorithm

```text
for i from 1 to num:
    if i*i == num:
        return true
return false
```

---

## Complexity

Time:
[
O(num)
]

Space:
[
O(1)
]

Too slow for large inputs.

---

# Optimal Solution — Binary Search

## Core Idea

Search for integer `mid` such that:

[
mid^2 = num
]

---

## Python Code

```python
class Solution:
    def isPerfectSquare(self, num: int) -> bool:

        left = 1
        right = num

        while left <= right:

            mid = (left + right) // 2

            square = mid * mid

            # Perfect square found
            if square == num:
                return True

            # Need larger square
            elif square < num:
                left = mid + 1

            # Need smaller square
            else:
                right = mid - 1

        return False
```

---

# Complexity

Time:
[
O(\log n)
]

Space:
[
O(1)
]

---

# Step-by-Step Trace

Example:

```text
num = 16
```

| left | right | mid | mid² | Action              |
| ---- | ----- | --- | ---- | ------------------- |
| 1    | 16    | 8   | 64   | Too big → move left |
| 1    | 7     | 4   | 16   | Found               |

Return:

```text
true
```

---

# Interview Thinking

### What to say in interview

> “The square values increase monotonically, so I can binary search the possible root between 1 and num.”

Also mention:

* avoid overflow using:

  ```python
  mid <= num // mid
  ```

  in languages with integer overflow risk.

---

# Alternative Overflow-Safe Check

Instead of:

```python
mid * mid
```

Use:

```python
mid == num // mid and num % mid == 0
```

Useful in Java/C++.

---

# Related Problems

1. Sqrt(x)
   Find floor square root using binary search.

2. Binary Search
   Core binary search template.

3. Search Insert Position
   Binary search boundary movement practice.

4. Guess Number Higher or Lower
   Binary search on hidden answer space.

5. Arranging Coins
   Binary search on mathematical condition.
