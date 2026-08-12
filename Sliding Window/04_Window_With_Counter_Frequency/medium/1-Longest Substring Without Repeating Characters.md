# 3. Longest Substring Without Repeating Characters (LeetCode 3)

**Pattern:** Variable Size Sliding Window + HashMap/HashSet

---

# 1. Problem Statement

Given a string `s`, find the **length of the longest substring** without repeating characters.

A **substring** consists of contiguous characters.

### Constraints

* `0 <= s.length <= 5 * 10^4`
* `s` contains English letters, digits, symbols and spaces.
* Need an **O(N)** solution.

---

# 2. Diagram

Example:

```
s = "abcabcbb"

Start

a b c a b c b b
L
R

Window = "a"

------------------------

a b c a b c b b
L     R

Window = "abc"

------------------------

Next R = a

a b c a b c b b
L       R

Duplicate 'a'

Move L →

a b c a b c b b
  L     R

Window = "bca"

Continue...
```

Window always contains **unique characters**.

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
Longest substrings:
"abc"
"bca"
"cab"

Length = 3
```

---

### Example 2 (Edge Case)

```
Input:
s = "bbbbb"

Output:
1
```

Explanation

```
Only one unique character can stay.

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
Longest = "wke"
```

---

### Example 4

```
Input:
s = ""

Output:
0
```

---

# 4. Intuition & Pattern Recognition

### Signals

Whenever you see

* Longest/Maximum substring
* Contiguous string
* Constraint up to 50k
* Need O(N)

Think:

> **Sliding Window**

Now ask:

Can window size remain fixed?

No.

Whenever duplicate appears,
window must shrink.

Hence:

> **Variable Size Sliding Window**

### Interview Thinking

Tell yourself:

```
I need the longest valid substring.

Window becomes invalid when
a duplicate enters.

So expand with right pointer.

Whenever duplicate appears,
move left pointer until window
becomes valid again.

Track maximum length.
```

---

# 5. Simpler Version

## Simpler Question 1

### Maximum Number of Vowels in a Substring of Size K

```
Fixed window

Expand
Remove left
Add right
```

Easy because window never changes size.

---

## Simpler Question 2

### Contains Duplicate II

Need to keep only K elements.

Uses HashSet + Sliding Window.

Introduces removing from left.

---

## Current Question

Now window size is **not fixed**.

Instead,

```
Expand

If invalid

Shrink

Continue expanding
```

This becomes the foundation for nearly every sliding window problem.

---

### Thinking Progression

```
Fixed Window

↓

Need HashSet

↓

Need removing from left

↓

Variable Window

↓

Shrink until valid

↓

Longest Substring Without Repeating Characters
```

---

# 6. Brute Force

Generate every substring.

For each substring,

check if all characters are unique.

```
for every i
    for every j
        check uniqueness
```

Checking uniqueness costs O(N).

Overall:

```
Time = O(N³)

Space = O(N)
```

(Using a set during uniqueness check.)

---

# 7. Optimal Solution (Sliding Window)

### Idea

Maintain

```
left
right
HashSet
```

HashSet always stores characters inside current window.

When duplicate arrives,

remove characters from left until duplicate disappears.

Then continue.

### Python

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        seen = set()
        left = 0
        ans = 0

        for right in range(len(s)):

            # Shrink window until current character becomes unique
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            # Add current character to the window
            seen.add(s[right])

            # Update maximum window length
            ans = max(ans, right - left + 1)

        return ans
```

### Complexity

```
Time  : O(N)

Space : O(min(N, Charset))
```

Every character is added once and removed once.

---

# 8. Step-by-Step Trace

Example

```
s = "abcabcbb"
```

| Right | Char | Action                                                                          | Window | Left | Max |
| ----- | ---- | ------------------------------------------------------------------------------- | ------ | ---- | --- |
| 0     | a    | Add                                                                             | a      | 0    | 1   |
| 1     | b    | Add                                                                             | ab     | 0    | 2   |
| 2     | c    | Add                                                                             | abc    | 0    | 3   |
| 3     | a    | Remove a, Add a                                                                 | bca    | 1    | 3   |
| 4     | b    | Remove b, Add b                                                                 | cab    | 2    | 3   |
| 5     | c    | Remove c, Add c                                                                 | abc    | 3    | 3   |
| 6     | b    | Remove a,c? Actually remove a→window "bcb" still duplicate, remove b→then add b | cb     | 5    | 3   |
| 7     | b    | Remove c, remove b, Add b                                                       | b      | 7    | 3   |

Final Answer

```
3
```

### Detailed duplicate handling at `right = 6`

Current window before processing:

```
Window = "abcb"
         ^
Duplicate = b
```

Shrink:

```
Remove 'a' -> "bcb"   (duplicate still exists)

Remove 'b' -> "cb"    (duplicate removed)

Add new 'b' -> "cb"
```

---

# 9. Related Problems

| Problem                                                                 | Connection                                                                           |
| ----------------------------------------------------------------------- | ------------------------------------------------------------------------------------ |
| **485. Max Consecutive Ones**                                           | Fixed expansion only; simplest sliding window intuition.                             |
| **643. Maximum Average Subarray I**                                     | Fixed-size sliding window.                                                           |
| **209. Minimum Size Subarray Sum**                                      | Variable window that shrinks based on a sum condition.                               |
| **904. Fruit Into Baskets**                                             | At most 2 distinct characters; same expand-then-shrink pattern with a frequency map. |
| **340. Longest Substring with At Most K Distinct Characters** (Premium) | Generalization of this problem from "no duplicates" to "at most K distinct".         |

---

# Key Interview Takeaways

* **Pattern:** Variable Size Sliding Window.
* **Data Structure:** `HashSet` (or `HashMap` with last seen index optimization).
* **Invariant:** The current window always contains **unique characters**.
* **Rule:** Expand with `right`; if a duplicate appears, shrink from `left` until the window becomes valid again.
* **Complexity:** **O(N)** time because each character enters and leaves the window at most once.
