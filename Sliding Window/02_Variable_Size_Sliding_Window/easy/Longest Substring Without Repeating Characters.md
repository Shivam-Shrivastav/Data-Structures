**LeetCode 3 – Longest Substring Without Repeating Characters**, following your requested format. I've also incorporated the uploaded revision notes where relevant. 

---

# 3. Longest Substring Without Repeating Characters (LeetCode 3)

**Pattern:** Variable Size Sliding Window + HashSet / HashMap

---

# 1. Problem Statement

Given a string `s`, return the **length of the longest substring** that contains **no repeated characters**.

A **substring** is a **contiguous** sequence of characters.

### Example

```
Input:
s = "abcabcbb"

Output:
3

Explanation:
The longest substrings are:
"abc"
"bca"
"cab"

Length = 3
```

### Constraints

* `0 <= s.length <= 5 × 10⁴`
* Characters can be letters, digits, spaces, or symbols.
* Expected solution: **O(N)**

---

# 2. Diagram

```
s = "abcabcbb"

          Right
            ↓
a  b  c  a  b  c  b  b
↑
Left

Window = "abc"
Unique ✔

------------------------------------

Move Right →

a  b  c  a  b  c  b  b
          ↑
       Duplicate 'a'

Window becomes invalid

Move Left →

a  b  c  a  b  c  b  b
   ↑      ↑

Window = "bca"
Unique again ✔
```

### Sliding Window Rule

```
Expand Right

        ↓
Duplicate?

   No  ----------> Update answer

   Yes ----------> Shrink Left
                   Until valid
```

---

# 3. Example I/O

### Example 1

```
Input:
s = "abcabcbb"

Output:
3
```

Explanation

```
Longest substring:
"abc"
```

---

### Example 2

```
Input:
s = "bbbbb"

Output:
1
```

Explanation

```
Only one unique character can exist.

Longest:
"b"
```

---

### Example 3

```
Input:
s = "pwwkew"

Output:
3
```

Explanation

```
Longest:
"wke"
```

---

### Edge Case

```
Input:
s = ""

Output:
0
```

---

# 4. Intuition & Pattern Recognition

## How to recognize this pattern

Whenever you see:

* Longest substring
* Contiguous characters
* Constraint around 10⁵ or 5×10⁴
* Need O(N)

Think immediately:

> **Sliding Window**

Now ask yourself:

### Can the window stay fixed?

No.

Because duplicates can appear anywhere.

Window size must increase and decrease dynamically.

Therefore:

> **Variable Size Sliding Window**

---

## Interview Thinking

> I need the longest valid substring.

```
Expand Right

↓

If duplicate appears

↓

Shrink Left

↓

Window becomes valid

↓

Continue expanding
```

The window is **always valid** before calculating the answer.

---

# 5. Simpler Version

## Simpler Question 1

### Maximum Average Subarray I

Fixed-size Sliding Window

```
Expand

Remove left

Add right
```

Window size never changes.

Learns:

* Sliding window movement

---

## Simpler Question 2

### Contains Duplicate II

Uses HashSet + Sliding Window

```
Keep only K elements

Remove from left
```

Learns:

* Maintaining a set
* Removing elements while moving left

---

## Simpler Question 3

### Longest Substring with At Most Two Distinct Characters

Instead of

```
No duplicates
```

Allow

```
At most 2 distinct characters
```

Introduces frequency maps.

---

## Current Question

Now combine everything.

```
Sliding Window

+

HashSet

+

Shrink until valid
```

---

### Thinking Progression

```
Fixed Window

↓

Sliding Window

↓

HashSet

↓

Remove Left

↓

Variable Window

↓

Shrink Until Valid

↓

Longest Substring Without Repeating Characters
```

---

# 6. Brute Force

Generate every possible substring.

For each substring,

check whether every character is unique.

```python
ans = 0

for i in range(len(s)):
    for j in range(i, len(s)):
        if len(set(s[i:j+1])) == (j - i + 1):
            ans = max(ans, j - i + 1)

return ans
```

