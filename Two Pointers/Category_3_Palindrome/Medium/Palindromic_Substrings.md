# Palindromic Substrings (LeetCode 647)

**Pattern:** Expand Around Center (Two Pointers)

---

# 1. Problem Statement

Given a string `s`, return the **total number of palindromic substrings** in it.

A **substring** is a contiguous sequence of characters.

A palindrome reads the same forward and backward.

Unlike *Longest Palindromic Substring*, here we need to **count every palindrome**, even if multiple palindromes have the same value but occur at different positions.

### Constraints

* `1 <= s.length <= 1000`
* `s` consists of lowercase English letters.
* An **O(N²)** solution is expected.

---

# 2. Diagram

Example:

```text
s = "aaa"

Indices

0   1   2
a   a   a

Every center can generate palindromes.

Odd Centers

    a
    ↑

    a
        ↑

    a
            ↑

Even Centers

a | a
  ↑

    a | a
      ↑
```

Expand from every center.

```
Center (0)

a

Count = 1

-------------------

Center (0,1)

aa

Expand

aaa

Count += 2

-------------------

Center (1)

a

Expand

aaa

Count += 2

-------------------

Center (1,2)

aa

Count +=1

-------------------

Center (2)

a

Count +=1

Total = 6
```

---

# 3. Example I/O

### Example 1

```text
Input:
s = "abc"

Output:
3
```

Explanation

```text
"a"
"b"
"c"

Total = 3
```

---

### Example 2

```text
Input:
s = "aaa"

Output:
6
```

Explanation

```text
"a"
"a"
"a"
"aa"
"aa"
"aaa"

Total = 6
```

---

### Example 3 (Edge Case)

```text
Input:
s = "a"

Output:
1
```

---

# 4. Intuition & Pattern Recognition

### Signals

Whenever you see

* Palindrome
* Substring
* Count all palindromes
* String length around 1000

Think:

> **Expand Around Center**

### Why?

Every palindrome has a **center**.

There are only

```
N odd centers

+

N-1 even centers

=

2N-1 centers
```

Instead of checking every substring, start from each center and expand outward while characters match.

---

### Interview Thinking

Tell yourself:

```text
Every palindrome has one center.

Try every possible center.

Expand left and right
while characters are equal.

Every successful expansion
forms one palindrome.
```

---

# 5. Simpler Version

## Simpler Question 1

### Valid Palindrome (LeetCode 125)

```text
Given one string,

check if it's a palindrome.
```

Uses two pointers moving inward.

---

## Simpler Question 2

### Longest Palindromic Substring (LeetCode 5)

Same expansion idea.

Difference:

```text
Longest Palindrome

↓

Keep maximum length.

Current Problem

↓

Count every successful expansion.
```

---

## Current Question

Instead of

```text
Find longest palindrome
```

We do

```text
Expand

↓

Each successful expansion

↓

count++

↓

Continue
```

---

### Thinking Progression

```text
Check Palindrome

↓

Expand Around Center

↓

Find Longest

↓

Count Every Expansion

↓

Palindromic Substrings
```

---

# 6. Brute Force

Generate every substring.

For each substring,

check whether it is a palindrome.

```text
for every start
    for every end
        check palindrome
```

Checking palindrome costs **O(N)**.

### Complexity

```text
Time = O(N³)

Space = O(1)
```

---

# 7. Optimal Solution (Expand Around Center)

### Idea

Every index is

* an odd-length center
* an even-length center

Expand both and count every palindrome.

### Python

```python
class Solution:
    def countSubstrings(self, s: str) -> int:

        n = len(s)
        count = 0

        def expand(left, right):
            nonlocal count

            # Expand while characters match
            while left >= 0 and right < n and s[left] == s[right]:
                count += 1      # Found one palindrome
                left -= 1
                right += 1

        for i in range(n):

            # Odd-length palindromes
            expand(i, i)

            # Even-length palindromes
            expand(i, i + 1)

        return count
```

### Complexity

```text
Time  : O(N²)

Space : O(1)
```

---

# 8. Step-by-Step Trace

Example

```text
s = "aaa"
```

| Center | Expansion | Count |
| ------ | --------- | ----- |
| (0)    | a         | 1     |
| (0,1)  | aa → aaa  | 3     |
| (1)    | a → aaa   | 5     |
| (1,2)  | aa        | 6     |
| (2)    | a         | 7?    |

Notice that `(1)` already counted `"aaa"` centered at index 1, so let's list them correctly:

| Center | Palindromes Found | Running Count |
| ------ | ----------------- | ------------- |
| (0)    | "a"               | 1             |
| (0,1)  | "aa"              | 2             |
| (1)    | "a","aaa"         | 4             |
| (1,2)  | "aa"              | 5             |
| (2)    | "a"               | 6             |

Final Answer

```text
6
```

---

### Another Example

```text
s = "abc"
```

```
Center a → a

Center b → b

Center c → c

No further expansions.

Answer = 3
```

---

# 9. Related Problems

| Problem                                  | Connection                                                                     |
| ---------------------------------------- | ------------------------------------------------------------------------------ |
| **125. Valid Palindrome**                | Basic palindrome checking with two pointers.                                   |
| **5. Longest Palindromic Substring**     | Same expand-around-center technique; keep the longest instead of counting all. |
| **516. Longest Palindromic Subsequence** | Dynamic Programming on palindromes (subsequence instead of substring).         |
| **131. Palindrome Partitioning**         | Uses palindrome expansion/precomputation with DFS backtracking.                |
| **132. Palindrome Partitioning II**      | Builds on palindrome detection with Dynamic Programming for minimum cuts.      |

---

# Key Interview Takeaways

* **Pattern:** Expand Around Center.
* **Observation:** Every palindrome has a unique center.
* **Centers:** There are **2N − 1** possible centers (N odd + N−1 even).
* **Rule:** Expand while `s[left] == s[right]`; every successful expansion contributes **one palindrome**.
* **Why O(N²)?** Each center expands outward, and across all centers the worst-case work is quadratic.
* **When to use this pattern:** Whenever the problem involves **palindromic substrings** (counting or finding the longest) and `N ≤ 1000`, Expand Around Center is usually the cleanest interview solution.
