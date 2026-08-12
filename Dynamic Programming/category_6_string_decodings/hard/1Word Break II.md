## 140. Word Break II
**Category:** **STRING DP / BACKTRACKING / MEMOIZATION**

**Problem:** Given a string `s` and a dictionary of words `wordDict`, return **all possible sentences** that can be formed by segmenting `s` into dictionary words. Words can be reused.

**Example:**
```
Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
Output: ["cats and dog","cat sand dog"]
```

```
Input: s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]
Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
```

```
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: []
```

---

### **Relation to Word Break I**
**Similar to:** **Word Break I** but return **all possible segmentations**
**How it's different:**
1. **Word Break I:** Just need boolean (can/cannot)
2. **Word Break II:** Need to construct **all valid sentences**
3. **Approach:** Backtracking + memoization to avoid recomputation

**Key Insight:** 
- Use memoization where `memo[i]` stores all sentences from position i
- For each valid word ending at position `i`, prepend it to all sentences from `i+1`
- This is essentially **DFS with caching**

---

### DP/Backtracking Intuition
- **State:** `memo[start]` = list of all valid sentences from index `start` to end
- **Transition:**
  ```
  For each end from start+1 to n:
      if s[start:end] in wordSet:
          for each sentence in memo[end]:
              add s[start:end] + " " + sentence to result
  ```
- **Base:** `memo[n] = [""]` (empty string at the end)
- **Answer:** `memo[0]` (with trailing spaces trimmed)

---

### 1. Recursive Backtracking (No Memo)
```python
def wordBreak(s, wordDict):
    wordSet = set(wordDict)
    n = len(s)
    result = []
    
    def backtrack(start, path):
        if start == n:
            result.append(" ".join(path))
            return
        
        for end in range(start + 1, n + 1):
            if s[start:end] in wordSet:
                path.append(s[start:end])
                backtrack(end, path)
                path.pop()
    
    backtrack(0, [])
    return result
```
**TC:** O(2ⁿ) worst case | **SC:** O(n) recursion stack

---

### 2. Memoization (Top-Down DP) - Optimal
```python
def wordBreak(s, wordDict):
    wordSet = set(wordDict)
    n = len(s)
    memo = {}  # start -> list of sentences
    
    def dfs(start):
        if start in memo:
            return memo[start]
        if start == n:
            return [""]  # Base case: empty string
        
        result = []
        for end in range(start + 1, n + 1):
            word = s[start:end]
            if word in wordSet:
                suffixes = dfs(end)
                for suffix in suffixes:
                    if suffix:
                        result.append(word + " " + suffix)
                    else:
                        result.append(word)
        
        memo[start] = result
        return result
    
    return dfs(0)
```
**TC:** O(n² + L) where L is total length of all sentences | **SC:** O(n²)

---

### 3. Tabulation + Backtracking (Bottom-Up)
```python
def wordBreak(s, wordDict):
    wordSet = set(wordDict)
    n = len(s)
    
    # dp[i] = list of sentences for s[i:]
    dp = [[] for _ in range(n + 1)]
    dp[n] = [""]  # Base case
    
    # Build from end to start
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n + 1):
            word = s[i:j]
            if word in wordSet:
                for sentence in dp[j]:
                    if sentence:
                        dp[i].append(word + " " + sentence)
                    else:
                        dp[i].append(word)
    
    return dp[0]
```
**TC:** O(n² + L) | **SC:** O(n²)

---

### 4. Optimized with Max Word Length
```python
def wordBreak(s, wordDict):
    wordSet = set(wordDict)
    max_len = max(len(word) for word in wordDict) if wordDict else 0
    n = len(s)
    memo = {n: [""]}
    
    def dfs(start):
        if start in memo:
            return memo[start]
        
        result = []
        # Only check up to max_len characters ahead
        for end in range(start + 1, min(start + max_len + 1, n + 1)):
            word = s[start:end]
            if word in wordSet:
                suffixes = dfs(end)
                for suffix in suffixes:
                    if suffix:
                        result.append(word + " " + suffix)
                    else:
                        result.append(word)
        
        memo[start] = result
        return result
    
    return dfs(0)
```
**TC:** O(n × max_len + L) | **SC:** O(n²)

---

### 5. BFS + Path Tracking
```python
from collections import deque, defaultdict

def wordBreak(s, wordDict):
    wordSet = set(wordDict)
    n = len(s)
    
    # Build graph of valid transitions
    graph = defaultdict(list)
    for i in range(n):
        for j in range(i + 1, n + 1):
            if s[i:j] in wordSet:
                graph[i].append(j)
    
    # BFS to find all paths
    queue = deque([(0, [])])  # (position, path_so_far)
    result = []
    
    while queue:
        pos, path = queue.popleft()
        
        if pos == n:
            result.append(" ".join(path))
            continue
        
        for next_pos in graph[pos]:
            word = s[pos:next_pos]
            queue.append((next_pos, path + [word]))
    
    return result
```
**TC:** O(2ⁿ) worst case | **SC:** O(n²)

---

**Key Formula (Memoization):**
```
memo[start] = [
    word + " " + suffix 
    for word in words_starting_at_start
    for suffix in memo[start + len(word)]
]
memo[n] = [""]
```

