## 🧠 **Factor Combinations (LeetCode Premium) — Backtracking Pattern**

---

## 1. **Problem Statement**

Given an integer `n`, return all **unique combinations of its factors** such that:

* Each combination contains **factors > 1**
* Factors multiply to `n`
* Order does not matter (e.g., `[2,6]` and `[6,2]` are the same → include only one)

### ⚠️ Constraints

* `1 <= n <= 10^7`

---

## 2. **Diagram (Factor Tree Exploration)**

Example: `n = 12`

```text
Start: []
 ├── pick 2 → [2], remaining = 6
 │    ├── pick 2 → [2,2], remaining = 3
 │    │    ├── pick 3 → [2,2,3] ✅
 │    ├── pick 3 → [2,3], remaining = 2 ❌ (invalid order avoided)
 │    ├── pick 6 → [2,6] ✅
 │
 ├── pick 3 → [3], remaining = 4
 │    ├── pick 4 → [3,4] ✅
 │
 ├── pick 4 → [4], remaining = 3 ❌
 ├── pick 6 → [6], remaining = 2 ❌
```

👉 Key idea:

* Always pick factors **≥ last chosen factor**
* This avoids duplicate permutations

---

## 3. **Example I/O**

### ✅ Example 1

```text
Input: n = 12
Output: [[2,6], [2,2,3], [3,4]]
```

✔ Explanation:

* All factor combinations (excluding `[12]`)

---

### ⚠️ Edge Case

```text
Input: n = 7
Output: []
```

✔ Explanation:

* Prime number → no valid factor combinations

---

## 4. **Intuition & Pattern Recognition**

### 🔑 Signals:

* "Find all combinations" → backtracking
* "Multiply to n" → think like **reverse combination sum**
* "Avoid duplicates" → enforce ordering (non-decreasing)

### 🧠 Interview Thought:

> “Instead of adding to target, I’m dividing n. Each recursive call reduces the remaining value. This is like combination sum but with multiplication.”

---

## 5. **Simpler Version**

### 🔹 Step 1:

👉 **Combination Sum**

* Add numbers to reach target

### 🔹 Step 2:

👉 Think:

* Instead of `target - num`
* Do → `n / factor`

### 🔹 Current Problem:

👉 Factor decomposition using backtracking

### 🧠 Transition Thinking:

* Addition → subtraction → `target - num`
* Multiplication → division → `n // factor`

---

## 6. **Brute Force**

* Try all combinations of numbers from `2 → n`
* Check if product == n

### ⏱ Complexity:

* Extremely large (exponential)

---

## 7. **Optimal Solution (Backtracking + Pruning)**

```python
class Solution:
    def getFactors(self, n):
        res = []
        
        def dfs(start, curr, remaining):
            # try factors from 'start' to sqrt(remaining)
            for i in range(start, int(remaining ** 0.5) + 1):
                if remaining % i == 0:
                    # found a factor pair
                    res.append(curr + [i, remaining // i])
                    
                    # explore further breakdown
                    dfs(i, curr + [i], remaining // i)
        
        dfs(2, [], n)
        return res
```

### 🔑 Key Points:

* Only iterate till `sqrt(n)` → avoids duplicates
* Always pass `i` as next start → maintain order
* Add `[i, remaining//i]` directly → valid combination

### ⏱ Complexity:

* Time: ~ **O(n log n)** (pruned heavily)
* Space: recursion depth

---

## 8. **Step-by-Step Trace**

Input: `n = 12`

| Step | start             | curr    | remaining | Action        |
| ---- | ----------------- | ------- | --------- | ------------- |
| 1    | 2                 | []      | 12        | start         |
| 2    | 2                 | []      | 12        | try 2 → valid |
| 3    | -                 | [2,6]   | -         | ✅ add         |
| 4    | 2                 | [2]     | 6         | recurse       |
| 5    | 2                 | [2]     | 6         | try 2         |
| 6    | -                 | [2,2,3] | -         | ✅ add         |
| 7    | 2                 | [2,2]   | 3         | recurse       |
| 8    | stop (no factors) |         |           |               |
| 9    | backtrack         |         |           |               |
| 10   | try 3 → valid     |         |           |               |
| 11   | [3,4] ✅           |         |           |               |

Final: `[[2,6], [2,2,3], [3,4]]`

---

## 9. **Related Problems (Pattern Build-Up)**

1. **Combination Sum**
   → Add to target (base pattern)

2. **Combination Sum II**
   → No reuse + duplicates

3. **Combination Sum III**
   → Fixed size constraint

4. **Subsets**
   → Core backtracking structure

5. **Expression Add Operators**
   → Build expressions to match target (advanced)

---

## 🔥 Final Interview Insight

### 💥 Think in reverse:

> Instead of building sum → reduce number via division

### 💥 Core Pattern:

```python
dfs(start, curr, remaining)
```

### 💥 Golden Rules:

* Only try factors up to `√remaining`
* Maintain order → avoid duplicates
* Add `[i, remaining//i]` directly

---

If you want next:

* 🔥 I can give a **unified backtracking template** for all problems you've asked (this will simplify everything)
* 🔥 Or a **visual mental model to never forget recursion trees again**
    