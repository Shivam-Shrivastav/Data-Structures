# 383. Ransom Note

**Pattern:** Frequency Counting / HashMap
**Difficulty:** Easy

---

## 1. Problem Statement

Given two strings, `ransomNote` and `magazine`, return `True` if `ransomNote` can be constructed using characters from `magazine`.

Each character in `magazine` can be used **at most once**.

### Example

```text
ransomNote = "aa"
magazine   = "aab"

Output: True
```

The magazine contains two `a`s, so both required `a`s are available.

### Constraints

```text
1 <= ransomNote.length, magazine.length <= 10^5
Both contain only lowercase English letters.
```

The important detail is **frequency**, not just whether a character exists.

---

## 2. Diagram

```text
ransomNote = "aa"
magazine   = "aab"

Magazine frequencies:

a → 2
b → 1

Need first 'a':

a → 2 → 1

Need second 'a':

a → 1 → 0

All required characters found
→ True
```

Think of `magazine` as your **inventory** and `ransomNote` as what you need to consume.

---

## 3. Example I/O

### Example 1 — Typical

```text
Input:
ransomNote = "aa"
magazine   = "aab"

Output:
True
```

Magazine has `a:2`, exactly enough for the two `a`s.

### Example 2 — Edge Case

```text
Input:
ransomNote = "aa"
magazine   = "ab"

Output:
False
```

There is an `a`, but only **one**. We need two.

This distinction is crucial:

```text
character existence ❌
character frequency ✅
```

---

# 4. Intuition & Pattern Recognition

### What should trigger frequency counting?

Look for wording like:

> "Can string A be constructed from characters of string B?"

or:

> "Each character can only be used once."

Immediately think:

```text
How many of each character do I HAVE?
How many of each character do I NEED?
```

That's a **frequency counting** problem.

For example:

```text
ransomNote = "aabc"

Need:
a → 2
b → 1
c → 1
```

So simply checking:

```python
'a' in magazine
```

is insufficient because you need **two copies** of `a`.

### Interview thought process

```text
I need characters from magazine.

Each occurrence can be consumed only once.

So I'll count available characters.

Then consume one count for every character
required by ransomNote.

If a count is unavailable → False.
```

---

# 5. Simpler Version

Start with:

### Simplest: Contains Duplicate

**LeetCode 217 — Contains Duplicate**

You learn to use a set/hash structure to answer:

```text
Have I seen this value before?
```

Then:

### Valid Anagram

**LeetCode 242 — Valid Anagram**

Now instead of existence:

```text
Does character exist?
```

you learn frequency:

```text
How many times does character exist?
```

```text
"anagram"
"nagaram"

Both need identical frequencies.
```

Then comes **Ransom Note**.

Unlike Valid Anagram, frequencies don't need to be equal.

They only need:

```text
available >= required
```

Example:

```text
ransomNote = "aa"
magazine   = "aaabbb"

Need a = 2
Have a = 3

3 >= 2

Valid
```

So the progression is:

```text
Contains Duplicate
        ↓
HashSet / existence

Valid Anagram
        ↓
Frequency counting
        ↓
Need frequencies to be equal

Ransom Note
        ↓
Frequency counting
        ↓
Available frequency >= required frequency
```

This is the key difference:

```text
Valid Anagram:
count(s) == count(t)

Ransom Note:
count(magazine) >= count(ransomNote)
```

---

# 6. Brute Force

For every character needed by `ransomNote`, search for it in `magazine`.

Once found, mark/remove it so it cannot be reused.

Conceptually:

```python
for char in ransomNote:
    find char in magazine

    if not found:
        return False

    remove that occurrence

return True
```

For example:

```text
ransomNote = "aa"
magazine   = "aab"

Need a
"aab"
 ^
consume

Need a
"_ab"
  ^
consume

Success
```

Searching/removing can take `O(M)` for every ransom-note character.

**Time:** `O(N × M)`
**Space:** depends on how the magazine is modified/copied.

---

# 7. Optimal Solution

Count all characters available in `magazine`, then consume them while processing `ransomNote`.

```python
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freq = {}

        # Build inventory from magazine
        for char in magazine:
            freq[char] = freq.get(char, 0) + 1

        # Consume inventory for ransomNote
        for char in ransomNote:
            if freq.get(char, 0) == 0:
                return False  # Character unavailable

            freq[char] -= 1

        return True
```

### Complexity

Let:

```text
N = len(ransomNote)
M = len(magazine)
```

**Time:** `O(N + M)`
**Space:** `O(1)` because only 26 lowercase English letters are possible.

Although we're using a HashMap, its maximum size is 26.

### Tiny optimization

You can immediately reject:

```python
if len(ransomNote) > len(magazine):
    return False
```

because you cannot construct a longer string from fewer available characters.

---

# 8. Step-by-Step Trace

```text
ransomNote = "aab"
magazine   = "baaac"
```

First build magazine frequencies:

```text
b → 1
a → 3
c → 1
```

Now consume:

| Need | Counts Before   | Action      | Counts After    |
| ---- | --------------- | ----------- | --------------- |
| `a`  | `a:3, b:1, c:1` | consume `a` | `a:2, b:1, c:1` |
| `a`  | `a:2, b:1, c:1` | consume `a` | `a:1, b:1, c:1` |
| `b`  | `a:1, b:1, c:1` | consume `b` | `a:1, b:0, c:1` |

Every required character was available.

```text
return True
```

### Failure case

```text
ransomNote = "aaa"
magazine   = "aab"
```

```text
Magazine:

a → 2
b → 1

Need a → a becomes 1
Need a → a becomes 0
Need a → count is 0 ❌

return False
```

---

# 9. Related Problems

| Problem                                     | Connection                                                       |
| ------------------------------------------- | ---------------------------------------------------------------- |
| **217. Contains Duplicate**                 | Basic hash-based existence checking.                             |
| **242. Valid Anagram**                      | Count characters and compare frequencies.                        |
| **387. First Unique Character in a String** | Frequency count, then use counts to identify uniqueness.         |
| **49. Group Anagrams**                      | Character frequencies become a signature for grouping strings.   |
| **438. Find All Anagrams in a String**      | Frequency counting + sliding window; a natural harder extension. |

### Quick Revision

```text
Ransom Note
    ↓
"Can I construct A using B?"
    ↓
Each character consumed once
    ↓
Need FREQUENCIES, not existence
    ↓
Count magazine
    ↓
Consume for ransomNote
    ↓
count == 0 before consuming?
    YES → False
    NO  → decrement
    ↓
True

Time:  O(N + M)
Space: O(1) — 26 lowercase letters
```

This follows the same quick-revision style as your sliding-window revision material. 
