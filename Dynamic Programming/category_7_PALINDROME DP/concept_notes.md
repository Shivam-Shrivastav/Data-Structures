# Palindrome — DP

### 1. Pattern in One Minute

**Core idea:** Determine whether substrings are palindromes by reusing answers for smaller substrings.

The key recurrence:

> `s[i:j]` is palindrome **if** `s[i] == s[j]` **and** the inside `s[i+1:j-1]` is palindrome.

So:

```text
dp[i][j] = True
if:
    s[i] == s[j]
    AND
    dp[i+1][j-1] == True
```

**Immediately think of this when:**

* Asked whether a **substring** is a palindrome.
* Need to find **all palindromic substrings**.
* Need **longest palindromic substring**.
* Need **minimum cuts/partitions into palindromes**.

---

## 2. Recognition Signals

### Strong signals

* "Is this substring a palindrome?"
* "Longest palindromic substring"
* "Count palindromic substrings"
* "Partition string into palindromes"
* "Minimum cuts to make every substring palindrome"

### Typical constraints

If `n <= 2000`, an `O(n²)` DP solution is usually intended.

### Common disguise

Instead of saying palindrome:

> "Find the longest substring that reads the same forwards and backwards."

### Don't use this pattern when

You only need **one** palindrome check for a given string.

Use two pointers:

```python
l, r = 0, len(s) - 1
while l < r:
    if s[l] != s[r]:
        return False
    l += 1
    r -= 1
```

---

# 3. Mental Model

Think of every substring as a box:

```text
s[i ........ j]
  ↑          ↑
same?      same?

If same:
    check the inside

s[i+1 .... j-1]
```

The important recurrence:

```text
Palindrome(i, j)
    ↓
s[i] == s[j]
    AND
Palindrome(i+1, j-1)
```

### Base cases

```text
length 1 → always palindrome

length 2 → palindrome if s[i] == s[j]
```

Example:

```text
"racecar"

r a c e c a r
↑           ↑
same

 a c e c a
 ↑       ↑
 same

  c e c
  ↑   ↑
  same

   e
```

You keep shrinking from the outside inward.

### DP direction

Because:

```python
dp[i][j] depends on dp[i+1][j-1]
```

you must calculate **smaller substrings first**.

That's why the common implementation goes by increasing substring length.

---

# 4. Boilerplate Template

### Longest Palindromic Substring

```python
def longestPalindrome(s):
    n = len(s)

    dp = [[False] * n for _ in range(n)]

    best_start = 0
    best_len = 1

    for length in range(1, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1

            # Same ends + inside is palindrome
            if s[i] == s[j] and (
                length <= 2 or dp[i + 1][j - 1]
            ):
                dp[i][j] = True

                if length > best_len:
                    best_start = i
                    best_len = length

    return s[best_start:best_start + best_len]
```

### Complexity

```text
Time:  O(n²)
Space: O(n²)
```

---

# 5. Variations

### 1. Valid Palindrome

No DP needed.

```text
Two pointers
O(n) time / O(1) space
```

---

### 2. Longest Palindromic Substring

Use:

```text
Palindrome DP
```

OR **expand around center**:

```text
"abcba"
   ↑
 center
```

Expand:

```text
c
bcb
abcba
```

Center expansion is usually preferable:

```text
O(n²) time
O(1) space
```

---

### 3. Count Palindromic Substrings

Same DP.

Whenever:

```python
dp[i][j] = True
```

do:

```python
count += 1
```

---

### 4. Palindrome Partitioning

First build:

```text
palindrome[i][j]
```

Then use **backtracking** to generate partitions.

Example:

```text
"aab"

["a", "a", "b"]
["aa", "b"]
```

This is really:

```text
Palindrome DP + Backtracking
```

---

### 5. Palindrome Partitioning II

Minimum number of cuts.

Combine:

```text
Palindrome DP
+
1D DP for minimum cuts
```

Think:

```text
palindrome[i][j]
    ↓
can I make s[i:j+1] the final piece?
```

---

# 6. Common Pitfalls

### ❌ Forgetting length 2

For:

```text
"aa"
```

there is no `dp[i+1][j-1]` meaningful inner substring.

So:

```python
length <= 2
```

handles it.

---

### ❌ Wrong DP order

This is dangerous:

```python
for i in range(n):
    for j in range(i, n):
```

You need to make sure `dp[i+1][j-1]` has already been computed.

Safest mental model:

> **Process by substring length.**

---

### ❌ Confusing substring and subsequence

Palindrome **substring**:

```text
contiguous
```

Palindrome **subsequence**:

```text
can skip characters
```

They are different DP problems.

---

### ❌ Using DP when center expansion is simpler

For just:

> "Longest Palindromic Substring"

center expansion is often cleaner than `O(n²)` memory DP.

---

# 7. Interview Checklist

✓ Asked about a **contiguous palindrome**?
→ Think substring.

✓ Need palindrome status for **many substrings**?
→ Palindrome DP.

✓ `n ≈ 2000`?
→ `O(n²)` DP is appropriate.

✓ Need longest palindrome only?
→ Consider **expand around center**.

✓ Need all palindrome partitions?
→ **Palindrome DP + Backtracking**.

✓ Need minimum cuts?
→ **Palindrome DP + 1D DP**.

✓ Need only check one string?
→ **Two pointers**, not DP.

---

# 8. Must-Do Problems

### Easy

* **Valid Palindrome** — LC 125
* **Valid Palindrome II** — LC 680

### Medium

* ⭐ **Longest Palindromic Substring** — LC 5
* ⭐ **Palindromic Substrings** — LC 647
* ⭐ **Palindrome Partitioning** — LC 131
* **Palindrome Partitioning II** — LC 132

### Hard

* **Palindrome Removal** — LC 1246 — useful but lower ROI for normal interviews

### Top 3 for revision

1. ⭐ **LC 5 — Longest Palindromic Substring**
2. ⭐ **LC 647 — Palindromic Substrings**
3. ⭐ **LC 131 — Palindrome Partitioning**

These three cover most of the pattern.

---

# 9. 30-Second Cheat Sheet

```text
PALINDROME DP
─────────────────────────────────

Recognition:
"substring palindrome"
"longest palindrome"
"count palindromes"
"partition into palindromes"

Core:
dp[i][j] =
    s[i] == s[j]
    AND
    dp[i+1][j-1]

Base:
length 1 → True
length 2 → s[i] == s[j]

Order:
increasing substring length

Complexity:
O(n²) time
O(n²) space

Variations:
Longest substring → DP / center expansion
Count → count dp[i][j] == True
Partition → palindrome DP + backtracking
Min cuts → palindrome DP + 1D DP

Mnemonic:
"Same ends + Palindromic inside"
```

**The one thing to remember:**

> **Palindrome DP = check the two ends, then trust the inside.**
