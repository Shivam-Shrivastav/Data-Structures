# Palindrome Number (LeetCode 9)

**Pattern:** Math / Digit Manipulation

---

# 1. Problem Statement

Given an integer `x`, return **`true`** if `x` is a palindrome, and **`false`** otherwise.

A palindrome number reads the same **forward and backward**.

You **cannot** convert the integer into a string for the optimal mathematical solution.

### Constraints

* `-2^31 <= x <= 2^31 - 1`
* Follow-up: Solve it **without converting the integer to a string**.

---

# 2. Diagram

Example:

```
x = 1221

Original Number

1 2 2 1
↑       ↑
Compare from both ends

Using Math

x = 1221

Take last digit:
1

Reversed Half:
1

Remaining:
122

------------------

Take last digit:
2

Reversed Half:
12

Remaining:
12

Now:

Remaining = 12
Reversed Half = 12

Equal ✓
```

Instead of reversing the **entire** number, we only reverse **half** of it.

---

# 3. Example I/O

### Example 1

```
Input:
x = 121

Output:
true
```

Explanation

```
Forward : 121
Backward: 121
```

---

### Example 2

```
Input:
x = -121

Output:
false
```

Explanation

```
Forward : -121
Backward: 121-

Negative sign changes position.
```

---

### Example 3

```
Input:
x = 10

Output:
false
```

Explanation

```
Forward : 10
Backward: 01

Leading zero isn't allowed.
```

---

### Example 4 (Edge Case)

```
Input:
x = 0

Output:
true
```

---

# 4. Intuition & Pattern Recognition

### Signals

Whenever you see

* Digits of an integer
* Reverse number
* Palindrome
* No string conversion

Think:

> **Extract digits using `% 10` and remove digits using `// 10`.**

### Key Observation

To check whether a number is a palindrome, we **don't need to reverse the whole number**.

Why?

```
12321

Reverse only half

Original Half : 12
Reversed Half : 12

Middle digit doesn't matter.
```

This avoids integer overflow and performs fewer operations.

### Interview Thinking

Tell yourself:

```
Palindrome means
left half == reversed right half.

Instead of reversing everything,

keep moving digits from the end
to another number until
half the digits are processed.

Finally compare both halves.
```

---

# 5. Simpler Version

## Simpler Question 1

### Reverse Integer (LeetCode 7)

```
Extract last digit

Reverse whole number

return reversed
```

Difference:

* Reverse Integer reverses **all digits**.
* This problem reverses **only half**.

---

## Simpler Question 2

### Valid Palindrome (LeetCode 125)

Uses two pointers on a string.

```
Compare left
Compare right

Move inward
```

Current problem performs the same idea, but using **digits** instead of characters.

---

## Current Question

Instead of

```
Reverse Entire Number
```

we do

```
Reverse Half

↓

Compare

↓

Done
```

---

### Thinking Progression

```
Extract Digits

↓

Reverse Integer

↓

Need only half

↓

Compare halves

↓

Palindrome Number
```

---

# 6. Brute Force

Convert the integer to a string.

Compare both ends.

```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        return s == s[::-1]
```

### Complexity

```
Time  : O(N)

Space : O(N)
```

Where **N = number of digits**.

---

# 7. Optimal Solution (Reverse Half)

### Idea

1. Negative numbers are never palindromes.
2. Numbers ending in `0` (except `0`) cannot be palindromes.
3. Reverse only half the digits.
4. Compare both halves.

### Python

```python
class Solution:
    def isPalindrome(self, x: int) -> bool:

        # Negative numbers and numbers ending with 0
        # (except 0 itself) can't be palindromes.
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_half = 0

        # Reverse only half of the number.
        while x > reversed_half:
            digit = x % 10
            reversed_half = reversed_half * 10 + digit
            x //= 10

        # Even digits: x == reversed_half
        # Odd digits: x == reversed_half // 10 (ignore middle digit)
        return x == reversed_half or x == reversed_half // 10
```

### Complexity

```
Time  : O(log10 N)

Space : O(1)
```

Only half the digits are processed.

---

# 8. Step-by-Step Trace

Example

```
x = 1221
```

| Step  | x    | Last Digit | reversed_half |
| ----- | ---- | ---------- | ------------- |
| Start | 1221 | -          | 0             |
| 1     | 122  | 1          | 1             |
| 2     | 12   | 2          | 12            |

Loop stops because

```
x = 12
reversed_half = 12
```

Compare

```
12 == 12

Answer = True
```

---

### Odd-Length Example

```
x = 12321
```

| Step  | x     | reversed_half |
| ----- | ----- | ------------- |
| Start | 12321 | 0             |
| 1     | 1232  | 1             |
| 2     | 123   | 12            |
| 3     | 12    | 123           |

Now

```
x = 12
reversed_half = 123

Ignore middle digit

123 // 10 = 12

Equal ✓
```

---

# 9. Related Problems

| Problem                              | Connection                                                 |
| ------------------------------------ | ---------------------------------------------------------- |
| **7. Reverse Integer**               | Reverse digits of an integer; foundation for this problem. |
| **125. Valid Palindrome**            | Palindrome checking using two pointers on strings.         |
| **564. Find the Closest Palindrome** | Builds palindrome numbers mathematically from prefixes.    |
| **866. Prime Palindrome**            | Combines palindrome generation with prime checking.        |
| **479. Largest Palindrome Product**  | Uses palindrome construction and mathematical reasoning.   |

---

# Key Interview Takeaways

* **Pattern:** Math / Digit Manipulation.
* **Key Trick:** Reverse **only half** of the number.
* **Early Exit:** Negative numbers and numbers ending in `0` (except `0`) are never palindromes.
* **Odd-Length Handling:** Ignore the middle digit using `reversed_half // 10`.
* **Complexity:** **O(log N)** time and **O(1)** space.

This follows the same interview-focused revision style as your previous sheets. 
