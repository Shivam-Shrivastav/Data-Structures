# **227. Basic Calculator II**

## 1. Problem Statement

Given a string `s` representing a valid mathematical expression, evaluate it and return its integer result.

The expression contains:

* Non-negative integers
* Operators: `+`, `-`, `*`, `/`
* Spaces
* **No parentheses**

Division should truncate toward zero.

### Constraints

* `1 <= s.length <= 3 * 10^5`
* `s` consists of digits, spaces, and operators.
* Expression is always valid.
* Intermediate results fit in a 32-bit integer.

---

### Example

```text
Input:  s = "3+2*2"
Output: 7

Explanation:
2 * 2 = 4
3 + 4 = 7
```

---

# 2. Diagram

Expression:

```text
3 + 5 / 2 - 4 * 3

Read left to right

          Stack

3        -> [3]
+5       -> [3,5]
/2       -> [3,2]      (5/2 = 2)
-4       -> [3,2,-4]
*3       -> [3,2,-12]  (-4*3)

Final sum:
3 + 2 - 12 = -7
```

The stack stores numbers after handling operator precedence.

---

# 3. Example I/O

### Example 1

```text
Input:
"3+2*2"

Output:
7
```

Explanation

```text
3 + (2×2)
= 3 + 4
= 7
```

---

### Example 2

```text
Input:
" 14-3/2 "

Output:
13
```

Explanation

```text
3/2 = 1

14 - 1 = 13
```

---

### Edge Case

```text
Input:
"42"

Output:
42
```

Only one number.

---

# 4. Intuition & Pattern Recognition

### Interview Hint

Whenever you see

> Evaluate an expression with only `+ - * /`

think:

> **Stack + previous operator**

Why?

* Multiplication/division have higher precedence.
* Addition/subtraction can wait until the end.

Instead of building a parser:

* Push numbers for `+`
* Push negative numbers for `-`
* Immediately calculate for `*` and `/`

Finally,

```text
sum(stack)
```

gives the answer.

---

### Pattern

```
Expression Parsing
+
Operator Precedence
+
Stack
```

---

# 5. Simpler Version

## Simpler Problem 1

Evaluate

```text
1+2+3+4
```

Simply keep adding.

---

## Simpler Problem 2

Evaluate

```text
6*3*2
```

Just multiply continuously.

---

## Simpler Problem 3

Evaluate

```text
2+3*4
```

Need precedence.

Instead of evaluating left-to-right,

store 2 first.

When seeing `*`,

modify the previous number.

```
Stack

2

see 3
push

2 3

see *

pop 3

3*4

push 12

2 12

sum = 14
```

---

### Related Simpler LeetCode

* **224. Basic Calculator**

  * Only `+`, `-`, parentheses.
* **150. Evaluate Reverse Polish Notation**

  * Uses stack for operators.
* **772. Basic Calculator III**

  * Parentheses + precedence.

Progression:

```
Simple +/-
↓

+,-,*,/

↓

Parentheses

↓

Full expression parser
```

---

# 6. Brute Force

A naive approach:

Repeatedly

* Find first `*` or `/`
* Evaluate it
* Replace expression
* Repeat

Then process `+` and `-`.

This requires rebuilding strings many times.

### Complexity

Time

```
O(n²)
```

Space

```
O(n)
```

---

# 7. Optimal Solution (Stack)

### Idea

Maintain

```python
num      -> current number
sign     -> previous operator
stack    -> processed numbers
```

Whenever an operator (or end of string) is reached:

Use previous operator.

```
+  -> push num

-  -> push -num

*  -> pop, multiply, push

/  -> pop, divide, push
```

Finally

```
sum(stack)
```

---

### Python

```python
class Solution:
    def calculate(self, s: str) -> int:
        stack = []

        num = 0
        sign = '+'

        for i, ch in enumerate(s):

            # Build the current number (handles multi-digit numbers)
            if ch.isdigit():
                num = num * 10 + int(ch)

            # Process when we hit an operator or the end of the string
            if (not ch.isdigit() and ch != ' ') or i == len(s) - 1:

                if sign == '+':
                    stack.append(num)

                elif sign == '-':
                    stack.append(-num)

                elif sign == '*':
                    stack.append(stack.pop() * num)

                elif sign == '/':
                    # int(a / b) truncates toward zero
                    stack.append(int(stack.pop() / num))

                # Current operator becomes the sign for the next number
                sign = ch

                # Reset current number
                num = 0

        return sum(stack)
```

---

### Complexity

Time

```
O(n)
```

Each character visited once.

Space

```
O(n)
```

Stack may contain all numbers.

---

# 8. Step-by-Step Trace

Expression

```text
3+5/2-4*3
```

| Char | num | Previous Sign | Stack     |
| ---- | --- | ------------- | --------- |
| 3    | 3   | +             | []        |
| +    | 0   | +             | [3]       |
| 5    | 5   | +             | [3]       |
| /    | 0   | +             | [3,5]     |
| 2    | 2   | /             | [3,5]     |
| -    | 0   | /             | [3,2]     |
| 4    | 4   | -             | [3,2]     |
| *    | 0   | -             | [3,2,-4]  |
| 3    | 3   | *             | [3,2,-4]  |
| End  | 0   | *             | [3,2,-12] |

Final answer

```
3 + 2 - 12 = -7
```

---

# 9. Related Problems

### Easy

* **150. Evaluate Reverse Polish Notation** — Stack-based expression evaluation without precedence handling.

### Medium

* **224. Basic Calculator** — Introduces parentheses with only `+` and `-`.

* **71. Simplify Path** — Uses a stack to process sequential tokens and simplify state.

* **856. Score of Parentheses** — Stack-based parsing of structured expressions.

### Hard

* **772. Basic Calculator III** — Extends this problem to include both operator precedence and nested parentheses, requiring recursive parsing or multiple stacks.

---

# Interview Recognition Cheat Sheet

| If you see...          | Think...                                 |
| ---------------------- | ---------------------------------------- |
| `+ - * /` expression   | Stack + previous operator                |
| `*` and `/` precedence | Update the last stack value immediately  |
| Multi-digit numbers    | Build `num = num * 10 + digit`           |
| Spaces                 | Ignore them                              |
| Integer division       | Use `int(a / b)` to truncate toward zero |
| Final answer           | `sum(stack)`                             |
