# 76. Minimum Window Substring

**Pattern:** Variable Size Sliding Window + HashMap (Frequency Count)

---

# 1. Problem Statement

Given two strings `s` and `t`, return the **smallest substring of `s`** that contains **every character of `t` (including duplicates)**.

If no such substring exists, return an empty string `""`.

Unlike the previous longest substring problem, here **every required character must appear with the correct frequency**.

### Constraints

* `1 <= s.length, t.length <= 10^5`
* English letters
* Expected complexity: **O(N)**

---

# 2. Diagram

Example

```text
s = "ADOBECODEBANC"
t = "ABC"

Required:
A : 1
B : 1
C : 1

L
↓
A D O B E C O D E B A N C
                  ↑
                  R

Current Window

"ADOBECODEBA"

Contains:
A ✓
B ✓
C ✓

Valid window

Shrink from left

↓

DOBECODEBA   ❌ Missing A

Previous valid window recorded.

Continue...

Eventually:

BANC

Smallest valid window.
```

---

# 3. Example I/O

### Example 1

```text
Input:
s = "ADOBECODEBANC"
t = "ABC"

Output:
"BANC"
```

Explanation

```text
"BANC"

contains

A
B
C

Length = 4

No smaller valid substring exists.
```

---

### Example 2

```text
Input:
s = "a"
t = "a"

Output:
"a"
```

---

### Example 3 (Edge Case)

```text
Input:
s = "a"
t = "aa"

Output:
""
```

Explanation

```text
Need two 'a'

Only one exists.
```

---

# 4. Intuition & Pattern Recognition

### Signals

Whenever you see

* Minimum / Smallest substring
* Contains all characters
* Frequency matters
* Contiguous substring
* Large constraints

Think

> **Variable Sliding Window**

Unlike Longest Substring Without Repeating Characters:

There we maintain

> Window should stay valid (unique)

Here we maintain

> Window should contain all required characters.

---

### Interview Thinking

Tell yourself

```text
Expand right pointer until
the window satisfies all requirements.

Once valid,

try shrinking from left.

Every valid window is a candidate answer.

Keep shrinking until
window becomes invalid again.

Repeat.
```

This is the classic

> Expand → Become Valid → Shrink → Become Invalid → Expand Again

pattern.

---

# 5. Simpler Version

## Simpler Question 1

### Longest Substring Without Repeating Characters

Window validity:

```text
No duplicate allowed.
```

When invalid

```text
Shrink.
```

---

## Simpler Question 2

### Fruit Into Baskets

Window validity

```text
At most 2 distinct fruits.
```

Shrink when invalid.

---

## Current Question

Now validity becomes

```text
Every required character

AND

Correct frequency
```

instead of

```text
No duplicates
```

So instead of HashSet,

we use

```text
HashMap (frequency).
```

---

### Thinking Progression

```text
Fixed Window

↓

Variable Window

↓

Shrink Until Valid

↓

Track Frequencies

↓

Minimum Window Substring
```

---

# 6. Brute Force

Generate every substring.

For each substring

check whether it contains every character of `t`.

```python
for i:
    for j:
        check frequency
```

Complexity

```text
Time : O(N² × 26) or O(N³)

Space : O(26)
```

Too slow.

---

# 7. Optimal Solution

### Idea

Maintain

```text
need = Counter(t)

window = {}

formed = number of characters
         satisfying required count

required = len(need)
```

Expand right.

Whenever

```text
formed == required
```

Window becomes valid.

Now shrink from left while maintaining validity.

Record minimum length.

---

### Python

```python
from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        need = Counter(t)
        window = defaultdict(int)

        required = len(need)
        formed = 0

        left = 0

        ansLen = float("inf")
        ansStart = 0

        for right in range(len(s)):

            ch = s[right]
            window[ch] += 1

            # Requirement for this character just got satisfied
            if ch in need and window[ch] == need[ch]:
                formed += 1

            # Window contains every required character
            while formed == required:

                # Update minimum answer
                if right - left + 1 < ansLen:
                    ansLen = right - left + 1
                    ansStart = left

                leftChar = s[left]
                window[leftChar] -= 1

                # Removing this character breaks validity
                if leftChar in need and window[leftChar] < need[leftChar]:
                    formed -= 1

                left += 1

        if ansLen == float("inf"):
            return ""

        return s[ansStart:ansStart + ansLen]
```

---

### Complexity

```text
Time : O(N)

Space : O(Alphabet)
```

Every character enters and leaves the window at most once.

---

# 8. Step-by-Step Trace

Example

```text
s = ADOBECODEBANC
t = ABC
```

Need

```text
A =1
B =1
C =1
```

| Right | Char | Formed | Window Valid? | Action | Best   |
| ----- | ---- | ------ | ------------- | ------ | ------ |
| 0     | A    | 1      | No            | Expand | -      |
| 1     | D    | 1      | No            | Expand | -      |
| 2     | O    | 1      | No            | Expand | -      |
| 3     | B    | 2      | No            | Expand | -      |
| 4     | E    | 2      | No            | Expand | -      |
| 5     | C    | 3      | Yes           | Shrink | ADOBEC |
| 6-9   | ...  | Varies | Expand        | -      | ADOBEC |
| 10    | A    | 3      | Yes           | Shrink | EBANC  |
| 11    | N    | 3      | Yes           | Shrink | EBANC  |
| 12    | C    | 3      | Yes           | Shrink | BANC   |

Final answer

```text
"BANC"
```

---

### Window Evolution

```text
Expand

ADOBEC

✓ valid

↓

Shrink

DOBEC ❌

Expand

DOBECODEBA

✓ valid

↓

Shrink

OBECODEBA
BECODEBA
ECODEBA
...

↓

Eventually

BANC

✓ smallest
```

---

# 9. Related Problems

| Problem                                               | Connection                                                          |
| ----------------------------------------------------- | ------------------------------------------------------------------- |
| **3. Longest Substring Without Repeating Characters** | Variable window with uniqueness instead of frequency requirements.  |
| **438. Find All Anagrams in a String**                | Fixed-size window matching character frequencies.                   |
| **567. Permutation in String**                        | Checks if any window is a valid permutation of `t`.                 |
| **904. Fruit Into Baskets**                           | Window with at most two distinct characters.                        |
| **76. Minimum Window Substring**                      | The most common interview problem for "minimum valid window".       |

---

# Key Interview Takeaways

* **Pattern:** Variable Size Sliding Window.
* **Data Structure:** Two HashMaps (`need` and `window`).
* **Invariant:** The current window is **valid only when all required character frequencies are satisfied**.
* **Rule:** Expand with `right`; once the window becomes valid, shrink from `left` as much as possible while keeping it valid.
* **Answer Update:** Record the minimum window **before** removing the leftmost character.
* **Complexity:** **O(N)** time since each character is added and removed at most once.

---

# Difference from "Longest Substring Without Repeating Characters"

| Longest Substring Without Repeating    | Minimum Window Substring                      |
| -------------------------------------- | --------------------------------------------- |
| Goal: Longest valid window             | Goal: Smallest valid window                   |
| Valid if **all characters are unique** | Valid if **all required frequencies are met** |
| Uses a `HashSet` (or last-seen map)    | Uses frequency `HashMap`s                     |
| Shrink when a duplicate appears        | Shrink after all requirements are satisfied   |
| Update answer after expansion          | Update answer while shrinking                 |

### Interview shortcut

```text
Longest problems:
Expand as much as possible.
Shrink only when forced.

Minimum problems:
Expand until valid.
Shrink as much as possible.
Repeat.
```
