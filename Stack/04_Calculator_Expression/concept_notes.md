# Calculator Expression Pattern (Stack)

This is one of the most common **Stack interview sub-patterns**. It covers problems where you evaluate mathematical expressions while respecting **operator precedence**, **parentheses**, and **sign propagation**.

---

# 1. Pattern in One Minute

### Core Idea

Instead of evaluating the expression left-to-right, **use a stack to remember previous state** (numbers, operators, signs, or partial results) whenever the expression structure changes.

The stack acts like the program's call stack.

---

### Why does this pattern exist?

Expressions are **hierarchical**, not linear.

Example:

```text
2 + (3 - (4 + 5))
```

You cannot compute the outer expression until the inner one finishes.

The stack stores the unfinished computation.

---

### When should I immediately think of it?

Whenever the problem contains

* `+ - * /`
* parentheses
* nested expressions
* expression evaluation
* calculators
* Reverse Polish Notation (RPN)

---

# 2. Recognition Signals

## Strong clues

✅ Arithmetic expression

```text
"1+2-3"
```

---

✅ Parentheses

```text
"(1+(4+5)-3)"
```

---

✅ Different operator precedence

```text
2+3*4
```

---

✅ Nested evaluation

```text
1-(2-(3+4))
```

---

✅ Parse while scanning once

Usually O(n)

---

## Common disguises

Instead of saying calculator, they may say

* Evaluate expression
* Parse arithmetic
* Expression parser
* Mathematical interpreter

---

## When NOT to use

If expression already comes in

* Postfix (RPN) → easier stack
* Prefix
* AST given

No need for calculator parsing.

---

# 3. Mental Model

Think of reading expression character by character.

```
3 + 5 * 2
```

As you scan:

```
number
↓

operator
↓

next number
↓

evaluate if possible
```

---

With parentheses

```
2+(3-4)

outside
↓

(
save current answer
save sign

↓

solve inside

↓

combine back
```

The stack stores

```
previous answer

previous sign
```

---

For precedence

```
2+3*4

cannot compute +

must wait

compute *

first
```

The stack delays low-priority operators.

---

Remember

> **Parentheses change scope.**
> **Stack remembers previous scope.**

---

# 4. Boilerplate Templates

## Template 1 — Basic Calculator I (+, -, parentheses)

LeetCode 224

```python
stack = []
num = 0
result = 0
sign = 1

for ch in s:

    if ch.isdigit():
        num = num * 10 + int(ch)

    elif ch in "+-":
        result += sign * num
        num = 0
        sign = 1 if ch == '+' else -1

    elif ch == "(":
        stack.append(result)
        stack.append(sign)

        result = 0
        sign = 1

    elif ch == ")":
        result += sign * num
        num = 0

        prev_sign = stack.pop()
        prev_result = stack.pop()

        result = prev_result + prev_sign * result

result += sign * num
```

---

## Template 2 — Basic Calculator II (+ - * /)

LeetCode 227

Use stack to handle precedence.

```python
stack = []
num = 0
op = "+"

for ch in s + "+":

    if ch.isdigit():
        num = num*10 + int(ch)

    elif ch == " ":
        continue

    else:

        if op == "+":
            stack.append(num)

        elif op == "-":
            stack.append(-num)

        elif op == "*":
            stack.append(stack.pop()*num)

        elif op == "/":
            stack.append(int(stack.pop()/num))

        op = ch
        num = 0

answer = sum(stack)
```

Key trick:

```
+,- → push

*,/ → immediately evaluate
```

---

## Template 3 — RPN

```python
for token in tokens:

    if number:
        stack.append(num)

    else:
        b = stack.pop()
        a = stack.pop()

        stack.append(eval(a,b))
```

---

# 5. Variations

| Problem                           | Change                           |
| --------------------------------- | -------------------------------- |
| Basic Calculator I                | parentheses only                 |
| Basic Calculator II               | precedence                       |
| Basic Calculator III              | precedence + parentheses         |
| Evaluate RPN                      | operands already ordered         |
| Different Ways to Add Parentheses | recursion + divide & conquer     |
| Parse Boolean Expression          | same parsing idea with operators |

---

# 6. Common Pitfalls

### Forgetting last number

Need

```python
result += sign * num
```

after loop.

---

### Multi-digit numbers

Wrong

```python
num = int(ch)
```

Correct

```python
num = num*10 + int(ch)
```

---

### Integer division

LeetCode expects

```python
int(a / b)
```

NOT

```python
a // b
```

because negatives differ.

---

### Parentheses order

Push

```
result

sign
```

Pop

```
sign

result
```

Reverse order causes bugs.

---

### Ignoring spaces

Always

```python
if ch == " ":
    continue
```

---

# 7. Interview Checklist

✓ Expression parsing?

✓ Contains `+ - * /`?

✓ Parentheses?

✓ Need precedence?

✓ Scan once?

✓ Need previous computation after parentheses?

→ Use Stack.

---

# 8. Must-Do Problems

### ⭐ Top 3 (Enough for Revision)

1. Basic Calculator ⭐⭐⭐
2. Basic Calculator II ⭐⭐⭐
3. Basic Calculator III ⭐⭐⭐

---

### Easy

* Evaluate Reverse Polish Notation

---

### Medium

* Basic Calculator II
* Ternary Expression Parser (Premium)

---

### Hard

* Basic Calculator III
* Different Ways to Add Parentheses

---

# 9. 30-Second Cheat Sheet

### Recognition

* Expression parsing
* `+ - * /`
* Parentheses
* Nested calculations
* Operator precedence

---

### Core Idea

* Scan once.
* Build multi-digit numbers.
* Store unfinished computations on a stack.
* Evaluate immediately for high-precedence operators.
* Restore previous context after `)`.

---

### Templates

* **224** → `result + sign + stack`
* **227** → `number stack`
* **772** → Combine both ideas (precedence + parentheses)
* **150** → Operand stack

---

### Complexity

* **Time:** O(n)
* **Space:** O(n)

---

### Variations

* Parentheses only
* Operator precedence
* Parentheses + precedence
* Reverse Polish Notation
* Recursive expression parsing

---

### Pitfalls

* ❌ Forget final number
* ❌ Incorrect multi-digit parsing
* ❌ Use `//` instead of `int(a/b)` for division
* ❌ Pop stack in wrong order
* ❌ Forget to skip spaces

---

## Pattern Insight

Although these problems look different, nearly all calculator questions reduce to one of **three stack strategies**:

1. **Context Stack** → Save `(result, sign)` when entering parentheses (Calculator I).
2. **Operand Stack** → Push numbers; immediately resolve `*` and `/` while delaying `+` and `-` (Calculator II).
3. **Combined Stack** → Use both context restoration and precedence handling for nested expressions (Calculator III).

If you can recognize **which of these three strategies** the problem requires, you've effectively mastered the entire calculator-expression family.
