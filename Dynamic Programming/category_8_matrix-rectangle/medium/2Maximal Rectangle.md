## 85. Maximal Rectangle
**Category:** **MATRIX/RECTANGLE DP / HISTOGRAM**

**Problem:** Given a `rows x cols` binary matrix filled with `0`s and `1`s, find the **largest rectangle** containing only `1`s and return its **area**.

**Example:**
```
Input: matrix = 
[["1","0","1","0","0"],
 ["1","0","1","1","1"],
 ["1","1","1","1","1"],
 ["1","0","0","1","0"]]
Output: 6
Explanation: The largest rectangle of 1's has area 6
```

```
Input: matrix = [["0"]]
Output: 0
```

```
Input: matrix = [["1"]]
Output: 1
```

---

### **Relation to Square Problems**
**Similar to:** **Maximal Square (221)** but **rectangle** (any dimensions)
**How it's different:**
1. **Maximal Square:** Equal sides, simple DP with min of neighbors
2. **Maximal Rectangle:** Can be any width/height, need histogram approach
3. **Key Insight:** Convert each row to histogram heights, then find largest rectangle in histogram

**Key Insight:** 
- For each row, treat it as base and compute heights of consecutive 1's above
- Then problem reduces to **Largest Rectangle in Histogram (84)** for each row
- Heights[i][j] = if matrix[i][j]=='1' then heights[i-1][j]+1 else 0

---

### DP/Histogram Intuition
- **Step 1:** Build `heights` array for each row
  ```
  heights[j] = heights[j] + 1 if matrix[i][j] == '1' else 0
  ```
- **Step 2:** For each row's heights, find largest rectangle area using stack
- **Step 3:** Track maximum across all rows

**Largest Rectangle in Histogram Algorithm:**
- Use stack to maintain increasing heights
- When height decreases, pop and calculate area with popped height as smallest

---

### 1. Brute Force (Check all rectangles)
```python
def maximalRectangle(matrix):
    if not matrix or not matrix[0]:
        return 0
    
    m, n = len(matrix), len(matrix[0])
    max_area = 0
    
    for top in range(m):
        for bottom in range(top, m):
            # Check if all rows from top to bottom form valid rectangle
            width = 0
            for col in range(n):
                # Check if column has all 1's from top to bottom
                valid = True
                for row in range(top, bottom + 1):
                    if matrix[row][col] == '0':
                        valid = False
                        break
                
                if valid:
                    width += 1
                    max_area = max(max_area, width * (bottom - top + 1))
                else:
                    width = 0
    
    return max_area
```
**TC:** O(m² × n × m) = O(m³n) terrible | **SC:** O(1)

---

### 2. DP Heights + Brute Force Histogram
```python
def maximalRectangle(matrix):
    if not matrix or not matrix[0]:
        return 0
    
    m, n = len(matrix), len(matrix[0])
    heights = [0] * n
    max_area = 0
    
    for i in range(m):
        # Update heights
        for j in range(n):
            if matrix[i][j] == '1':
                heights[j] += 1
            else:
                heights[j] = 0
        
        # Brute force find largest rectangle in histogram
        for j in range(n):
            min_height = heights[j]
            for k in range(j, n):
                min_height = min(min_height, heights[k])
                max_area = max(max_area, min_height * (k - j + 1))
    
    return max_area
```
**TC:** O(m × n²) | **SC:** O(n)

---

### 3. DP Heights + Stack (Optimal)
```python
def maximalRectangle(matrix):
    if not matrix or not matrix[0]:
        return 0
    
    m, n = len(matrix), len(matrix[0])
    heights = [0] * n
    max_area = 0
    
    def largest_rectangle_area(heights):
        stack = [-1]  # sentinel
        max_area = 0
        
        for i, h in enumerate(heights + [0]):  # add 0 at end to flush stack
            while stack[-1] != -1 and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                width = i - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(i)
        
        return max_area
    
    for i in range(m):
        # Update heights
        for j in range(n):
            if matrix[i][j] == '1':
                heights[j] += 1
            else:
                heights[j] = 0
        
        # Find largest rectangle in current histogram
        max_area = max(max_area, largest_rectangle_area(heights))
    
    return max_area
```
**TC:** O(m × n) | **SC:** O(n)

---

### 4. DP with Left/Right Boundaries
```python
def maximalRectangle(matrix):
    if not matrix or not matrix[0]:
        return 0
    
    m, n = len(matrix), len(matrix[0])
    heights = [0] * n
    left = [0] * n    # left boundary where height >= current
    right = [n] * n   # right boundary where height >= current
    max_area = 0
    
    for i in range(m):
        # Update heights and left boundaries
        curr_left = 0
        for j in range(n):
            if matrix[i][j] == '1':
                heights[j] += 1
                left[j] = max(left[j], curr_left)
            else:
                heights[j] = 0
                left[j] = 0
                curr_left = j + 1
        
        # Update right boundaries
        curr_right = n
        for j in range(n-1, -1, -1):
            if matrix[i][j] == '1':
                right[j] = min(right[j], curr_right)
            else:
                right[j] = n
                curr_right = j
            
            # Calculate area
            max_area = max(max_area, heights[j] * (right[j] - left[j]))
    
    return max_area
```
**TC:** O(m × n) | **SC:** O(n)

