# 242. Valid Anagram

**Pattern:** Frequency Counting / HashMap
**Difficulty:** Easy

---

## 1. Problem Statement

Given two strings `s` and `t`, return `True` if `t` is an **anagram** of `s`; otherwise return `False`.

An anagram contains **exactly the same characters with exactly the same frequencies**, but the order can be different.

```text
s = "anagram"
t = "nagaram"

Output: True
```

Both contain:

```text
a → 3
n → 1
g → 1
r → 1
m → 1
```

### Constraints

```text
1 <= s.length, t.length <= 5 * 10^4
s and t contain lowercase English letters.
```

The key is that **order does not matter, frequency does**.

---

## 2. Diagram

```text
s = "anagram"
t = "nagaram"

        s                   t
    ┌─────────┐         ┌─────────┐
    │ anagram │         │ nagaram │
    └─────────┘         └─────────┘
         ↓                   ↓

       Frequency           Frequency

       a → 3               a → 3
       n → 1               n → 1
       g → 1               g → 1
       r → 1               r → 1
       m → 1               m → 1

              SAME
               ↓
             True
```

Compare **counts**, not positions.

---

## 3. Example I/O

### Example 1 — Typical

```text
Input:
s = "anagram"
t = "nagaram"

Output:
True
```

Same characters, same frequencies.

### Example 2 — Edge Case

```text
Input:
s = "rat"
t = "car"

Output:
False
```

Their frequencies differ:

```text
s: r → 1, a → 1, t → 1
t: c → 1, a → 1, r → 1

t is missing 't'
s is missing 'c'
```

### Important early check

```text
s = "abc"
t = "abcd"

False
```

Different lengths can **never** be anagrams.

---

# 4. Intuition & Pattern Recognition

The biggest signal is:

> **Same characters, order doesn't matter.**

Whenever order doesn't matter but occurrences do, think:

**Frequency Counting**

Do **not** think:

```text
"Does t contain every character from s?"
```

Because:

```text
s = "aa"
t = "ab"
```

`a` exists in both, but:

```text
s needs a → 2
t has   a → 1
```

Instead ask:

```text
For every character:

count in s == count in t ?
```

### Interview thinking

```text
Order doesn't matter.

So positions are irrelevant.

I only care about how many times
each character occurs.

First check equal lengths.

Then count characters.

If all frequencies match → anagram.
```

---

# 5. Simpler Version

## Step 1: Contains Duplicate — LeetCode 217

The simplest HashSet idea:

```text
Have I seen this value before?
```

You learn:

```text
value → existence
```

---

## Step 2: Ransom Note — LeetCode 383

Now existence isn't enough.

```text
ransomNote = "aa"
magazine   = "aab"
```

You need:

```text
How many copies are available?
```

So:

```text
character → frequency
```

But Ransom Note only requires:

```text
available >= required
```

Magazine can contain extra characters.

---

## Step 3: Valid Anagram

Now the requirement becomes stricter:

```text
count_s(char) == count_t(char)
```

for **every character**.

### Progression

```text
Contains Duplicate
        ↓
Do I have this value?
        ↓
      HashSet


Ransom Note
        ↓
Do I have ENOUGH of each character?
        ↓
available >= required
        ↓
      HashMap


Valid Anagram
        ↓
Do I have EXACTLY the same characters?
        ↓
count(s) == count(t)
        ↓
      HashMap
```

So Valid Anagram is fundamentally a **frequency equality** problem.

---

# 6. Brute Force — Sorting

A straightforward approach is to sort both strings.

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
```

Why?

```text
s = "anagram"
t = "nagaram"

sorted(s) = "aaagmnr"
sorted(t) = "aaagmnr"

Same → True
```

### Complexity

```text
Time:  O(N log N)
Space: O(N)
```

This is simple and perfectly valid, but we can avoid sorting.

---

# 7. Optimal Solution — Frequency Counting

Use one HashMap.

For every character in `s`, increase its count.

For every character in `t`, decrease its count.

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # Anagrams must have equal lengths
        if len(s) != len(t):
            return False

        freq = {}

        # Count characters from s
        for char in s:
            freq[char] = freq.get(char, 0) + 1

        # Consume those counts using t
        for char in t:
            if freq.get(char, 0) == 0:
                return False

            freq[char] -= 1

        return True
```

### Why does this work?

Think:

```text
s adds characters into inventory
t removes characters from inventory
```

Example:

```text
s = "aab"

After s:

a → 2
b → 1

t = "aba"

process a → a = 1
process b → b = 0
process a → a = 0

Everything matched.
```

Because we already verified:

```python
len(s) == len(t)
```

we don't need a final loop checking that every count is zero.

### Complexity

```text
Time:  O(N)
Space: O(1)
```

Why `O(1)` space?

The problem only allows 26 lowercase English letters, so the HashMap can contain at most 26 keys.

---

# 8. Step-by-Step Trace

Consider:

```text
s = "aacc"
t = "ccac"
```

Lengths:

```text
4 == 4 ✓
```

Build frequency from `s`:

```text
a → 2
c → 2
```

Now process `t`:

| `char` | Count Before | Action        | Count After |
| ------ | -----------: | ------------- | ----------: |
| `c`    |            2 | decrement     |           1 |
| `c`    |            1 | decrement     |           0 |
| `a`    |            2 | decrement     |           1 |
| `c`    |            0 | unavailable ❌ |           — |

Immediately:

```text
return False
```

Why?

```text
s = a a c c
    2a + 2c

t = c c a c
    1a + 3c
```

Same length does **not** guarantee same frequencies.

---

# 9. Related Problems

| Problem                                     | Connection                                                              |
| ------------------------------------------- | ----------------------------------------------------------------------- |
| **217. Contains Duplicate**                 | Simplest hashing problem: existence rather than frequency.              |
| **383. Ransom Note**                        | Frequency availability: `available >= required`.                        |
| **387. First Unique Character in a String** | Count frequencies, then find a character with count `1`.                |
| **49. Group Anagrams**                      | Use character frequencies as a signature to group many anagrams.        |
| **438. Find All Anagrams in a String**      | Frequency matching + sliding window; harder extension of Valid Anagram. |

## Quick Revision

```text
VALID ANAGRAM
      ↓
Order doesn't matter
      ↓
Frequency matters
      ↓
len(s) != len(t)?
      ↓ YES
    False

      NO
      ↓
Count chars in s
      ↓
Consume using t
      ↓
Required count unavailable?
      ↓ YES
    False

      NO
      ↓
     True
```

**Remember:**
**Ransom Note = enough frequency**
**Valid Anagram = exact frequency**