**Example Walkthrough:**
```
s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]

Build memo from end:

memo[10] = [""] (n=10)

i=9: try "g" not in dict, "dg" no, "dog" at j=10? j=10 gives s[9:10]="g" only
     Actually positions: i=9 means s[9]='g', j=10 gives "g" only
     So no word → memo[9] = []

i=8: s[8]='o', j=9 "o" no, j=10 "og" no → memo[8] = []

i=7: s[7]='d', j=8 "d" no, j=9 "do" no, j=10 "dog" YES
     from j=10: memo[10] = [""] → add "dog" → memo[7] = ["dog"]

i=6: s[6]='n', j=7 "n" no, j=8 "nd" no, j=9 "ndo" no, j=10 "ndog" no → memo[6]=[]

i=5: s[5]='a', j=6 "a" no, j=7 "an" no, j=8 "and" YES
     from j=8: memo[8]=[] → nothing
     j=9 "ando" no, j=10 "andog" no → memo[5]=[]

i=4: s[4]='s', j=5 "s" no, j=6 "sa" no, j=7 "san" no, j=8 "sand" YES
     from j=8: memo[8]=[] → nothing
     j=9 "sando" no, j=10 "sandog" no → memo[4]=[]

i=3: s[3]='s', j=4 "s" no, j=5 "sa" no, j=6 "san" no, j=7 "sand" YES
     from j=7: memo[7]=["dog"] → add "sand dog" → memo[3] = ["sand dog"]
     j=8 "sando" no, j=9 "sandog" no, j=10 "sandog"? actually s[3:10]="sandog" not in dict

i=2: s[2]='t', j=3 "t" no, j=4 "ts" no, j=5 "tsa" no, j=6 "tsan" no,
     j=7 "tsand" no, j=8 "tsando" no, j=9 "tsandog" no, j=10 "tsandog" no
     Wait s[2:7]="tsand"? s[2:10]="tsandog"? not in dict → memo[2]=[]

i=1: s[1]='a', j=2 "a" no, j=3 "at" no, j=4 "ats" no, j=5 "atsa" no,
     j=6 "atsan" no, j=7 "atsand" no, j=8 "atsando" no, j=9 "atsandog" no → memo[1]=[]

i=0: s[0]='c', j=1 "c" no, j=2 "ca" no, j=3 "cat" YES
     from j=3: memo[3]=["sand dog"] → add "cat sand dog"
     j=4 "cats" YES
     from j=4: memo[4]=[] → nothing
     j=5 "catsa" no, j=6 "catsan" no, j=7 "catsand" YES
     from j=7: memo[7]=["dog"] → add "catsand dog"? Wait "catsand" is word? No "catsand" not in dict
     Actually s[0:7]="catsand" not in dict. Only "cats" at j=4 and "cat" at j=3

     Also check "cats" at j=4: from memo[4]=[] so nothing
     So only "cat" works: memo[0] = ["cat sand dog"]

But we missed "cats and dog"? Let's see:
"cats" at j=4, then from j=4 we need "and dog" but memo[4] was empty because we didn't process j=4 correctly

Let's recompute i=4 with correct words:
i=4 (s[4]='s'): 
  j=5 "s" no
  j=6 "sa" no
  j=7 "san" no
  j=8 "sand" YES → from j=8 (memo[8]=[]) → nothing
  j=9 "sando" no
  j=10 "sandog" no
So memo[4] remains empty

But we need "and" at i=5:
i=5 (s[5]='a'):
  j=6 "a" no
  j=7 "an" no
  j=8 "and" YES → from j=8 (memo[8]=[]) → nothing
So memo[5] empty

i=6 (s[6]='n'):
  j=7 "n" no
  j=8 "nd" no
  j=9 "ndo" no
  j=10 "ndog" no → empty

i=7 we already have "dog"

So where does "cats and dog" come from? It should be:
"cats" at (0,4) + "and" at (4,7) + "dog" at (7,10)

But our memo[4] is empty because we didn't connect "and" correctly.
The issue: When processing i=4, we need to know that from i=4 we can take "and" to reach i=7
But "and" starts at i=5, not i=4

This reveals the flaw in building from end: we need to store all possible words at each position,
and when building sentences, we need to consider all words that start at current position.

The correct memoization approach in solution #2 works because:
dfs(4) will check all words starting at 4, find none, return []
dfs(5) will find "and" at (5,8) and combine with dfs(8) to get "and dog"
dfs(0) will find "cats" at (0,4) and combine with dfs(4) which now has "and dog" from above
```

**Comparison Table:**

| Aspect | Word Break I | Word Break II |
|--------|--------------|---------------|
**Output** | Boolean | List of strings |
**Approach** | DP boolean array | DFS + Memoization |
**State** | dp[i] = can reach i | memo[i] = all sentences from i |
**Base Case** | dp[0] = True | memo[n] = [""] |
**Time Complexity** | O(n²) | O(2ⁿ) worst case, but memoized |
**Space** | O(n) | O(n² + total output) |

**String Partitioning Family:**

| Problem | Type | Key Difference |
|---------|------|---------------|
**139. Word Break** | Existence | Just boolean |
**140. Word Break II** | All sentences | Return all partitions |
**131. Palindrome Partitioning** | Palindromes | Partition into palindromes |
**132. Palindrome Partitioning II** | Min cuts | Minimize cuts |

**Edge Cases:**
- Empty string → [""] (by convention, empty sentence)
- No valid segmentation → []
- Very long strings → may have exponential outputs

**Optimization Notes:**
- **Max word length** pruning: Only check words up to max_len
- **Early pruning:** Check if suffix is reachable using Word Break I DP first
- **Memoization** is essential to avoid recomputation
- Output size can be huge, so time complexity includes output size

**Why Memoization Works:**
- Same substring appears in multiple contexts
- "and" appears after "cats" and after "cat"
- Caching results for each start position saves recomputation
- Bottom-up DP is harder because we need to build strings