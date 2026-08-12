# Decode String (Stack Pattern)

> LeetCode 394 — **Decode String**

This is a **Stack Simulation** pattern. The stack is used to **remember the previous state** whenever we enter a new bracketed expression.

---

# 1. Pattern in One Minute

### Core Idea

Whenever you see an opening bracket `[`, you need to remember:

* the string built so far
* the repetition count

Then start building the inner string.

When you reach `]`, restore the previous state from the stack and append:

```
previous_string + current_string * repeat_count
```

---

### Why does this pattern exist?

Nested brackets create **nested contexts**.

Example:

```
3[a2[c]]
```

When you start decoding `2[c]`, you must temporarily pause building `"a"`.

A stack naturally stores these paused contexts.

---

### Think of this pattern when

* Nested encoded strings
* Parentheses/brackets
* Need to pause current computation
* Need to restore previous state later

---

# 2. Recognition Signals

### Keywords

* Decode
* Nested
* Parentheses
* Brackets
* Repeat k times

---

### Constraints

```
3[a]
2[abc]
3[a2[c]]
```

Nested expressions.

---

### Common disguises

* Arithmetic expressions
* XML tags
* Nested folders
* Parentheses parsing
* String expansion

---

### Don't use this if

No nesting exists.

Example

```
aaaaabbb
```

No stack required.

---

# 3. Mental Model

Imagine reading left to right.

Maintain

```
current_string
current_number
```

Whenever

```
[
```

means

> "Pause here."

Push everything.

```
Stack

(count, previous_string)
```

Reset.

```
current_string = ""
current_number = 0
```

Now decode inside.

---

Whenever

```
]
```

means

> "Resume previous work."

Pop

```
count
previous_string
```

Compute

```
current_string = previous_string + current_string * count
```

Continue.

---

# Example

```
3[a2[c]]
```

Initial

```
curr = ""
num = 0
stack = []
```

Read

```
3
```

```
num = 3
```

Read

```
[
```

Push

```
(3,"")
```

Reset

```
curr=""
num=0
```

---

Read

```
a
```

```
curr="a"
```

---

Read

```
2
```

```
num=2
```

---

Read

```
[
```

Push

```
(2,"a")
```

Reset

```
curr=""
```

---

Read

```
c
```

```
curr="c"
```

---

Read

```
]
```

Pop

```
(2,"a")
```

Compute

```
curr="a"+"c"*2

acc
```

---

Read

```
]
```

Pop

```
(3,"")
```

Compute

```
curr=""+"acc"*3

accaccacc
```

Done.

---

# 4. Boilerplate Template (Python)

```python
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        curr = ""
        num = 0

        for ch in s:

            if ch.isdigit():
                num = num * 10 + int(ch)

            elif ch == '[':
                stack.append((num, curr))
                curr = ""
                num = 0

            elif ch == ']':
                repeat, prev = stack.pop()
                curr = prev + curr * repeat

            else:
                curr += ch

        return curr
```

---

## Complexity

```
Time:
O(n + output_length)

Space:
O(depth)
```

(Output size dominates if expansion is large.)

---

# 5. Variations

| Variation                     | Change                                  |
| ----------------------------- | --------------------------------------- |
| Decode String                 | Standard pattern                        |
| Nested parentheses evaluation | Store previous state                    |
| Basic Calculator              | Push previous result and sign           |
| Mini Parser                   | Build nested objects instead of strings |
| Ternary Expression Parser     | Store pending expressions               |

---

# 6. Common Pitfalls

### ❌ Forgetting multi-digit numbers

Wrong

```python
num = int(ch)
```

Correct

```python
num = num * 10 + int(ch)
```

Handles

```
12[a]
```

---

### ❌ Not resetting after '['

Must

```python
curr = ""
num = 0
```

Otherwise inner strings mix with outer ones.

---

### ❌ Pushing only count

Need BOTH

```
(count, previous_string)
```

Otherwise you lose outer context.

---

### ❌ Wrong concatenation order

Wrong

```python
curr = curr * count + prev
```

Correct

```python
curr = prev + curr * count
```

---

# 7. Interview Checklist

✓ Input contains nested brackets

✓ Need to pause current work

✓ Need to resume later

✓ Previous context must be remembered

✓ Stack stores **(count, previous_string)**

---

# 8. Must-Do Problems

### ⭐ Top 3

1. **394. Decode String** ⭐⭐⭐
2. **224. Basic Calculator** ⭐⭐⭐
3. **385. Mini Parser** ⭐⭐⭐

---

### Easy

* 20. Valid Parentheses

---

### Medium

* 394. Decode String ⭐
* 224. Basic Calculator ⭐
* 227. Basic Calculator II
* 71. Simplify Path

---

### Hard

* 772. Basic Calculator III
* 726. Number of Atoms

---

# 9. 30-Second Cheat Sheet

### Recognition

* Nested brackets
* String expansion
* Save and restore context

### Core Idea

Push state at `'['`:

```text
(count, previous_string)
```

Pop state at `']'`:

```text
previous_string + current_string * count
```

### Template

```python
digit  -> build number
'['    -> push (num, curr), reset
letter -> append
']'    -> pop and combine
```

### Complexity

* Time: **O(n + output_length)**
* Space: **O(depth)**

### Variations

* Decode String
* Basic Calculator
* Mini Parser
* Simplify Path
* Number of Atoms

### Pitfalls

* Handle multi-digit numbers (`num = num * 10 + digit`)
* Reset `curr` and `num` after `'['`
* Push both count and previous string
* Combine as `prev + curr * count`
