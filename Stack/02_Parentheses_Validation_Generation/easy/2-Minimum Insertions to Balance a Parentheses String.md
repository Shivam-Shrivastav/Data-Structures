# 1541. Minimum Insertions to Balance a Parentheses String (Greedy)

---

# 1. Problem Statement

A parentheses string consists of `'('` and `')'`.

Unlike normal parentheses matching, here **every `'('` must be matched with exactly two consecutive `')'` characters (`"))"`).**

You may insert `'('` or `')'` anywhere in the string.

Return the **minimum number of insertions** needed to make the string balanced.

### A balanced string follows these rules:

* Every `'('` is matched with **two consecutive `')'`**.
* `'('` must appear **before** its matching `"))"`.

### Constraints

* `1 <= s.length <= 10^5`
* `s` contains only `'('` and `')'`.

---

## Example

```text
Input:
s = "(()))"

Output:
1
```

Explanation

```text
Original:

(()))

Grouping:

( () ))

First '(' -> matched by "))"

Second '(' -> only gets one ')'

Need one more ')'

Result:

(())))
```

---

# 2. Diagram

Think in terms of **how many ')' are still needed**.

Example:

```
String

(()))
```

```
Read '('

Need 2 )

need = 2


Read '('

Need 2 more

need = 4


Read ')'

One requirement fulfilled

need = 3


Read ')'

need = 2


Read ')'

need = 1
```

End:

```
Still need one ')'

Insert one

Answer = 1
```

---

# 3. Example I/O

### Example 1

```
Input

"(()))"

Output

1
```

Need one extra `')'`.

---

### Example 2

```
Input

"))())("

Output

3
```

Explanation

Several unmatched `')'` require inserting `'('`, and the final `'('` needs two `')'`.

---

### Example 3 (Edge Case)

```
Input

"("

Output

2
```

One `'('` always requires **two ')'**.

---

# 4. Intuition & Pattern Recognition

### First Observation

Unlike **Valid Parentheses**, one `'('` is **not** matched by one `')'`.

Instead

```
(
↓

))
```

So each `'('` contributes **2 required closing parentheses**.

---

### Key Insight

Maintain:

```
need = number of ')' still required
```

Whenever we see

```
(
```

Increase

```
need += 2
```

Whenever we see

```
)
```

Decrease

```
need -= 1
```

---

### Odd `need`

Suppose

```
need = 3
```

Impossible.

Why?

Because every `'('` contributes exactly **2**.

Need should always be

```
0
2
4
6
...
```

Odd means

```
(
)
```

already exists.

Need another `')'` before processing a new `'('`.

So:

```
Insert one ')'

answer++

need--
```

---

### Recognition Pattern

Whenever the problem asks:

* minimum insertions
* balancing
* local fixes while scanning

Think

> **Greedy**

---

# 5. Simpler Version

### Simpler Problem

**LeetCode 20 — Valid Parentheses**

Each

```
(
```

needs

```
)
```

One-to-one matching.

---

### Next Level

Now every

```
(
```

needs

```
))
```

One-to-two matching.

The same scanning idea works, only the bookkeeping changes.

---

### Simpler Questions Leading Here

1. Valid Parentheses
2. Minimum Add to Make Parentheses Valid (921)
3. Remove Outermost Parentheses
4. Minimum Insertions to Balance Parentheses String

---

# 6. Brute Force

Repeatedly insert parentheses until the string becomes balanced.

After every insertion:

* Recheck the whole string.

Very inefficient.

### Complexity

Time

```
O(n²)
```

Space

```
O(n)
```

---

# 7. Optimal Solution (Greedy)

### Idea

Maintain

```
need = number of ')' required
```

and

```
insertions = answer
```

Rules:

### If current is '('

Need two more `)`.

```
need += 2
```

If need becomes odd

```
need = 3

Insert one ')'

answer++

need--
```

---

### If current is ')'

```
need--
```

If

```
need == -1
```

means we have

```
)
```

without matching `'('`.

Insert one `'('`.

```
answer++

need = 1
```

Why 1?

Inserted `'('` needs two `')'`.

Current `')'` already satisfies one.

Still need one more.

---

Finally

```
answer += need
```

because every remaining required `')'` must be inserted.

---

### Python

```python
class Solution:
    def minInsertions(self, s: str) -> int:
        insertions = 0
        need = 0  # Number of ')' still required

        for ch in s:

            if ch == '(':

                # If need is odd, complete the previous pair first
                if need % 2 == 1:
                    insertions += 1
                    need -= 1

                need += 2

            else:
                need -= 1

                # Extra ')' without matching '('
                if need == -1:
                    insertions += 1
                    need = 1

        return insertions + need
```

---

### Complexity

Time

```
O(n)
```

Space

```
O(1)
```

---

# 8. Step-by-Step Trace

Example

```
s = "(()))"
```

| Character | Need | Insertions | Explanation           |
| --------- | ---- | ---------- | --------------------- |
| Start     | 0    | 0          |                       |
| (         | 2    | 0          | Needs `))`            |
| (         | 4    | 0          | Another `))`          |
| )         | 3    | 0          | One ')' matched       |
| )         | 2    | 0          | Pair completed        |
| )         | 1    | 0          | Still one ')' missing |

End:

```
need = 1

Insert one ')'
```

Answer

```
0 + 1 = 1
```

---

## Another Trace

```
s = ")"
```

| Character | Need | Insertions |
| --------- | ---- | ---------- |
| )         | -1   | 0          |

Need became -1

Insert `'('`

```
insertions = 1

need = 1
```

End

```
need = 1

Insert one ')'

Total = 2
```

Balanced string becomes

```
())
```

One inserted `'('`, one inserted `')'`.

---

# 9. Related Problems

| Problem                                                       | Connection                                       |
| ------------------------------------------------------------- | ------------------------------------------------ |
| **20. Valid Parentheses**                                     | Basic parentheses matching using a stack.        |
| **921. Minimum Add to Make Parentheses Valid**                | Greedy counting when each `'('` needs one `')'`. |
| **32. Longest Valid Parentheses**                             | Parentheses processing using stack/DP.           |
| **1249. Minimum Remove to Make Valid Parentheses**            | Remove instead of insert to balance.             |
| **1963. Minimum Number of Swaps to Make the String Balanced** | Another greedy parentheses balancing problem.    |

---

# Interview Takeaway

The trick is to think in terms of **how many closing parentheses are still needed**, not in terms of matching pairs.

Maintain:

* `need` → number of `')'` still required.
* `insertions` → number of characters inserted.

### Core Rules

```text
'(':
    if need is odd:
        insert one ')'
        need--

    need += 2

')':
    need--

    if need == -1:
        insert one '('
        need = 1

Answer = insertions + need
```

The most important insight is that **each `'('` requires two consecutive `')'`**, so `need` should normally remain **even**. Whenever it becomes **odd**, you greedily insert one `')'` immediately to complete the previous pair before processing further. This greedy approach guarantees the minimum number of insertions in **O(n)** time and **O(1)** space.
