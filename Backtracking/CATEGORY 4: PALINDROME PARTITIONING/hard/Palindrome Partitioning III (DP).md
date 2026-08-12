    ## 🔹 Palindrome Partitioning III (DP Pattern)

---

## 1. Problem Statement with Example

Given a string `s` and an integer `k`, partition `s` into **exactly k substrings**, such that:

👉 Each substring can be converted into a palindrome
👉 Minimize the **total number of character changes**

Return the **minimum number of changes required**

---

### Example

```
Input: s = "abc", k = 2
Output: 1
```

👉 Possible split:

```
"a" | "bc"
```

* "a" → already palindrome (0 changes)
* "bc" → change 1 char → "bb" or "cc"

Total = 1

---

### Constraints

* 1 ≤ len(s) ≤ 100
* 1 ≤ k ≤ len(s)

---

## 2. Diagram (Partition + Cost)

```
s = "abc", k = 2

Possible splits:

[a] | [bc]   → cost = 0 + 1 = 1
[ab] | [c]   → cost = 1 + 0 = 1

Answer = 1
```

---

## 3. Example I/O

### Example 1 (Typical)

```
Input: "abc", k = 2
Output: 1
```

---

### Example 2

```
Input: "aabbc", k = 3
Output: 0
```

👉 Split:

```
"aa" | "bb" | "c"
```

---

### Example 3 (Edge Case)

```
Input: "a", k = 1
Output: 0
```

---

## 4. Intuition & Pattern Recognition

### 🚨 Signals

* “Split into k parts”
* “Minimize cost”
* “Substring cost precomputation”

👉 This screams:

> **DP on partitions + precomputed cost**

---

### Core Idea

We need:

### 1. Cost Function

👉 `cost(i, j)` = minimum changes to make `s[i:j]` palindrome

---

### 2. DP Definition

```
dp[i][k] = min cost to split s[i:] into k parts
```

---

### Recurrence

```
dp[i][k] = min over j:
    cost(i, j) + dp[j+1][k-1]
```

---

## 5. Simpler Version

### Step 1: Palindrome Cost

👉 From **Palindrome Partitioning**

* Only checking palindrome (0/1)

Now:
👉 We allow modification → cost-based

---

### Step 2: Partition DP

👉 Similar to:

* **Word Break**
* **Minimum Cuts for Palindrome Partitioning**

---

### Thinking Flow

```
Instead of boolean (valid palindrome)
→ we compute cost

Instead of all partitions
→ we minimize cost
```

---

## 6. Brute Force

### Idea

* Try all ways to split into k parts
* Compute cost each time

### Complexity

* Time: **Exponential**

❌ Not feasible

---

## 7. Optimal Solution (DP + Precomputation)

---

### Step 1: Precompute Cost Matrix

```
cost[i][j] = min changes to make s[i:j] palindrome
```

👉 Two-pointer:

* compare ends
* count mismatches

---

### Step 2: DP

---

### Code

```python
class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        n = len(s)
        
        # Step 1: precompute cost
        cost = [[0]*n for _ in range(n)]
        
        for length in range(2, n+1):
            for i in range(n - length + 1):
                j = i + length - 1
                cost[i][j] = cost[i+1][j-1] + (s[i] != s[j])
        
        # Step 2: dp
        dp = [[float('inf')] * (k+1) for _ in range(n+1)]
        
        # base case
        dp[n][0] = 0
        
        for i in range(n-1, -1, -1):
            for parts in range(1, k+1):
                for j in range(i, n):
                    if n - i < parts:  # not enough chars
                        break
                    
                    dp[i][parts] = min(
                        dp[i][parts],
                        cost[i][j] + dp[j+1][parts-1]
                    )
        
        return dp[0][k]
```

---

### Complexity

* Cost computation: **O(n²)**
* DP transitions: **O(n² * k)**

✅ Efficient for n ≤ 100

---

## 8. Step-by-Step Trace

### Input:

```
s = "abc", k = 2
```

---

### Cost Table

```
cost[0][0] = 0   ("a")
cost[1][1] = 0   ("b")
cost[2][2] = 0   ("c")

cost[0][1] = 1   ("ab")
cost[1][2] = 1   ("bc")
cost[0][2] = 1   ("abc")
```

---

### DP

```
dp[3][0] = 0
```

---

### i = 2

```
dp[2][1] = 0  ("c")
```

---

### i = 1

```
dp[1][1] = 1  ("bc")
dp[1][2] = 0  ("b" | "c")
```

---

### i = 0

```
dp[0][2] = min(
    cost[0][0] + dp[1][1] = 0 + 1 = 1
    cost[0][1] + dp[2][1] = 1 + 0 = 1
)
```

👉 Answer = **1**

---

## 9. Related Problems

1. **Palindrome Partitioning**
   → Generate all partitions (backtracking)

2. **Palindrome Partitioning II**
   → Min cuts (no k constraint)

3. **Word Break**
   → Partition with validity check

4. **Split Array Largest Sum**
   → Partition into k parts (DP)

5. **Allocate Mailboxes**
   → Partition + cost minimization

---

## 🔥 Interview One-Liner

👉 *“I precompute the cost to convert any substring into a palindrome, then use DP to split the string into k parts minimizing total cost.”*

---

If you want, next I can:

* 🔥 Show **top-down memo version (cleaner for interviews)**
* 🔥 Optimize space to **O(nk) → O(nk/2)**
* 🔥 Give a **pattern template for all partition DP problems**
