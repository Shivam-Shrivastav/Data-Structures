# 1249. Minimum Remove to Make Valid Parentheses (Stack)

---

# 1. Problem Statement

Given a string `s` containing lowercase English letters and parentheses `'('` and `')'`, remove the **minimum number of parentheses** so that the resulting string is **valid**.

A valid parentheses string is one where:

* Every `'('` has a matching `')'`.
* Every `')'` has a matching `'('`.
* The order is correct.

Letters should **never be removed**.

Return **any valid string** after the minimum removals.

### Constraints

* `1 <= s.length <= 10^5`
* `s` contains lowercase English letters, `'('`, and `')'`.

---

## Example

```text
Input:
s = "lee(t(c)o)de)"

Output:
"lee(t(c)o)de"
```

Explanation

The last `')'` has no matching `'('`, so we remove it.

---

# 2. Diagram

### Example

```text
s = "a)b(c)d"
```

Scan from left to right.

```
Index: 0 1 2 3 4 5 6
Char : a ) b ( c ) d
```

### Processing

```
Stack = []

a
↓

Keep

--------------------------------

)

Stack empty

Remove it

--------------------------------

b

Keep

--------------------------------

(

Push index

Stack

[3]

--------------------------------

)

Matches '('

Pop

Stack

[]

--------------------------------

Answer

a b ( c ) d

↓

"ab(c)d"
```

---

# 3. Example I/O

### Example 1

```
Input

"a)b(c)d"

Output

"ab(c)d"
```

---

### Example 2

```
Input

"))(("

Output

""
```

Every parenthesis must be removed.

---

### Example 3 (Edge Case)

```
Input

"(a(b(c)d)"

Output

"a(b(c)d)"
```

One unmatched `'('` removed.

---

# 4. Intuition & Pattern Recognition

### Interview Hint

Whenever you hear

> "Make parentheses valid"

or

> "Remove invalid parentheses"

Think:

> **Stack**

because every `'('` needs to remember its position until a matching `')'` appears.

---

### Key Observation

There are only **two invalid cases**:

### Case 1

Extra `')'`

```
abc)

Stack empty

↓

Cannot match

↓

Remove
```

---

### Case 2

Extra `'('`

```
((abc

Stack

[0,1]

Never matched

↓

Remove later
```

---

### Recognition Pattern

Problems involving:

* matching brackets
* matching indices
* nearest previous parenthesis

usually use a **stack**.

---

# 5. Simpler Version

### Simpler Problem

LeetCode **20. Valid Parentheses**

Only check if the string is valid.

No modification.

---

Now upgrade it.

Instead of returning

```
True

False
```

Actually remove invalid parentheses.

Need to know **where** invalid parentheses occur.

Hence store **indices** in the stack.

---

### Simpler Questions Leading Here

1. Valid Parentheses (20)
2. Minimum Add to Make Parentheses Valid (921)
3. Minimum Remove to Make Valid Parentheses (1249)
4. Remove Invalid Parentheses (301)

---

# 6. Brute Force

Try removing every parenthesis.

After every removal:

* Check validity.

Choose the smallest removal.

### Complexity

Very expensive.

Time

```
O(2^n)
```

---

# 7. Optimal Solution (Stack)

### Idea

Maintain

```
stack = indices of unmatched '('
```

Also maintain

```
remove = indices to delete
```

---

### Scan

#### If '('

Push index.

```
stack.append(i)
```

---

#### If ')'

If stack is non-empty

```
Match found

stack.pop()
```

Else

```
No matching '('

Mark this ')' for removal
```

---

After traversal

Any indices left inside stack

```
Unmatched '('

Remove them
```

---

Finally

Build answer skipping removed indices.

---

### Python

```python
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:

        stack = []          # Indices of unmatched '('
        remove = set()      # Indices to remove

        for i, ch in enumerate(s):

            if ch == '(':
                stack.append(i)

            elif ch == ')':

                if stack:
                    stack.pop()
                else:
                    remove.add(i)

        # Remaining '(' are unmatched
        while stack:
            remove.add(stack.pop())

        result = []

        for i, ch in enumerate(s):
            if i not in remove:
                result.append(ch)

        return "".join(result)
```

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
s = "a)b(c)d"
```

| Index | Char | Stack | Remove |
| ----- | ---- | ----- | ------ |
| 0     | a    | []    | {}     |
| 1     | )    | []    | {1}    |
| 2     | b    | []    | {1}    |
| 3     | (    | [3]   | {1}    |
| 4     | c    | [3]   | {1}    |
| 5     | )    | []    | {1}    |
| 6     | d    | []    | {1}    |

Build answer

Skip index **1**

```
ab(c)d
```

---

## Another Trace

```
s = "((a)"
```

| Index | Char | Stack |
| ----- | ---- | ----- |
| 0     | (    | [0]   |
| 1     | (    | [0,1] |
| 2     | a    | [0,1] |
| 3     | )    | [0]   |

End

Stack

```
[0]
```

Remove index **0**

Result

```
(a)
```

---

# 9. Related Problems

| Problem                                                      | Connection                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------------ |
| **20. Valid Parentheses**                                    | Basic stack matching.                                              |
| **921. Minimum Add to Make Parentheses Valid**               | Count additions instead of removals.                               |
| **1541. Minimum Insertions to Balance a Parentheses String** | Greedy balancing where `'('` needs `"))"`.                         |
| **301. Remove Invalid Parentheses**                          | Return **all** valid strings after minimum removals using BFS/DFS. |
| **32. Longest Valid Parentheses**                            | Stack used to find the longest valid substring.                    |

---

# Interview Takeaway

Whenever you see:

> **"Remove the minimum parentheses to make the string valid"**

Think:

* **Stack stores indices of unmatched `'('`.**
* **Extra `')'` are removed immediately.**
* **Leftover `'('` in the stack are removed at the end.**

### Core Algorithm

```text
For each character:

If '(':
    push index

If ')':
    if stack:
        pop
    else:
        mark ')' for removal

After traversal:
    remove every '(' left in stack

Build answer skipping removed indices
```

### Why store **indices** instead of characters?

We don't just need to know whether a parenthesis is unmatched—we need to **remove it from the original string**. Storing indices lets us precisely identify which characters to skip when constructing the final valid string. This is the key insight that differentiates this problem from **Valid Parentheses (20)**, where storing only characters is sufficient.
