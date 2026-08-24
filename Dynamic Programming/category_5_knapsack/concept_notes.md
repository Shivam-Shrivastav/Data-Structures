# Knapsack Subpattern — DP

## 1. Pattern in One Minute

**Core idea:**
You have items with a **weight/cost** and usually a **value/profit**, and you must decide **take vs skip** each item under a constraint.

The classic question:

> “Given capacity `W`, what is the maximum value I can get?”

Think **Knapsack immediately** when:

* Each item has a **cost/weight**
* There is a **capacity/budget/limit**
* You must optimize something: max value, min cost, possible/not possible
* Every item creates a **take / don't take** decision

The fundamental recurrence:

```text
dp[i][capacity] =
    max(
        skip item i,
        take item i
    )
```

---

## 2. Recognition Signals

### Strong signals

| Signal                        | Think                           |
| ----------------------------- | ------------------------------- |
| Weight + Value + Capacity     | 0/1 Knapsack                    |
| Choose items within budget    | Knapsack                        |
| Maximize profit under limit   | Knapsack                        |
| Can we reach a target sum?    | Knapsack / Subset Sum           |
| Minimum items to reach amount | Unbounded Knapsack              |
| Each item can be used once    | 0/1 Knapsack                    |
| Items can be reused           | Unbounded Knapsack              |
| Exactly/at most `K` items     | Knapsack with another dimension |

### Common disguises

**Partition Equal Subset Sum**

> Can array be split into two equal-sum subsets?

Convert to:

```text
Can I select elements whose sum = total // 2?
```

→ **0/1 Knapsack / Subset Sum**

**Target Sum**

> Assign `+` or `-` to numbers to reach target.

Can often transform into a subset-sum problem.

### Don't use it when

There isn't really a **take/skip decision under a capacity/target constraint**.

For example:

* "Maximum subarray" → Kadane
* "Choose non-adjacent houses" → House Robber
* "Unlimited choices with local minimum" → often different DP
* Items have ordering/sequence dependency → may be sequence DP instead

---

# 3. Mental Model

Imagine processing items one by one.

For every item:

```text
             item
            /    \
         TAKE    SKIP
```

### 0/1 Knapsack

Each item can be used **at most once**.

Suppose:

```text
weights = [2, 3, 4]
values  = [4, 5, 7]
capacity = 5
```

At item `i` and capacity `c`:

### Skip

Don't use the item:

```python
dp[i-1][c]
```

### Take

Use the item:

```python
value[i] + dp[i-1][c-weight[i]]
```

So:

```python
dp[i][c] = max(
    dp[i-1][c],
    value[i] + dp[i-1][c-weight[i]]
)
```

The key mental phrase:

> **"For every item, can I afford it? If yes → take or skip."**

---

# 4. Boilerplate Template

### 0/1 Knapsack — 2D

```python
def knapsack(weights, values, capacity):
    n = len(weights)

    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        w = weights[i - 1]
        v = values[i - 1]

        for c in range(capacity + 1):

            # Skip
            dp[i][c] = dp[i - 1][c]

            # Take
            if w <= c:
                dp[i][c] = max(
                    dp[i][c],
                    v + dp[i - 1][c - w]
                )

    return dp[n][capacity]
```

### 1D optimized version

This is the **important interview template**:

```python
def knapsack(weights, values, capacity):
    dp = [0] * (capacity + 1)

    for w, v in zip(weights, values):

        # Reverse => item used at most once
        for c in range(capacity, w - 1, -1):
            dp[c] = max(
                dp[c],
                v + dp[c - w]
            )

    return dp[capacity]
```

### 🔥 Critical trick

For **0/1 Knapsack**:

```python
for c in range(capacity, w - 1, -1):
```

**Go backward.**

Why?

Because you don't want the current item to be reused.

---

# 5. Variations

### ① 0/1 Knapsack

Each item once.

```text
capacity → decreasing
```

```python
for c in range(capacity, w - 1, -1):
```

---

### ② Unbounded Knapsack

Each item can be used unlimited times.

```text
capacity → increasing
```

```python
for c in range(w, capacity + 1):
```

The direction is the major difference.

