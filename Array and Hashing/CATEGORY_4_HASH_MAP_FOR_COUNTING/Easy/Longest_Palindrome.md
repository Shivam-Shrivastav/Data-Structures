# Longest Palindrome — LeetCode 409

**Pattern:** Frequency Counting / HashMap
**Core idea:** Use characters in **pairs**, and allow **one odd-frequency character** in the center.

> Important: This is **Longest Palindrome (409)**, not **Longest Palindromic Substring (5)**.

---

## 1. Problem Statement

Given a string `s` containing lowercase and uppercase English letters, return the **length of the longest palindrome that can be built using those characters**.

Characters may be rearranged.

Uppercase and lowercase are different:

```text
'a' != 'A'
```

### Example

```text
s = "abccccdd"

Counts:
a → 1
b → 1
c → 4
d → 2

Palindrome possible:

dccaccd
```

Length = **7**.

### Constraints

```text
1 <= s.length <= 2000
s contains lowercase and uppercase English letters.
```

The key detail is **"can be built"**: we do not need to find a palindrome already present as a substring. We can rearrange characters.

---

## 2. Diagram

A palindrome is symmetric around its center:

```text
      left       center       right

       d c c        a          c c d
       └─┬─┘                   └─┬─┘
         │                       │
         └──── matching pairs ───┘
```

Every character outside the center must occur in a pair.

For:

```text
a → 1
b → 1
c → 4
d → 2
```

We can use:

```text
c:  cc | cc      → 4
d:   d | d       → 2

Center:
a OR b           → 1

Total = 4 + 2 + 1 = 7
```

Only **one** odd leftover can occupy the center.

---

## 3. Example I/O

### Example 1 — Typical

```text
Input:
s = "abccccdd"

Output:
7
```

Because we use:

```text
c → 4
d → 2
a → 1 center

Total = 7
```

### Example 2 — Edge Case

```text
Input:
s = "abcdef"

Output:
1
```

Every character occurs once. Since there are no pairs, only one character can be placed at the center.

---

## 4. Intuition & Pattern Recognition

### What should trigger frequency counting?

The problem says:

> Build the longest palindrome **using the given characters**.

Since characters can be rearranged, their **positions don't matter**.

That is the biggest signal:

```text
Positions irrelevant
        ↓
Only number of each character matters
        ↓
Frequency counting
```

Now remember the palindrome property:

```text
a b c X c b a
↑ ↑ ↑   ↑ ↑ ↑
matching pairs
```

Everything except the center needs a matching character.

Therefore, for frequency `f`:

```text
f even → use all f

f odd  → use f - 1
         because f - 1 is even
```

Then, if **any odd count exists**, add one character back as the center.

### Interview thought

```text
I can rearrange the characters.

A palindrome needs pairs on both sides,
so every frequency contributes its largest even part.

If anything remains after taking pairs,
one leftover can become the center.
```

That's the entire problem.

---

## 5. Simpler Version

The easiest way to reach this problem is through basic frequency-counting problems.

### Step 1 — Ransom Note

**LeetCode 383 — Ransom Note**

Learn:

```text
character → frequency
```

Question:

> Do I have enough occurrences of every required character?

That introduces counting characters.

### Step 2 — Valid Anagram

**LeetCode 242 — Valid Anagram**

Learn to compare complete frequency distributions:

```text
s = "anagram"
t = "nagaram"

same counts → anagram
```

Now you're comfortable treating a string as **counts instead of positions**.

### Step 3 — Palindrome Permutation idea

Ask the simpler question:

> Can these characters be rearranged into **a palindrome**?

Rule:

```text
Even length palindrome:
all counts even

Odd length palindrome:
at most ONE odd count
```

Example:

```text
"aabbc"

a → 2
b → 2
c → 1

Possible:
abcba
```

### Step 4 — Longest Palindrome

Now instead of asking:

> Can I use **all** characters?

