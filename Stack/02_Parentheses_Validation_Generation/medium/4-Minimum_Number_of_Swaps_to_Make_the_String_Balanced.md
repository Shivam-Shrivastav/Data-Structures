# 1963. Minimum Number of Swaps to Make the String Balanced (Greedy)

---

# 1. Problem Statement

You are given a string `s` consisting only of `'['` and `']'`.

The string contains an **equal number** of `'['` and `']'`.

You may swap **any two characters** (not necessarily adjacent).

Return the **minimum number of swaps** required to make the string balanced.

A string is balanced if:

* Every opening bracket `'['` has a matching closing bracket `']'`.
* At any prefix of the string, the number of `']'` never exceeds `'['`.

### Constraints

* `2 <= s.length <= 10^6`
* `s.length` is even.
* Number of `'['` equals number of `']'`.

---

## Example

```text
Input:
s = "][]["

Output:
1
```

Explanation

Swap the first `']'` with the last `'['`.

```text
Before

] [ ] [

↓

Swap

[ [ ] ]

Balanced
```

---

# 2. Diagram

Example

```text
s = "]]][[["
```

Scan while maintaining **unmatched opening brackets**.

```text
Char      Balance

]         0
]         0
]         0
[         1
[         2
[         3
```

Maximum imbalance creates unmatched brackets.

Visualizing pairs:

```text
]]] [[[

Need swaps

Swap

] ] ] [ [ [

↓

[ ] ] ] [ [

↓

[ [ ] ] ] [

↓

[ [ ] ] [ ]
```

Total swaps = **2**

---

# 3. Example I/O

### Example 1

```text
Input

"][]["

Output

1
```

---

### Example 2

```text
Input

"[]"

Output

0
```

Already balanced.

---

### Example 3 (Edge Case)

```text
Input

"]]][[["

Output

2
```

---

# 4. Intuition & Pattern Recognition

### Interview Hint

Unlike previous parentheses problems:

* We are **not inserting**.
* We are **not removing**.
* We are **swapping**.

Since swaps can occur between **any two positions**, we don't care about the exact indices—only the amount of imbalance.

---

### Key Observation

Maintain

```text
balance = unmatched '['
```

Rules:

### '['

```text
balance++
```

---

### ']'

If

```text
balance > 0
```

Match one.

```text
balance--
```

Else

Ignore.

This ']' is currently unmatched.

````

After scanning,

`balance` represents the number of unmatched `'['` remaining after greedy matching.

Those unmatched `'['` correspond to the imbalance that must be fixed.

---

### Amazing Formula

If

