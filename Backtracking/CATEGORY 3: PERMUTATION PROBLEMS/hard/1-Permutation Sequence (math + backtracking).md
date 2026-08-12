## 🧠 **Permutation Sequence — Math + Backtracking (Optimized with Factorial Number System)**

---

## 1. **Problem Statement**

Given two integers `n` and `k`, return the **k-th permutation sequence** of numbers `[1, 2, ..., n]` in **lexicographic order**.

---

### ⚠️ Constraints

* `1 <= n <= 9`
* `1 <= k <= n!`

---

## 2. **Diagram (Lexicographic Ordering)**

Example: `n = 3`

```text
All permutations (sorted):

1. 123
2. 132
3. 213
4. 231
5. 312
6. 321
```

👉 If `k = 4` → answer = `"231"`

---

## 3. **Example I/O**

### ✅ Example 1

```text
Input: n = 3, k = 4
Output: "231"
```

✔ Explanation:

* 4th permutation in sorted order

---

### ⚠️ Edge Case

```text
Input: n = 1, k = 1
Output: "1"
```

✔ Only one permutation

---

## 4. **Intuition & Pattern Recognition**

### 🔑 Signals:

* "k-th permutation" → not asking to generate all
* `n <= 9` → factorial fits
* Lexicographic ordering → **factorial blocks**

---

### 🧠 Interview Thought:

> “Each digit position fixes blocks of size `(n-1)!`. I can directly jump to the correct block instead of generating all permutations.”

---

## 5. **Simpler Version**

### 🔹 Step 1:

👉 **Permutations**

* Generate all permutations

### 🔹 Step 2:

* Sort and pick k-th → inefficient

### 🔹 Step 3 (Optimal):

* Use factorial math to directly compute

---

### 🧠 Transition Thinking:

* Instead of generating → **index into permutations**

---

## 6. **Brute Force**

* Generate all permutations
* Sort
* Return k-th

### ⏱ Complexity:

* Time: **O(n! * n)**
* Space: **O(n!)**

---

## 7. **Optimal Solution (Factorial Math)**

---

### 🔥 Core Idea (Block Size)

Each position splits permutations into blocks of size:

(n-1)!

---

### 🧮 Logic:

* Convert `k → k-1` (0-based index)
* Maintain list of numbers `[1..n]`
* At each step:

  * Pick index = `k // fact`
  * Remove that number
  * Update `k = k % fact`

---

### ✅ Code

```python
class Solution:
    def getPermutation(self, n, k):
        from math import factorial
        
        nums = [str(i) for i in range(1, n+1)]
        k -= 1  # 🔑 convert to 0-based
        
        res = []
        
        for i in range(n, 0, -1):
            fact = factorial(i - 1)
            
            index = k // fact  # which block
            
            res.append(nums[index])
            nums.pop(index)  # remove used number
            
            k %= fact  # move to next block
        
        return "".join(res)
```

---

### ⏱ Complexity:

* Time: **O(n²)** (list pop cost)
* Space: **O(n)**

---

## 8. **Step-by-Step Trace**

Input: `n=4, k=9`

### Step 0:

```
nums = [1,2,3,4]
k = 8 (0-based)
```

---

### Iteration 1:

* fact = 3! = 6
* index = 8 // 6 = 1
* pick → 2

```
res = [2]
nums = [1,3,4]
k = 8 % 6 = 2
```

---

### Iteration 2:

* fact = 2! = 2
* index = 2 // 2 = 1
* pick → 3

```
res = [2,3]
nums = [1,4]
k = 2 % 2 = 0
```

---

### Iteration 3:

* fact = 1! = 1
* index = 0 // 1 = 0
* pick → 1

```
res = [2,3,1]
nums = [4]
```

---

### Iteration 4:

* pick → 4

```
Final = "2314"
```

---

## 9. **Related Problems (Pattern Build-Up)**

1. **Permutations**
   → Generate all permutations

2. **Permutations II**
   → Handle duplicates

3. **Next Permutation**
   → Next lexicographic permutation

4. **Kth Smallest in Lexicographical Order**
   → Tree-based lexicographic traversal

5. **Combinations**
   → Choosing subsets

---

## 🔥 Final Interview Insight

### 💥 Core Idea:

> “Each position reduces the problem size using factorial blocks.”

---

### 💥 Golden Formula:

* Block size = `(n-1)!`
* Index = `k // fact`

---

### 💥 One-line intuition:

> “Jump directly to the k-th permutation without generating all.”

---

If you want next:

* 🔥 I can show **how to derive this formula from scratch (important for interviews)**
* 🔥 Or compare **math vs backtracking approach trade-offs**
