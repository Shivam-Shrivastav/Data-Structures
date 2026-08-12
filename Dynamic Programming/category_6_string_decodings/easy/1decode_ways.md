## 91. Decode Ways
**Category:** **STRING DECODING / PARTITIONING**

**Problem:** A message containing letters A-Z is encoded as:
- 'A' = 1, 'B' = 2, ..., 'Z' = 26

Given a string `s` containing digits, return the **number of ways** to decode it.

**Example:**
```
Input: s = "12"
Output: 2
Explanation: "12" → "AB" (1,2) or "L" (12)
```

```
Input: s = "226"
Output: 3
Explanation: "226" → "BZ" (2,26), "VF" (22,6), or "BBF" (2,2,6)
```

```
Input: s = "06"
Output: 0
Explanation: "06" cannot be decoded as "6" (leading zero)
```

---

### **Relation to Other Problems**
**Similar to:** **Climbing Stairs** but with constraints
**How it's different:**
1. **Climbing Stairs:** Always can take 1 or 2 steps
2. **Decode Ways:** Can take 1 digit (must be 1-9) or 2 digits (must be 10-26)
3. **Constraints:** Leading zeros invalid, 2-digit numbers must be 10-26

**Key Insight:** 
- This is essentially **constrained Fibonacci**
- `dp[i]` = ways to decode first i characters
- At position i, we can:
  - Take 1 digit: valid if s[i-1] is 1-9
  - Take 2 digits: valid if s[i-2:i] is 10-26

---

### DP Intuition
- **State:** `dp[i]` = number of ways to decode first i characters (s[0..i-1])
- **Transition:**
  ```
  dp[i] = 0
  if s[i-1] is valid 1-digit (1-9):
      dp[i] += dp[i-1]
  if s[i-2:i] is valid 2-digit (10-26):
      dp[i] += dp[i-2]
  ```
- **Base:** 
  - `dp[0] = 1` (empty string: one way)
  - `dp[1] = 1` if s[0] != '0' else 0
- **Answer:** `dp[n]`

---

### 1. Recursive Solution
```python
def numDecodings(s):
    n = len(s)
    
    def dfs(i):
        # i is current index to decode from
        if i == n:
            return 1
        if s[i] == '0':
            return 0
        
        # Take 1 digit
        ways = dfs(i + 1)
        
        # Take 2 digits if possible
        if i + 1 < n and (s[i] == '1' or (s[i] == '2' and s[i+1] <= '6')):
            ways += dfs(i + 2)
        
        return ways
    
    return dfs(0)
```
**TC:** O(2ⁿ) | **SC:** O(n) recursion stack

---

### 2. Memoization (Top-Down DP)
```python
def numDecodings(s):
    n = len(s)
    memo = [-1] * (n + 1)
    
    def dfs(i):
        if i == n:
            return 1
        if s[i] == '0':
            return 0
        if memo[i] != -1:
            return memo[i]
        
        ways = dfs(i + 1)
        
        if i + 1 < n and (s[i] == '1' or (s[i] == '2' and s[i+1] <= '6')):
            ways += dfs(i + 2)
        
        memo[i] = ways
        return ways
    
    return dfs(0)
```
**TC:** O(n) | **SC:** O(n)

---

### 3. Tabulation (Bottom-Up DP)
```python
def numDecodings(s):
    n = len(s)
    if n == 0 or s[0] == '0':
        return 0
    
    dp = [0] * (n + 1)
    dp[0] = 1  # empty string
    dp[1] = 1  # first character (already checked not '0')
    
    for i in range(2, n + 1):
        # One digit (current character)
        if s[i-1] != '0':
            dp[i] += dp[i-1]
        
        # Two digits (previous + current)
        two_digit = int(s[i-2:i])
        if 10 <= two_digit <= 26:
            dp[i] += dp[i-2]
    
    return dp[n]
```
**TC:** O(n) | **SC:** O(n)

---

