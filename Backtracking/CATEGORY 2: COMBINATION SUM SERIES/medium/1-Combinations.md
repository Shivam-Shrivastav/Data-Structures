## **🔹 Combinations (LeetCode 77) — Backtracking Pattern**

---

### **1. Problem Statement with Example**

Given two integers `n` and `k`, return **all possible combinations of k numbers chosen from [1 … n]**.

* Each combination has exactly `k` elements
* Order **does NOT matter**

---

#### Example:

```text
Input: n = 4, k = 2

Output:
[
 [1,2],
 [1,3],
 [1,4],
 [2,3],
 [2,4],
 [3,4]
]
```

#### Constraints:

* `1 <= n <= 20`
* `1 <= k <= n`

---

### **2. Diagram (Combination Tree)**

👉 Choose numbers in increasing order to avoid duplicates

```text
Start: []

            []
      /      |      |      \
    [1]     [2]    [3]     [4]
   / | \    /  \     \       
[1,2][1,3][1,4][2,3][2,4]  [3,4]
```

👉 Always move forward → no reuse of previous elements

---

### **3. Example I/O**

#### Example 1 (Typical)

```
Input: n = 3, k = 2
Output: [[1,2], [1,3], [2,3]]
```

---

#### Example 2 (Edge Case)

```
Input: n = 1, k = 1
Output: [[1]]
```

---

### **4. Intuition & Pattern Recognition**

💡 Signals:

* “choose k elements”
* “combinations”
* “order doesn’t matter”

👉 Think:

> “Pick k elements in increasing order”

---

### **5. Simpler Version**

#### 🔹 Start from:

* Subsets
  → choose any number of elements

#### 🔹 Add constraint:

* Only keep subsets of size `k`

---

### 🧠 Transition Thinking

```text
Subsets:
    take or skip → any size

Combinations:
    take only k elements
```

---

### **6. Brute Force**

Generate all subsets and filter size `k`

```python
def combine(n, k):
    res = []

    def dfs(i, subset):
        if i > n:
            if len(subset) == k:
                res.append(subset.copy())
            return

        # include
        subset.append(i)
        dfs(i + 1, subset)

        # exclude
        subset.pop()
        dfs(i + 1, subset)

    dfs(1, [])
    return res
```

⏱ Time: `O(2^n)`
📦 Space: `O(n)`

---

### **7. Optimal Solution (Backtracking)**

👉 Avoid unnecessary branches by:

* Only picking next elements
* Stop when size = k

```python
class Solution:
    def combine(self, n, k):
        res = []
        comb = []

        def dfs(start):
            # base case
            if len(comb) == k:
                res.append(comb.copy())
                return

            for num in range(start, n + 1):
                # choose
                comb.append(num)

                dfs(num + 1)

                # backtrack
                comb.pop()

        dfs(1)
        return res
```

---

### **🔥 Pruning Optimization (Important)**

👉 If remaining elements < needed → stop early

```python
for num in range(start, n - (k - len(comb)) + 2):
```

---

⏱ Time: `O(C(n, k))`
📦 Space: `O(k)`

---

### **8. Step-by-Step Trace**

Input: `n = 4, k = 2`

| Step | comb  | start | Action        |
| ---- | ----- | ----- | ------------- |
| 1    | []    | 1     | start         |
| 2    | [1]   | 2     | pick 1        |
| 3    | [1,2] | 3     | pick 2 → save |
| 4    | [1]   | 2     | backtrack     |
| 5    | [1,3] | 4     | pick 3 → save |
| 6    | [1,4] | 5     | save          |
| 7    | []    | 1     | backtrack     |
| 8    | [2]   | 3     | pick 2        |
| 9    | [2,3] | 4     | save          |

---

### **9. Related Problems (Pattern Building)**

1. Subsets
   → base pattern

2. Combination Sum
   → combinations with sum constraint

3. Combination Sum II
   → duplicates + combinations

4. Subsets II
   → duplicates handling

---

## 🔥 Interview Shortcut

### Core Template:

```python
for num in range(start, n+1):
    choose
    dfs(num+1)
    backtrack
```

---

## ⚡ Key Insight

```text
Subsets → any size
Combinations → fixed size k
```

---

## 🧠 Mental Model

```text
Subsets:
    include/exclude

Combinations:
    controlled inclusion (size k)
```

---

If you want:
I can show you **how ALL backtracking problems reduce to 3 templates (Subsets, Permutations, Combinations)** — super powerful for interviews 🚀
