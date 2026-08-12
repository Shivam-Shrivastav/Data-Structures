# Palindrome Problems — Two Pointers

## 1. Pattern in One Minute

**Core idea:** A palindrome is symmetric around its center. So instead of comparing every possible pair, place two pointers at the ends and move them **toward each other**.

```text
s = "racecar"

     L     R
     ↓     ↓
     r a c e c a r
     →           ←
```

At each step:

```python
if s[left] != s[right]:
    # not a palindrome
left += 1
right -= 1
```

**Why this pattern exists:** Palindrome validity depends on **mirrored positions**. Two pointers naturally compare those positions in one pass.

Immediately think **two pointers** when you see:

> palindrome + compare characters symmetrically + start/end or center expansion

**Mnemonic:** **Palindrome = Mirror → Two Pointers.**

---

## 2. Recognition Signals

Strong signals:

* "Is this string/array a palindrome?"
* "Can it become a palindrome after deleting at most one character?"
* Ignore punctuation, spaces, or capitalization while checking palindrome.
* Find/count palindromic substrings.
* Find the longest palindrome centered somewhere.
* Linked list palindrome.
* Characters need to match **symmetrically**.

There are actually **two major palindrome two-pointer shapes**:

```text
Outside → Inside                 Center → Outside

L                 R                  L R
↓                 ↓                  ↓ ↓
a b c b a                        a b b a
  →             ←                    ← →
```

Use **outside → inside** for validation/deletion problems.

Use **center → outside** for palindromic substring problems.

### When NOT to use it

If the problem asks for something like:

* Longest Palindromic **Subsequence**
* Minimum insertions/deletions to create a palindrome
* Complex palindrome optimization over many subsequences

then think **DP**, not plain two pointers.

---

## 3. Mental Model

For **palindrome validation**:

1. Start `left = 0`, `right = n - 1`.
2. `s[left]` must match `s[right]`.
3. If they match, move both inward.
4. One mismatch means the string isn't a palindrome.
5. Stop when the pointers meet/cross.
6. Odd length → one center character remains; irrelevant.
7. Even length → pointers cross between the middle characters.

```text
"abccba"

a b c c b a
L         R     a == a ✓

  L     R       b == b ✓

    L R         c == c ✓

      crossed   palindrome ✓
```

For **palindromic substrings**, reverse the direction:

1. Every palindrome has a **center**.
2. Pick a center.
3. Put pointers around it.
4. While characters match, expand outward.
5. Every successful expansion gives another palindrome.
6. Odd palindrome has one-character center: `"racecar"`.
7. Even palindrome has gap center: `"abba"`.

This distinction is the key:

> **Validate → ends inward. Find substrings → center outward.**

---

## 4. Boilerplate Templates

### A. Validate Palindrome

```python
def is_palindrome(s: str) -> bool:
    left, right = 0, len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False

        left += 1
        right -= 1

    return True
```

**Time:** `O(n)`
**Space:** `O(1)`

---

### B. Expand Around Center

This is the reusable template for **Longest Palindromic Substring** and **Palindromic Substrings**.

```python
def expand(s: str, left: int, right: int):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        # s[left:right + 1] is a palindrome here
        left -= 1
        right += 1
```

For every index `i`, check both possible centers:

```python
expand(s, i, i)       # odd:  "racecar"
expand(s, i, i + 1)   # even: "abba"
```

**Time:** `O(n²)` worst case
**Extra space:** `O(1)`

---

## 5. Variations

| Variation                     | Change                                             |
| ----------------------------- | -------------------------------------------------- |
| Basic palindrome              | Compare `left` and `right`, move inward            |
| Ignore non-alphanumeric       | Skip invalid characters before comparing           |
| Case insensitive              | Compare `.lower()` values                          |
| Delete at most one char       | On mismatch, try skipping left OR right            |
| Linked-list palindrome        | Find middle → reverse second half → compare halves |
| Longest palindromic substring | Expand from every odd/even center                  |
| Count palindromic substrings  | Increment count on every successful expansion      |

