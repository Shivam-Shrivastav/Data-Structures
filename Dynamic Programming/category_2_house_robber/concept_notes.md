## House Robber — DP Pattern

House Robber is one of the **most important 1D DP patterns** because it teaches:

> **At every position, choose between TAKE and SKIP.**

### 1. Core idea

Given:

```text
nums = [2, 7, 9, 3, 1]
```

You cannot rob two adjacent houses.

At house `i`, you have two choices:

```text
TAKE nums[i]  → then you cannot take nums[i-1]
SKIP nums[i]  → keep whatever answer you had before
```

So:

```text
dp[i] = max(
    dp[i-1],              # SKIP current
    dp[i-2] + nums[i]     # TAKE current
)
```

That's the entire pattern.

---

## 2. Think in TAKE / SKIP

For:

```text
[2, 7, 9, 3, 1]
```

At `9`:

```text
SKIP 9 → best from [2,7] = 7

TAKE 9 → best from [2] + 9
        = 2 + 9
        = 11
```

Therefore:

```text
dp[9] = max(7, 11)
      = 11
```

This is exactly the same **Take / Skip thinking** you've been using for subset/backtracking problems, except here we **store the best result instead of exploring both branches**.

---

## 3. DP definition

The cleanest definition:

```text
dp[i] = maximum money we can rob from houses 0...i
```

Then:

```text
dp[i] = max(
    dp[i-1],        # don't rob i
    dp[i-2] + nums[i]   # rob i
)
```

### Example

```text
nums = [2, 7, 9, 3, 1]

dp:

i       0   1   2   3   4
nums    2   7   9   3   1
dp      2   7   11  11  12
```

Answer:

```text
12
```

Rob:

```text
2 + 9 + 1 = 12
```

---

# 4. Why `i-2`?

This is the key thing to understand.

If you **TAKE `nums[i]`**:

```text
        i-2    i-1    i
         ↓      ↓      ↓
       [  ? ] [ X ] [9]
```

You cannot take `i-1`.

So the best previous answer available is:

```text
dp[i-2]
```

Therefore:

```text
TAKE = dp[i-2] + nums[i]
```

If you **SKIP `i`**:

```text
SKIP = dp[i-1]
```

Hence:

```text
dp[i] = max(dp[i-1], dp[i-2] + nums[i])
```

---

# 5. Space optimization

Notice that to calculate `dp[i]`, we only need:

```text
dp[i-1]
dp[i-2]
```

So we don't actually need the entire array.

```python
def rob(nums):
    prev2 = 0
    prev1 = 0

    for money in nums:
        curr = max(
            prev1,          # SKIP
            prev2 + money   # TAKE
        )

        prev2 = prev1
        prev1 = curr

    return prev1
```

Think:

```text
prev2 = dp[i-2]
prev1 = dp[i-1]

curr = max(SKIP, TAKE)
```

---

# 6. Similar Problems — Same Pattern

When you see these types of problems, immediately think:

> **"Can I TAKE this item or SKIP it, and does taking it prevent me from taking something nearby?"**

### A. House Robber

```text
Cannot take adjacent houses
```

```text
dp[i] = max(dp[i-1], dp[i-2] + nums[i])
```

---

### B. House Robber II

Same problem, but houses are in a **circle**.

First and last houses are adjacent.

So split into two cases:

```text
Case 1: Don't take first
        rob(nums[1:])

Case 2: Don't take last
        rob(nums[:-1])
```

Then:

```text
answer = max(case1, case2)
```

The underlying DP is **exactly House Robber**.

---

### C. Delete and Earn

Example:

```text
[3, 4, 2]
```

If you take `3`, you cannot take `2` or `4`.

You can first convert it into:

```text
value → total points

2 → 2
3 → 3
4 → 4
```

Now it becomes essentially:

```text
House Robber on [2, 3, 4]
```

Because taking `3` prevents taking neighboring values `2` and `4`.

**Pattern: transform → House Robber DP.**

---

### D. Maximum Sum of Non-Adjacent Elements

Literally the same problem without the story.

```text
nums = [4, 1, 2, 7, 5]
```

Choose elements such that no two chosen elements are adjacent.

```text
dp[i] = max(dp[i-1], dp[i-2] + nums[i])
```

This is basically the **purest form of House Robber**.

---

# 7. A broader pattern

You can group these problems like this:

```text
                TAKE / SKIP
                    |
          ┌─────────┴─────────┐
          |                   |
    Taking i affects      Taking i doesn't
    i-1 / nearby           affect previous
          |
     House Robber
          |
    dp[i-2] + value
```

The most important recognition signal is:

### 🚨 Keywords

If the problem says:

* choose elements
* maximize/minimize
* cannot choose adjacent
* cannot choose consecutive
* picking one prevents another
* skip one after taking
* non-adjacent
* houses/items/jobs in sequence

Immediately consider:

```python
TAKE = dp[i-2] + value
SKIP = dp[i-1]

dp[i] = max(TAKE, SKIP)
```

---

## 8. The mental template

Don't memorize the House Robber code.

Memorize this:

```text
At index i:

        ┌── SKIP → dp[i-1]
dp[i] ──┤
        └── TAKE → dp[i-2] + value

dp[i] = max(SKIP, TAKE)
```

That's the **House Robber / non-adjacent DP pattern**.

And the progression I'd recommend for this pattern is:

```text
1. Maximum Sum of Non-Adjacent Elements
             ↓
2. House Robber
             ↓
3. House Robber II
             ↓
4. Delete and Earn
             ↓
5. More general "Take / Skip" DP
```

The big jump after House Robber is learning to recognize when the **state changes from `i-2` to something else**.
