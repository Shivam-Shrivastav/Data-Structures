# 20. Valid Parentheses (Stack)

## 1. Problem Statement

Given a string `s` containing only the characters:

* `'('`, `')'`
* `'{'`, `'}'`
* `'['`, `']'`

Determine if the input string is **valid**.

A string is valid if:

1. Every opening bracket has a corresponding closing bracket of the same type.
2. Brackets close in the correct order.
3. Every closing bracket has a matching opening bracket.

### Constraints

* `1 <= s.length <= 10^4`
* `s` consists only of `'()[]{}'`.

---

## Example

```
Input:
s = "()[]{}"

Output:
True

Explanation:
Each opening bracket is closed by the correct bracket in the proper order.
```

---

# 2. Diagram

### Example: `"({[]})"`

```
Read '('  -> Stack: (

Read '{'  -> Stack: ( {

Read '['  -> Stack: ( { [

Read ']'  -> '[' matches
             Stack: ( {

Read '}'  -> '{' matches
             Stack: (

Read ')'  -> '(' matches
             Stack: empty

Result = Valid
```

---

### Invalid Example

```
Input: "(]"

Read '(' -> Stack: (

Read ']'

Expected ')' but found ']'

Invalid
```

---

# 3. Example I/O

### Example 1 (Typical)

```
Input:
s = "()[]{}"

Output:
True
```

Explanation:

```
()   ✓
[]   ✓
{}   ✓
```

Everything matches.

---

### Example 2

```
Input:
s = "([)]"

Output:
False
```

Explanation:

```
Expected:

(
  [
  ]
)

Actual:

(
  [
  )
```

The order is wrong.

---

### Example 3 (Edge Case)

```
Input:
s = "]"

Output:
False
```

Explanation:

Closing bracket appears before any opening bracket.

---

### Example 4

```
Input:
s = ""

Output:
True
```

(If empty strings were allowed, they are considered valid.)

---

# 4. Intuition & Pattern Recognition

## Interview Hint

Whenever a problem asks:

* matching symbols
* nested expressions
* balanced parentheses
* XML tags
* undo operations

Think:

> **STACK**

---

### Why?

The most recently opened bracket must be closed first.

That is exactly **Last In First Out (LIFO).**

Example:

```
({[]})

Open:
(
{
[

Must close:

]
}
)

Reverse order.

Stack naturally stores this.
```

---

### Interview Thinking

> "Every opening bracket waits for its closing bracket."

Where should it wait?

**Inside a stack.**

---

# 5. Simpler Version

## Simpler Problem

Only `'('` and `')'`.

Example:

```
(()())
```

Solution:

* Push '('
* Pop when ')' arrives

Easy.

---

## Next Level

Now introduce:

```
[]
{}
```

Instead of checking only `'('`, we must check **matching types**.

So we keep a dictionary:

```
')' -> '('
']' -> '['
'}' -> '{'
```

Everything else remains exactly the same.

---

## Simpler LeetCode Problems

### Easy

**20. Valid Parentheses** ← Current

---

### Similar

**1047. Remove All Adjacent Duplicates**

Uses stack for removing previous characters.

---

### Similar

**1544. Make The String Great**

Remove adjacent opposite-case letters using stack.

---

### Harder

**32. Longest Valid Parentheses**

Uses stack but computes longest valid substring.

---

### Hardest

**301. Remove Invalid Parentheses**

Uses BFS + parentheses validation.

---

# Simpler Thinking → Current Thinking

```
Only ()

↓

Need multiple bracket types

↓

Need to remember opening brackets

↓

Need latest opening bracket first

↓

Use Stack

↓

Compare using mapping
```

---

# 6. Brute Force

Idea:

Repeatedly remove:

```
()
[]
{}
```

until no more changes occur.

If string becomes empty → valid.

Otherwise invalid.

### Time Complexity

```
O(n²)
```

### Space Complexity

```
O(n)
```

Not efficient.

---

# 7. Optimal Solution (Stack)

### Algorithm

1. Create empty stack.
2. Traverse string.
3. If opening bracket:

   * Push.
4. Else:

   * Stack empty → False
   * Top doesn't match → False
   * Else pop.
5. End:

   * Stack empty → True

---

### Python Code

```python
class Solution:
    def isValid(self, s: str) -> bool:

        # Maps each closing bracket to its matching opening bracket
        matching = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        stack = []

        for ch in s:

            # Opening bracket
            if ch not in matching:
                stack.append(ch)

            else:
                # No opening bracket available
                if not stack:
                    return False

                # Top doesn't match expected opening bracket
                if stack[-1] != matching[ch]:
                    return False

                # Correct match
                stack.pop()

        # Valid only if no unmatched opening brackets remain
        return len(stack) == 0
```

---

### Time Complexity

```
O(n)
```

Each bracket is pushed and popped at most once.

---

### Space Complexity

```
O(n)
```

Worst case:

```
((((((((
```

All opening brackets remain in stack.

---

# 8. Step-by-Step Trace

Example:

```
s = "({[]})"
```

| Step | Character | Stack Before | Action  | Stack After |
| ---- | --------- | ------------ | ------- | ----------- |
| 1    | (         | []           | Push    | [(]         |
| 2    | {         | [(]          | Push    | [(,{]       |
| 3    | [         | [(,{]        | Push    | [(,{,[]     |
| 4    | ]         | [(,{,[]      | Pop `[` | [(,{]       |
| 5    | }         | [(,{]        | Pop `{` | [(]         |
| 6    | )         | [(]          | Pop `(` | []          |

End:

```
Stack empty

Return True
```

---

### Invalid Example

```
s = "([)]"
```

| Step | Character | Stack      |
| ---- | --------- | ---------- |
| 1    | (         | (          |
| 2    | [         | ( [        |
| 3    | )         | Top is '[' |

Expected:

```
(
```

Found:

```
[
```

Mismatch → False immediately.

---

# 9. Related Problems

### 1. LeetCode 1047 — Remove All Adjacent Duplicates in String (Easy)

Uses a stack to remove adjacent duplicate characters by comparing with the top of the stack.

---

### 2. LeetCode 1544 — Make The String Great (Easy)

Uses a stack to remove adjacent letters that differ only in case.

---

### 3. LeetCode 71 — Simplify Path (Medium)

Uses a stack to process directory names and `".."` operations while building the canonical path.

---

### 4. LeetCode 32 — Longest Valid Parentheses (Hard)

Uses a stack (or DP) to find the length of the longest valid parentheses substring instead of just validating.

---

### 5. LeetCode 301 — Remove Invalid Parentheses (Hard)

Builds on the validation concept by removing the minimum number of parentheses to generate all valid strings.

---

# Interview Cheat Sheet

### Recognition

* Matching symbols
* Nested structure
* Correct closing order
* Balanced expressions

→ **Use a Stack**

---

### Core Idea

```
Opening bracket
    ↓
Push into stack

Closing bracket
    ↓
Must match stack top

Mismatch
    ↓
False

Stack empty at end
    ↓
True
```

---

### Pattern Template

```python
stack = []

for ch in s:
    if opening:
        stack.append(ch)
    else:
        if not stack:
            return False
        if stack[-1] != expected:
            return False
        stack.pop()

return not stack
```

**Key takeaway:** This is the canonical **Stack** problem. The moment you see *balanced brackets*, *nested expressions*, or *LIFO matching*, your first instinct should be to use a stack with a mapping from closing brackets to their corresponding opening brackets.
