# Reverse Vowels of a String (LeetCode 345)

**Pattern:** Two Pointers

---

# 1. Problem Statement

Given a string `s`, reverse **only the vowels** in the string while keeping all consonants and other characters in their original positions.

The vowels are:

```text
a, e, i, o, u
A, E, I, O, U
```

Return the modified string.

### Constraints

* `1 <= s.length <= 3 × 10^5`
* `s` consists of printable ASCII characters.

---

# 2. Diagram

Example:

```text
s = "hello"

Initial

L               R
↓               ↓
h   e   l   l   o

L moves → (skip h)

h   e   l   l   o
    L       R

Both are vowels

Swap

h   o   l   l   e

Move inward

Stop
```

Only vowels are swapped.

---

# 3. Example I/O

### Example 1

```text
Input:
s = "hello"

Output:
"holle"
```

Explanation

```text
Vowels:
e o

Reverse them

o e
```

---

### Example 2

```text
Input:
s = "leetcode"

Output:
"leotcede"
```

Explanation

```text
Vowels:
e e o e

↓

e o e e
```

---

### Example 3 (Edge Case)

```text
Input:
s = "bcdfg"

Output:
"bcdfg"
```

No vowels exist.

---

### Example 4

```text
Input:
s = "aA"

Output:
"Aa"
```

Uppercase vowels are also considered.

---

# 4. Intuition & Pattern Recognition

### Signals

Whenever you see:

* Reverse only specific elements
* Preserve positions of everything else
* Compare elements from both ends

Think:

> **Two Pointers**

---

### Interview Thinking

Tell yourself:

```text
Only vowels need to move.

Left pointer finds next vowel.

Right pointer finds previous vowel.

Swap them.

Continue until pointers meet.
```

---

# 5. Simpler Version

## Simpler Question 1

### Reverse String

Reverse every character.

```text
Swap first and last.

Move inward.
```

---

## Simpler Question 2

### Move Zeroes

Skip unwanted elements while processing.

Introduces the idea of ignoring certain values.

---

## Current Question

Now we combine both ideas.

```text
Move pointers

Skip consonants

Swap vowels

Repeat
```

---

### Thinking Progression

```text
Reverse String

↓

Two pointers

↓

Need to ignore some characters

↓

Skip until vowel found

↓

Swap vowels

↓

Reverse Vowels
```

---

# 6. Brute Force

Store all vowels.

Reverse them.

Replace vowels one by one.

```python
vowels = []

Collect all vowels

Reverse list

Traverse again

Replace vowels
```

### Complexity

```text
Time  : O(N)

Space : O(N)
```

---

# 7. Optimal Solution (Two Pointers)

### Idea

Maintain two pointers.

* Left searches for the next vowel.
* Right searches for the previous vowel.
* Swap when both point to vowels.

---

### Python

```python
class Solution:
    def reverseVowels(self, s: str) -> str:

        vowels = set("aeiouAEIOU")

        s = list(s)

        left = 0
        right = len(s) - 1

        while left < right:

            # Skip non-vowels from the left
            while left < right and s[left] not in vowels:
                left += 1

            # Skip non-vowels from the right
            while left < right and s[right] not in vowels:
                right -= 1

            # Swap vowels
            s[left], s[right] = s[right], s[left]

            left += 1
            right -= 1

        return "".join(s)
```

---

### Complexity

```text
Time  : O(N)

Space : O(N)
```

> **Why O(N) space?**
>
> In Python, strings are immutable, so we convert the string to a list (`list(s)`), which requires O(N) space.
>
> Algorithmically, the two-pointer technique itself uses **O(1)** extra space. In languages like C++ or Java (using a mutable character array), the reversal is done in-place.

---

# 8. Step-by-Step Trace

Example

```text
s = "leetcode"
```

Initial

```text
l e e t c o d e
L             R
```

| Left | Right | Action     | String   |
| ---- | ----- | ---------- | -------- |
| 0    | 7     | Skip 'l'   | leetcode |
| 1    | 7     | Swap e ↔ e | leetcode |
| 2    | 6     | Skip d     | leetcode |
| 2    | 5     | Swap e ↔ o | leotcede |
| 3    | 4     | Skip t, c  | Stop     |

Final Answer

```text
leotcede
```

---

# 9. Related Problems

| Problem                             | Connection                                                 |
| ----------------------------------- | ---------------------------------------------------------- |
| **344. Reverse String**             | Basic two-pointer reversal.                                |
| **125. Valid Palindrome**           | Skip unwanted characters while moving inward.              |
| **680. Valid Palindrome II**        | Similar inward traversal with one deletion allowed.        |
| **917. Reverse Only Letters**       | Reverse only letters while leaving other characters fixed. |
| **1768. Merge Strings Alternately** | Another easy two-pointer string manipulation problem.      |

---

# Key Interview Takeaways

* **Pattern:** Two Pointers.
* **Data Structure:** HashSet for O(1) vowel lookup.
* **Invariant:** Characters outside `[left, right]` are already finalized.
* **Rule:** Move both pointers until vowels are found, swap them, then continue inward.
* **Complexity:** **O(N)** time. **O(1)** auxiliary algorithmic space (or **O(N)** in Python due to string immutability).

---

# Pattern Summary

```text
Need to reverse something?

↓

Whole string?
    → Reverse String

↓

Only selected characters?

↓

Use Two Pointers

↓

Left finds valid character

↓

Right finds valid character

↓

Swap

↓

Continue until pointers meet

↓

Reverse Vowels of a String
```