### Important variation: Delete One Character

For `"abca"`:

```text
a b c a
L     R     match

  b c
  L R       mismatch
```

At the **first mismatch**, only two possibilities matter:

```text
skip left:   check "c"
skip right:  check "b"
```

More generally:

```python
is_palindrome(left + 1, right) or is_palindrome(left, right - 1)
```

This is the heart of **Valid Palindrome II**.

---

## 6. Common Pitfalls

**Forgetting even-length centers**

Only doing:

```python
expand(i, i)
```

misses `"abba"`.

Always consider:

```python
(i, i)      # odd
(i, i + 1)  # even
```

**Deleting greedily after mismatch**

If:

```text
s[left] != s[right]
```

don't blindly delete one side. Either side might produce the palindrome.

Try **both possibilities**.

**Building reversed strings unnecessarily**

```python
s == s[::-1]
```

works for basic validation but uses `O(n)` extra space. Two pointers give `O(1)` auxiliary space and generalize much better to interview variants.

**Confusing substring and subsequence**

```text
Substring    → contiguous
Subsequence  → may skip characters
```

Longest Palindromic Substring → center expansion works.

Longest Palindromic Subsequence → usually DP.

---

## 7. Interview Checklist

✓ Is symmetry around the center important?

✓ Am I comparing the beginning against the end?

✓ Do mismatches determine validity?

→ **Outside-in two pointers.**

Or:

✓ Am I finding/counting contiguous palindromes?

✓ Could each index/gap act as the center?

→ **Expand-around-center two pointers.**

Remember:

```text
VALIDATE palindrome
Ends → Center

DISCOVER palindromes
Center → Ends
```

---

## 8. Must-Do Problems

### Easy

**⭐ Top 3 — Valid Palindrome (LC 125)**
Canonical outside-in two pointers, including skipping irrelevant characters.

**⭐ Top 3 — Valid Palindrome II (LC 680)**
The crucial "one mismatch → try skipping either side" variation.

**Palindrome Linked List (LC 234)**
Combines fast/slow pointers + reverse linked list + palindrome comparison.

### Medium

**⭐ Top 3 — Longest Palindromic Substring (LC 5)**
Canonical **expand-around-center** problem.

**Palindromic Substrings (LC 647)**
Same center-expansion pattern, but count instead of maximizing length.

**Palindrome Number (LC 9)**
Useful variation, although mathematical digit manipulation is usually preferable.

### Hard

No hard problem is necessary purely for revising this two-pointer sub-pattern. The Top 3 cover the highest-ROI interview variations.

---

# 9. 30-Second Cheat Sheet

```text
PALINDROME — TWO POINTERS

Recognition:
symmetry / palindrome / mirrored characters

─────────────────────────────────

1. VALIDATION → OUTSIDE IN

L                     R
↓                     ↓
a b c d c b a
  →                 ←

while L < R:
    if s[L] != s[R]:
        return False
    L += 1
    R -= 1

Time:  O(n)
Space: O(1)

─────────────────────────────────

2. SUBSTRINGS → CENTER OUT

Odd:               Even:

    L                 L R
    ↓                 ↓ ↓
a b c b a           a b b a
    ← →               ← →

For every i:
    expand(i, i)       # odd
    expand(i, i + 1)   # even

Worst case: O(n²)
Space:      O(1)

─────────────────────────────────

DELETE ≤ 1 CHARACTER:

At first mismatch:

skip L OR skip R

pal(L + 1, R) or pal(L, R - 1)

─────────────────────────────────

Pitfalls:
• Always check odd + even centers
• Don't greedily choose which char to delete
• Substring ≠ subsequence
• Palindromic subsequence → think DP

Mnemonic:
Palindrome = Mirror → Two Pointers

Top 3:
125 Valid Palindrome
680 Valid Palindrome II
5   Longest Palindromic Substring
```
