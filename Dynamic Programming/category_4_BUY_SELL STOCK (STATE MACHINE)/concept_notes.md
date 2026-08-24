# Buy & Sell Stock — State Machine DP

This is one of the **most important DP sub-patterns** because many stock problems look different, but the solution is basically:

> **Track what state you are in → decide BUY / SELL / SKIP → move to the next state.**

---

## 1. Pattern in One Minute

### Core idea

At any day, your situation can usually be represented by a small **state**:

* `holding = 0` → you **do not own** a stock
* `holding = 1` → you **own** a stock

Then every day:

```text
NOT HOLDING
    ├── skip → NOT HOLDING
    └── buy  → HOLDING

HOLDING
    ├── skip → HOLDING
    └── sell → NOT HOLDING
```

The DP stores:

> **maximum profit possible from each state.**

### When should I immediately think of it?

When you see:

* Stock prices over days
* Buy / sell decisions
* Maximum profit
* Cannot perform certain actions simultaneously
* Cooldown / transaction fee / limited transactions
* "You may buy/sell multiple times"

Think:

> **"What state am I in after today's decision?"**

---

# 2. Recognition Signals

### Strong signals

| Signal                        | Think                       |
| ----------------------------- | --------------------------- |
| Buy and sell stock            | State Machine DP            |
| Maximum profit                | DP optimization             |
| Can buy/sell multiple times   | Holding vs not holding      |
| Cannot sell before buying     | State transition            |
| Cooldown after selling        | Add cooldown state          |
| Transaction fee               | Modify SELL transition      |
| At most `k` transactions      | Add transaction dimension   |
| Must sell before buying again | Holding state captures this |

### Common disguises

The problem might never explicitly say "state machine."

For example:

> "You can buy and sell stocks multiple times, but after selling you must wait one day."

Still:

```text
holding
not_holding
cooldown
```

### Don't use this pattern when...

The problem is simply:

> Buy once and sell once.

Then a simple running minimum is enough:

```python
min_price = min(min_price, price)
profit = max(profit, price - min_price)
```

No need for DP.

---

# 3. Mental Model

Remember this:

### **Every day = choose an action based on your state.**

1. You start with **nothing**.
2. If you don't own stock, you have two choices:

   * Do nothing.
   * Buy.
3. If you own stock, you have two choices:

   * Do nothing.
   * Sell.
4. Every action moves you to another state.
5. Each state stores the **best profit achievable** there.
6. Buying costs money → subtract price.
7. Selling gives money → add price.
8. `skip` keeps the same state.
9. The final answer normally comes from the **not-holding** state.
10. Think **"state → action → next state."**

The fundamental transition is:

```text
cash ──BUY──> hold
cash <──SELL── hold
```

where:

```text
cash = max profit while NOT holding
hold = max profit while HOLDING
```

---

# 4. Boilerplate Template

### Bottom-up — most useful interview template

```python
def maxProfit(prices):
    cash = 0                 # Not holding stock
    hold = float("-inf")     # Holding stock

    for price in prices:

        # Sell today OR keep holding
        new_cash = max(cash, hold + price)

        # Buy today OR keep holding
        new_hold = max(hold, cash - price)

        cash = new_cash
        hold = new_hold

    return cash
```

### The two equations to memorize

```text
cash = max(
    cash,          # skip
    hold + price   # sell
)

hold = max(
    hold,          # skip
    cash - price   # buy
)
```

**Mnemonic:**

> **BUY = minus price**
> **SELL = plus price**

---

## Why `hold = -∞` initially?

You cannot start the problem while magically owning a stock.

So:

```python
hold = -inf
```

means:

> "Holding is initially impossible."

Then on day 1:

```python
hold = max(-inf, 0 - price)
```

which correctly represents buying the stock.

This is the same idea as the `-inf` discussion you were asking about earlier: use an impossible state with an extreme value so it can't accidentally become optimal.

---

# 5. Variations

This is where the **state machine pattern becomes extremely powerful.**

### A. Best Time to Buy and Sell Stock I

Only **one transaction**.

Use:

```text
minimum price so far
maximum profit
```

No full state-machine DP needed.

---

### B. Unlimited Transactions

**LeetCode 122**

Same two states:

```text
cash
hold
```

```python
cash = max(cash, hold + price)
hold = max(hold, cash - price)
```

---

### C. Transaction Fee

**LeetCode 714**

Selling costs a fee:

```python
cash = max(cash, hold + price - fee)
hold = max(hold, cash - price)
```

Only the SELL transition changes.