```text
balance = unmatched '['
````

Then

```text
swaps = (balance + 1) // 2
```

This is the entire solution.

---

### Why?

Suppose

```text
balance = 4
```

```text
]]]][[[[
```

Each swap fixes **two unmatched brackets**.

```text
4 unmatched

↓

2 swaps
```

If

```text
balance = 3
```

Need

```text
(3+1)//2 = 2
```

Works for both odd and even.

---

### Recognition Pattern

Whenever you hear

* minimum swaps
* brackets
* equal number of opening/closing

Think

> **Greedy counting**

---

# 5. Simpler Version

### Simpler Problem

**Valid Parentheses**

Only determine whether valid.

---

Upgrade

Count insertions.

(LeetCode 921)

---

Upgrade

Remove invalid parentheses.

(LeetCode 1249)

---

Upgrade

Instead of adding/removing,

you can **swap**.

Since swaps are unrestricted,

only the imbalance matters.

---

### Simpler Questions Leading Here

1. Valid Parentheses (20)
2. Minimum Add to Make Parentheses Valid (921)
3. Minimum Remove to Make Valid Parentheses (1249)
4. Minimum Number of Swaps to Make the String Balanced (1963)

---

# 6. Brute Force

Repeatedly:

* Find first invalid `']'`.
* Search ahead for `'['`.
* Swap.
* Repeat.

Worst case

Searching each swap

```text
O(n²)
```

---

# 7. Optimal Solution (Greedy)

### Idea

Maintain

```text
balance = unmatched '['
```

Rules

### '['

Increase

```text
balance += 1
```

---

### ']'

If possible,

match it.

```text
if balance > 0:
    balance -= 1
```

Otherwise,

ignore.

---

Finally

```text
return (balance + 1) // 2
```

---

### Python

```python
class Solution:
    def minSwaps(self, s: str) -> int:

        balance = 0

        for ch in s:

            if ch == '[':
                balance += 1

            elif balance > 0:
                balance -= 1

        return (balance + 1) // 2
```

---

## Alternative (Track Maximum Imbalance)

Another common solution tracks the maximum number of unmatched `']'`.

```python
class Solution:
    def minSwaps(self, s: str) -> int:

        balance = 0
        max_imbalance = 0

        for ch in s:

            if ch == '[':
                balance += 1
            else:
                balance -= 1

            max_imbalance = min(max_imbalance, balance)

        return (-max_imbalance + 1) // 2
```

Both solutions are equivalent.

---

### Complexity

Time

```text
O(n)
```

Space

```text
O(1)
```

---

# 8. Step-by-Step Trace

Example

```text
s = "][]["
```

| Character | Balance |
| --------- | ------- |
| ]         | 0       |
| [         | 1       |
| ]         | 0       |
| [         | 1       |

End

```text
balance = 1

Swaps

(1+1)//2

= 1
```

---

## Another Trace

```text
s = "]]][[["
```

| Character | Balance |
| --------- | ------- |
| ]         | 0       |
| ]         | 0       |
| ]         | 0       |
| [         | 1       |
| [         | 2       |
| [         | 3       |

End

```text
balance = 3

(3+1)//2

= 2
```

---

# Why `(balance + 1) // 2` Works

Suppose after greedy matching we have:

```text
balance = 1

Remaining

][
```

One swap fixes it.

---

Suppose

```text
balance = 2

]][[
```

One swap fixes both unmatched pairs.

---

Suppose

```text
balance = 3

]]][[[
```

First swap:

```text
]][[][
```

Second swap:

```text
[][][]
```

Two swaps.

Hence

```text
balance = 3

↓

(3+1)//2

= 2
```

---

# 9. Related Problems

| Problem                                                      | Connection                                                |
| ------------------------------------------------------------ | --------------------------------------------------------- |
| **20. Valid Parentheses**                                    | Basic bracket matching.                                   |
| **921. Minimum Add to Make Parentheses Valid**               | Add brackets instead of swapping.                         |
| **1249. Minimum Remove to Make Valid Parentheses**           | Remove invalid brackets instead of swapping.              |
| **1541. Minimum Insertions to Balance a Parentheses String** | Different balancing rule (`'('` needs `"))"`).            |
| **32. Longest Valid Parentheses**                            | Stack-based matching to find the longest valid substring. |

---

# Interview Takeaway

The key observation is that **swaps can happen between any two positions**, so we don't need to simulate them.

Maintain only the number of unmatched `'['` after greedily matching brackets.

### Core Algorithm

```text
balance = 0

for ch:

    if '[':
        balance++

    elif balance > 0:
        balance--

return (balance + 1) // 2
```

### Difference from Similar Problems

| Problem                   | Operation       | Technique       |
| ------------------------- | --------------- | --------------- |
| **20. Valid Parentheses** | Check validity  | Stack           |
| **921. Minimum Add**      | Add brackets    | Greedy Counter  |
| **1249. Minimum Remove**  | Remove brackets | Stack (indices) |
| **1963. Minimum Swaps**   | Swap brackets   | Greedy Counter  |

**Key insight:** Because a swap can exchange **any two characters**, each swap can fix **two unmatched brackets**, leading to the elegant formula:

```text
Minimum Swaps = (unmatched_open + 1) // 2
```

This gives an **O(n)** time and **O(1)** space solution.
