## 1416. Restore The Array
**Category:** **STRING DP / DECODING**

**Problem:** A program intended to print an array of integers accidentally omitted the spaces, concatenating all numbers into a single string `s`. We know that:
- All original integers were in the range `[1, k]`
- No integer had leading zeros
- The order of integers is preserved in `s`

Return the **number of possible original arrays** (mod 10⁹+7).

**Example:**
```
Input: s = "1317", k = 2000
Output: 8
Explanation: Possible arrays:
[1317], [131,7], [13,17], [1,317], 
[13,1,7], [1,31,7], [1,3,17], [1,3,1,7]
```

```
Input: s = "1000", k = 10
Output: 0
Explanation: Numbers must be ≤10, but "1000" is too large, 
and "1","000" invalid due to leading zero.
```

```
Input: s = "2020", k = 30
Output: 1
Explanation: Only [20,20] works. [2020] >30, [2,020] has leading zero.
```

---

### **Relation to Decode Ways**
**Similar to:** **Decode Ways (91)** but numbers can be **multi-digit** up to `k`
**How it's different:**
1. **Decode Ways:** Fixed mapping (1-26), always 1 or 2 digits
2. **Restore Array:** Numbers can be 1 to `len(k)` digits, with upper bound `k`
3. **Constraint:** Must check numeric value ≤ k, not just digit range

**Key Insight:** 
- At position `i`, we try all possible ending positions `j` where `s[i:j+1]` ≤ k
- If valid, add ways from `dp[j+1]` to `dp[i]`
- Must stop when number exceeds k (numbers only get larger as we add digits)
- Need to handle leading zeros (any segment starting with '0' is invalid)

---

### DP Intuition
- **State:** `dp[i]` = number of ways to decode suffix starting at index `i`
- **Transition:**
  ```
  For each j from i to n-1:
      num = int(s[i:j+1])
      if num > k: break  # further digits only increase number
      if s[i] != '0':    # no leading zero
          dp[i] += dp[j+1]
  ```
- **Base:** `dp[n] = 1` (empty suffix)
- **Answer:** `dp[0]`

---

### 1. Recursive Solution
```python
def numberOfArrays(s, k):
    MOD = 10**9 + 7
    n = len(s)
    
    def dfs(i):
        if i == n:
            return 1
        if s[i] == '0':
            return 0
        
        ways = 0
        num = 0
        for j in range(i, n):
            num = num * 10 + int(s[j])
            if num > k:
                break
            ways += dfs(j + 1)
        
        return ways % MOD
    
    return dfs(0)
```
**TC:** O(2ⁿ) worst case | **SC:** O(n) recursion stack

---

### 2. Memoization (Top-Down DP)
```python
def numberOfArrays(s, k):
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
        
        ways = 0
        num = 0
        for j in range(i, n):
            num = num * 10 + int(s[j])
            if num > k:
                break
            ways += dfs(j + 1)
        
        memo[i] = ways % MOD
        return memo[i]
    
    return dfs(0)
```
**TC:** O(n × max_digits) where max_digits = len(str(k)) ≤ 10 | **SC:** O(n)

---

### 3. Tabulation (Bottom-Up DP)
```python
def numberOfArrays(s, k):
    MOD = 10**9 + 7
    n = len(s)
    dp = [0] * (n + 1)
    dp[n] = 1  # Base case: empty string
    
    for i in range(n - 1, -1, -1):
        if s[i] == '0':
            continue
        
        num = 0
        for j in range(i, n):
            num = num * 10 + int(s[j])
            if num > k:
                break
            dp[i] = (dp[i] + dp[j + 1]) % MOD
    
    return dp[0]
```
**TC:** O(n × max_digits) | **SC:** O(n)

---

