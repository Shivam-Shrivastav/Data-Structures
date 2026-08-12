## 639. Decode Ways II
**Category:** **STRING DECODING / DP WITH WILDCARDS**

**Problem:** A message containing letters A-Z is encoded as:
- 'A' = 1, 'B' = 2, ..., 'Z' = 26
- '*' represents any digit from 1 to 9 (cannot be 0)

Given a string `s` containing digits and '*', return the **number of ways** to decode it. Return answer modulo 10⁹+7.

**Example:**
```
Input: s = "*"
Output: 9
Explanation: '*' can be 1-9 → 9 ways (A-I)
```

```
Input: s = "1*"
Output: 18
Explanation: 
- '*' as single digit: 1-9 → 9 ways (1A-1I)
- Two digits "1*": 11-19 → 9 ways (K-S)
Total = 18
```

```
Input: s = "2*"
Output: 15
Explanation:
- '*' as single: 1-9 → 9 ways
- Two digits "2*": 21-26 → 6 ways (U-Z)
Total = 15
```

---

### **Relation to Decode Ways I**
**Similar to:** **Decode Ways (91)** but with **wildcard '*'**
**How it's different:**
1. **Decode Ways I:** Digits only, simple checks
2. **Decode Ways II:** '*' can be 1-9, need to count all possibilities
3. **Multipliers:** When '*' appears, multiply by number of possibilities

**Key Insight:** 
- Same DP structure as Decode Ways I
- But when encountering '*', need to multiply by 9 (for single digit) or appropriate range (for two digits)
- Need to handle all combinations of digits and '*'

---

### DP Intuition
- **State:** `dp[i]` = number of ways to decode first i characters (s[0..i-1])
- **Transition:** For position i, consider:
  - **1-digit decode:** s[i-1] as single digit (if valid)
  - **2-digit decode:** s[i-2:i] as two digits (if valid)
- **Base:** `dp[0] = 1` (empty string)
- **Answer:** `dp[n] % MOD`

**Valid 1-digit:**
- `'1'-'9'` → 1 way
- `'*'` → 9 ways (1-9)

**Valid 2-digit:**
Need to check all combinations:

| First | Second | Valid Range | Count |
|-------|--------|-------------|-------|
| '1' | '0'-'9' | 10-19 | 9 if second is '*', else 1 if valid |
| '1' | '*' | 11-19 | 9 |
| '2' | '0'-'6' | 20-26 | 6 if second is '*', else 1 if valid |
| '2' | '*' | 21-26 | 6 |
| '*' | '0'-'9' | 10-19 (if first='1'), 20-26 (if first='2') | Depends |
| '*' | '*' | 11-19 + 21-26 = 15 | 15 |
| '0' | anything | Invalid | 0 |

---

### 1. Recursive Solution
```python
def numDecodings(s):
    MOD = 10**9 + 7
    n = len(s)
    
    def dfs(i):
        if i == n:
            return 1
        if s[i] == '0':
            return 0
        
        # One digit
        if s[i] == '*':
            ways = 9 * dfs(i + 1)
        else:
            ways = dfs(i + 1)
        
        # Two digits
        if i + 1 < n:
            if s[i] == '*':
                if s[i+1] == '*':
                    ways += 15 * dfs(i + 2)
                elif '0' <= s[i+1] <= '6':
                    ways += 2 * dfs(i + 2)  # 1x and 2x
                else:  # '7'-'9'
                    ways += 1 * dfs(i + 2)  # only 1x
            elif s[i] == '1':
                if s[i+1] == '*':
                    ways += 9 * dfs(i + 2)
                else:
                    ways += dfs(i + 2)
            elif s[i] == '2':
                if s[i+1] == '*':
                    ways += 6 * dfs(i + 2)
                elif '0' <= s[i+1] <= '6':
                    ways += dfs(i + 2)
        
        return ways % MOD
    
    return dfs(0)
```
**TC:** O(2ⁿ) | **SC:** O(n) recursion stack

---

### 2. Memoization (Top-Down DP)
```python
def numDecodings(s):
    MOD = 10**9 + 7
    n = len(s)
    memo = [-1] * (n + 1)
    
    def dfs(i):
        if i == n:
            return 1
        if s[i] == '0':
            return 0
        if memo[i] != -1:
            return memo[i]
        
        # One digit
        if s[i] == '*':
            ways = 9 * dfs(i + 1)
        else:
            ways = dfs(i + 1)
        
        # Two digits
        if i + 1 < n:
            if s[i] == '*':
                if s[i+1] == '*':
                    ways += 15 * dfs(i + 2)
                elif '0' <= s[i+1] <= '6':
                    ways += 2 * dfs(i + 2)
                else:  # '7'-'9'
                    ways += 1 * dfs(i + 2)
            elif s[i] == '1':
                if s[i+1] == '*':
                    ways += 9 * dfs(i + 2)
                else:
                    ways += dfs(i + 2)
            elif s[i] == '2':
                if s[i+1] == '*':
                    ways += 6 * dfs(i + 2)
                elif '0' <= s[i+1] <= '6':
                    ways += dfs(i + 2)
        
        memo[i] = ways % MOD
        return memo[i]
    
    return dfs(0)
```
**TC:** O(n) | **SC:** O(n)

---

