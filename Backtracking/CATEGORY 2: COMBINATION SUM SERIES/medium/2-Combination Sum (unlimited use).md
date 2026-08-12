## 🧠 **Combination Sum (Unlimited Use) — Backtracking Pattern**

---

## 1. **Problem Statement**

Given an array of **distinct integers** `candidates` and a target integer `target`, return all **unique combinations** where:

* The chosen numbers sum to `target`
* You can use the **same number unlimited times**

### ⚠️ Constraints

* `1 <= candidates.length <= 30`
* `2 <= candidates[i] <= 40`
* `1 <= target <= 40`
* All numbers are **distinct**

---

## 2. **Diagram (Backtracking Tree)**

Example: `candidates = [2,3,6,7], target = 7`

```
Start: []
 ├── [2]
 │    ├── [2,2]
 │    │    ├── [2,2,2]
 │    │    │    ├── [2,2,2,2] ❌ (sum > 7)
 │    │    │    └── ...
 │    │    └── [2,2,3] ✅ (sum = 7)
 │    ├── [2,3]
 │    │    ├── [2,3,3] ❌
 │    └── ...
 ├── [3]
 │    ├── [3,3]
 │    │    ├── [3,3,3] ❌
 ├── [6]
 │    ├── [6,?] ❌
 └── [7] ✅
```

👉 Key idea:

* Stay on same index → reuse element
* Move forward → avoid duplicates

---

## 3. **Example I/O**

### ✅ Example 1

```
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3], [7]]
```

✔ Explanation:

* 2+2+3 = 7
* 7 itself is valid

---

### ⚠️ Edge Case

```
Input: candidates = [5], target = 3
Output: []
```

✔ Explanation:

* No way to reach target

---

## 4. **Intuition & Pattern Recognition**

### 🔑 Signals:

* "Find all combinations" → **Backtracking**
* "Unlimited use" → stay on same index
* "Distinct candidates" → no need to handle duplicates

### 🧠 Interview Thought:

> “This is a subset generation problem where I can reuse elements → I should use DFS + backtracking and **not increment index after choosing**.”

---

## 5. **Simpler Version**

### 🔹 Start Simple:

👉 **Subset**

* Pick or not pick each element once

### 🔹 Next Level:

👉 **Combination Sum II**

* Each number used once + duplicates present

### 🔹 Current Problem:

👉 **Combination Sum**

### 🧠 Key Difference:

| Problem            | Reuse Allowed | Duplicate Handling |
| ------------------ | ------------- | ------------------ |
| Subsets            | ❌             | No                 |
| Combination Sum II | ❌             | Yes                |
| Combination Sum    | ✅             | No                 |

### 🧠 Transition Thinking:

* Subsets → move index `i+1`
* Combination Sum → stay at `i` (reuse allowed)

---

## 6. **Brute Force**

Generate all subsets with repetition (huge search space).

### ❌ Approach:

* Try all combinations of all lengths
* Check if sum == target

### ⏱ Complexity:

* Time: **O(2^target)** (very bad)
* Space: recursion stack

---

## 7. **Optimal Solution (Backtracking)**

```python
class Solution:
    def combinationSum(self, candidates, target):
        res = []
        
        def dfs(i, curr, total):
            # ✅ Found valid combination
            if total == target:
                res.append(curr.copy())
                return
            
            # ❌ Out of bounds or exceeded
            if i >= len(candidates) or total > target:
                return
            
            # 🔹 Choice 1: include current element (reuse allowed)
            curr.append(candidates[i])
            dfs(i, curr, total + candidates[i])  # stay at i
            
            # 🔙 backtrack
            curr.pop()
            
            # 🔹 Choice 2: skip current element
            dfs(i + 1, curr, total)
        
        dfs(0, [], 0)
        return res
```

### ⏱ Complexity:

* Time: **O(2^target)** (pruned heavily)
* Space: **O(target)** recursion depth

---

## 8. **Step-by-Step Trace**

Input: `[2,3], target = 5`

| Step | i               | curr    | total | Action       |
| ---- | --------------- | ------- | ----- | ------------ |
| 1    | 0               | []      | 0     | start        |
| 2    | 0               | [2]     | 2     | include 2    |
| 3    | 0               | [2,2]   | 4     | include 2    |
| 4    | 0               | [2,2,2] | 6     | ❌ > target   |
| 5    | 1               | [2,2]   | 4     | try next     |
| 6    | 1               | [2,2,3] | 7     | ❌            |
| 7    | backtrack → [2] |         |       |              |
| 8    | 1               | [2,3]   | 5     | ✅ add result |
| 9    | backtrack → []  |         |       |              |
| 10   | 1               | [3]     | 3     | include 3    |
| 11   | 1               | [3,3]   | 6     | ❌            |

Final: `[[2,3]]`

---

## 9. **Related Problems (Pattern Build-Up)**

1. **Subsets**
   → Base backtracking (pick / not pick)

2. **Combination Sum II**
   → No reuse + handle duplicates

3. **Permutations**
   → Order matters (use visited)

4. **Palindrome Partitioning**
   → Partitioning + backtracking

5. **Letter Combinations of a Phone Number**
   → Build combinations using DFS

---

## 🔥 Final Interview Insight

👉 The **core trick**:

* Same index → reuse allowed
* Next index → skip

👉 If you remember only one line:

```
dfs(i, ...)  # reuse
dfs(i+1, ...)  # skip
```

---

If you want, I can next show:

* 🔥 How to **optimize with sorting + pruning**
* 🔥 Or dry run visualization like your DFS tree confusion earlier
