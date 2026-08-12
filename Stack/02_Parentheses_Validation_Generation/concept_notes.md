# Valid / Add / Remove Parentheses — Stack Pattern (Interview Revision)

---

# 1. Pattern in One Minute

### Core Idea

Whenever you need to verify, repair, or generate a valid parentheses/bracket sequence, the **stack** is the natural data structure because it remembers the **most recent unmatched opening bracket**.

Think of it as:

> Every closing bracket must match the latest unmatched opening bracket.

LIFO perfectly models nested structures.

### Why does this pattern exist?

Nested expressions always require remembering the last opened scope.

Examples:

* `()`
* `([])`
* `{[()]}`

The newest opening bracket must close first.

### Immediately think of this pattern when

* Parentheses/Brackets
* Nested expressions
* Balanced symbols
* Removing invalid brackets
* Longest valid parentheses
* Minimum additions/removals
* Expression parsing

---

# 2. Recognition Signals

### Strong clues

* `()`, `{}`, `[]`
* "Valid parentheses"
* "Balanced brackets"
* "Nested"
* "Expression"
* "Need matching pair"
* "Remove minimum"
* "Longest valid substring"

### Common disguises

* HTML/XML tags
* Function calls
* Mathematical expressions
* Nested folders
* Nested recursion
* Compiler parsing

### When NOT to use Stack

Don't use stack if:

* Parentheses depth isn't important.
* Only counts matter.

Example:

Minimum Add to Make Parentheses Valid

Only `(` and `)` exist.

A counter solution works in O(1) space.

---

# 3. Mental Model

Remember these bullets:

* Every opening bracket waits.
* Push opening brackets.
* Closing bracket tries to match top.
* Wrong type → invalid.
* Empty stack on closing → invalid.
* Finish with empty stack → valid.
* Stack stores **unmatched openings**.
* Most recent opening closes first.
* Nested = LIFO.

---

# 4. Boilerplate Template (Python)

```python
stack = []

pairs = {
    ')': '(',
    ']': '[',
    '}': '{'
}

for ch in s:

    if ch in "([{":
        stack.append(ch)

    else:
        if not stack:
            return False

        if stack[-1] != pairs[ch]:
            return False

        stack.pop()

return len(stack) == 0
```

### Complexity

* Time → **O(n)**
* Space → **O(n)**

---

# 5. Variations

| Variation                              | Change                      |
| -------------------------------------- | --------------------------- |
| Valid Parentheses                      | Store opening brackets      |
| Remove Invalid Parentheses             | DFS/BFS + validation        |
| Minimum Remove to Make Valid           | Store indices in stack      |
| Minimum Add to Make Valid              | Counter or stack            |
| Longest Valid Parentheses              | Stack of indices            |
| Score of Parentheses                   | Stack of scores             |
| Reverse Substrings Between Parentheses | Stack of strings            |
| Decode String                          | Stack of numbers + strings  |
| Basic Calculator                       | Stack for expression states |

---

# 6. Common Pitfalls

### ❌ Forgetting empty stack check

Wrong

```python
stack.pop()
```

Correct

```python
if not stack:
    return False
```

---

### ❌ Matching wrong bracket

```
([)]
```

Need mapping dictionary.

---

### ❌ Forgetting leftover openings

```
(((
```

Need

```python
return not stack
```

---

### ❌ Using characters instead of indices

Problems like

* Longest Valid Parentheses
* Minimum Remove

need

```python
stack.append(index)
```

not

```python
stack.append(char)
```

---

### ❌ Not pushing sentinel (-1)

Longest Valid Parentheses requires

```python
stack = [-1]
```

Otherwise length calculation breaks.

---

# 7. Interview Checklist

✅ Problem involves brackets

✅ Nested structure

✅ Need matching pair

✅ Recent opening matters

➡️ Use Stack

---

If the question asks

* minimum remove
* longest valid
* repair expression

Think:

> "Should I store characters or indices?"

---

# 8. Must-Do Problems

## ⭐ Top 3 (Enough for Revision)

1. ✅ **20. Valid Parentheses** ⭐⭐⭐
2. ✅ **1249. Minimum Remove to Make Valid Parentheses** ⭐⭐⭐
3. ✅ **32. Longest Valid Parentheses** ⭐⭐⭐

---

## Easy

* 20. Valid Parentheses ⭐⭐⭐
* 921. Minimum Add to Make Parentheses Valid

---

## Medium

* 1249. Minimum Remove to Make Valid Parentheses ⭐⭐⭐
* 856. Score of Parentheses
* 1190. Reverse Substrings Between Each Pair of Parentheses
* 678. Valid Parenthesis String *(Greedy/DP—not pure stack)*

---

## Hard

* 32. Longest Valid Parentheses ⭐⭐⭐
* 301. Remove Invalid Parentheses

---

# 9. 30-Second Cheat Sheet

## Recognition

* Parentheses
* Matching pairs
* Nested expressions
* Balanced brackets
* Repair/remove invalid
* Longest valid

---

## Core Idea

Stack stores **unmatched opening brackets** (or indices). Every closing bracket must match the **top**.

---

## Generic Template

```python
for ch in s:
    if opening:
        push
    else:
        if invalid:
            return False
        pop

return stack empty
```

---

## Complexity

* **Time:** O(n)
* **Space:** O(n)

---

## Common Variations

* Valid Parentheses → Characters
* Longest Valid → Indices + sentinel `-1`
* Minimum Remove → Indices
* Minimum Add → Counter/Stack
* Remove Invalid → BFS/DFS + validation

---

## Pitfalls

* ❌ Pop empty stack
* ❌ Wrong bracket mapping
* ❌ Forget leftover openings
* ❌ Use characters when indices are required
* ❌ Forget sentinel in Longest Valid Parentheses

---

## Pattern Mnemonic

> **"Open → Push, Close → Match & Pop."**

If you ever need to **remember an unmatched opening until its corresponding closing appears**, you're almost certainly looking at the **Parentheses Stack Pattern**.
