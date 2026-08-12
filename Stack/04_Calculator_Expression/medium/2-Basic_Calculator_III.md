# **772. Basic Calculator III**

---

# 1. Problem Statement

Given a string `s` representing a valid mathematical expression, return the result after evaluating it.

The expression may contain:

* Non-negative integers
* Operators: `+`, `-`, `*`, `/`
* Parentheses `(` and `)`
* Spaces

Division truncates toward zero.

Unlike **Basic Calculator II**, this problem also supports **nested parentheses**, so expressions inside parentheses must be evaluated before applying the outer operations.

---

### Constraints

* `1 <= s.length <= 10^4`
* Expression is always valid.
* No use of `eval()`.

---

### Example

```text
Input:
s = "2*(5+5*2)/3+(6/2+8)"

Output:
21

Explanation:

(5+5*2)
= 5+10
=15

2*15=30

30/3=10

(6/2+8)
=3+8
=11

10+11=21
```

---

# 2. Diagram

Expression

```text
2 * (5 + 5 * 2) / 3 + (6 / 2 + 8)
```

```text
Main Expression
│
├── (5 + 5 * 2)
│      │
│      ├── 5
│      ├── +
│      └── 5*2
│             │
│             ├──5
│             └──2
│
└── (6/2+8)
       │
       ├──6/2
       └──+8
```

Think of every parenthesis as **a completely new Basic Calculator II problem**.

---

# 3. Example I/O

## Example 1

```text
Input:
"2*(5+5*2)/3+(6/2+8)"

Output:
21
```

---

## Example 2

```text
Input:
"(2+6*3+5-(3*14/7+2)*5)+3"

Output:
-12
```

---

## Edge Case

```text
Input:
"7"

Output:
7
```

---

# 4. Intuition & Pattern Recognition

## Recognition

Whenever you see

* `+`
* `-`
* `*`
* `/`
* **Parentheses**

immediately think

> **Recursion + Stack**

Why?

Because

```text
(....)
```

is simply

> another expression.

So whenever you reach

```text
(
```

start solving that sub-expression independently.

When you reach

```text
)
```

return its value to the caller.

---

### Mental Model

```
Basic Calculator II
        +
Parentheses
=
Recursion
```

This is exactly how compilers evaluate expressions.

---

# 5. Simpler Version

## Simpler Question 1

### 224. Basic Calculator

Supports

```
+
-
()
```

Need recursion because of parentheses.

---

## Simpler Question 2

### 227. Basic Calculator II

Supports

```
+
-
*
/
```

Need stack because of precedence.

---

## Current Problem

Need BOTH

```
+
-
*
/
()
```

So combine

```
224
+
227
=
772
```

---

### Progression

```
Only +,-

↓

Parentheses

↓

+ - * /

↓

Parentheses + Precedence
```

---

# 6. Brute Force

Idea

Repeatedly

* Find innermost parentheses
* Evaluate
* Replace string
* Repeat

Then solve remaining expression.

This involves many string rebuilds.

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

# 7. Optimal Solution

## Core Idea

Exactly like Basic Calculator II.

Only difference:

Whenever we encounter

```
(
```

we recursively compute its value.

Whenever recursion reaches

```
)
```

it returns the computed number.

---

## Flow

```
Read character

digit
↓

build number

operator
↓

apply previous sign

(
↓

solve recursively

)

↓

return answer
```

---

## Python Solution

```python
class Solution:
    def calculate(self, s: str) -> int:

        def helper(i):
            stack = []
            num = 0
            sign = '+'

            while i < len(s):
                ch = s[i]

                if ch.isdigit():
                    num = num * 10 + int(ch)

                elif ch == '(':
                    # Evaluate the sub-expression recursively
                    num, i = helper(i + 1)

                # Process the previous operator when we hit
                # an operator, a closing parenthesis, or the end
                if ((not ch.isdigit() and ch != ' ')
                        or i == len(s) - 1):

                    if sign == '+':
                        stack.append(num)

                    elif sign == '-':
                        stack.append(-num)

                    elif sign == '*':
                        stack.append(stack.pop() * num)

                    elif sign == '/':
                        stack.append(int(stack.pop() / num))

                    # If current character closes this level,
                    # return the evaluated result
                    if ch == ')':
                        return sum(stack), i

                    sign = ch
                    num = 0

                i += 1

            return sum(stack), i

        return helper(0)[0]
```

---

## Complexity

Time

```
O(n)
```

Every character is processed once.

Space

```
O(n)
```

For recursion stack + evaluation stack.

---

# 8. Step-by-Step Trace

Expression

```
2*(5+5*2)
```

---

### Level 1

```
stack = []

2

operator *

stack = [2]
```

Encounter

```
(
```

Recursive call.

---

### Level 2

Expression

```
5+5*2
```

```
stack=[]

5

+

stack=[5]

5

*

stack=[5,5]

2

)

multiply

stack=[5,10]

sum=15
```

Return

```
15
```

---

### Back to Level 1

```
2 * 15

stack=[30]
```

End

```
30
```

---

# 9. Related Problems

| Problem                                    | Connection                                                          |
| ------------------------------------------ | ------------------------------------------------------------------- |
| **224. Basic Calculator**                  | Parentheses + recursion, but only `+` and `-`.                      |
| **227. Basic Calculator II**               | Operator precedence with `+`, `-`, `*`, `/`, but no parentheses.    |
| **150. Evaluate Reverse Polish Notation**  | Stack-based evaluation of expressions in postfix form.              |
| **241. Different Ways to Add Parentheses** | Recursively evaluate expressions in all possible parenthesizations. |
| **726. Number of Atoms**                   | Recursive parsing of nested structures using parentheses.           |

---

# Interview Recognition Cheat Sheet

| If you see...    | Think...                                                          |
| ---------------- | ----------------------------------------------------------------- |
| `+ - * /`        | Use the Basic Calculator II stack strategy                        |
| Parentheses `()` | Solve recursively; each pair defines a new sub-expression         |
| `(`              | Start a recursive call and treat its result as the current number |
| `)`              | Finish the current recursive level and return its computed value  |
| `*` / `/`        | Apply immediately to the top of the stack                         |
| Final answer     | Sum the stack at the current recursion level                      |

## Relationship Between the Calculator Problems

```text
224. Basic Calculator
(+, -, ())
        │
        ▼
227. Basic Calculator II
(+, -, *, /)
        │
        ▼
772. Basic Calculator III
(+, -, *, /, ())
```

A useful interview insight is to view **Basic Calculator III** as a combination of the previous two problems:

* **227** contributes the **operator precedence** logic using a stack.
* **224** contributes the **recursive handling of parentheses**.

Combining these two ideas yields an `O(n)` solution that processes each character only once.