### 4. Space Optimized
```python
def numDecodings(s):
    n = len(s)
    if n == 0 or s[0] == '0':
        return 0
    
    prev2 = 1  # dp[i-2]
    prev1 = 1  # dp[i-1]
    
    for i in range(1, n):
        curr = 0
        
        # One digit
        if s[i] != '0':
            curr += prev1
        
        # Two digits
        two_digit = int(s[i-1:i+1])
        if 10 <= two_digit <= 26:
            curr += prev2
        
        prev2, prev1 = prev1, curr
    
    return prev1
```
**TC:** O(n) | **SC:** O(1)

---

### 5. With Detailed Comments
```python
def numDecodings(s):
    if not s or s[0] == '0':
        return 0
    
    n = len(s)
    dp = [0] * (n + 1)
    dp[0] = 1  # Base case: empty string
    
    for i in range(1, n + 1):
        # Check single digit decode
        if s[i-1] != '0':
            dp[i] += dp[i-1]
        
        # Check two digit decode
        if i > 1:
            two_digit = int(s[i-2:i])
            if 10 <= two_digit <= 26:
                dp[i] += dp[i-2]
    
    return dp[n]
```

---

**Key Formula:**
```
dp[i] = dp[i-1] (if s[i-1] != '0') + dp[i-2] (if 10 ≤ int(s[i-2:i]) ≤ 26)
dp[0] = 1
dp[1] = 1 if s[0] != '0' else 0
```

**Example Walkthrough:**
```
s = "226"

dp[0] = 1 (empty)

i=1 (s[0]='2'): 
  single digit '2' != '0' → dp[1] += dp[0] = 1
  dp[1] = 1

i=2 (s[1]='2'):
  single digit '2' != '0' → dp[2] += dp[1] = 1
  two digits "22" = 22 → 10-26? yes → dp[2] += dp[0] = 1
  dp[2] = 2

i=3 (s[2]='6'):
  single digit '6' != '0' → dp[3] += dp[2] = 2
  two digits "26" = 26 → 10-26? yes → dp[3] += dp[1] = 1
  dp[3] = 3

Answer = dp[3] = 3
```

**Another Example:**
```
s = "06"

dp[0] = 1
i=1: s[0]='0' → single digit invalid, no two digits → dp[1]=0
i=2: s[1]='6' → single digit '6' valid? but i=1 was 0, so dp[2] = dp[1] if valid? Actually:
  single digit: s[1]='6' != '0' → dp[2] += dp[1] = 0
  two digits: "06" = 6 → not 10-26
  dp[2] = 0
Answer = 0
```

**Comparison Table:**

| Aspect | Climbing Stairs | Decode Ways |
|--------|-----------------|-------------|
**Steps** | Always 1 or 2 steps | 1 digit (1-9) or 2 digits (10-26) |
**Constraints** | None | Leading zeros invalid, range check |
**Base Cases** | dp[0]=1, dp[1]=1 | dp[0]=1, dp[1]=1 if s[0]!='0' |
**Transition** | dp[i] = dp[i-1] + dp[i-2] | dp[i] = (if valid1)dp[i-1] + (if valid2)dp[i-2] |
**Pattern** | Fibonacci | Constrained Fibonacci |

**String Decoding/Partitioning Family:**

| Problem | Pattern | Key Difference |
|---------|---------|---------------|
**91. Decode Ways** | Constrained Fibonacci | Digits to letters, range 1-26 |
**639. Decode Ways II** | With wildcard '*' | '*' can be 1-9 or 10-26 depending |
**139. Word Break** | Dictionary lookup | Words from dictionary, not fixed mapping |
**132. Palindrome Partitioning II** | Min cuts | Palindrome checking |

**Edge Cases:**
- Empty string → 0 (or 1? problem usually says 0)
- Single digit '0' → 0
- Single digit 1-9 → 1
- Leading zeros → 0
- "10", "20" → valid (1 way each)
- "27" → only "2","7" (1 way, "27" invalid)

**Common Pitfalls:**
- Forgetting that '0' alone is invalid
- Forgetting that '0' in two-digit only valid as 10 or 20
- Off-by-one in dp indexing

**Why dp[0] = 1:**
- Represents empty string as base case
- When we take two digits, we add dp[i-2] which for i=2 means dp[0]=1
- This correctly counts the two-digit decode as one way