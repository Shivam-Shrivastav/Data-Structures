# 205. Isomorphic Strings

**Pattern:** HashMap + One-to-One Mapping
**Difficulty:** Easy

---

## 1. Problem Statement

Given two strings `s` and `t`, determine whether they are **isomorphic**.

Two strings are isomorphic when characters in `s` can be replaced to produce `t`, while preserving these rules:

* Every occurrence of a character must map to the **same** character.
* Two different characters **cannot map to the same** character.
* A character may map to itself.

### Example

```text
s = "egg"
t = "add"

Mapping:

e → a
g → d

egg
↓↓↓
add

Output: true
```

### Constraints

```text
1 <= s.length <= 5 * 10^4
t.length == s.length
```

---

# 2. Diagram

### Valid mapping

```text
s = "paper"
t = "title"

p ─────→ t
a ─────→ i
p ─────→ t
e ─────→ l
r ─────→ e

Every mapping is consistent.

p always → t

Output = true
```

### Invalid mapping

```text
s = "foo"
t = "bar"

f ─────→ b
o ─────→ a
o ─────→ r   ❌

Same 'o' wants to map to
both 'a' and 'r'.

Output = false
```

But there is a **second kind of invalid mapping**:

```text
s = "badc"
t = "baba"

b → b
a → a
d → b   ❌

'b' is already mapped from 'b'.

Two source characters cannot map
to the same target character.
```

That second condition is the main trap.

---

# 3. Example I/O

### Example 1 — Valid

```text
Input:
s = "egg"
t = "add"

Output:
true
```

Because:

```text
e → a
g → d
```

---

### Example 2 — Invalid consistency

```text
Input:
s = "foo"
t = "bar"

Output:
false
```

Initially:

```text
f → b
o → a
```

But later:

```text
o → r
```

`o` cannot map to both `a` and `r`.

---

### Edge Case — Invalid one-to-one mapping

```text
Input:
s = "badc"
t = "baba"

Output:
false
```

Because both `b` and `d` would need to map to `b`.

---

# 4. Intuition & Pattern Recognition

The key phrase is:

> **"Characters can be replaced consistently."**

That means we need to remember relationships:

```text
source character → target character
```

Whenever you need to remember:

```text
key → associated value
```

think **HashMap**.

But one map alone isn't enough.

Suppose:

```text
s = "ab"
t = "cc"
```

Using only:

```text
a → c
b → c
```

Each source character is technically consistent.

But this is **not isomorphic**, because:

```text
a ──→ c
       ↑
b ─────┘
```

Two source characters mapped to the same target.

So we need a **bijection / one-to-one mapping**:

```text
s → t
AND
t → s
```

### Interview thinking

> "I need a one-to-one character mapping. I'll maintain mappings in both directions. For every character pair, an existing mapping must match; otherwise I'll create the mapping."

---

# 5. Simpler Version

## Simpler 1 — Consistent mapping only

Imagine the problem only required:

> Every character in `s` must always map to the same character in `t`.

Then one HashMap is enough.

```text
s = "egg"
t = "add"

map = {}

e → a
g → d
g → d ✓
```

Code concept:

```python
if c1 in mapping and mapping[c1] != c2:
    return False
```

---

## But that misses collisions

Consider:

```text
s = "ab"
t = "cc"
```

One map gives:

```text
a → c
b → c
```

No source mapping changes.

So one-map consistency says:

```text
valid
```

But the problem says:

```text
invalid
```

because the relationship must be one-to-one.

---

## Simpler 2 — Valid Anagram

**242. Valid Anagram** also compares relationships between two strings, but only asks whether their **character counts** match.

```text
anagram:
frequency matters

isomorphic:
position-wise mapping matters
```

For example:

```text
s = "egg"
t = "add"
```

They are isomorphic even though they contain completely different characters.

So frequency maps alone are insufficient.

---

## Current Question

Add reverse mapping:

```text
mapST:
a → c

mapTS:
c → a
```

Now when processing:

```text
b → c
```

check reverse:

```text
c → a

but we're asking:

c → b

Mismatch ❌
```

### Thinking progression

```text
Need consistent replacement
        ↓
source → target HashMap

But target cannot be reused
        ↓
Need one-to-one mapping

        ↓

source → target
target → source

        ↓

Isomorphic Strings
```

