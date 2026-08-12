## Dungeon Game
**Problem:** Knight starts at top-left of dungeon (m×n grid), needs to reach bottom-right. Each cell has value:
- Positive: gains health
- Negative: loses health (demons)
- Cannot go below 1 health at any point
Find **minimum initial health** needed.

**Example:**
```
Input: dungeon = [[-2,-3,3],
                  [-5,-10,1],
                  [10,30,-5]]
Output: 7
Explanation: Path: Right → Right → Down → Down
Start health = 7
Path: 7 → 5 → 2 → 1 → 6 → 1
```

---

### DP Intuition
- **Key Insight:** Work **backwards** from princess to knight
- **State:** `dp[i][j]` = minimum health needed to reach princess starting from (i,j)
- **Transition:**
  - Need at least 1 health always
  - Health at (i,j) = max(1, min(right, down) - dungeon[i][j])
- **Base:** Bottom-right cell: need enough to survive that cell
- **Answer:** `dp[0][0]`

---

### 1. Recursive Solution
```python
def calculateMinimumHP(dungeon):
    m, n = len(dungeon), len(dungeon[0])
    
    def dfs(i, j):
        if i >= m or j >= n:
            return float('inf')
        if i == m-1 and j == n-1:
            return max(1, 1 - dungeon[i][j])
        
        right = dfs(i, j+1)
        down = dfs(i+1, j)
        min_req = min(right, down)
        
        return max(1, min_req - dungeon[i][j])
    
    return dfs(0, 0)
```
**TC:** O(2ᵐ⁺ⁿ) | **SC:** O(m+n) recursion stack

---

### 2. Memoization (Top-Down DP)
```python
def calculateMinimumHP(dungeon):
    m, n = len(dungeon), len(dungeon[0])
    memo = {}
    
    def dfs(i, j):
        if i >= m or j >= n:
            return float('inf')
        if i == m-1 and j == n-1:
            return max(1, 1 - dungeon[i][j])
        if (i, j) in memo:
            return memo[(i, j)]
        
        right = dfs(i, j+1)
        down = dfs(i+1, j)
        min_req = min(right, down)
        
        memo[(i, j)] = max(1, min_req - dungeon[i][j])
        return memo[(i, j)]
    
    return dfs(0, 0)
```
**TC:** O(m×n) | **SC:** O(m×n)

---

### 3. Tabulation (Bottom-Up DP)
```python
def calculateMinimumHP(dungeon):
    m, n = len(dungeon), len(dungeon[0])
    
    # Create DP table with extra row/col for boundaries
    dp = [[float('inf')] * (n+1) for _ in range(m+1)]
    
    # Princess cell requirements
    dp[m-1][n] = dp[m][n-1] = 1  # imaginary cells before princess
    
    # Fill from bottom-right to top-left
    for i in range(m-1, -1, -1):
        for j in range(n-1, -1, -1):
            min_health_on_exit = min(dp[i+1][j], dp[i][j+1])
            dp[i][j] = max(1, min_health_on_exit - dungeon[i][j])
    
    return dp[0][0]
```
**TC:** O(m×n) | **SC:** O(m×n)

---

### 4. Space Optimized (1D DP)
```python
def calculateMinimumHP(dungeon):
    m, n = len(dungeon), len(dungeon[0])
    
    dp = [float('inf')] * (n+1)
    dp[n-1] = 1  # bottom-right cell's requirement
    
    # Fill from bottom to top
    for i in range(m-1, -1, -1):
        for j in range(n-1, -1, -1):
            if i == m-1 and j == n-1:
                dp[j] = max(1, 1 - dungeon[i][j])
            else:
                min_health_on_exit = min(dp[j], dp[j+1])
                dp[j] = max(1, min_health_on_exit - dungeon[i][j])
    
    return dp[0]
```
**TC:** O(m×n) | **SC:** O(n)

---

**Key Transition Formula:**
```
dp[i][j] = max(1, min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j])
```

**Why Backwards DP works:**
- Forward DP fails because path affects future requirements
- Backwards: we know health needed to survive from each cell to princess
- At each cell: need enough health to survive current cell + next step

**Example Walkthrough:**
```
Dungeon:        DP (backwards):
-2  -3   3      7   5   2
-5 -10   1  →   6  11   5
10  30  -5      1   1   6

Start from (2,2): need max(1, 1-(-5)) = 6
(2,1): need max(1, min(6, 5) - 30) = 1
(0,0): need max(1, min(5, 6) - (-2)) = 7
```

**Edge Cases:**
- All positive cells → need only 1 health
- All negative cells → need sum of negatives + 1
- Single cell: need max(1, 1 - dungeon[0][0])