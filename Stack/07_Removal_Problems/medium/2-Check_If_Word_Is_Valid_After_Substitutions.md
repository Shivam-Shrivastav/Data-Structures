# **1003. Check If Word Is Valid After Substitutions**

## 1. Problem Statement

Given a string `s`, determine whether it can be obtained by repeatedly inserting the string `"abc"` into an initially empty string.

Equivalently, you can repeatedly remove any occurrence of `"abc"` from `s`. If the string becomes empty after all possible removals, return `True`; otherwise, return `False`.

### Constraints

* `1 <= s.length <= 2 × 10^4`
* `s` consists only of `'a'`, `'b'`, and `'c'`.

The large input size means repeatedly searching and removing `"abc"` from the string (`O(N²)`) is too slow.

---

# 2. Diagram

Think of building the string while validating it.

```text
s = "aabcbc"

Read a
[a]

Read a
[a a]

Read b
[a a b]

Read c

Top becomes:
a b c

Remove it

[a]

Continue...

Read b
[a b]

Read c

Top:
a b c

Remove

[]

Empty Stack

✓ Valid
```

Another example:

```text
abccba

Stack

a
ab
abc -> remove

[]

c
[c]

b
[c b]

a
[c b a]

Cannot form abc

✗ Invalid
```

---

# 3. Example I/O

### Example 1

**Input**

```text
s = "aabcbc"
```

**Output**

```text
True
```

Explanation

```text
aabcbc

↓

a + abc

↓

abc

↓

""
```

---

### Example 2

**Input**

```text
s = "abccba"
```

**Output**

```text
False
```

Explanation

After removing the first `"abc"`,

```text
cba
```

cannot be reduced further.

---

# 4. Intuition & Pattern Recognition

## Key Observation

The only valid removable substring is

```text
abc
```

Whenever the latest three characters become `"abc"`, they should disappear.

That immediately suggests:

* process left to right
* keep previously seen characters
* remove recent characters when they form `"abc"`

This is exactly what a **stack** is good at.

---

### Interview Thought Process

> "Whenever removing a recently formed pattern, think Stack."

As soon as the top three stack elements are

```text
a b c
```

pop them immediately.

Nested insertions are handled automatically.

---

# 5. Simpler Version

## Simpler Problem

### 20. Valid Parentheses

Remove matching

```text
(
)
```

using a stack.

---

### Another Similar Problem

### 1047. Remove All Adjacent Duplicates

Remove

```text
aa
```

using stack.

---

### Current Problem

Instead of removing

```text
aa
```

or matching parentheses,

remove

```text
abc
```

when it appears on top of the stack.

---

### Thinking Evolution

```text
Valid Parentheses
        ↓
Need Stack

↓

Remove Adjacent Duplicates
Remove top pattern

↓

Current Problem
Remove fixed sequence "abc"
```

---

### Simpler Questions

| Problem                             | Relation                          |
| ----------------------------------- | --------------------------------- |
| 20. Valid Parentheses               | Basic stack removal               |
| 1047. Remove Adjacent Duplicates    | Remove recent pattern             |
| 1209. Remove Adjacent Duplicates II | Store extra frequency information |
| 71. Simplify Path                   | Undo recent operations            |
| 1003. Current Problem               | Remove fixed pattern `"abc"`      |

---

# 6. Brute Force

Repeatedly

* search for `"abc"`
* remove it
* repeat until no `"abc"` exists.

Pseudo

```text
while "abc" exists:
      remove first occurrence
```

Finally

```text
return string == ""
```

### Complexity

Time

```text
O(N²)
```

Space

```text
O(N)
```

---

# 7. Optimal Solution (Stack)

## Idea

Push every character.

Whenever stack size ≥ 3,

check

```text
top3 == ['a','b','c']
```

If yes,

pop them.

At the end,

if stack is empty,

the string is valid.

---

## Python

```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for ch in s:
            stack.append(ch)

            # Check whether the top three characters form "abc"
            if len(stack) >= 3:
                if stack[-3] == 'a' and stack[-2] == 'b' and stack[-1] == 'c':
                    stack.pop()
                    stack.pop()
                    stack.pop()

        return len(stack) == 0
```

---

### Complexity

Time

```text
O(N)
```

Each character is pushed once and popped at most once.

Space

```text
O(N)
```

---

# 8. Step-by-Step Trace

Example

```text
s = "aabcbc"
```

| Character | Stack | Action          |
| --------- | ----- | --------------- |
| a         | a     | Push            |
| a         | aa    | Push            |
| b         | aab   | Push            |
| c         | aabc  | Top = abc → Pop |
| b         | ab    | Push            |
| c         | abc   | Top = abc → Pop |

Final Stack

```text
[]
```

Return

```text
True
```

---

Second Example

```text
abccba
```

| Character | Stack        |
| --------- | ------------ |
| a         | a            |
| b         | ab           |
| c         | abc → remove |
| c         | c            |
| b         | cb           |
| a         | cba          |

Final

```text
[c,b,a]
```

Not empty

Return

```text
False
```

---

# 9. Related Problems

1. **20. Valid Parentheses** – The classic stack problem where matching symbols are removed from the top.

2. **1047. Remove All Adjacent Duplicates in String** – Remove adjacent duplicate pairs using a stack.

3. **1209. Remove All Adjacent Duplicates in String II** – Generalizes stack removals by tracking character frequencies and removing groups of size `k`.

4. **394. Decode String** – Uses a stack to process nested encoded patterns.

5. **71. Simplify Path** – Uses a stack to cancel or remove the most recent components.

---

# Pattern Summary (Interview Revision)

| Clue                                   | Pattern                    |
| -------------------------------------- | -------------------------- |
| Need to remove recently formed pattern | Stack                      |
| Fixed removable substring              | Check top of stack         |
| Pattern is `"abc"`                     | Pop top 3 when matched     |
| Nested removals possible               | Handled naturally by stack |
| Time Complexity                        | **O(N)**                   |
| Space Complexity                       | **O(N)**                   |
