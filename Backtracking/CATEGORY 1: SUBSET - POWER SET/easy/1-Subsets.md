
## **🔹 Subsets (LeetCode 78) — Backtracking Pattern**

---

### **1. Problem Statement with Example**

Given an integer array `nums` of **unique elements**, return **all possible subsets (the power set)**.

* A subset can be empty or full.
* No duplicate subsets allowed.

#### Example:

```
Input: nums = [1,2,3]
Output:
[
  [], 
  [1], 
  [2], 
  [3], 
  [1,2], 
  [1,3], 
  [2,3], 
  [1,2,3]
]
```

#### Constraints:

* `1 <= nums.length <= 10`
* Elements are unique

---

### **2. Diagram (Decision Tree Visualization)**

Each element → **2 choices: include OR exclude**

```
                 []
          /              \
       [1]                []
     /     \           /     \
 [1,2]    [1]       [2]      []
  /  \    /  \      /  \     /  \
[1,2,3] [1,2] [1,3] [1] [2,3] [2] [3] []
```

👉 Depth = index
👉 At each level → choose or skip

---

### **3. Example I/O**

#### Example 1 (Typical)

```
Input: [1,2]
Output: [[], [1], [2], [1,2]]
```

Explanation:

* Pick none → []
* Pick 1 → [1]
* Pick 2 → [2]
* Pick both → [1,2]

---

#### Example 2 (Edge Case)

```
Input: [1]
Output: [[], [1]]
```

Explanation:
Only two choices → include or exclude

---

### **4. Intuition & Pattern Recognition**

💡 **Signals for Backtracking:**

* “Return ALL possible combinations”
* “Subsets / Power set”
* Each element has a binary decision

👉 Think:

> “For every number, I can either take it or skip it”

This naturally forms a **binary tree (DFS)**.

---

### **5. Simpler Version**

#### 🔹 Simplest problem:

**Subsets of [1,2]**

* Just manually try all combinations

#### 🔹 Related simpler LeetCode:

* Subsets (this itself is base)
* Combinations
  → fixed size subsets
* Permutations
  → order matters
* Subsets II
  → duplicates handling

#### 🧠 Thinking progression:

```
Start → generate all subsets manually
→ realize binary decision
→ implement using recursion
→ optimize using backtracking
```

---

### **6. Brute Force**

Generate all subsets using bit masking:

```python
def subsets(nums):
    n = len(nums)
    res = []

    for mask in range(1 << n):  # 2^n subsets
        subset = []
        for i in range(n):
            if mask & (1 << i):
                subset.append(nums[i])
        res.append(subset)

    return res
```

⏱ Time: `O(n * 2^n)`
📦 Space: `O(1)` (excluding output)

---

### **7. Optimal Solution (Backtracking)**

```python
class Solution:
    def subsets(self, nums):
        res = []
        subset = []

        def dfs(i):
            # Base case: reached end
            if i == len(nums):
                res.append(subset.copy())  # store current subset
                return

            # INCLUDE nums[i]
            subset.append(nums[i])
            dfs(i + 1)

            # BACKTRACK (remove last element)
            subset.pop()

            # EXCLUDE nums[i]
            dfs(i + 1)

        dfs(0)
        return res
```

⏱ Time: `O(n * 2^n)`
📦 Space: `O(n)` recursion stack

---

### **8. Step-by-Step Trace**

Input: `[1,2]`

| Step | i | subset | Action    |
| ---- | - | ------ | --------- |
| 1    | 0 | []     | start     |
| 2    | 0 | [1]    | include 1 |
| 3    | 1 | [1,2]  | include 2 |
| 4    | 2 | [1,2]  | save      |
| 5    | 1 | [1]    | backtrack |
| 6    | 2 | [1]    | save      |
| 7    | 0 | []     | backtrack |
| 8    | 1 | [2]    | include 2 |
| 9    | 2 | [2]    | save      |
| 10   | 1 | []     | backtrack |
| 11   | 2 | []     | save      |

Output:

```
[ [1,2], [1], [2], [] ]
```

---

### **9. Related Problems (Pattern Building)**

1. Subsets II
   → Same but handle duplicates (skip duplicates)

2. Combinations
   → Choose k elements → add constraint

3. Combination Sum
   → unlimited reuse → adds looping

4. Permutations
   → order matters → use visited array

5. Generate Parentheses
   → backtracking with constraints

---

## 🔥 Interview Shortcut

If you see:

* “all subsets”
* “power set”
* “each element pick/not pick”

👉 Immediately think:

```
Backtracking + binary choice
```

---

If you want, I can also show:

* iterative subset generation (very important trick)
* how to convert this template into Combination Sum / Subsets II quickly 🚀