### 4. Space Optimized (Still O(n) due to DP array)
```python
def numberOfArrays(s, k):
    MOD = 10**9 + 7
    n = len(s)
    dp = [0] * (n + 1)
    dp[n] = 1
    
    for i in range(n - 1, -1, -1):
        if s[i] == '0':
            continue
        
        num = 0
        j = i
        while j < n and num <= k:
            num = num * 10 + int(s[j])
            if num > k:
                break
            dp[i] = (dp[i] + dp[j + 1]) % MOD
            j += 1
    
    return dp[0]
```
**TC:** O(n × max_digits) | **SC:** O(n) (cannot reduce further due to dependencies)

---

### 5. Forward DP (Alternative direction)
```python
def numberOfArrays(s, k):
    MOD = 10**9 + 7
    n = len(s)
    dp = [0] * (n + 1)
    dp[0] = 1
    
    for i in range(n):
        if s[i] == '0':
            continue
        
        num = 0
        j = i
        while j < n and num <= k:
            num = num * 10 + int(s[j])
            if num > k:
                break
            dp[j + 1] = (dp[j + 1] + dp[i]) % MOD
            j += 1
    
    return dp[n]
```
**TC:** O(n × max_digits) | **SC:** O(n)

---

**Key Formula:**
```
dp[i] = sum(dp[j+1]) for all j ≥ i where:
  1. s[i] != '0'
  2. int(s[i:j+1]) ≤ k
  3. break when int(s[i:j+1]) > k (monotonic)
```

**Example Walkthrough:**
```
s = "1317", k = 2000, n=4

Initialize: dp[4] = 1

i=3 (s[3]='7'):
  num = 7 ≤ 2000 → dp[3] += dp[4] = 1
  dp[3] = 1

i=2 (s[2]='1'):
  j=2: num=1 ≤ 2000 → dp[2] += dp[3] = 1
  j=3: num=17 ≤ 2000 → dp[2] += dp[4] = 1
  dp[2] = 2

i=1 (s[1]='3'):
  j=1: num=3 ≤ 2000 → dp[1] += dp[2] = 2
  j=2: num=31 ≤ 2000 → dp[1] += dp[3] = 1
  j=3: num=317 ≤ 2000 → dp[1] += dp[4] = 1
  dp[1] = 4

i=0 (s[0]='1'):
  j=0: num=1 ≤ 2000 → dp[0] += dp[1] = 4
  j=1: num=13 ≤ 2000 → dp[0] += dp[2] = 2
  j=2: num=131 ≤ 2000 → dp[0] += dp[3] = 1
  j=3: num=1317 ≤ 2000 → dp[0] += dp[4] = 1
  dp[0] = 8

Answer = 8
```

**Comparison Table:**

| Aspect | Decode Ways (91) | Restore Array (1416) |
|--------|------------------|----------------------|
**Number length** | 1-2 digits | Up to len(str(k)) digits |
**Upper bound** | 26 | k (up to 10⁹) |
**Leading zero** | Invalid for '0' alone | Invalid for any segment |
**Max digits check** | Implicit (2) | Explicit (break when >k) |
**Time Complexity** | O(n) | O(n × log₁₀(k)) |
**Space** | O(1) | O(n) |

**String Decoding Family:**

| Problem | Type | Key Difference |
|---------|------|---------------|
**91. Decode Ways I** | Fixed 1-26 mapping | 1-2 digits only |
**639. Decode Ways II** | With '*' wildcard | Multipliers for '*' |
**1416. Restore Array** | Variable up to k | Numbers can be longer |
**2267. Check if There Is a Valid Parentheses String Path** | Grid DP | Different context |

**Edge Cases:**
- Empty string → 1 (by convention)
- String starting with '0' → 0
- k < 10 → numbers are single digits only (simpler)
- Very large k → effectively unlimited, just avoid leading zeros
- Very long string (10⁵) → need efficient O(n) solution

**Optimization Notes:**
- Maximum number length to check = number of digits in k (≤ 10 for k ≤ 10⁹)
- This makes inner loop constant time → O(n) effectively
- Break early when num > k (numbers only increase)
- Skip when s[i] == '0' entirely

**Why Break Early:**
```
Once number exceeds k, adding more digits makes it even larger
Example: k=100, current num=101, next digit makes it 101x ≥ 1010 > k
So we can safely break the inner loop
```