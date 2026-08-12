# **394. Decode String (Stack)**

---

# 1. Problem Statement

Given an encoded string `s`, decode it according to the following rule:

* `k[encoded_string]` means the `encoded_string` inside the square brackets should be repeated exactly `k` times.
* `k` is always a positive integer.
* The input is always valid.
* Digits are only used for repeat counts (not part of the original string).

Return the fully decoded string.

### Constraints

* `1 <= s.length <= 30`
* `1 <= k <= 300`
* Input is guaranteed to be valid.
* Output length ≤ `10^5`

---

## Example

```
Input:
s = "3[a2[c]]"

Output:
"accaccacc"
```

Explanation

```
a2[c]
↓

acc

3[acc]
↓

accaccacc
```

---

# 2. Diagram

```
Input:

3[a2[c]]

Read characters one by one

        Stack
-------------------------
3
3 [
3 [ a
3 [ a 2
3 [ a 2 [
3 [ a 2 [ c

Encounter ]

Pop until '['

c
↓

Repeat 2 times

cc

Push back

Stack

3 [ a cc

Encounter ]

Pop until '['

acc

Repeat 3 times

accaccacc
```

---

# 3. Example I/O

### Example 1

```
Input:
"3[a]2[bc]"

Output:
"aaabcbc"
```

Explanation

```
3[a] -> aaa

2[bc] -> bcbc

Result

aaabcbc
```

---

### Example 2 (Nested)

```
Input:
"2[abc]3[cd]ef"

Output:
"abcabccdcdcdef"
```

Explanation

```
2[abc]
↓

abcabc

3[cd]
↓

cdcdcd

Append ef

abcabccdcdcdef
```

---

### Edge Case

```
Input:
"10[a]"

Output:
"aaaaaaaaaa"
```

Shows handling of multi-digit numbers.

---

# 4. Intuition & Pattern Recognition

### Signals

* Nested brackets
* Need to remember previous context
* Matching brackets
* Evaluate from inside outward

These are classic **Stack** signals.

### Interview Thinking

Whenever you see

```
3[...]
2[...]
nested [...]
```

Think:

> "Every time I hit `]`, I have enough information to decode one complete block."

A stack naturally stores unfinished expressions until they are complete.

---

# 5. Simpler Version

## Simpler Question

```
3[a]
```

Output

```
aaa
```

Just read number and repeat.

---

### Slightly Harder

```
3[ab]
```

Output

```
ababab
```

Still no nesting.

---

### Harder

```
3[a2[c]]
```

Now inside result must be decoded first.

```
2[c]
↓

cc

a + cc

↓

acc

Repeat 3 times

↓

accaccacc
```

So the stack lets us solve the innermost expression first.

---

### Related Simpler Problems

* **20. Valid Parentheses** → learn bracket matching.
* **71. Simplify Path** → stack for nested structures.
* **394. Decode String** → stack + reconstruction.

Thinking progression

```
Matching brackets
        ↓
Store unfinished expressions
        ↓
Process inner block first
        ↓
Decode nested strings
```

---

# 6. Brute Force

Idea:

Repeatedly locate the innermost bracket pair, decode it, replace it, and continue until no brackets remain.

Example

```
3[a2[c]]

↓

3[acc]

↓

accaccacc
```

### Time Complexity

Worst-case

```
O(n²)
```

because string replacement is expensive.

### Space

```
O(n)
```

---

# 7. Optimal Solution (Single Stack)

### Idea

Maintain one stack.

When encountering:

* digit → push
* letter → push
* '[' → push
* ']' →

  * pop characters until '['
  * pop '['
  * pop digits
  * repeat substring
  * push repeated string back

---

## Python Solution

```python
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for ch in s:
            if ch != "]":
                # Keep pushing until a closing bracket is found
                stack.append(ch)
            else:
                # Build the encoded substring
                substring = []

                while stack[-1] != "[":
                    substring.append(stack.pop())

                stack.pop()  # Remove '['

                # Build the repeat count (supports multi-digit numbers)
                digits = []

                while stack and stack[-1].isdigit():
                    digits.append(stack.pop())

                k = int("".join(reversed(digits)))

                decoded = "".join(reversed(substring)) * k

                # Push decoded string back for outer levels
                stack.append(decoded)

        return "".join(stack)
```

---

## Complexity

Time

```
O(n)
```

Each character is pushed and popped at most once.

Space

```
O(n)
```

---

# 8. Step-by-Step Trace

Input

```
3[a2[c]]
```

| Character | Stack                               |
| --------- | ----------------------------------- |
| 3         | 3                                   |
| [         | 3 [                                 |
| a         | 3 [ a                               |
| 2         | 3 [ a 2                             |
| [         | 3 [ a 2 [                           |
| c         | 3 [ a 2 [ c                         |
| ]         | Pop c → repeat 2 → push cc          |
| Stack     | 3 [ a cc                            |
| ]         | Pop acc → repeat 3 → push accaccacc |
| End       | accaccacc                           |

Output

```
accaccacc
```

---

# 9. Related Problems (Increasing Difficulty)

1. **20. Valid Parentheses**
   Learn how stacks handle matching brackets.

2. **71. Simplify Path**
   Uses a stack to process nested path components.

3. **150. Evaluate Reverse Polish Notation**
   Stack-based evaluation of expressions.

4. **394. Decode String**
   Stack for nested string decoding.

5. **772. Basic Calculator III**
   Extends stack usage to nested arithmetic expressions with parentheses.

---

# Interview Cheat Sheet

### Recognition Keywords

* Nested brackets
* Decode expression
* Repeat substring
* Matching parentheses
* Evaluate inner block first

### Pattern

```
Read left → right

Push everything

When ']' appears

↓

Pop substring

↓

Pop number

↓

Repeat

↓

Push back
```

### Template

```python
stack = []

for ch in s:
    if ch != "]":
        stack.append(ch)
    else:
        # 1. Pop substring
        # 2. Pop '['
        # 3. Pop number
        # 4. Repeat
        # 5. Push back

return "".join(stack)
```

### Common Mistakes

* Forgetting to reverse the popped substring before repeating.
* Not handling **multi-digit repeat counts** (e.g., `"12[a]"`).
* Forgetting to remove `'['` after collecting the substring.
* Pushing repeated characters individually instead of as one decoded string (either works, but pushing the full decoded string is cleaner).
