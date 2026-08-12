# **1006. Clumsy Factorial**

---

# 1. Problem Statement

The **clumsy factorial** of a positive integer `n` is computed by replacing the usual multiplication sequence with a repeating pattern of operations:

```text
*, /, +, -
```

applied from **left to right**.

Specifically:

* Start with `n`
* Multiply by `n-1`
* Divide by `n-2`
* Add `n-3`
* Subtract `n-4`
* Repeat the same operation cycle (`*, /, +, -`) until reaching `1`.

Division uses **integer floor division** (the LeetCode problem guarantees positive intermediate divisions, so Python's `//` works correctly).

Return the clumsy factorial of `n`.

---

### Constraints

* `1 <= n <= 10^4`

---

### Example

```text
Input:
n = 10

Expression:

10 * 9 / 8 + 7 - 6 * 5 / 4 + 3 - 2 * 1

Output:
12
```

---

# 2. Diagram

For `n = 10`

```text
          *      /      +      -
10 -----> 9 ----> 8 ----> 7 ----> 6 ----> 5 ----> 4 ----> 3 ----> 2 ----> 1
          │               │               │
          ▼               ▼               ▼
      10*9/8          -(6*5/4)        -(2*1)

Final:
10*9/8 +7 -(6*5/4)+3 -(2*1)
```

Think of it as evaluating a normal arithmetic expression.

---

# 3. Example I/O

### Example 1

```text
Input:
n = 4

Expression:
4 * 3 / 2 + 1

Output:
7
```

Explanation

```text
4*3=12

12/2=6

6+1=7
```

---

### Example 2

```text
Input:
n = 10

Output:
12
```

Explanation

```text
10*9/8+7-6*5/4+3-2*1

=11+7-7+3-2

=12
```

---

### Edge Case

```text
Input:
n=1

Output:
1
```

---

# 4. Intuition & Pattern Recognition

## Recognition

Whenever you see

> Evaluate an expression with operator precedence

think

> **Basic Calculator II**

The expression

```text
10*9/8+7-6*5/4+3-2*1
```

is literally a valid calculator expression.

The only difference is that we generate it ourselves.

---

### Pattern

```text
Expression Evaluation

↓

Stack

↓

Operator Precedence
```

---

# 5. Simpler Version

## Simpler Problem

Evaluate

```text
5*4/3+2
```

Exactly Basic Calculator II.

---

Current problem simply generates

```text
n*(n-1)/(n-2)+(n-3)-...
```

and evaluates it.

---

### Related Simpler Questions

### 227. Basic Calculator II

Learn

* operator precedence
* stack

↓

Current problem uses the exact same idea.

---

Progression

```text
Evaluate expression

↓

Generate expression

↓

Evaluate using stack
```

---

# 6. Brute Force

Construct the entire expression string

Example

```text
10*9/8+7-6*5/4+3-2*1
```

Then run a calculator/parser.

### Complexity

Time

```text
O(n)
```

Space

```text
O(n)
```

Extra space for the generated expression.

---

# 7. Optimal Solution (Stack)

## Idea

Maintain

```python
stack
op = 0
```

where

```text
0 → *

1 → /

2 → +

3 → -
```

For every number from `n-1` down to `1`:

* `*` → multiply top of stack
* `/` → divide top of stack
* `+` → push positive number
* `-` → push negative number

Finally,

```python
sum(stack)
```

---

### Python

```python
class Solution:
    def clumsy(self, n: int) -> int:
        stack = [n]
        op = 0  # 0:*, 1:/, 2:+, 3:-

        for num in range(n - 1, 0, -1):

            if op == 0:
                stack.append(stack.pop() * num)

            elif op == 1:
                stack.append(stack.pop() // num)

            elif op == 2:
                stack.append(num)

            else:
                stack.append(-num)

            op = (op + 1) % 4

        return sum(stack)
```

---

### Note about Division in Python

For this problem, all divisions occur on **positive intermediate multiplication results**, so:

```python
a // b
```

works correctly.

(If negative values could be divided, you would use `int(a / b)` to truncate toward zero, as in **Basic Calculator II**.)

---

### Complexity

Time

```text
O(n)
```

Space

```text
O(n)
```

---

# 8. Step-by-Step Trace

For

```text
n = 7
```

Initial

```text
stack=[7]
```

| Current Number | Operation | Stack    |
| -------------- | --------- | -------- |
| 6              | *         | [42]     |
| 5              | /         | [8]      |
| 4              | +         | [8,4]    |
| 3              | -         | [8,4,-3] |
| 2              | *         | [8,4,-6] |
| 1              | /         | [8,4,-6] |

Final

```text
8 + 4 - 6 = 6
```

---

# 9. Related Problems

| Problem                                    | Connection                                                        |
| ------------------------------------------ | ----------------------------------------------------------------- |
| **227. Basic Calculator II**               | Identical stack logic for handling `+`, `-`, `*`, `/` precedence. |
| **772. Basic Calculator III**              | Extends expression evaluation to include parentheses.             |
| **150. Evaluate Reverse Polish Notation**  | Another classic stack-based expression evaluator.                 |
| **241. Different Ways to Add Parentheses** | Evaluates expressions by recursively splitting at operators.      |
| **224. Basic Calculator**                  | Simpler expression parsing with only `+`, `-`, and parentheses.   |

---

# Interview Recognition Cheat Sheet

| If you see...                            | Think...                                       |
| ---------------------------------------- | ---------------------------------------------- |
| Fixed repeating operators (`*, /, +, -`) | Simulate operations in order                   |
| Need operator precedence                 | Use the **Basic Calculator II** stack approach |
| `*` or `/`                               | Update the top of the stack immediately        |
| `+`                                      | Push the number                                |
| `-`                                      | Push the negative number                       |
| Final answer                             | `sum(stack)`                                   |

### Mental Shortcut

```text
Basic Calculator II

+
Generate numbers from n to 1

=

Clumsy Factorial
```

The only new part is generating the sequence of operations; the evaluation logic is exactly the same as **Basic Calculator II**.