> **Fee = subtract on SELL.**

---

### D. Cooldown

**LeetCode 309**

After selling, you cannot buy the next day.

Now two states aren't enough.

Think:

```text
hold
sold / cooldown
rest
```

Typical transitions:

```text
hold → hold
hold → sold
sold → rest
rest → hold
rest → rest
```

The important recognition:

> **A restriction creates another state.**

---

### E. At Most K Transactions

**LeetCode 188**

Now state needs:

```text
day
transactions_used
holding
```

Conceptually:

```text
dp[i][k][0] = max profit on day i,
              with k transactions,
              not holding

dp[i][k][1] = max profit on day i,
              with k transactions,
              holding
```

You add a dimension because the problem adds a **resource constraint**.

---

### F. Two Transactions

**LeetCode 123**

Specialized version of the `k` transaction problem.

Think:

```text
buy1 → sell1 → buy2 → sell2
```

You can compress this into four states:

```text
buy1
sell1
buy2
sell2
```

---

# 6. Common Pitfalls

### ❌ 1. Thinking greedily first

Don't immediately think:

> "Buy at the lowest price and sell at the highest."

That only works for specific versions.

Instead ask:

> **What states can I be in?**

---

### ❌ 2. Updating states incorrectly

This can cause today's newly calculated state to accidentally influence another transition.

Safer:

```python
new_cash = max(cash, hold + price)
new_hold = max(hold, cash - price)

cash = new_cash
hold = new_hold
```

---

### ❌ 3. Forgetting that BUY decreases profit

```python
hold = max(hold, cash - price)
```

Not:

```python
cash + price
```

Buying is an expense.

---

### ❌ 4. Returning `hold`

Usually:

```python
return cash
```

because an unfinished stock position isn't realized profit.

---

### ❌ 5. Using DP when a simpler solution exists

Stock I:

```text
one transaction
→ running minimum
```

Don't unnecessarily build a state machine.

---

# 7. Interview Checklist

When you see a stock problem:

### ✓ Ask:

**1. Can I buy/sell multiple times?**

→ State machine likely.

**2. Can I hold at most one stock?**

→ `hold / cash`.

**3. Is there a cooldown?**

→ Add state.

**4. Is there a transaction fee?**

→ Modify transition.

**5. Is there a limit of K transactions?**

→ Add transaction dimension.

**6. Is it only one transaction?**

→ Probably running minimum, not DP.

---

# 8. Must-Do Problems

### Easy

**Top 3 → ⭐**

1. ⭐ **Best Time to Buy and Sell Stock** — LC 121
   Learn the one-transaction baseline.

2. ⭐ **Best Time to Buy and Sell Stock II** — LC 122
   Learn the fundamental state machine.

### Medium

3. ⭐ **Best Time to Buy and Sell Stock with Cooldown** — LC 309
   Learn how a restriction creates another state.

4. **Best Time to Buy and Sell Stock with Transaction Fee** — LC 714
   Learn transition modification.

5. **Best Time to Buy and Sell Stock III** — LC 123
   At most 2 transactions.

6. **Best Time to Buy and Sell Stock IV** — LC 188
   General `k` transactions.

### Hard

None are strictly necessary for the core pattern. **LC 188** is enough to understand the generalized state-machine formulation.

---

# 9. 30-Second Cheat Sheet

```text
STOCK STATE MACHINE DP
────────────────────────────────

Recognition:
Stock + buy/sell + maximize profit
        ↓
Think: STATES

Core states:
cash = NOT holding
hold = HOLDING

Transitions:

cash = max(
    cash,          # skip
    hold + price   # sell
)

hold = max(
    hold,          # skip
    cash - price   # buy
)

Mnemonic:
BUY  → - price
SELL → + price

Initial:
cash = 0
hold = -∞

Answer:
cash

Complexity:
Time  O(n)
Space O(1)

Variations:
1 transaction → running minimum
Unlimited     → cash / hold
Fee            → modify SELL
Cooldown       → add state
K transactions → add K dimension

MASTER IDEA:
State → Action → Next State
```

### The one mental picture to retain

```text
              BUY (-price)
        ┌────────────────────┐
        ↓                    │
   ┌──────────┐         ┌──────────┐
   │   CASH   │         │   HOLD   │
   │ no stock │         │  stock   │
   └──────────┘         └──────────┘
        ↑                    │
        └──── SELL (+price) ─┘
        
At every state:
        └── SKIP → stay in same state
```

**If you remember only one sentence:**

> **Stock DP = "What is my maximum profit if I am currently holding vs not holding?"**
