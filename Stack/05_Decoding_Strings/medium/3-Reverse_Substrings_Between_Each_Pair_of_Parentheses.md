# **1190. Reverse Substrings Between Each Pair of Parentheses**

## 1. Problem Statement

Given a string `s` consisting of lowercase English letters and parentheses `'('` and `')'`, reverse the characters inside **each pair of matching parentheses**, starting from the innermost pair.

After processing all parentheses, remove all parentheses from the final string.

### Constraints

* `1 <= s.length <= 2000`
* `s` contains lowercase English letters and parentheses.
* Parentheses are balanced.

---

## Example

```
Input:
s = "(abcd)"

Output:
"dcba"
```

Explanation:

```
(abcd)
 ↓ reverse
dcba
```

---

# 2. Diagram

### Example

```
Input:
(a(bc)d)

Stack processing

(
a
(
b c
)

Reverse "bc"
↓

(
a
c b
d
)

Reverse "acbd"
↓

d b c a

Final:
dbca
```

Or visualize recursively:

```
(a(bc)d)

Inner:
(bc)
  ↓
(cb)

Now:
(acbd)

Reverse again:
(dbca)
```

---

# 3. Example I/O

### Example 1 (Typical)

```
Input:
"(u(love)i)"

Output:
"iloveu"
```

Explanation

```
(love)
↓

evol

Now string:
(uevoli)

Reverse:
iloveu
```

---

### Example 2 (Nested)

```
Input:
"(ed(et(oc))el)"

Output:
"leetcode"
```

Explanation

```
(oc)
↓

co

(etco)
↓

octe

(edocteel)
↓

leetcode
```

---

### Edge Case

```
Input:
"abc"

Output:
"abc"
```

No parentheses.

---

# 4. Intuition & Pattern Recognition

### Signals

Whenever you see

* nested parentheses
* matching brackets
* reverse after closing bracket

think

> **Stack**

Why?

Because

* every '(' opens a new segment
* ')' means current segment is complete
* reverse it
* append to previous segment

Exactly the same idea as evaluating nested expressions.

Interview thought:

> "Whenever I need to process nested structures from inside to outside, a stack is the first thing to consider."

---

# 5. Simpler Version

## Simpler Problem

Reverse characters inside **one pair** of parentheses.

```
(abcd)

↓

dcba
```

Easy:

```
find '('
find ')'
reverse
```

---

### Next

Multiple non-nested parentheses

```
(ab)(cd)

↓

badc
```

Process each independently.

---

### Final Problem

Nested parentheses

```
(a(bc)d)
```

Now you **cannot** process left-to-right.

Need

```
inner first

↓

outer later
```

That's exactly what stacks naturally provide.

---

### Related Simpler Questions

| Problem                                        | Relation                     |
| ---------------------------------------------- | ---------------------------- |
| 20. Valid Parentheses                          | Learn stack for brackets     |
| 394. Decode String                             | Same nested stack processing |
| 71. Simplify Path                              | Stack with nested structure  |
| 1249. Minimum Remove to Make Valid Parentheses | Parentheses processing       |

Thinking progression:

```
Valid Parentheses
        ↓
Decode String
        ↓
Reverse Parentheses
```

---

# 6. Brute Force

Whenever we find a `')'`

* search backward for matching `'('`
* reverse substring
* remove parentheses

Each reverse may cost O(n).

Overall

```
Time:
O(n²)

Space:
O(n)
```

---

# 7. Optimal Solution (Stack of Strings)

### Idea

Maintain a stack of strings.

* Push current string when encountering `'('`
* Start a fresh current string.
* On `')'`

  * reverse current string
  * pop previous string
  * append reversed part
* Characters are simply appended.

---

### Python

```python
class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        curr = []

        for ch in s:

            if ch == '(':
                # Save the string built so far
                stack.append(curr)
                curr = []

            elif ch == ')':
                # Reverse current substring
                curr.reverse()

                # Append it to previous level
                prev = stack.pop()
                curr = prev + curr

            else:
                curr.append(ch)

        return "".join(curr)
```

---

### Why it works

Suppose

```
(a(bc)d)
```

Process

```
curr = a

(
push a

curr = bc

)

reverse

cb

previous = a

acb

continue

acbd

)

reverse

dbca
```

Exactly what problem wants.

---

### Complexity

```
Time:
O(n²) worst case

```

Why?

```
prev + curr
```

copies lists.

For `n ≤ 2000`, accepted.

```
Space:
O(n)
```

---

# Better Optimal (Index Jumping)

There is an O(n) solution.

Idea:

1. Precompute matching parentheses.
2. Traverse with direction.
3. Whenever encountering '(' or ')'

```
jump to partner

flip direction
```

Each character visited once.

---

### O(n) Python

```python
class Solution:
    def reverseParentheses(self, s: str) -> str:
        pair = {}
        stack = []

        # Find matching parentheses
        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            elif ch == ')':
                j = stack.pop()
                pair[i] = j
                pair[j] = i

        ans = []
        i = 0
        direction = 1

        while 0 <= i < len(s):

            if s[i] == '(' or s[i] == ')':
                i = pair[i]
                direction *= -1
            else:
                ans.append(s[i])

            i += direction

        return "".join(ans)
```

---

### Complexity

```
Time:
O(n)

Space:
O(n)
```

This is the most interview-optimal solution.

---

# 8. Step-by-Step Trace

Example

```
s = "(u(love)i)"
```

### Pair mapping

```
0 ↔ 8
2 ↔ 7
```

| Step | Index | Char | Direction | Answer         |
| ---- | ----- | ---- | --------- | -------------- |
| 1    | 0     | (    | →         | jump→8 reverse |
| 2    | 7     | )    | ←         | jump→2 reverse |
| 3    | 3     | l    | →         | l              |
| 4    | 4     | o    | →         | lo             |
| 5    | 5     | v    | →         | lov            |
| 6    | 6     | e    | →         | love           |
| 7    | 2     | (    | →         | jump→7 reverse |
| 8    | 8     | )    | ←         | jump→0 reverse |
| 9    | 1     | u    | →         | loveu          |
| 10   | 9     | i    | →         | loveui         |

Traversal direction automatically creates

```
iloveu
```

without explicitly reversing strings.

---

# 9. Related Problems

1. **20. Valid Parentheses**
   Learn how stacks manage nested parentheses.

2. **394. Decode String**
   Uses a stack to process nested encoded substrings, similar inside-out evaluation.

3. **71. Simplify Path**
   Another stack-based problem where nested components are resolved incrementally.

4. **1249. Minimum Remove to Make Valid Parentheses**
   Focuses on matching and validating parentheses with a stack.

5. **856. Score of Parentheses**
   Builds values from nested parentheses using stack-like processing, increasing the complexity of nested-structure handling.

---

## Interview Takeaway

* **Key Pattern:** Stack for nested structures.
* **Simple Approach:** Use a stack of strings/lists and reverse at each closing parenthesis (easy to explain, accepted for constraints).
* **Optimal Approach:** Precompute matching parentheses and traverse with **direction switching** for an elegant **O(n)** solution—a common interview favorite when asked to optimize.