> **Backward = once**
> **Forward = unlimited**

---

### ③ Subset Sum

No values; just ask:

> Can I achieve target sum?

```python
dp = [False] * (target + 1)
dp[0] = True

for x in nums:
    for s in range(target, x - 1, -1):
        dp[s] |= dp[s - x]

return dp[target]
```

Same 0/1 Knapsack skeleton.

---

### ④ Partition Equal Subset Sum

```text
total must be even
target = total // 2
```

Then:

> Can I select elements that sum to `target`?

→ Subset Sum.

---

### ⑤ Minimum Coins

Classic **Coin Change**:

```text
minimum number of coins to reach amount
```

Because coins can generally be reused:

```python
for coin in coins:
    for amount in range(coin, target + 1):
        dp[amount] = min(
            dp[amount],
            1 + dp[amount - coin]
        )
```

That's **unbounded knapsack**.

---

### ⑥ Count Ways

Instead of:

```python
max(...)
```

you use:

```python
dp[target] += dp[target - x]
```

Same structure, different objective.

---

# 6. Common Pitfalls

### ❌ Confusing 0/1 and Unbounded

This is the biggest one.

```text
0/1       → iterate capacity BACKWARD
Unbounded → iterate capacity FORWARD
```

---

### ❌ Wrong previous state

For 0/1:

```python
v + dp[c - w]
```

in the 1D version is safe **only because we're iterating backward**.

---

### ❌ Forgetting impossible states

For boolean:

```python
dp[0] = True
```

For minimum:

```python
dp = [float('inf')] * (amount + 1)
dp[0] = 0
```

For maximum:

```python
dp = [0] * (capacity + 1)
```

---

### ❌ Mixing "exactly" vs "at most"

`dp[c]` can mean:

> best answer with capacity **at most** `c`

But some problems ask:

> use **exactly** `c`

Then initialization and impossible states matter.

---

# 7. Interview Checklist

✓ Do I have **items + a limit/capacity/budget/target**?

✓ Does every item have a **take/skip** decision?

✓ Can each item be used **once**?

→ **0/1 Knapsack**

✓ Can an item be reused?

→ **Unbounded Knapsack**

✓ Is the question simply **"can I make this sum?"**

→ **Subset Sum**

✓ Is it **maximize/minimize/count/possible**?

→ Same basic Knapsack structure; change the DP operation.

✓ Using 1D DP?

→ Ask:

> **Can the current item reuse itself?**

If **NO → backward**

If **YES → forward**

---

# 8. Must-Do Problems

### 🟢 Easy

**Top 3 for revision**

1. ⭐ **Partition Equal Subset Sum** — understand subset-sum transformation
2. ⭐ **Target Sum** — understand transformation into knapsack
3. ⭐ **Coin Change** — understand unbounded version

### 🟡 Medium

* ⭐ **0/1 Knapsack** — fundamental template
* **Partition Equal Subset Sum**
* **Target Sum**
* **Coin Change**
* **Coin Change II**
* **Ones and Zeroes**
* **Last Stone Weight II**

### 🔴 Hard

Usually **not necessary for basic pattern revision**. Once you understand the above variations, harder problems mostly add another state/dimension.

---

# 9. 30-Second Cheat Sheet

```text
KNAPSACK
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Recognition:
items + capacity/target + take/skip

Core:
        TAKE vs SKIP

0/1:
each item ONCE
→ capacity BACKWARD

Unbounded:
item reusable
→ capacity FORWARD

MAX:
dp[c] = max(dp[c], value + dp[c-weight])

MIN:
dp[c] = min(dp[c], 1 + dp[c-weight])

COUNT:
dp[c] += dp[c-weight]

BOOLEAN:
dp[c] |= dp[c-weight]

Complexity:
Time  = O(N × Capacity)
Space = O(Capacity)

Mnemonic:
BACKWARD = ONE TIME
FORWARD  = AGAIN
```

### 🧠 The one thing to remember

> **Knapsack = "I have items, I have a limit, and for every item I decide TAKE or SKIP."**

Then immediately ask:

**Once or unlimited?**
→ **Backward or Forward.**
