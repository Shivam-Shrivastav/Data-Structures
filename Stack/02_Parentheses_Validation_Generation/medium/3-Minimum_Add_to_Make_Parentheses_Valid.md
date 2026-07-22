# 921. Minimum Add to Make Parentheses Valid (Greedy / Stack)

---

# 1. Problem Statement

Given a string `s` consisting only of `'('` and `')'`, return the **minimum number of parentheses that must be added** to make the string valid.

A parentheses string is valid if:

* Every `'('` has a matching `')'`.
* Every `')'` has a matching `'('`.
* Parentheses are properly nested.

You may insert `'('` or `')'` at any position.

### Constraints

* `1 <= s.length <= 1000`
* `s` consists only of `'('` and `')'`.

---

## Example

```text
Input:
s = "())"

Output:
1
```

Explanation

```text
())

Need one '('?

No.

Need one ')' at the end.

Result

()()
```

Only **one insertion** is required.

---

# 2. Diagram

Example

```text
s = "()))("
```

Process from left to right.

```text
Balance = unmatched '('

Start

balance = 0
additions = 0

--------------------------------

(

balance = 1

--------------------------------

)

balance = 0

--------------------------------

)

No '(' available

Insert '('

additions = 1

--------------------------------

)

Again no '('

Insert '('

additions = 2

--------------------------------

(

balance = 1
```

End

```text
Still one unmatched '('

Need one ')'

additions = 3
```

Answer = **3**

---

# 3. Example I/O

### Example 1

```text
Input

"())"

Output

1
```

Need one `')'`.

---

### Example 2

```text
Input

"((("

Output

3
```

Need three `')'`.

---

### Example 3 (Edge Case)

```text
Input

")))"

Output

3
```

Need three `'('`.

---

# 4. Intuition & Pattern Recognition

### Interview Hint

Whenever you hear

> **"Minimum additions to make parentheses valid"**

Think:

> **Greedy counting**

Unlike **Valid Parentheses**, we don't need to remember the exact positions of `'('`.

We only care about:

* How many `'('` are unmatched.
* How many `'('` we need to insert.

---

### Key Observation

Maintain

```text
balance = unmatched '('
```

When reading:

### '('

```text
balance++
```

because it now needs a future `')'`.

---

### ')'

If

```text
balance > 0
```

Match one.

```text
balance--
```

Else

```text
No '(' exists.

Insert '('

answer++
```

---

At the end

Any remaining `'('`

```text
balance
```

need matching `')'`.

Answer

```text
answer + balance
```

---

### Recognition Pattern

Problems asking:

* minimum insertions
* balancing parentheses
* only count required operations

often use **Greedy** rather than a stack.

---

# 5. Simpler Version

### Simpler Problem

**Valid Parentheses (20)**

Return

```text
True

False
```

---

Upgrade:

Instead of checking validity,

count how many insertions are needed.

You no longer reject invalid strings—you fix them greedily.

---

### Simpler Questions Leading Here

1. Valid Parentheses (20)
2. Minimum Add to Make Parentheses Valid (921)
3. Minimum Remove to Make Valid Parentheses (1249)
4. Minimum Insertions to Balance Parentheses String (1541)

---

# 6. Brute Force

Try inserting parentheses at every position.

Check validity after every insertion.

Very inefficient.

### Complexity

Time

```text
O(n²)
```

or worse.

---

# 7. Optimal Solution (Greedy)

### Idea

Maintain

```text
balance = unmatched '('

answer = insertions
```

Rules

### If '('

```text
balance += 1
```

---

### If ')'

If

```text
balance > 0
```

Match it.

```text
balance -= 1
```

Else

Need to insert `'('`.

```text
answer += 1
```

---

Finally

```text
answer += balance
```

because every remaining `'('` needs one `')'`.

---

### Python

```python
class Solution:
    def minAddToMakeValid(self, s: str) -> int:

        balance = 0      # Unmatched '('
        answer = 0       # Insertions needed

        for ch in s:

            if ch == '(':
                balance += 1

            else:

                if balance > 0:
                    balance -= 1
                else:
                    answer += 1

        return answer + balance
```

---

## Alternative Stack Solution

Although Greedy is optimal, a stack also works.

```python
class Solution:
    def minAddToMakeValid(self, s: str) -> int:

        stack = []

        for ch in s:

            if ch == '(':
                stack.append(ch)

            else:
                if stack:
                    stack.pop()
                else:
                    stack.append(ch)

        return len(stack)
```

Why?

Every unmatched parenthesis remains in the stack.

Its size equals the required insertions.

---

### Complexity

Greedy

Time

```text
O(n)
```

Space

```text
O(1)
```

Stack

Time

```text
O(n)
```

Space

```text
O(n)
```

---

# 8. Step-by-Step Trace

Example

```text
s = "()))("
```

| Character | Balance | Answer | Explanation   |
| --------- | ------- | ------ | ------------- |
| Start     | 0       | 0      |               |
| (         | 1       | 0      | Unmatched '(' |
| )         | 0       | 0      | Match         |
| )         | 0       | 1      | Insert '('    |
| )         | 0       | 2      | Insert '('    |
| (         | 1       | 2      | Needs ')'     |

End

```text
answer = 2

balance = 1

Total = 3
```

---

## Another Trace

```text
s = "((("
```

| Character | Balance | Answer |
| --------- | ------- | ------ |
| (         | 1       | 0      |
| (         | 2       | 0      |
| (         | 3       | 0      |

End

```text
Need three ')'

Answer

3
```

---

# 9. Related Problems

| Problem                                                      | Connection                                                   |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| **20. Valid Parentheses**                                    | Basic parentheses validation.                                |
| **1249. Minimum Remove to Make Valid Parentheses**           | Remove invalid parentheses instead of adding them.           |
| **1541. Minimum Insertions to Balance a Parentheses String** | Each `'('` requires `"))"` instead of `")"`.                 |
| **301. Remove Invalid Parentheses**                          | Return all valid strings after minimum removals.             |
| **32. Longest Valid Parentheses**                            | Find the longest valid parentheses substring using stack/DP. |

---

# Interview Takeaway

This problem is **Greedy**, not really a Stack problem.

The only information we need is:

* `balance` → number of unmatched `'('`.
* `answer` → number of inserted `'('` for extra `')'`.

### Core Algorithm

```text
For each character:

If '(':
    balance++

Else:
    if balance > 0:
        balance--
    else:
        answer++

Return answer + balance
```

### Difference from Similar Problems

| Problem                                | Operation               | Technique                  |
| -------------------------------------- | ----------------------- | -------------------------- |
| **20. Valid Parentheses**              | Check validity          | Stack                      |
| **921. Minimum Add to Make Valid**     | Add parentheses         | Greedy                     |
| **1249. Minimum Remove to Make Valid** | Remove parentheses      | Stack (store indices)      |
| **1541. Minimum Insertions**           | Each `'('` needs `"))"` | Greedy with `need` counter |

**Key insight:** We never need to know **where** to insert parentheses—only **how many**. That's why a simple `balance` counter is sufficient, giving an **O(n)** time and **O(1)** space solution.