### 3. Tabulation (Bottom-Up DP)
```python
def numDecodings(s):
    MOD = 10**9 + 7
    n = len(s)
    dp = [0] * (n + 1)
    dp[0] = 1
    
    if s[0] == '0':
        dp[1] = 0
    elif s[0] == '*':
        dp[1] = 9
    else:
        dp[1] = 1
    
    for i in range(2, n + 1):
        # One digit (current character)
        if s[i-1] == '*':
            dp[i] += 9 * dp[i-1]
        elif s[i-1] != '0':
            dp[i] += dp[i-1]
        
        # Two digits (previous + current)
        first = s[i-2]
        second = s[i-1]
        
        if first == '*':
            if second == '*':
                dp[i] += 15 * dp[i-2]
            elif '0' <= second <= '6':
                dp[i] += 2 * dp[i-2]
            else:  # '7'-'9'
                dp[i] += 1 * dp[i-2]
        elif first == '1':
            if second == '*':
                dp[i] += 9 * dp[i-2]
            else:
                dp[i] += dp[i-2]
        elif first == '2':
            if second == '*':
                dp[i] += 6 * dp[i-2]
            elif '0' <= second <= '6':
                dp[i] += dp[i-2]
        
        dp[i] %= MOD
    
    return dp[n]
```
**TC:** O(n) | **SC:** O(n)

---

### 4. Space Optimized
```python
def numDecodings(s):
    MOD = 10**9 + 7
    n = len(s)
    
    # dp[i-2], dp[i-1], dp[i]
    prev2 = 1  # dp[0]
    
    if s[0] == '0':
        prev1 = 0
    elif s[0] == '*':
        prev1 = 9
    else:
        prev1 = 1
    
    for i in range(2, n + 1):
        curr = 0
        
        # One digit
        if s[i-1] == '*':
            curr += 9 * prev1
        elif s[i-1] != '0':
            curr += prev1
        
        # Two digits
        first = s[i-2]
        second = s[i-1]
        
        if first == '*':
            if second == '*':
                curr += 15 * prev2
            elif '0' <= second <= '6':
                curr += 2 * prev2
            else:
                curr += 1 * prev2
        elif first == '1':
            if second == '*':
                curr += 9 * prev2
            else:
                curr += prev2
        elif first == '2':
            if second == '*':
                curr += 6 * prev2
            elif '0' <= second <= '6':
                curr += prev2
        
        curr %= MOD
        prev2, prev1 = prev1, curr
    
    return prev1
```
**TC:** O(n) | **SC:** O(1)

---

**Key Formulas (Two-Digit Cases):**

| Pattern | Count | Reason |
|---------|-------|--------|
| `**` | 15 | 11-19 (9) + 21-26 (6) |
| `*d` where d=0-6 | 2 | 1d and 2d both valid |
| `*d` where d=7-9 | 1 | Only 1d valid |
| `1*` | 9 | 11-19 |
| `2*` | 6 | 21-26 |
| `1d` | 1 | 10-19 if d valid |
| `2d` with d=0-6 | 1 | 20-26 |

**Example Walkthrough:**
```
s = "1*", n=2

dp[0] = 1
dp[1]: s[0]='1' → dp[1] = 1

i=2 (second char):
  One digit: s[1]='*' → 9 * dp[1] = 9 * 1 = 9
  
  Two digits: first='1', second='*' → 9 * dp[0] = 9 * 1 = 9
  
  Total = 9 + 9 = 18

Answer = 18
```

```
s = "2*", n=2

dp[0] = 1
dp[1]: s[0]='2' → dp[1] = 1

i=2:
  One digit: s[1]='*' → 9 * dp[1] = 9
  
  Two digits: first='2', second='*' → 6 * dp[0] = 6
  
  Total = 9 + 6 = 15
```

```
s = "*1", n=2

dp[0] = 1
dp[1]: s[0]='*' → dp[1] = 9

i=2:
  One digit: s[1]='1' → dp[2] += dp[1] = 9
  
  Two digits: first='*', second='1' → '1' is 0-6? Yes, so 2 * dp[0] = 2
  Total = 9 + 2 = 11
```

**Comparison Table:**

| Aspect | Decode Ways I | Decode Ways II |
|--------|---------------|----------------|
**Input** | Digits only | Digits and '*' |
**1-digit cases** | 1 if 1-9 | 9 if '*', else same |
**2-digit cases** | Simple range check | Complex multipliers |
**Time Complexity** | O(n) | O(n) |
**Space** | O(1) | O(1) |
**Modulo** | Not needed | Required (large numbers) |

**Decode Ways Family:**

| Problem | Key Feature | Difficulty |
|---------|------------|------------|
**91. Decode Ways I** | Digits only | Medium |
**639. Decode Ways II** | With '*' wildcard | Hard |

**Edge Cases:**
- Empty string → 1 (by convention)
- Single '*' → 9
- "0" → 0
- "10" → 1
- "1*" → 18
- "**" → 96? Let's check: 
  - First '*' as single: 9 * ways from second char
  - Second '*' has 9 ways as single, so first part = 9*9=81
  - Two digits: "**" = 15 ways
  - Total = 81 + 15 = 96

**Common Pitfalls:**
- Forgetting that '*' cannot be 0
- Double-counting in two-digit cases
- Not handling modulo for large numbers
- Off-by-one in DP indices

**Why Modulo Needed:**
- With n=100, numbers can be enormous
- All counts are modulo 10⁹+7
- Apply modulo at each step, not just at end