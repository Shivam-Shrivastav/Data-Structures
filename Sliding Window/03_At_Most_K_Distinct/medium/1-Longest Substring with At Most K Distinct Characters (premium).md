# 340. Longest Substring with At Most K Distinct Characters (Premium)

## 1. Problem Statement

Given a string `s` and an integer `k`, return the **length of the longest substring** that contains **at most `k` distinct characters**.

A substring must be **contiguous**.

### Constraints

* `1 <= s.length <= 5 × 10^4`
* `0 <= k <= 50`
* `s` consists of English letters.

Since `n` can be large, an **O(n²)** solution is too slow.

---

# 2. Diagram

We expand the window while the number of distinct characters is ≤ `k`.

If it becomes **greater than `k`**, shrink from the left.

Example:

```text
s = "eceba"
k = 2
```

```text
            right
              ↓
e c e
↑
left

Window = "ece"

Frequency
e -> 2
c -> 1

Distinct = 2 ✅
Length = 3
```

Next character:

```text
e c e b
      ↑

Distinct

e
c
b

= 3 ❌
```

Shrink:

```text
Remove e

c e b

Still 3

Remove c

e b

Distinct = 2 ✅
```

Continue...

---

# 3. Example I/O

### Example 1

```text
Input:
s = "eceba"
k = 2

Output:
3
```

Explanation

```text
Longest substring

"ece"

Length = 3
```

---

### Example 2

```text
Input:
s = "aa"
k = 1

Output:
2
```

Explanation

```text
Entire string has only one distinct character.
```

---

### Edge Case

```text
Input:
s = "abc"
k = 0

Output:
0
```

No characters are allowed.

---

# 4. Intuition & Pattern Recognition

## Signal 1

Question asks

> Longest Substring

Whenever you see

* longest
* shortest
* substring

think

> **Sliding Window**

---

## Signal 2

Need

> At most K distinct characters

That means we need to know

* how many unique characters exist inside window

A **HashMap (frequency map)** is perfect.

---

## Pattern

Expand window.

```text
Add right character
Increase frequency
```

If

```text
distinct > k
```

Shrink until

```text
distinct <= k
```

Update answer whenever window is valid.

---

### Interview Thought Process

> "Longest valid substring."

> "Validity depends on number of distinct characters."

> "Use a frequency map."

> "Whenever validity breaks, shrink."

---

# 5. Simpler Version

## Simpler Problem 1

### 3. Longest Substring Without Repeating Characters

Need

```text
Distinct = Window Size
```

No duplicates allowed.

---

## Simpler Problem 2

Longest substring containing only one distinct character.

Very easy sliding window.

---

## Current Problem

Instead of

```text
Distinct <= 1
```

or

```text
No duplicates
```

Generalize to

```text
Distinct <= K
```

---

### Thinking Progression

```text
Longest substring

↓

Need window validity

↓

Validity = Number of distinct characters

↓

Maintain frequencies

↓

Shrink whenever
distinct > K
```

---

### Related Simpler Questions

* 3. Longest Substring Without Repeating Characters
* 904. Fruit Into Baskets (`k = 2`)
* 1004. Max Consecutive Ones III (different validity condition)

---

# 6. Brute Force

Generate every substring.

Count distinct characters.

```python
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s, k):
        n = len(s)
        ans = 0

        for i in range(n):
            freq = {}

            for j in range(i, n):
                freq[s[j]] = freq.get(s[j], 0) + 1

                if len(freq) <= k:
                    ans = max(ans, j - i + 1)
                else:
                    break

        return ans
```

### Complexity

Time

```text
O(n²)
```

Space

```text
O(k)
```

---

# 7. Optimal Solution (Sliding Window + Frequency Map)

```python
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s, k):
        if k == 0:
            return 0

        freq = {}
        left = 0
        ans = 0

        for right in range(len(s)):

            # Include current character.
            freq[s[right]] = freq.get(s[right], 0) + 1

            # Too many distinct characters? Shrink window.
            while len(freq) > k:
                freq[s[left]] -= 1

                # Remove character completely when its count becomes 0.
                if freq[s[left]] == 0:
                    del freq[s[left]]

                left += 1

            # Current window is valid.
            ans = max(ans, right - left + 1)

        return ans
```

---

### Why Frequency Map?

A **set** only tells whether a character exists.

When shrinking,

```text
eceba

remove e
```

There is still another `e` inside.

Need counts.

Hence

```text
HashMap
```

instead of

```text
HashSet
```

---

### Complexity

Time

```text
O(n)
```

Each character enters and leaves the window once.

Space

```text
O(k)
```

The map stores at most `k + 1` distinct characters before shrinking, so the auxiliary space is effectively bounded by the number of distinct characters in the window.

---

# 8. Step-by-Step Trace

Example

```text
s = "eceba"
k = 2
```

| Right | Char | Window | Frequency     | Distinct | Action | Answer |
| ----- | ---- | ------ | ------------- | -------- | ------ | ------ |
| 0     | e    | e      | {e:1}         | 1        | Valid  | 1      |
| 1     | c    | ec     | {e:1,c:1}     | 2        | Valid  | 2      |
| 2     | e    | ece    | {e:2,c:1}     | 2        | Valid  | 3      |
| 3     | b    | eceb   | {e:2,c:1,b:1} | 3        | Shrink | 3      |
|       |      | ceb    | {e:1,c:1,b:1} | 3        | Shrink | 3      |
|       |      | eb     | {e:1,b:1}     | 2        | Valid  | 3      |
| 4     | a    | eba    | {e:1,b:1,a:1} | 3        | Shrink | 3      |
|       |      | ba     | {b:1,a:1}     | 2        | Valid  | 3      |

Final Answer

```text
3
```

---

# 9. Related Problems (Increasing Difficulty)

| Problem                                                         | Connection                                                                                                                |
| --------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| **159. Longest Substring with At Most Two Distinct Characters** | Same algorithm with `k = 2`. This is the direct simpler version of the current problem.                                   |
| **904. Fruit Into Baskets**                                     | Identical pattern on arrays instead of strings; at most two distinct values.                                              |
| **1004. Max Consecutive Ones III**                              | Variable-size sliding window where the validity condition is based on the number of zeros instead of distinct characters. |
| **424. Longest Repeating Character Replacement**                | Sliding window with a frequency map, but validity depends on the most frequent character in the window.                   |
| **76. Minimum Window Substring**                                | Uses the same expand/shrink framework, but finds the **smallest** valid window satisfying character requirements.         |
