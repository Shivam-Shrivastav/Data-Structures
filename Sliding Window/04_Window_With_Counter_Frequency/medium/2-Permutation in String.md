# 567. Permutation in String

**Pattern:** Fixed Size Sliding Window + Frequency Count

---

# 1. Problem Statement

Given two strings `s1` and `s2`, return **true** if `s2` contains a substring that is a **permutation (anagram)** of `s1`, otherwise return **false**.

A permutation means the characters are the same, but the order can be different.

### Constraints

* `1 <= s1.length, s2.length <= 10^4`
* `s1` and `s2` contain only lowercase English letters.
* Need an **O(N)** solution.

---

# 2. Diagram

Example:

```text
s1 = "ab"
s2 = "eidbaooo"

Need a window of size = 2

e i d b a o o o
L R

Window = "ei" ❌

--------------------

e i d b a o o o
    L   R

Window = "db" ❌

--------------------

e i d b a o o o
      L   R

Window = "ba" ✅

"ba" is a permutation of "ab"

Answer = True
```

The window size **never changes**. Only slide it one step at a time.

---

# 3. Example I/O

### Example 1

```text
Input:
s1 = "ab"
s2 = "eidbaooo"

Output:
True
```

Explanation

```text
Substring = "ba"

Permutation of "ab"
```

---

### Example 2

```text
Input:
s1 = "ab"
s2 = "eidboaoo"

Output:
False
```

No substring of length 2 has the same character frequencies.

---

### Example 3 (Edge Case)

```text
Input:
s1 = "adc"
s2 = "dcda"

Output:
True
```

Explanation

```text
Substring = "cda"

Permutation of "adc"
```

---

### Example 4

```text
Input:
s1 = "abc"
s2 = "ab"

Output:
False
```

Window can never reach size 3.

---

# 4. Intuition & Pattern Recognition

### Signals

Whenever you see

* "Permutation"
* "Anagram"
* "Substring"
* Exact window length

Think:

> **Fixed Size Sliding Window + Frequency Count**

### Why?

Every valid substring must have

* Same length as `s1`
* Same frequency of every character

Instead of sorting every window (O(K log K)), maintain character counts while sliding.

### Interview Thinking

```text
Every candidate substring must have length = len(s1).

I'll maintain a window of exactly that size.

Whenever the window slides:
- Remove left character
- Add right character

If window frequency == s1 frequency,
I've found a permutation.
```

---

# 5. Simpler Version

## Simpler Question 1

### Find All Anagrams in a String (LeetCode 438)

Instead of returning **True/False**, return **all starting indices**.

Exactly the same sliding window.

---

## Simpler Question 2

Compare two strings

```text
"abc"
"bca"

Do they have the same frequency?
```

Use two frequency arrays.

---

## Current Question

Now instead of comparing one string,

compare **every window** of length `len(s1)`.

### Thinking Progression

```text
Compare two strings

↓

Frequency Array

↓

Fixed Window

↓

Slide Window

↓

Permutation in String
```

---

# 6. Brute Force

For every substring of size `len(s1)`:

1. Extract substring.
2. Sort it.
3. Compare with sorted `s1`.

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

Maintain two frequency arrays of size **26**.

* `need` → frequency of `s1`
* `window` → frequency of current window

When window exceeds size:

* Remove left character
* Add new right character

If both arrays are equal → return True.

### Python

```python
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        need = [0] * 26
        window = [0] * 26

        # Frequency of s1
        for ch in s1:
            need[ord(ch) - ord('a')] += 1

        left = 0

        for right in range(len(s2)):

            # Add current character
            window[ord(s2[right]) - ord('a')] += 1

            # Keep window size equal to len(s1)
            if right - left + 1 > len(s1):
                window[ord(s2[left]) - ord('a')] -= 1
                left += 1

            # Compare frequencies
            if window == need:
                return True

        return False
```

---

### Complexity

```text
Time  : O(N)

Space : O(1)
```

> Comparing two arrays of size 26 is constant time.

---

# 8. Step-by-Step Trace

Example

```text
s1 = "ab"
s2 = "eidbaooo"
```

Need Frequency

```text
a : 1
b : 1
```

| Right | Window | Action          | Match |
| ----- | ------ | --------------- | ----- |
| 0     | e      | Add e           | ❌     |
| 1     | ei     | Compare         | ❌     |
| 2     | id     | Remove e, Add d | ❌     |
| 3     | db     | Remove i, Add b | ❌     |
| 4     | ba     | Remove d, Add a | ✅     |

Window frequencies now equal:

```text
a : 1
b : 1
```

Return

```text
True
```

---

# 9. Related Problems

| Problem                                                           | Connection                                                        |
| ----------------------------------------------------------------- | ----------------------------------------------------------------- |
| **643. Maximum Average Subarray I**                               | Simplest fixed-size sliding window.                               |
| **1456. Maximum Number of Vowels in a Substring of Given Length** | Fixed-size window with incremental updates.                       |
| **438. Find All Anagrams in a String**                            | Same algorithm; return all matching indices instead of a boolean. |
| **76. Minimum Window Substring**                                  | Variable-size version using frequency maps.                       |
| **30. Substring with Concatenation of All Words**                 | Advanced fixed-size sliding window with frequency matching.       |

---

# Key Interview Takeaways

* **Pattern:** Fixed Size Sliding Window.
* **Window Size:** Always `len(s1)`.
* **Data Structure:** Two frequency arrays (`26` lowercase letters).
* **Invariant:** The window always has the same length as `s1`.
* **Rule:** Add the new character, remove the left character when needed, then compare frequency arrays.
* **Complexity:** **O(N)** time and **O(1)** space.

---

### Sliding Window Revision Flow

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
Permutation in String
        │
        ▼
Find All Anagrams in a String
        │
        ▼
Minimum Window Substring (Variable Window)
```

For your sliding-window revision roadmap, this problem comes **immediately before "Find All Anagrams in a String"**, since both use the exact same frequency-array technique—the only difference is that this problem returns a boolean, while the latter collects all valid starting indices. (Your previous revision sheet on **Longest Substring Without Repeating Characters** covered the variable-size sliding window pattern, which contrasts nicely with this fixed-size frequency-window approach.) 
