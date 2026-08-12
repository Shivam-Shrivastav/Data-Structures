# 438. Find All Anagrams in a String

**Pattern:** Fixed Size Sliding Window + Frequency Count

---

# 1. Problem Statement

Given two strings `s` and `p`, return **all starting indices** of `p`'s anagrams in `s`.

An **anagram** is formed by rearranging the characters of another string using all the original characters exactly once.

The answer can be returned in **any order**.

### Constraints

* `1 <= s.length, p.length <= 3 × 10⁴`
* `s` and `p` contain only lowercase English letters.
* Need an **O(N)** solution.

---

# 2. Diagram

Example

```text
p = "abc"

s = "cbaebabacd"

Window Size = 3

c b a e b a b a c d
L   R

Window = "cba" ✅
Index = 0

-------------------------

c b a e b a b a c d
  L   R

Window = "bae" ❌

-------------------------

c b a e b a b a c d
              L   R

Window = "bac" ✅
Index = 6
```

The window size **never changes**.

---

# 3. Example I/O

### Example 1

```text
Input:
s = "cbaebabacd"
p = "abc"

Output:
[0,6]
```

Explanation

```text
Index 0 → "cba"

Index 6 → "bac"

Both are permutations of "abc".
```

---

### Example 2

```text
Input:
s = "abab"
p = "ab"

Output:
[0,1,2]
```

Explanation

```text
0 → "ab"

1 → "ba"

2 → "ab"
```

---

### Example 3 (Edge Case)

```text
Input:
s = "a"
p = "aa"

Output:
[]
```

Window of size 2 can never be formed.

---

# 4. Intuition & Pattern Recognition

### Signals

Whenever you see

* Anagram
* Permutation
* Substring
* Return all matches

Think:

> **Fixed Size Sliding Window + Frequency Array**

### Why?

Every valid substring

* Has length exactly `len(p)`
* Has identical character frequencies

Instead of sorting each window,

maintain character counts while sliding.

### Interview Thinking

```text
Every candidate substring must be the
same size as p.

I'll slide one window of size len(p).

If frequency arrays match,
record the starting index.
```

---

# 5. Simpler Version

## Simpler Question 1

Compare two strings

```text
abc

bca
```

Do they have identical character counts?

---

## Simpler Question 2

### Permutation in String (LeetCode 567)

Same algorithm.

Difference:

```text
Return True

instead of

Return every index
```

---

## Current Question

Instead of stopping after the first match,

continue sliding and collect every valid index.

### Thinking Progression

```text
Frequency Comparison

↓

Permutation in String

↓

Don't stop

↓

Store every matching index

↓

Find All Anagrams
```

---

# 6. Brute Force

Generate every substring of size `len(p)`.

Sort and compare.

```text
for every window

    sort(window)

    compare
```

### Complexity

```text
Time = O((N-K+1) × K log K)

Space = O(K)
```

---

# 7. Optimal Solution (Sliding Window)

### Idea

Maintain

* `need` → frequency of `p`
* `window` → frequency of current window

Window size is always `len(p)`.

Whenever frequencies match,

store `left`.

### Python

```python
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        if len(p) > len(s):
            return []

        need = [0] * 26
        window = [0] * 26

        # Build frequency of p
        for ch in p:
            need[ord(ch) - ord('a')] += 1

        left = 0
        ans = []

        for right in range(len(s)):

            # Add current character
            window[ord(s[right]) - ord('a')] += 1

            # Keep window size fixed
            if right - left + 1 > len(p):
                window[ord(s[left]) - ord('a')] -= 1
                left += 1

            # Found an anagram
            if window == need:
                ans.append(left)

        return ans
```

### Complexity

```text
Time  : O(N)

Space : O(1)
```

Comparing two arrays of size 26 is constant time.

---

# 8. Step-by-Step Trace

Example

```text
s = "cbaebabacd"

p = "abc"
```

Need Frequency

```text
a : 1

b : 1

c : 1
```

| Right | Window | Left | Match       | Answer |
| ----- | ------ | ---- | ----------- | ------ |
| 0     | c      | 0    | No (size<3) | []     |
| 1     | cb     | 0    | No (size<3) | []     |
| 2     | cba    | 0    | ✅           | [0]    |
| 3     | bae    | 1    | ❌           | [0]    |
| 4     | aeb    | 2    | ❌           | [0]    |
| 5     | eba    | 3    | ❌           | [0]    |
| 6     | bab    | 4    | ❌           | [0]    |
| 7     | aba    | 5    | ❌           | [0]    |
| 8     | bac    | 6    | ✅           | [0,6]  |
| 9     | acd    | 7    | ❌           | [0,6]  |

Final Answer

```text
[0,6]
```

---

# 9. Related Problems

| Problem                                                           | Connection                                               |
| ----------------------------------------------------------------- | -------------------------------------------------------- |
| **643. Maximum Average Subarray I**                               | Basic fixed-size sliding window.                         |
| **1456. Maximum Number of Vowels in a Substring of Given Length** | Fixed-size window with incremental updates.              |
| **567. Permutation in String**                                    | Same algorithm; returns `True/False` instead of indices. |
| **76. Minimum Window Substring**                                  | Variable-size sliding window using frequencies.          |
| **30. Substring with Concatenation of All Words**                 | Advanced frequency-based sliding window.                 |

---

# Key Interview Takeaways

* **Pattern:** Fixed Size Sliding Window.
* **Window Size:** Always `len(p)`.
* **Data Structure:** Two frequency arrays of size 26.
* **Invariant:** The window always has the same length as `p`.
* **Rule:** Add the new character, remove the left character when the window grows too large, compare frequency arrays, and record the left index on every match.
* **Complexity:** **O(N)** time and **O(1)** space.

---

# Difference from "Permutation in String"

| Permutation in String (567)        | Find All Anagrams (438)         |
| ---------------------------------- | ------------------------------- |
| Return `True` if one match exists  | Return every matching index     |
| Stop immediately after first match | Continue scanning entire string |
| Output: `bool`                     | Output: `List[int]`             |
| Logic is identical                 | Logic is identical              |

### Interview Shortcut

```text
438 = 567 + store answers

Everything else is exactly the same.
```

---

# Sliding Window Revision Flow

```text
Fixed Window
      │
      ▼
Maximum Average Subarray I
      │
      ▼
Maximum Number of Vowels
      │
      ▼
Permutation in String (567)
      │
      ▼
Find All Anagrams in a String (438)
      │
      ▼
Minimum Window Substring (76)
```

**Key observation:** LeetCode **438** is essentially an extension of **567**. If you can solve **Permutation in String**, you already know 95% of the solution—just replace `return True` with `ans.append(left)` and continue sliding until the end.
