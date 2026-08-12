# **844. Backspace String Compare**

**Pattern:** Stack (or Two Pointers with O(1) Space)

---

# 1. Problem Statement

Given two strings `s` and `t` containing lowercase English letters and the character `'#'` (backspace), determine whether they are equal after both are typed into an empty text editor.

* A lowercase letter is typed into the editor.
* `'#'` means **backspace** (delete the previous character if one exists).

Return `True` if both strings become the same after processing; otherwise return `False`.

### Constraints

* `1 <= s.length, t.length <= 2 × 10^5`
* `s` and `t` contain only lowercase letters and `'#'`.

---

# 2. Diagram

### Example

```text
s = "ab#c"
t = "ad#c"

Process s:

a → a
b → ab
# → a
c → ac

Process t:

a → a
d → ad
# → a
c → ac

Both become:

ac
```

Stack visualization:

```text
s = a b # c

[]
[a]
[a b]
[a]
[a c]
```

---

# 3. Example I/O

### Example 1

**Input**

```text
s = "ab#c"
t = "ad#c"
```

**Output**

```text
True
```

Explanation

```text
ab#c → ac
ad#c → ac
```

---

### Example 2

**Input**

```text
s = "ab##"
t = "c#d#"
```

**Output**

```text
True
```

Explanation

```text
ab## → ""
c#d# → ""
```

---

### Edge Case

**Input**

```text
s = "a##"
t = "#"
```

**Output**

```text
True
```

Explanation

```text
a## → ""
# → ""
```

Backspacing an empty string has no effect.

---

# 4. Intuition & Pattern Recognition

### Signal 1

The string is being **edited sequentially**.

Every character depends only on the current state.

---

### Signal 2

A backspace always removes the **most recently added** character.

This is exactly **Last In First Out (LIFO)** behavior.

---

### Interview Thought Process

> "Whenever I see an operation that undoes the most recent action, I immediately think of a stack."

---

# 5. Simpler Version

## Simpler Problem

Given one string with `'#'`, return the final typed string.

Example

```text
abc#d

↓

abd
```

A stack easily simulates typing.

---

## Full Problem

Now process **both strings** independently and compare the results.

---

## Similar Simpler LeetCode Problems

### 1047. Remove All Adjacent Duplicates in String

Uses a stack where the latest character may be removed.

Difference:

* Here removal is triggered by `'#'`.
* There removal is triggered by matching adjacent characters.

---

### 20. Valid Parentheses

Stack remembers previously seen characters.

Difference:

* Parentheses matching instead of text editing.

---

### Thinking Progression

```text
Typing characters

↓

Need to undo last typed character

↓

Stack

↓

Process both strings

↓

Compare results
```

---

# 6. Brute Force

Actually simulate typing into a text editor.

For each string:

* append characters
* remove last character on `'#'`

Finally compare.

This simulation is already optimal enough.

---

# 7. Optimal Solution (Stack)

### Idea

Create a helper function:

* Push letters.
* Pop on `'#'` (if stack isn't empty).

Return the processed string.

Compare both processed strings.

### Python

```python
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        def build(string):
            stack = []

            for ch in string:

                if ch == "#":
                    if stack:
                        stack.pop()
                else:
                    stack.append(ch)

            return "".join(stack)

        return build(s) == build(t)
```

---

### Time Complexity

```text
O(n + m)
```

---

### Space Complexity

```text
O(n + m)
```

---

# 8. Step-by-Step Trace

Example

```text
s = "ab#c"
```

| Character | Stack Before | Action | Stack After |
| --------- | ------------ | ------ | ----------- |
| a         | []           | push   | a           |
| b         | a            | push   | ab          |
| #         | ab           | pop    | a           |
| c         | a            | push   | ac          |

Processed string

```text
ac
```

---

Process

```text
t = "ad#c"
```

| Character | Stack Before | Action | Stack After |
| --------- | ------------ | ------ | ----------- |
| a         | []           | push   | a           |
| d         | a            | push   | ad          |
| #         | ad           | pop    | a           |
| c         | a            | push   | ac          |

Both become

```text
ac
```

Answer

```text
True
```

---

# 9. Optimal Follow-up (O(1) Space)

Instead of building the strings, traverse **from right to left**.

Maintain a **skip counter**:

* If current character is `'#'`, increment `skip`.
* If current character is a letter and `skip > 0`, decrement `skip` and skip the letter.
* Otherwise, this letter is the next valid character.

Compare the next valid character from both strings.

### Time Complexity

```text
O(n + m)
```

### Space Complexity

```text
O(1)
```

This is the follow-up solution interviewers often ask for after the stack approach.

---

# 10. Related Problems

### Easy

**1047. Remove All Adjacent Duplicates in String**
Another stack simulation where characters are removed based on adjacency instead of backspaces.

### Easy

**20. Valid Parentheses**
Classic stack problem for matching opening and closing brackets.

### Medium

**71. Simplify Path**
Uses a stack to process directory names, popping on `".."` similar to backspacing.

### Medium

**394. Decode String**
Uses stacks to process nested encoded strings like `3[a2[c]]`.

### Medium

**1209. Remove All Adjacent Duplicates in String II**
Extends the stack idea by tracking both characters and their frequencies to remove groups of size `k`.