---

# 6. Brute Force

A naive approach is to repeatedly search previous positions to determine whether the current characters have appeared before and what they corresponded to.

```python
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        n = len(s)

        for i in range(n):
            for j in range(i):
                # Same source must imply same target
                if s[i] == s[j] and t[i] != t[j]:
                    return False

                # Same target must imply same source
                if t[i] == t[j] and s[i] != s[j]:
                    return False

        return True
```

### Complexity

```text
Time  → O(N²)
Space → O(1)
```

We're repeatedly checking old relationships.

HashMaps let us store those relationships directly.

---

# 7. Optimal Solution — Two HashMaps

```python
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        mapST = {}
        mapTS = {}

        for c1, c2 in zip(s, t):

            # Existing s → t mapping must remain consistent
            if c1 in mapST and mapST[c1] != c2:
                return False

            # Existing t → s mapping must remain consistent
            if c2 in mapTS and mapTS[c2] != c1:
                return False

            # Record both directions
            mapST[c1] = c2
            mapTS[c2] = c1

        return True
```

### Core logic

For every pair:

```text
(c1, c2)
```

we enforce:

```text
c1 → c2
c2 → c1
```

So:

```text
one source → one target
one target → one source
```

That guarantees a **one-to-one mapping**.

### Complexity

```text
Time  → O(N)
Space → O(K)
```

where `K` is the number of distinct characters.

---

# 8. Step-by-Step Trace

Take:

```text
s = "paper"
t = "title"
```

Start:

```text
mapST = {}
mapTS = {}
```

|  i | `c1` | `c2` | `mapST` after step  | `mapTS` after step  |
| -: | :--: | :--: | ------------------- | ------------------- |
|  0 |   p  |   t  | `{p:t}`             | `{t:p}`             |
|  1 |   a  |   i  | `{p:t,a:i}`         | `{t:p,i:a}`         |
|  2 |   p  |   t  | unchanged ✓         | unchanged ✓         |
|  3 |   e  |   l  | `{p:t,a:i,e:l}`     | `{t:p,i:a,l:e}`     |
|  4 |   r  |   e  | `{p:t,a:i,e:l,r:e}` | `{t:p,i:a,l:e,e:r}` |

At index 2:

```text
p → t
```

already exists, and the current pair is again:

```text
p → t
```

so it is valid.

Final:

```text
True
```

### Now see failure: `"foo"` vs `"bar"`

Start:

```text
f → b
o → a
```

Maps:

```text
mapST = {
    f: b,
    o: a
}
```

Next pair:

```text
o → r
```

But:

```text
mapST[o] = a

a != r
```

Therefore:

```text
False
```

---

# 9. Related Problems

| Problem                                         | Connection                                                                                  |
| ----------------------------------------------- | ------------------------------------------------------------------------------------------- |
| **290. Word Pattern**                           | Almost the exact same one-to-one mapping pattern, but maps characters to words.             |
| **242. Valid Anagram**                          | Uses HashMaps for character relationships through frequency rather than positional mapping. |
| **205. Isomorphic Strings**                     | Character ↔ character bijection.                                                            |
| **890. Find and Replace Pattern**               | Apply the isomorphic-string check against every candidate word.                             |
| **1153. String Transforms Into Another String** | More advanced character-mapping problem with additional transformation constraints.         |

# Quick Revision

```text
205. Isomorphic Strings

Pattern:
HashMap + One-to-One Mapping

Need:

s → t
AND
t → s

Why two maps?

One map catches:

o → a
o → r    ❌

Reverse map catches:

a → c
b → c    ❌

Algorithm:

for c1, c2:

    if existing c1 mapping != c2:
        False

    if existing c2 mapping != c1:
        False

    store both directions

return True

Time  → O(N)
Space → O(K)
```

### Interview memory hook

**"Isomorphic" = same structure, different symbols.**

Think:

```text
Character replacement
        ↓
Need consistent mapping
        ↓
Need one-to-one mapping
        ↓
Two HashMaps
```

The most closely related next problem is **290. Word Pattern**: same bijection idea, except the mapping becomes **character ↔ word** instead of **character ↔ character**.