### Complexity

```
Time : O(N³)

Space : O(N)
```

Reason:

* O(N²) substrings
* O(N) uniqueness check

---

# 7. Optimal Solution

## Approach 1 (Most Interview Friendly)

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        seen = set()
        left = 0
        ans = 0

        for right in range(len(s)):

            # Remove characters until duplicate disappears
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            # Add current character
            seen.add(s[right])

            # Update longest length
            ans = max(ans, right - left + 1)

        return ans
```

### Complexity

```
Time : O(N)

Space : O(min(N, Character Set))
```

Every character:

* Added once
* Removed once

Hence total work = **2N = O(N)**

---

## ⭐ Interview Optimization (HashMap)

Instead of removing one character at a time,

jump directly to the duplicate's next position.

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        last_seen = {}
        left = 0
        ans = 0

        for right, ch in enumerate(s):

            if ch in last_seen:
                # Never move left backwards
                left = max(left, last_seen[ch] + 1)

            last_seen[ch] = right
            ans = max(ans, right - left + 1)

        return ans
```

### Complexity

```
Time : O(N)

Space : O(min(N, Character Set))
```

### Why `max(left, last_seen[ch] + 1)`?

Example:

```
abba

Without max:

left moves backward ❌

With max:

left never decreases ✔
```

This is the version many interviewers prefer.

---

# 8. Step-by-Step Trace

Example

```
s = "abcabcbb"
```

| Right | Char | Action                      | Window | Left | Max |
| ----: | ---- | --------------------------- | ------ | ---: | --: |
|     0 | a    | Add                         | a      |    0 |   1 |
|     1 | b    | Add                         | ab     |    0 |   2 |
|     2 | c    | Add                         | abc    |    0 |   3 |
|     3 | a    | Remove a → Add a            | bca    |    1 |   3 |
|     4 | b    | Remove b → Add b            | cab    |    2 |   3 |
|     5 | c    | Remove c → Add c            | abc    |    3 |   3 |
|     6 | b    | Remove a → Remove b → Add b | cb     |    5 |   3 |
|     7 | b    | Remove c → Remove b → Add b | b      |    7 |   3 |

Final Answer

```
3
```

---

# 9. Related Problems

| Problem                                              | Connection                                              |
| ---------------------------------------------------- | ------------------------------------------------------- |
| Maximum Average Subarray I                           | Fixed-size sliding window; easiest introduction.        |
| Minimum Size Subarray Sum                            | Variable-size window that shrinks based on a condition. |
| Permutation in String                                | Sliding window + frequency counting.                    |
| Longest Substring with At Most K Distinct Characters | Generalizes this problem using a frequency map.         |
| Minimum Window Substring                             | Most advanced variable-size sliding window problem.     |

---

# 🚀 Interview Cheat Sheet

### Pattern Recognition

```
Longest + Substring

↓

Sliding Window

↓

Duplicate?

↓

Shrink Left

↓

Unique Again

↓

Update Answer
```

### Window Invariant

```
Window ALWAYS contains unique characters.
```

### Data Structure

```
HashSet
```

or

```
HashMap (last seen index)
```

### Core Template

```python
for right in range(len(s)):

    while window_invalid:
        remove_left()

    add_right()

    update_answer()
```

### Common Mistakes

* ❌ Using `if` instead of `while` when shrinking (multiple duplicates may need removal).
* ❌ Forgetting to update the answer **after** the window becomes valid.
* ❌ In the HashMap approach, using `left = last_seen[ch] + 1` without `max(...)`, which can incorrectly move `left` backwards.

### Complexity

```
Time  : O(N)
Space : O(min(N, Character Set))
```

This is one of the **foundation problems for the Variable Size Sliding Window pattern**. Once you're comfortable with it, the natural progression is:

**Longest Substring Without Repeating Characters → Fruit Into Baskets → Longest Substring with At Most K Distinct Characters → Minimum Window Substring → Substring with Concatenation of All Words**.
