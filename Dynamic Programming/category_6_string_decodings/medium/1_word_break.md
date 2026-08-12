## 139. Word Break
**Category:** **STRING DECODING / PARTITIONING**

**Problem:** Given a string `s` and a dictionary of words `wordDict`, return `true` if `s` can be segmented into a space-separated sequence of dictionary words. Words can be reused.

**Example:**
```
Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: "leetcode" = "leet" + "code"
```

```
Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: "applepenapple" = "apple" + "pen" + "apple"
```

```
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false
Explanation: No valid segmentation
```

---

### **Relation to Decode Ways**
**Similar to:** **Decode Ways** but with **variable word lengths** from dictionary
**How it's different:**
1. **Decode Ways:** Fixed mapping (1-26), always 1 or 2 digits
2. **Word Break:** Words of any length, must match dictionary exactly
3. **Dictionary:** Can reuse words, need to check substring in dictionary

**Key Insight:** 
- At each position `i`, we try to find a word that ends at `i`
- If `s[j:i]` is in dictionary and we can reach `j`, then we can reach `i`
- This is a **reachability problem** in a DAG

---

### DP Intuition
- **State:** `dp[i]` = whether first `i` characters (s[0..i-1]) can be segmented
- **Transition:**
  ```
  For each j from 0 to i-1:
      if dp[j] and s[j:i] in wordDict:
          dp[i] = true
          break
  ```
- **Base:** `dp[0] = true` (empty string)
- **Answer:** `dp[n]`

---

### 1. Recursive Solution
```python
def wordBreak(s, wordDict):
    wordSet = set(wordDict)
    n = len(s)
    
    def dfs(start):
        if start == n:
            return True
        
        for end in range(start + 1, n + 1):
            if s[start:end] in wordSet and dfs(end):
                return True
        
        return False
    
    return dfs(0)
```
**TC:** O(2ⁿ) | **SC:** O(n) recursion stack

---

### 2. Memoization (Top-Down DP)
```python
def wordBreak(s, wordDict):
    wordSet = set(wordDict)
    n = len(s)
    memo = [-1] * (n + 1)  # -1: uncomputed, 0: false, 1: true
    
    def dfs(start):
        if start == n:
            return True
        if memo[start] != -1:
            return memo[start] == 1
        
        for end in range(start + 1, n + 1):
            if s[start:end] in wordSet and dfs(end):
                memo[start] = 1
                return True
        
        memo[start] = 0
        return False
    
    return dfs(0)
```
**TC:** O(n²) | **SC:** O(n)

---

### 3. Tabulation (Bottom-Up DP)
```python
def wordBreak(s, wordDict):
    wordSet = set(wordDict)
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True
    
    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in wordSet:
                dp[i] = True
                break
    
    return dp[n]
```
**TC:** O(n²) | **SC:** O(n)

---

### 4. Optimized with Max Word Length
```python
def wordBreak(s, wordDict):
    wordSet = set(wordDict)
    max_len = max(len(word) for word in wordDict) if wordDict else 0
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True
    
    for i in range(1, n + 1):
        # Only check words that could end at i
        # Start from max(0, i-max_len) to i
        for j in range(max(0, i - max_len), i):
            if dp[j] and s[j:i] in wordSet:
                dp[i] = True
                break
    
    return dp[n]
```
**TC:** O(n × max_len) | **SC:** O(n)

---

### 5. BFS Approach
```python
from collections import deque

def wordBreak(s, wordDict):
    wordSet = set(wordDict)
    n = len(s)
    queue = deque([0])
    visited = [False] * (n + 1)
    visited[0] = True
    
    while queue:
        start = queue.popleft()
        if start == n:
            return True
        
        for end in range(start + 1, n + 1):
            if not visited[end] and s[start:end] in wordSet:
                visited[end] = True
                queue.append(end)
    
    return False
```
**TC:** O(n²) | **SC:** O(n)

---

**Key Formula:**
```
dp[i] = OR(dp[j] AND s[j:i] in wordDict) for all j < i
dp[0] = True
```

**Example Walkthrough (Tabulation):**
```
s = "leetcode", wordDict = ["leet","code"], n=8

dp[0] = True

i=1: j=0: s[0:1]="l" not in dict → dp[1]=False
i=2: j=0: s[0:2]="le" not in dict → dp[2]=False
i=3: j=0: s[0:3]="lee" not in dict → dp[3]=False
i=4: j=0: s[0:4]="leet" in dict and dp[0]=True → dp[4]=True
i=5: j=1: s[1:5]="eetc" not in dict
     j=2: s[2:5]="etc" not in dict
     j=3: s[3:5]="tc" not in dict
     j=4: s[4:5]="c" not in dict → dp[5]=False
i=6: j=2: s[2:6]="etc" not in dict
     j=3: s[3:6]="tco" not in dict
     j=4: s[4:6]="co" not in dict
     j=5: s[5:6]="o" not in dict → dp[6]=False
i=7: j=3: s[3:7]="tcod" not in dict
     j=4: s[4:7]="cod" not in dict
     j=5: s[5:7]="od" not in dict
     j=6: s[6:7]="d" not in dict → dp[7]=False
i=8: j=4: s[4:8]="code" in dict and dp[4]=True → dp[8]=True

Answer = dp[8] = True
```

**Example with Optimization:**
```
s = "applepenapple", wordDict = ["apple","pen"], max_len = 5

dp[0]=True

i=5: check j from max(0,5-5)=0 to 4:
  j=0: s[0:5]="apple" in dict → dp[5]=True
i=8: j from 3 to 7:
  j=5: s[5:8]="pen" in dict → dp[8]=True
i=13: j from 8 to 12:
  j=8: s[8:13]="apple" in dict → dp[13]=True
```

**Comparison Table:**

| Aspect | Decode Ways (91) | Word Break (139) |
|--------|------------------|------------------|
**Segments** | Fixed length (1-2) | Variable length |
**Mapping** | 1-26 to letters | Dictionary words |
**Validation** | Numeric range check | Exact string match |
**DP Transition** | dp[i] += dp[i-1] + dp[i-2] | dp[i] = OR(dp[j] AND s[j:i] in dict) |
**Time Complexity** | O(n) | O(n²) |
**Space** | O(1) | O(n) |

**String Partitioning Family:**

| Problem | Type | Key Difference |
|---------|------|---------------|
**91. Decode Ways** | Fixed mapping | 1-26 only, 1 or 2 digits |
**139. Word Break** | Dictionary words | Can reuse, any length |
**140. Word Break II** | Return all sentences | Backtracking + memo |
**132. Palindrome Partitioning II** | Min cuts | Palindrome checking |

**Edge Cases:**
- Empty string → True (can be segmented)
- Empty dictionary → False (unless s empty)
- Single char in dictionary → True
- Dictionary with overlapping words → handled

**Optimization Techniques:**
1. **Max word length:** Limit j range to `i - max_len` to i
2. **HashSet for dictionary:** O(1) lookup
3. **BFS:** Alternative approach, often similar complexity
4. **Trie:** For very large dictionaries

**Why BFS Works:**
- States are positions in string
- Edges are words that match from current position
- Find if we can reach end position n

**Common Pitfalls:**
- Forgetting to convert wordDict to set for O(1) lookup
- Not handling empty string case
- Off-by-one in substring indices (s[j:i] excludes i)