ask:

> What's the **maximum number** I can use?

For every frequency:

```text
take maximum even amount
```

and then:

```text
+1 if any leftover exists
```

So the progression is:

```text
Ransom Note
    ↓
Understand character frequencies

Valid Anagram
    ↓
Positions don't matter; counts matter

Palindrome Permutation
    ↓
Palindrome = pairs + at most one odd

Longest Palindrome
    ↓
Take all possible pairs + one center
```

---

## 6. Brute Force

A literal brute-force approach would try subsets/permutations of characters and check whether they form palindromes.

Conceptually:

```python
# Conceptual brute force:
# Generate possible arrangements/subsets,
# check each one for palindrome,
# keep the maximum length.
```

This becomes exponential/factorial and is completely impractical.

```text
Time: exponential or worse
Space: depends on generated permutations
```

The important realization is that permutations are unnecessary because **only frequencies determine whether a palindrome can be constructed**.

---

## 7. Optimal Solution

### Frequency-counting approach

```python
from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = Counter(s)

        length = 0
        has_odd = False

        for count in freq.values():
            # Largest even number <= count.
            length += (count // 2) * 2

            # Remember whether a leftover exists for the center.
            if count % 2 == 1:
                has_odd = True

        # At most one leftover character can be the center.
        if has_odd:
            length += 1

        return length
```

### The key formula

```python
(count // 2) * 2
```

means:

> Give me the largest even number ≤ `count`.

Examples:

```text
count = 6 → 6
count = 5 → 4
count = 4 → 4
count = 3 → 2
count = 1 → 0
```

Equivalent:

```python
count - count % 2
```

### Complexity

```text
Time:  O(N)
Space: O(1)
```

Technically the frequency map is `O(k)`, but since there are only 52 possible English letters, `k <= 52`, so auxiliary space is constant.

---

## 8. Step-by-Step Trace

Take:

```text
s = "abccccdd"
```

Frequency map:

```text
a → 1
b → 1
c → 4
d → 2
```

| Character | Count | Pairs used | Length | has_odd |
| --------- | ----: | ---------: | -----: | ------- |
| `a`       |     1 |          0 |      0 | True    |
| `b`       |     1 |          0 |      0 | True    |
| `c`       |     4 |          4 |      4 | True    |
| `d`       |     2 |          2 |      6 | True    |

After processing everything:

```text
length = 6
has_odd = True
```

We have one center position available:

```text
length += 1

6 + 1 = 7
```

Result:

```text
7
```

A possible construction:

```text
d c c a c c d
      ↑
    center
```

---

## 9. Related Problems

| Problem                                  | Connection                                                                         |
| ---------------------------------------- | ---------------------------------------------------------------------------------- |
| **242. Valid Anagram**                   | Basic frequency counting; learn to ignore positions and compare counts.            |
| **383. Ransom Note**                     | Uses frequencies to determine whether available characters are sufficient.         |
| **266. Palindrome Permutation**          | Direct prerequisite: determine whether frequencies can form a palindrome.          |
| **451. Sort Characters By Frequency**    | Uses the same character-frequency representation but reconstructs based on counts. |
| **1400. Construct K Palindrome Strings** | Extends the odd-frequency idea to constructing multiple palindromes.               |

---

## Quick Revision

```text
LONGEST PALINDROME
        ↓
Characters can be rearranged
        ↓
Frequency Counting
        ↓
Palindrome = pairs + optional center
        ↓
For each frequency:
    use largest even part

If any odd frequency exists:
    +1 center
```

### Formula to remember

```python
ans += (freq // 2) * 2

if any_odd:
    ans += 1
```

Or mentally:

> **Use every pair you can. If anything is left over, put exactly one character in the center.**

This contrasts with sliding-window problems such as Longest Substring Without Repeating Characters, where positions and contiguous windows matter; the uploaded revision material illustrates that distinction. 
