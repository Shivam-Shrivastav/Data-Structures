# 150. Evaluate Reverse Polish Notation (Stack)

---

# 1. Problem Statement

Given an array of strings `tokens` representing an arithmetic expression in **Reverse Polish Notation (RPN)**, evaluate the expression and return its value.

In Reverse Polish Notation:

* Every operand appears before its operator.
* Valid operators are:

  * `+`
  * `-`
  * `*`
  * `/`
* Division should truncate toward **zero**.
* The input is always valid.
* There is no division by zero.

### Constraints

* `1 <= tokens.length <= 10⁴`
* Tokens are either:

  * an integer
  * one of `+`, `-`, `*`, `/`
* Expression is guaranteed to be valid.

---

## Example

```
Input:
["2","1","+","3","*"]

Output:
9
```

Explanation

```
(2 + 1) * 3 = 9
```

---

# 2. Diagram

Think of the stack as holding numbers waiting to be combined.

Example:

```
Tokens

["2","1","+","3","*"]
```

```
Read 2

Stack

┌───┐
│ 2 │
└───┘
```

```
Read 1

┌───┐
│ 1 │
├───┤
│ 2 │
└───┘
```

```
Read +

Pop

1
2

Compute

2 + 1 = 3

Push 3

┌───┐
│ 3 │
└───┘
```

```
Read 3

┌───┐
│ 3 │
├───┤
│ 3 │
└───┘
```

```
Read *

Pop

3
3

3 * 3 = 9

Push

┌───┐
│ 9 │
└───┘
```

Answer = Top of stack.

---

# 3. Example I/O

### Example 1

```
Input

["2","1","+","3","*"]

Output

9
```

Explanation

```
2 + 1 = 3

3 * 3 = 9
```

---

### Example 2

```
Input

["4","13","5","/","+"]

Output

6
```

Explanation

```
13 / 5 = 2

4 + 2 = 6
```

---

### Example 3 (Edge Case)

```
Input

["10"]

Output

10
```

Only one number.

---

# 4. Intuition & Pattern Recognition

### Interview Hint

Whenever you see:

> "Evaluate an expression"

or

> "Postfix / Reverse Polish"

Immediately think:

> **Stack**

Because operators always work on the **last two operands** seen so far.

---

### Why Stack?

Whenever an operator appears:

```
a b +
```

the operator needs

```
a
b
```

which are exactly the last two numbers stored.

LIFO = perfect.

---

### Recognition Pattern

Problems involving:

* postfix expression
* parsing expressions
* matching operands/operators
* undoing recent operations

usually use a **stack**.

---

# 5. Simpler Version

### Simpler Problem

Suppose the expression contains only numbers.

```
["2","3","4"]
```

Just push everything.

```
Stack

2

2 3

2 3 4
```

Easy.

---

Now introduce an operator.

```
2 3 +
```

Need the last two numbers.

```
pop

3

pop

2

2+3

push 5
```

Repeat until finished.

---

### Simpler Questions Leading Here

1. Implement Stack
2. Valid Parentheses
3. Baseball Game (682) → stack simulation
4. Min Stack → stack with metadata
5. Evaluate Reverse Polish Notation → stack evaluation

---

# 6. Brute Force

Without using a stack:

* Scan tokens.
* Find the first operator.
* Evaluate its previous two operands.
* Replace them with the result.
* Repeat until one element remains.

Example

```
2 1 + 3 *

↓

3 3 *

↓

9
```

Each replacement shifts elements.

### Complexity

Time:

```
O(n²)
```

Space:

```
O(1)
```

(or O(n) depending on implementation)

---

# 7. Optimal Solution

### Idea

* If token is a number → push it.
* If token is an operator:

  * Pop second operand (`b`)
  * Pop first operand (`a`)
  * Compute `a op b`
  * Push result

> **Important:** For `-` and `/`, operand order matters.

### Python

```python
class Solution:
    def evalRPN(self, tokens):
        stack = []

        for token in tokens:

            # If token is an operator
            if token in "+-*/":
                b = stack.pop()   # second operand
                a = stack.pop()   # first operand

                if token == "+":
                    stack.append(a + b)

                elif token == "-":
                    stack.append(a - b)

                elif token == "*":
                    stack.append(a * b)

                else:
                    # Division truncated toward zero
                    stack.append(int(a / b))

            else:
                # Push number onto stack
                stack.append(int(token))

        return stack[-1]
```

---

### Why `int(a / b)`?

Python's `//` performs **floor division**, which is **not** what the problem asks.

Example

```
-3 // 2 = -2 ❌
```

But the problem wants

```
-3 / 2 = -1.5

truncate toward zero

= -1 ✅
```

Using

```python
int(a / b)
```

achieves this.

---

### Complexity

Time

```
O(n)
```

Space

```
O(n)
```

---

# 8. Step-by-Step Trace

Example

```
["4","13","5","/","+"]
```

| Token | Stack    | Action     |
| ----- | -------- | ---------- |
| 4     | [4]      | push       |
| 13    | [4,13]   | push       |
| 5     | [4,13,5] | push       |
| /     | [4,2]    | 13 ÷ 5 = 2 |
| +     | [6]      | 4 + 2      |

Final Answer

```
6
```

---

## Another Trace

```
["2","1","+","3","*"]
```

| Token | Stack |
| ----- | ----- |
| 2     | [2]   |
| 1     | [2,1] |
| +     | [3]   |
| 3     | [3,3] |
| *     | [9]   |

Answer

```
9
```

---

# 9. Related Problems

| Problem                      | Connection                                                   |
| ---------------------------- | ------------------------------------------------------------ |
| **20. Valid Parentheses**    | Basic stack operations.                                      |
| **682. Baseball Game**       | Stack simulation with arithmetic updates.                    |
| **155. Min Stack**           | Stack storing additional information.                        |
| **224. Basic Calculator**    | Stack-based expression evaluation with parentheses.          |
| **227. Basic Calculator II** | Stack + operator precedence while parsing infix expressions. |

---

# Interview Takeaway

Whenever you see:

> **"Evaluate a postfix / Reverse Polish expression"**

Think:

* **Numbers → Push**
* **Operator → Pop two numbers**
* **Compute**
* **Push result back**

### Core Algorithm

```
For each token:

If number:
    push

Else:
    b = pop()
    a = pop()

    push(a op b)

Return top
```

The crucial interview detail is to **pop `b` first, then `a`**, because subtraction and division are **not commutative**, and to use **`int(a / b)`** in Python so division truncates toward **zero** as required.
