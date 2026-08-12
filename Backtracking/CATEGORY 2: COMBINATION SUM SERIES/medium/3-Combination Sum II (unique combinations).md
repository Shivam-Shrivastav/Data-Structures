## 🧠 **Combination Sum II (Unique Combinations) — Backtracking Pattern**

---

## 1. **Problem Statement**

Given an array `candidates` (may contain **duplicates**) and a target integer `target`, return all **unique combinations** such that:

* Each number can be used **at most once**
* The sum equals `target`
* The result must not contain duplicate combinations

### ⚠️ Constraints

* `1 <= candidates.length <= 100`
* `1 <= candidates[i] <= 50`
* `1 <= target <= 30`

---

## 2. **Diagram (Backtracking Tree + Duplicate Handling)**

Example: `candidates = [1,1,2], target = 3`

```text
Sorted: [1,1,2]

Start: []
 ├── pick 1 (index 0) → [1]
 │    ├── pick 1 (index 1) → [1,1]
 │    │    ├── pick 2 → ❌ (sum > 3)
 │    ├── pick 2 → [1,2] ✅
 │
 ├── skip duplicate 1 (index 1) 🚫
 ├── pick 2 → [2]
```

👉 Key idea:

* **Sort first**
* Skip duplicates using:

  ```python
  if i > start and candidates[i] == candidates[i-1]:
      continue
  ```

---

## 3. **Example I/O**

### ✅ Example 1

```text
Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: [[1,1,6], [1,2,5], [1,7], [2,6]]
```

✔ Explanation:

* Each number used once
* No duplicate combinations

---

### ⚠️ Edge Case

```text
Input: candidates = [1,1,1,1], target = 2
Output: [[1,1]]
```

✔ Explanation:

* Only one unique combination despite many duplicates

---

## 4. **Intuition & Pattern Recognition**

### 🔑 Signals:

* "Unique combinations" + duplicates in input → **skip duplicates**
* "Use once" → move to `i + 1`
* "All combinations" → backtracking

### 🧠 Interview Thought:

> “This is Combination Sum I + duplicate handling + no reuse. So I must sort and skip duplicates at the same recursion level.”

---

## 5. **Simpler Version**

### 🔹 Step 1:

👉 **Combination Sum**

* Reuse allowed
* No duplicates

### 🔹 Step 2:

👉 **Subsets II**

* Handle duplicates (skip logic)

### 🔹 Current Problem:

👉 **Combination Sum II**

### 🧠 Transition Thinking:

* Combination Sum → reuse → `dfs(i, ...)`
* Here → no reuse → `dfs(i+1, ...)`
* Subsets II → skip duplicates → same logic here

---

## 6. **Brute Force**

Generate all subsets and filter:

* Generate all subsets (2^n)
* Check sum
* Deduplicate results

### ⏱ Complexity:

* Time: **O(2^n * n)**
* Space: high (store duplicates)

---

## 7. **Optimal Solution (Backtracking + Sorting)**

```python
class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()  # 🔑 sort to handle duplicates
        res = []
        
        def dfs(start, curr, total):
            # ✅ valid combination
            if total == target:
                res.append(curr.copy())
                return
            
            for i in range(start, len(candidates)):
                # 🚫 skip duplicates at same level
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                
                # ❌ pruning
                if total + candidates[i] > target:
                    break
                
                # 🔹 choose
                curr.append(candidates[i])
                
                # 🔹 move forward (no reuse)
                dfs(i + 1, curr, total + candidates[i])
                
                # 🔙 backtrack
                curr.pop()
        
        dfs(0, [], 0)
        return res
```

### ⏱ Complexity:

* Time: **O(2^n)** (pruned)
* Space: **O(n)** recursion

---

## 8. **Step-by-Step Trace**

Input: `[1,1,2], target = 3`

Sorted → `[1,1,2]`

| Step | start           | i | curr  | total | Action            |
| ---- | --------------- | - | ----- | ----- | ----------------- |
| 1    | 0               | 0 | []    | 0     | pick 1            |
| 2    | 1               | 1 | [1]   | 1     | pick 1            |
| 3    | 2               | 2 | [1,1] | 2     | pick 2 → ❌ (4)    |
| 4    | backtrack       |   |       |       |                   |
| 5    | 1               | 2 | [1]   | 1     | pick 2            |
| 6    | -               | - | [1,2] | 3     | ✅ add             |
| 7    | backtrack to [] |   |       |       |                   |
| 8    | 0               | 1 | []    | 0     | 🚫 skip duplicate |
| 9    | 0               | 2 | []    | 0     | pick 2            |

Final: `[[1,2]]`

---

## 9. **Related Problems (Pattern Build-Up)**

1. **Subsets II**
   → Learn duplicate skipping pattern

2. **Combination Sum**
   → Same base, but reuse allowed

3. **Permutations II**
   → Duplicate handling in permutations

4. **Palindrome Partitioning**
   → Backtracking with constraints

5. **Restore IP Addresses**
   → Combination building + pruning

---

## 🔥 Final Interview Insight

### 💥 3 Rules You Must Remember:

1. **Sort first**
2. **Skip duplicates**

   ```python
   if i > start and candidates[i] == candidates[i-1]:
       continue
   ```
3. **No reuse**

   ```python
   dfs(i + 1, ...)
   ```

---

If you want, I can next:

* 🔥 Compare **Combination Sum I vs II vs III (super important)**
* 🔥 Or visualize duplicate skipping deeply (this is where most people fail)

