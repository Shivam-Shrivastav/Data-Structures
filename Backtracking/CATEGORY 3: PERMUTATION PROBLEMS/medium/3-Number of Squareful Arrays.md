## 🧠 **Number of Squareful Arrays — Backtracking + Permutations + Graph**

---

## 1. **Problem Statement**

Given an integer array `nums`, return the number of **permutations** such that:

* The array is rearranged into a permutation
* For every adjacent pair `(a, b)`:
  [
  a + b \text{ is a perfect square}
  ]

---

### ⚠️ Constraints

* `1 <= nums.length <= 12`
* `0 <= nums[i] <= 10^9`
* Duplicates may exist

---

## 2. **Diagram (Graph + Permutation View)**

Example: `nums = [1,17,8]`

```text
Check edges (perfect square sum):

1 + 8 = 9 ✅
8 + 17 = 25 ✅
1 + 17 = 18 ❌

Graph:
1 ↔ 8 ↔ 17

Valid permutations:
[1,8,17]
[17,8,1]
```

👉 Think of it as:

* Build a **graph**
* Nodes = numbers
* Edge if sum is perfect square
* Count **valid paths covering all nodes**

---

## 3. **Example I/O**

### ✅ Example 1

```text
Input: nums = [1,17,8]
Output: 2
```

✔ Valid permutations:

* `[1,8,17]`
* `[17,8,1]`

---

### ⚠️ Edge Case

```text
Input: nums = [2,2,2]
Output: 1
```

✔ Explanation:

* Only one unique permutation
* 2+2=4 (perfect square)

---

## 4. **Intuition & Pattern Recognition**

### 🔑 Signals:

* "Count permutations" → backtracking with visited
* "Condition on adjacent pairs" → graph constraint
* "Duplicates present" → skip duplicates

### 🧠 Interview Thought:

> “This is permutation with constraints. I should build valid transitions (graph) and then DFS while avoiding duplicates.”

---

## 5. **Simpler Version**

### 🔹 Step 1:

👉 **Permutations**

* Generate all permutations

### 🔹 Step 2:

👉 Add condition:

* Only allow transitions where sum is perfect square

### 🔹 Step 3:

👉 Handle duplicates:
👉 **Permutations II**

---

### 🧠 Transition Thinking:

* Permutations → all arrangements
* Add constraint → restrict adjacency
* Add duplicates → skip repeated choices

---

## 6. **Brute Force**

* Generate all permutations (n!)
* Check each for square condition

### ⏱ Complexity:

* Time: **O(n! * n)**
* Too slow for n=12

---

## 7. **Optimal Solution (Backtracking + Graph + Duplicate Handling)**

```python
class Solution:
    def numSquarefulPerms(self, nums):
        from math import isqrt
        from collections import Counter
        
        def is_square(x):
            r = isqrt(x)
            return r * r == x
        
        count = Counter(nums)
        
        # 🔹 build graph
        graph = {x: [] for x in count}
        for x in count:
            for y in count:
                if is_square(x + y):
                    graph[x].append(y)
        
        def dfs(x, remaining):
            # remaining elements to place
            if remaining == 0:
                return 1
            
            total = 0
            
            for nei in graph[x]:
                if count[nei] > 0:
                    count[nei] -= 1
                    total += dfs(nei, remaining - 1)
                    count[nei] += 1
            
            return total
        
        res = 0
        
        for x in count:
            count[x] -= 1
            res += dfs(x, len(nums) - 1)
            count[x] += 1
        
        return res
```

---

### 🔑 Key Points:

* Use **Counter** → handle duplicates
* Build **graph of valid transitions**
* DFS over graph → count valid permutations

---

### ⏱ Complexity:

* Time: **O(n! / duplicates!)** (pruned)
* Space: **O(n)** recursion

---

## 8. **Step-by-Step Trace**

Input: `[1,17,8]`

### Graph:

```
1 → [8]
8 → [1,17]
17 → [8]
```

### DFS:

| Step | curr          | remaining | Action    |
| ---- | ------------- | --------- | --------- |
| 1    | 1             | 2         | start     |
| 2    | 8             | 1         | valid     |
| 3    | 17            | 0         | ✅ count++ |
| 4    | start from 17 |           |           |
| 5    | 8             | 1         |           |
| 6    | 1             | 0         | ✅ count++ |

Final: `2`

---

## 9. **Related Problems (Pattern Build-Up)**

1. **Permutations**
   → Base permutation generation

2. **Permutations II**
   → Handle duplicates

3. **Matchsticks to Square**
   → Partition with constraints

4. **Word Ladder**
   → Graph transitions between states

5. **N-Queens**
   → Backtracking with constraints

---

## 🔥 Final Interview Insight

### 💥 Think of it as:

> “Permutation + Graph constraint + duplicate handling”

---

### 💥 Core Flow:

```python
Build graph → DFS with count map
```

---

### 💥 Golden Rules:

* Precompute valid edges (huge optimization)
* Use **Counter instead of visited array**
* Avoid duplicate permutations via frequency tracking

---

### 🧠 One-line intuition:

> “Only permute along valid square-sum edges.”

---

If you want next:

* 🔥 I can show **why graph approach is MUCH faster than naive permutations**
* 🔥 Or give **a master template for all permutation + constraint problems**
