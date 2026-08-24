# Climbing Path — Dynamic Programming

### 1. Pattern in One Minute

**Core idea:**
You are moving through a sequence of positions, usually climbing stairs, where the number of ways/reward at position `i` depends on previous positions.

The classic recurrence:

> **`dp[i] = dp[i-1] + dp[i-2]`**

Why? To reach step `i`, your last move is either:

* from `i-1` → 1 step
* from `i-2` → 2 steps

**Immediately think of this when:**

> “How many ways can I reach the end?” + “I can move 1 or 2 steps.”

---

### 2. Recognition Signals

Strong clues:

* Climbing stairs / reaching destination
* Can take **1 or 2 steps**
* Count number of ways
* Minimum/maximum cost to reach the end
* Current position depends on previous positions
* Linear path with limited previous choices

Common disguises:

* **Min Cost Climbing Stairs**
* Frog Jump / minimum energy
* Number of ways to reach a position
* Ways to reach `n` with jumps of `1, 2, ...`

**Don't immediately use this pattern when:**

* Choices depend on arbitrary previous states → may need 2D/other DP
* You need to remember which elements were selected → subset/knapsack-style DP
* There are variable jumps with complex constraints → potentially different DP state

---

### 3. Mental Model

Think:

1. **`dp[i]` = answer for reaching position `i`.**
2. Ask: **"Where could I have come from?"**
3. If jumps are `1` or `2`, previous positions are `i-1` and `i-2`.
4. Therefore:
   `dp[i] = dp[i-1] + dp[i-2]`
5. The first few values are the **base cases**.
6. Once you recognize the recurrence, implementation is trivial.
7. Since only the previous two states matter, you don't actually need the whole array.
8. This is basically the **Fibonacci pattern in disguise**.

**Mnemonic:**

> **"Current = sum of ways from where I could have come."**

---

### 4. Boilerplate Template

#### Classic: Climbing Stairs

```python
def climbStairs(n):
    if n <= 2:
        return n

    prev2 = 1  # dp[i-2]
    prev1 = 2  # dp[i-1]

    for i in range(3, n + 1):
        curr = prev1 + prev2
        prev2 = prev1
        prev1 = curr

    return prev1
```

### DP-array version

```python
dp = [0] * (n + 1)

dp[1] = 1
dp[2] = 2

for i in range(3, n + 1):
    dp[i] = dp[i-1] + dp[i-2]

return dp[n]
```

**Recognition → recurrence → optimize space.**

---

### 5. Variations

| Variation           | Change                                       |
| ------------------- | -------------------------------------------- |
| 1 or 2 steps        | `dp[i] = dp[i-1] + dp[i-2]`                  |
| 1, 2, 3 steps       | `dp[i] = dp[i-1] + dp[i-2] + dp[i-3]`        |
| Minimum cost        | `dp[i] = cost[i] + min(dp[i-1], dp[i-2])`    |
| Maximum reward      | Replace `min` with `max`                     |
| Forbidden steps     | Don't transition from/to invalid positions   |
| Variable jump sizes | Loop over allowed jump sizes                 |
| Circular path       | Usually split into cases / modify boundaries |

---

### 6. Common Pitfalls

**1. Wrong base cases**

For `Climbing Stairs`:

```text
n = 1 → 1
n = 2 → 2
```

Don't accidentally use Fibonacci's `0, 1` initialization.

**2. Confusing "ways" with "cost"**

Ways → **sum**

```python
dp[i] = dp[i-1] + dp[i-2]
```

Minimum cost → **min**

```python
dp[i] = cost[i] + min(dp[i-1], dp[i-2])
```

**3. Off-by-one**

Always clarify:

> Is `n` the number of stairs, or the destination index?

**4. Storing unnecessary DP**

If only `i-1` and `i-2` are needed, use two variables.

---

### 7. Interview Checklist

✓ Linear path?

✓ Each position can be reached from a small number of previous positions?

✓ Choices are something like **1 or 2 jumps**?

✓ Asking for number of ways?

→ **DP**

✓ Asking minimum/maximum cost?

→ **Same DP structure, change `+` into `min/max` appropriately.**

✓ Only previous 2 states matter?

→ **O(1) space optimization.**

---

### 8. Must-Do Problems

**Easy**

1. 🥇 **TOP 3 — LeetCode 70: Climbing Stairs**
2. 🥇 **TOP 3 — LeetCode 746: Min Cost Climbing Stairs**

**Medium**

3. 🥇 **TOP 3 — LeetCode 198: House Robber** — important extension of the same "previous states" thinking
4. LeetCode 213: House Robber II
5. LeetCode 91: Decode Ways — similar linear DP/state-transition thinking

**For pure Climbing Path revision:**
**70 + 746 are the essential two.**

---

# 9. 30-Second Cheat Sheet

```text
CLIMBING PATH DP

Recognition:
→ Linear path
→ Reach position i
→ Small fixed set of previous positions
→ Count ways / min cost / max reward

Core:
dp[i] = answer for reaching i

1 or 2 jumps:
dp[i] = dp[i-1] + dp[i-2]

Min cost:
dp[i] = cost[i] + min(dp[i-1], dp[i-2])

Space:
Only i-1 and i-2 needed → O(1)

Complexity:
Time  = O(n)
Space = O(1)

Mnemonic:
"Where could I have come from?"
→ enumerate previous positions
→ combine their answers
```

**The big pattern to remember:**

> **Climbing Path DP = "Look backward at the possible previous positions."**
> Once you identify the previous states, the recurrence almost writes itself.
