# **1047. Remove All Adjacent Duplicates In String**

**Pattern:** Stack

---

# 1. Problem Statement

Given a string `s` consisting of lowercase English letters, repeatedly remove **adjacent duplicate characters** until no such duplicates remain.

Return the final string after all possible removals.

It is guaranteed that the final answer is unique.

### Constraints

* `1 <= s.length <= 10^5`
* `s` contains only lowercase English letters.

---

# 2. Diagram

Example:

```
s = "abbaca"

Read characters one by one.

          Stack

a          a
b          a b
b          a          <- bb removed
a          (empty)    <- aa removed
c          c
a          c a

Result = "ca"
```

Think of the stack as the current valid string.

---

# 3. Example I/O

### Example 1

**Input**

```
s = "abbaca"
```

**Output**

```
"ca"
```

Explanation

```
abbaca
 a bb aca  -> remove bb
aaca
 aa ca     -> remove aa
ca
```

---

### Example 2 (Edge Case)

**Input**

```
s = "aaaa"
```

**Output**

```
""
```

Explanation

```
aaaa
aa -> removed
aa -> removed
empty string
```

---

# 4. Intuition & Pattern Recognition

### Signal 1

Whenever you see

* remove adjacent
* matching neighbours
* repeated removals

think **Stack**.

---

### Signal 2

Every character only needs to know its immediate previous surviving character.

A stack naturally stores exactly that.

---

### Interview Thought Process

> "Every time I encounter a character, I only care whether it matches the last character that hasn't been removed. A stack always keeps the latest surviving character on top."

---

# 5. Simpler Version

## Simpler Problem

Remove adjacent duplicates **only once**.

Example

```
abbc

↓

ac
```

Easy:

```
compare current with previous
```

---

## Why doesn't that work here?

Example

```
azxxzy

remove xx

↓

azzy

Now zz became adjacent!

↓

ay
```

Removing one pair can create another pair.

So we need a structure that automatically checks the latest surviving character every time.

That is exactly what a stack does.

---

## Similar Simpler LeetCode Problems

### 20. Valid Parentheses

Uses stack to compare current character with previous unmatched one.

Difference:

* Parentheses matching
* Here duplicate matching

---

### 155. Min Stack

Teaches stack operations.

Difference:

* No removals
* Just stack implementation

---

### Thinking Progression

```
Remember previous character
        ↓

Need to undo previous character

        ↓

Use Stack

        ↓

Keep removing while scanning

        ↓

Final answer
```

---

# 6. Brute Force

Keep searching for adjacent duplicates.

Whenever found,

* remove them
* start again.

Pseudo

```
while duplicates exist:
      scan string
      remove duplicate pair
```

### Time Complexity

Worst case

```
O(n²)
```

### Space

```
O(n)
```

(for rebuilding strings)

---

# 7. Optimal Solution (Stack)

### Idea

For every character:

* If stack top equals current character

  * pop
* Otherwise

  * push

Finally join the stack.

### Python

```python
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []

        for ch in s:

            # Adjacent duplicate found
            if stack and stack[-1] == ch:
                stack.pop()

            # Different character
            else:
                stack.append(ch)

        return "".join(stack)
```

---

### Time Complexity

```
O(n)
```

Every character is

* pushed once
* popped at most once.

---

### Space Complexity

```
O(n)
```

---

# 8. Step-by-Step Trace

Example

```
s = "abbaca"
```

| Character | Stack Before | Action | Stack After |
| --------- | ------------ | ------ | ----------- |
| a         | []           | push   | a           |
| b         | a            | push   | ab          |
| b         | ab           | pop    | a           |
| a         | a            | pop    | ""          |
| c         | ""           | push   | c           |
| a         | c            | push   | ca          |

Final answer

```
"ca"
```

---

# 9. Related Problems

### Easy

**1209. Remove All Adjacent Duplicates in String II**

Instead of removing two duplicates, remove **k** consecutive duplicates. Extends the same stack idea by storing `(character, count)`.

---

### Medium

**394. Decode String**

Uses a stack to process nested encoded strings like `3[a2[c]]`.

---

### Medium

**1249. Minimum Remove to Make Valid Parentheses**

Uses a stack to track unmatched parentheses and remove invalid ones.

---

### Medium

**735. Asteroid Collision**

The stack stores surviving asteroids, and collisions remove elements in a way similar to popping adjacent duplicates.

---

### Medium

**71. Simplify Path**

Processes directory names with a stack, pushing valid folders and popping on `".."`, following the same push/pop pattern.