---

### 5. DP Heights + Stack (with detailed comments)
```python
def maximalRectangle(matrix):
    if not matrix or not matrix[0]:
        return 0
    
    m, n = len(matrix), len(matrix[0])
    heights = [0] * n
    max_area = 0
    
    for i in range(m):
        # Update histogram heights for current row
        for j in range(n):
            heights[j] = heights[j] + 1 if matrix[i][j] == '1' else 0
        
        # Find largest rectangle in current histogram using stack
        stack = []
        for j in range(n + 1):
            curr_height = heights[j] if j < n else 0
            
            while stack and heights[stack[-1]] > curr_height:
                height = heights[stack.pop()]
                left = stack[-1] if stack else -1
                width = j - left - 1
                max_area = max(max_area, height * width)
            
            stack.append(j)
    
    return max_area
```

---

**Key Formula:**
```
heights[j] = heights[j] + 1 if matrix[i][j] == '1' else 0
For each row, find largest rectangle in histogram of heights
```

**Example Walkthrough:**
```
matrix = 
[1,0,1,0,0]
[1,0,1,1,1]
[1,1,1,1,1]
[1,0,0,1,0]

Row 0: heights = [1,0,1,0,0]
  Histogram max area = 1 (from any single 1)

Row 1: heights = [2,0,2,1,1]
  Histogram: [2,0,2,1,1]
  Largest rectangle: 
    - Using height 2 at index 0: width 1 → area 2
    - Using height 2 at index 2: width 1 → area 2
    - Using height 1 at indices 2-4: width 3, height 1 → area 3
  Max = 3

Row 2: heights = [3,1,3,2,2]
  Histogram: [3,1,3,2,2]
  Largest rectangle:
    - Height 3 at index 0: width 1 → 3
    - Height 1: width 5 → 5
    - Height 3 at index 2: width 1 → 3
    - Height 2 at indices 2-4: width 3, height 2 → area 6
  Max = 6

Row 3: heights = [4,0,0,3,0]
  Histogram max = 4 (height 4 at index 0, width 1)

Overall max = 6
```

**Visual Heights Progression:**
```
Row 0: 1 0 1 0 0
Row 1: 2 0 2 1 1
Row 2: 3 1 3 2 2
Row 3: 4 0 0 3 0
```

**Stack Algorithm for Row 2 Heights [3,1,3,2,2]:**
```
i=0, h=3: stack=[0]
i=1, h=1: 3>1 → pop 0, area=3*(1-(-1)-1)=3*1=3, stack=[], push 1 → stack=[1]
i=2, h=3: 1<3 → push 2 → stack=[1,2]
i=3, h=2: 3>2 → pop 2, area=3*(3-1-1)=3*1=3, stack=[1]; 1<2 → push 3 → stack=[1,3]
i=4, h=2: 2==2 → push 4 → stack=[1,3,4]
i=5, h=0: pop 4, area=2*(5-3-1)=2*1=2
          pop 3, area=2*(5-1-1)=2*3=6
          pop 1, area=1*(5-(-1)-1)=1*5=5
max = 6
```

**Comparison Table:**

| Aspect | Maximal Square (221) | Maximal Rectangle (85) |
|--------|---------------------|----------------------|
**Shape** | Square only | Any rectangle |
**DP Approach** | 2D DP with min neighbors | Histogram + stack |
**State** | dp[i][j] = side length | heights[j] per row |
**Transition** | 1 + min(up, left, up-left) | Update heights, then histogram |
**Time** | O(m × n) | O(m × n) |
**Space** | O(n) | O(n) |

**Matrix/Rectangle DP Family:**

| Problem | Type | Key Difference |
|---------|------|---------------|
**221. Maximal Square** | Square | Equal sides |
**85. Maximal Rectangle** | Any rectangle | Histogram approach |
**84. Largest Rectangle in Histogram** | 1D | Base algorithm |
**1277. Count Square Submatrices** | Count squares | Sum of dp |
**1504. Count Submatrices With All Ones** | Count rectangles | More complex counting |

**Edge Cases:**
- Empty matrix → 0
- Single row → treat as histogram
- Single column → treat as histogram
- All zeros → 0
- All ones → m × n

**Why Stack Approach is Optimal:**
- Each element pushed/popped once → O(n) per row
- Total O(m × n) time
- Space O(n) for heights and stack

**Alternative Approaches:**
- **DP with left/right boundaries:** Same complexity, different implementation
- **Divide and conquer:** More complex, O(mn log n)
- **Segment tree:** Overkill for this problem