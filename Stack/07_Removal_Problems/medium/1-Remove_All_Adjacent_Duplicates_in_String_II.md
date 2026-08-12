# **1209. Remove All Adjacent Duplicates in String II**

## 1. Problem Statement

You are given a string `s` and an integer `k`.

Repeatedly remove any group of **exactly `k` adjacent identical characters** from the string until no more such groups exist.

Return the final string after all removals.

### Constraints

* `1 <= s.length <= 10^5`
* `2 <= k <= 10^4`
* `s` contains lowercase English letters.

The large constraints immediately rule out repeatedly scanning and rebuilding the string.

---

## 2. Diagram

Think of the stack storing:

```
(character, current consecutive count)
```

Example:

```
s = "deeedbbcccbdaa"
k = 3

Read d
Stack:
[d,1]

Read e
[d,1]
[e,1]

Read e
[d,1]
[e,2]

Read e
[d,1]
[e,3]  <-- count becomes 3
POP

Stack:
[d,1]
```

Later,

```
bbb
↓

[d,2]
[b,3] -> remove

ccc
↓

[c,3] -> remove

Finally

ddd

↓

[d,3] -> remove
```

Final:

```
aa
```

---

# 3. Example I/O

### Example 1

**Input**

```text
s = "abcd"
k = 2
```

**Output**

```text
"abcd"
```

Explanation:

No adjacent duplicates of length 2.

---

### Example 2

**Input**

```text
s = "deeedbbcccbdaa"
k = 3
```

**Output**

```text
"aa"
```

Explanation

```
deeedbbcccbdaa

remove eee
↓

ddbbcccbdaa

remove bbb
↓

ddccdaa

remove ccc
↓

dddaa

remove ddd
↓

aa
```

---

## 4. Intuition & Pattern Recognition

### Signals

* Remove characters while traversing.
* Future characters depend on previous removals.
* Need to maintain current consecutive characters.
* Nested removals can happen.

These are classic **Stack** signals.

Instead of storing every character separately, store

```
(character, frequency)
```

Whenever frequency reaches `k`, remove it immediately.

The stack automatically exposes previous characters, allowing chain reactions naturally.

### Interview Thought Process

> "Whenever I need to undo recently processed elements, I should think Stack."

Here,

* only recent characters matter
* deletions reveal previous characters
* stack perfectly models this behavior

---

# 5. Simpler Version

## Simpler Problem

### 1047. Remove All Adjacent Duplicates In String

```
abbaca

↓

aaca

↓

ca
```

Only remove **pairs**.

Stack solution:

```
if top == current:
    pop
else:
    push
```

---

### Current Problem

Instead of removing pairs,

remove after

```
count == k
```

So the stack becomes

```
(char, count)
```

instead of only

```
char
```

---

### Thinking Evolution

```
Valid Parentheses
        ↓
Need Stack

↓

Remove Adjacent Duplicates
Store characters

↓

Remove Duplicates II
Store character + frequency

↓

Need run-length compression inside stack
```

---

### Simpler Questions

| Problem                              | Relation                           |
| ------------------------------------ | ---------------------------------- |
| 20. Valid Parentheses                | Basic stack usage                  |
| 155. Min Stack                       | Store extra information with stack |
| 1047. Remove All Adjacent Duplicates | Same problem for k=2               |
| 71. Simplify Path                    | Remove recent elements using stack |
| 1209. Current Problem                | Stack + frequency counting         |

---

# 6. Brute Force

Keep scanning the string.

Whenever you find

```
k consecutive same characters
```

remove them.

Restart scanning from the beginning.

Pseudo:

```
repeat
    changed = False

    scan string

    if k duplicates found
         remove
         changed = True

until changed == False
```

### Complexity

Time:

```
O(N²)
```

Space:

```
O(N)
```

---

# 7. Optimal Solution (Stack + Frequency)

### Idea

Stack stores

```
(character, count)
```

For every character

```
if same as top
      increment count

      if count == k
            pop

else
      push(character,1)
```

Finally rebuild the answer.

---

### Python

```python
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []

        for ch in s:

            # Same character as previous
            if stack and stack[-1][0] == ch:
                stack[-1][1] += 1

                # Remove when count becomes k
                if stack[-1][1] == k:
                    stack.pop()

            else:
                stack.append([ch, 1])

        # Rebuild string
        ans = []

        for ch, count in stack:
            ans.append(ch * count)

        return "".join(ans)
```

---

### Complexity

Time

```
O(N)
```

Each character is pushed and popped at most once.

Space

```
O(N)
```

---

# 8. Step-by-Step Trace

Example

```
s = "deeedbbcccbdaa"
k = 3
```

| Character | Stack               |
| --------- | ------------------- |
| d         | [(d,1)]             |
| e         | [(d,1),(e,1)]       |
| e         | [(d,1),(e,2)]       |
| e         | count=3 → pop       |
| d         | [(d,2)]             |
| b         | [(d,2),(b,1)]       |
| b         | [(d,2),(b,2)]       |
| c         | [(d,2),(b,2),(c,1)] |
| c         | [(d,2),(b,2),(c,2)] |
| c         | pop c               |
| b         | count=3 → pop       |
| d         | count=3 → pop       |
| a         | [(a,1)]             |
| a         | [(a,2)]             |

Final stack

```
[(a,2)]
```

Answer

```
aa
```

---

# 9. Related Problems

1. **20. Valid Parentheses** — Learn the fundamental stack push/pop pattern.

2. **155. Min Stack** — Store additional metadata alongside stack elements, similar to storing `(char, count)`.

3. **1047. Remove All Adjacent Duplicates In String** — Same problem with `k = 2`; this is the direct precursor to 1209.

4. **71. Simplify Path** — Use a stack to remove or backtrack through the most recent elements.

5. **394. Decode String** — More advanced stack problem where you maintain additional state (counts and strings) to process nested structures.

---

## Pattern Summary (Interview Revision)

| Clue                           | Pattern                        |
| ------------------------------ | ------------------------------ |
| Undo recent work               | Stack                          |
| Need consecutive frequency     | Store `(char, count)`          |
| Delete after threshold `k`     | Pop when `count == k`          |
| Chain reactions after deletion | Naturally handled by the stack |
| Time Complexity                | **O(N)**                       |
| Space Complexity               | **O(N)**                       |
