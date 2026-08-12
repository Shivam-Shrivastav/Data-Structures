## 🧠 **Combination Sum III (k numbers, sum to n) — Backtracking Pattern**

---

## 1. **Problem Statement**

Find all valid combinations of **k distinct numbers** such that:

* Numbers are from **1 to 9**
* Each number is used **at most once**
* The sum of chosen numbers = `n`

Return all possible unique combinations.

### ⚠️ Constraints

* `2 <= k <= 9`
* `1 <= n <= 60`
* Numbers allowed: **[1..9] only**

---

## 2. **Diagram (Backtracking Tree)**

Example: `k = 3, n = 7`

```text
Start: []
 ├── [1]
 │    ├── [1,2]
 │    │    ├── [1,2,3] ❌ (sum=6, need 7)
 │    │    ├── [1,2,4] ✅ (sum=7)
 │    │    └── ...
 │    ├── [1,3]
 │    │    ├── [1,3,4] ❌ (8)
 │
 ├── [2]
 │    ├── [2,3]
 │    │    ├── [2,3,4] ❌
 │
 └── [3] ...
```

👉 Key idea:

* Always move forward → no reuse
* Track both:

  * **count (k)**
  * **sum (n)**

---

## 3. **Example I/O**

### ✅ Example 1

```text
Input: k = 3, n = 7
Output: [[1,2,4]]
```

✔ Explanation:

* Only combination of 3 numbers from 1–9 summing to 7

---

### ⚠️ Edge Case

```text
Input: k = 4, n = 1
Output: []
```

✔ Explanation:

* Impossible to pick 4 distinct positive numbers to sum to 1

---

## 4. **Intuition & Pattern Recognition**

### 🔑 Signals:

* Fixed range (1–9) → no input array needed
* "Pick k numbers" → track size
* "Sum to n" → track total
* "Use once" → move forward

### 🧠 Interview Thought:

> “This is a constrained combination problem: fixed choices (1–9), no reuse, exact size k → classic backtracking with pruning.”

---

## 5. **Simpler Version**

### 🔹 Step 1:

👉 **Combination Sum**

* Unlimited reuse, no size constraint

### 🔹 Step 2:

👉 **Combination Sum II**

* No reuse + duplicates handled

### 🔹 Current Problem:

👉 **Combination Sum III**

### 🧠 Key Differences:

| Feature             | CS I | CS II | CS III |
| ------------------- | ---- | ----- | ------ |
| Reuse allowed       | ✅    | ❌     | ❌      |
| Duplicates in input | ❌    | ✅     | ❌      |
| Fixed size (k)      | ❌    | ❌     | ✅      |
| Fixed range (1–9)   | ❌    | ❌     | ✅      |

### 🧠 Transition Thinking:

* CS II → no reuse → `dfs(i+1)`
* Add constraint → `len(curr) == k`

---

## 6. **Brute Force**

* Generate all subsets of `[1..9]`
* Filter:

  * length == k
  * sum == n

### ⏱ Complexity:

* Time: **O(2^9) ≈ constant but inefficient**
* Space: high due to storing subsets

---

## 7. **Optimal Solution (Backtracking + Pruning)**

```python
class Solution:
    def combinationSum3(self, k, n):
        res = []
        
        def dfs(start, curr, total):
            # ✅ valid combination
            if len(curr) == k and total == n:
                res.append(curr.copy())
                return
            
            # ❌ pruning
            if len(curr) > k or total > n:
                return
            
            for num in range(start, 10):  # numbers 1 to 9
                # 🔹 choose
                curr.append(num)
                
                # 🔹 move forward (no reuse)
                dfs(num + 1, curr, total + num)
                
                # 🔙 backtrack
                curr.pop()
        
        dfs(1, [], 0)
        return res
```

### ⏱ Complexity:

* Time: **O(C(9, k))**
* Space: **O(k)** recursion depth

---

## 8. **Step-by-Step Trace**

Input: `k=3, n=7`

| Step | start                     | curr    | total | Action   |
| ---- | ------------------------- | ------- | ----- | -------- |
| 1    | 1                         | []      | 0     | start    |
| 2    | 1                         | [1]     | 1     | pick 1   |
| 3    | 2                         | [1,2]   | 3     | pick 2   |
| 4    | 3                         | [1,2,3] | 6     | continue |
| 5    | 4                         | [1,2,4] | 7     | ✅ add    |
| 6    | backtrack                 |         |       |          |
| 7    | try next numbers → pruned |         |       |          |
| 8    | explore other branches    |         |       |          |

Final: `[[1,2,4]]`

---

## 9. **Related Problems (Pattern Build-Up)**

1. **Combination Sum**
   → Base version (reuse allowed)

2. **Combination Sum II**
   → No reuse + duplicates

3. **Subsets**
   → Basic pick / skip pattern

4. **Permutations**
   → Order-based backtracking

5. **N-Queens**
   → Advanced constraint-based backtracking

---

## 🔥 Final Interview Insight

### 💥 Think of it as:

> “Pick **k numbers from 1–9** such that sum = n”

### 💥 Core Template:

```python
dfs(start, curr, total)
```

### 💥 Golden Rules:

* `dfs(num + 1)` → no reuse
* `len(curr) == k` → size constraint
* `total > n` → prune early

---

If you want next:

* 🔥 I can give you **1 template that solves ALL Combination Sum variants**
* 🔥 Or a **mental model to instantly identify backtracking problems in interviews**
