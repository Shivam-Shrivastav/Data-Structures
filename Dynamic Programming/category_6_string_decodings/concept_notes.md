# String Decoding — DP

### 1. Pattern in One Minute

**Core idea:** Count how many ways a digit string can be decoded into letters.

Classic mapping:

`1 → A, 2 → B, ..., 26 → Z`

For every position, you have at most **two choices**:

* Decode **1 digit**: `s[i]`
* Decode **2 digits**: `s[i:i+2]` if it is between `10` and `26`

So:

> **`dp[i] = ways to decode the first i characters`**

And:

`dp[i] = dp[i-1] + dp[i-2]`

when both 1-digit and 2-digit decoding are valid.

---

### 2. Recognition Signals

Immediately think **Decode Ways DP** when you see:

* String of digits
* Digits map to letters/numbers
* Need to **count number of valid interpretations**
* At each position you can take **1 or 2 characters**
* Valid range is usually `1–26`

Example:

`"226"`

Ways:

```text
2 2 6
22 6
2 26
```

Answer = `3`

**Don't use this pattern** if:

* You need to find the actual decoded strings → backtracking may be more appropriate.
* Mapping allows arbitrary-length chunks → may become a different DP.
* There are no overlapping subproblems / choices.

---

### 3. Mental Model

Think:

```text
At every index:

        take 1 digit
             |
             v
           dp[i-1]

OR

        take 2 digits
             |
             v
           dp[i-2]
```

Important rules:

1. `0` **cannot be decoded alone**.
2. `10` and `20` are valid.
3. `01`, `02`, etc. are invalid.
4. Two-digit number must be `10–26`.
5. If `s[i] != '0'`, one-digit decoding contributes `dp[i-1]`.
6. If `10 <= int(s[i-2:i]) <= 26`, two-digit decoding contributes `dp[i-2]`.
7. This is basically **Fibonacci with validity conditions**.
8. The DP state is based only on the previous **two positions**.
9. Therefore, you can optimize space from `O(n)` to `O(1)`.

---

### 4. Boilerplate Template

```python
def numDecodings(s):
    n = len(s)

    dp = [0] * (n + 1)

    dp[0] = 1  # Empty string: one way
    dp[1] = 0 if s[0] == '0' else 1

    for i in range(2, n + 1):

        # Take 1 digit
        if s[i - 1] != '0':
            dp[i] += dp[i - 1]

        # Take 2 digits
        two = int(s[i - 2:i])

        if 10 <= two <= 26:
            dp[i] += dp[i - 2]

    return dp[n]
```

### Space-optimized version

This is the one I'd remember for interviews:

```python
def numDecodings(s):
    prev2 = 1  # dp[i-2]
    prev1 = 0 if s[0] == '0' else 1  # dp[i-1]

    for i in range(2, len(s) + 1):
        curr = 0

        # One digit
        if s[i - 1] != '0':
            curr += prev1

        # Two digits
        if 10 <= int(s[i - 2:i]) <= 26:
            curr += prev2

        prev2, prev1 = prev1, curr

    return prev1
```

**Mental template:**

> `curr = 0 → check 1 digit → check 2 digits → shift`

---

### 5. Variations

| Variation                             | Change                            |
| ------------------------------------- | --------------------------------- |
| Basic Decode Ways                     | `1–26`                            |
| Decode with `*` wildcard              | Count multiple possibilities      |
| Different alphabet mapping            | Change valid range                |
| Return actual decoding                | Store paths instead of counts     |
| Minimum/maximum cost decoding         | Change `+` into `min/max`         |
| Decode with arbitrary word dictionary | Usually becomes **Word Break DP** |

The important generalization:

> **String partitioning into valid pieces + count ways = DP over index.**

---

### 6. Common Pitfalls

**❌ Treating `0` as a valid character**

```text
0 → invalid
```

But:

```text
10 → valid
20 → valid
```

---

**❌ Accepting `27`**

```text
26 → valid
27 → invalid
```

---

**❌ Forgetting that `06` is invalid**

You cannot interpret:

```text
06 → F
```

because `0` cannot start a two-digit code.

---

**❌ Wrong base case**

The key trick:

```python
dp[0] = 1
```

Why?

Because if a valid two-digit number is taken at the beginning, e.g. `"12"`:

```text
dp[2] += dp[0]
```

There is **one way to decode the empty prefix** before `"12"`.

---

### 7. Interview Checklist

✓ String consists of digits
✓ Need number of valid decodings
✓ Each position has 1-digit / 2-digit choices
✓ Valid single digit = `1–9`
✓ Valid pair = `10–26`
✓ `0` requires special handling

→ **Think: Decode Ways DP**

The instant you see:

> **"How many ways can I partition this string into valid 1/2-character pieces?"**

Think **index DP**.

---

### 8. Must-Do Problems

**Easy**

* **Climbing Stairs** — recognize the basic Fibonacci-style recurrence.
* **Decode Ways** — ⭐ **Top 3**
* **Count Ways to Build Good Strings** — useful generalization.

**Medium**

* **Decode Ways II** — ⭐ **Top 3** if you want the harder variation.
* **Word Break** — ⭐ **Top 3** for the broader "partition string into valid pieces" pattern.
* Restore IP Addresses — connects partitioning with backtracking.

**Hard**

* Decode Ways II is already sufficient; no need to chase many harder problems here.

### Top 3 for revision

1. ⭐ **Decode Ways**
2. ⭐ **Word Break**
3. ⭐ **Decode Ways II**

---

# 9. 30-Second Cheat Sheet

```text
PATTERN:
String partitioning + count valid decodings

RECOGNITION:
Digit string
1-digit or 2-digit choices
1–26 mapping
Count number of ways

CORE IDEA:
At index i:
    take 1 digit → dp[i-1]
    take 2 digits → dp[i-2]

RECURRENCE:
dp[i] = 0

if s[i-1] != '0':
    dp[i] += dp[i-1]

if 10 <= int(s[i-2:i]) <= 26:
    dp[i] += dp[i-2]

BASE:
dp[0] = 1
dp[1] = 0 if s[0] == '0' else 1

COMPLEXITY:
Time  = O(n)
Space = O(n)
Optimized = O(1)

PITFALL:
0 cannot stand alone.
10/20 valid.
01/02 invalid.
27+ invalid as a pair.

MNEMONIC:
"1 digit or 2 digits → previous 1 or previous 2."
```
