# SUBSET, POWER SET, PERMUTATION (Backtracking)

---

# 1. Pattern in One Minute

### Core Idea

Backtracking explores **all possible choices** by:

1. Make a choice
2. Recurse
3. Undo the choice (backtrack)

Think of it as walking every path of a decision tree.

### Why does this pattern exist?

Whenever a problem asks to generate **every valid combination, subset, arrangement, or partition**, brute force is unavoidable.

Backtracking simply makes brute force elegant.

### Think of this pattern when you see

* Generate all...
* Return every possible...
* Enumerate...
* Print all...
* Choose k items
* Arrange items
* Include / Exclude decisions

---

# 2. Recognition Signals

## Strongest Clues

### Keywords

* All subsets
* Power set
* Combinations
* Permutations
* Generate
* Enumerate
* Every possible answer
* Return all solutions

---

### Problem Characteristics

Usually n ≤ 15-20

Reason:

Output itself is exponential.

Examples:

* 2ⁿ subsets
* n! permutations

So exponential solution is expected.

---

### Common Disguises

Instead of saying

> Generate subsets

they may say

* Pick any team
* Select ingredients
* Investment portfolio
* Feature selection
* Include or skip

Instead of saying

> Permutations

they may say

* Arrange
* Ordering matters
* Seat people
* Different sequences

---

## Don't use Backtracking if

* Need only count answers (DP may help)
* Need shortest path (BFS)
* Need optimal answer (Greedy/DP)
* Only one answer required (Binary Search/Hash/etc.)

---

# 3. Mental Model

## A. SUBSET / POWER SET

Imagine every element has only **2 decisions**

```
Take it
Skip it
```

Decision tree

```
1

Take
Skip
```

Every level processes one element.

Leaf = one subset.

---

Mental Recall

* Index moves forward
* Every element has 2 options
* Never revisit previous index
* Order doesn't matter

---

## B. PERMUTATION

Different mental model.

Instead of Take/Skip,

At every position

```
Choose one unused element
```

Example

```
[]

Pick 1

[1]

Pick 2

[1,2]

Pick 3

[1,2,3]
```

Each level fills one position.

---

Mental Recall

* Maintain current path
* Maintain visited[]
* Pick unused element
* Backtrack

---

# 4. Boilerplate Templates

---

## A. SUBSET / POWER SET

```python
def subsets(nums):
    ans = []
    path = []

    def dfs(index):
        if index == len(nums):
            ans.append(path[:])
            return

        # Include
        path.append(nums[index])
        dfs(index + 1)

        # Backtrack
        path.pop()

        # Exclude
        dfs(index + 1)

    dfs(0)
    return ans
```

Complexity

```
Time : O(n * 2^n)

Space: O(n)
```

---

## Alternative (Loop Style)

Very common interview template.

```python
def subsets(nums):
    ans = []
    path = []

    def dfs(start):
        ans.append(path[:])

        for i in range(start, len(nums)):
            path.append(nums[i])
            dfs(i + 1)
            path.pop()

    dfs(0)
    return ans
```

Remember

```
dfs(i+1)

NOT dfs(start+1)
```

---

## B. PERMUTATION

```python
def permute(nums):
    ans = []
    path = []
    used = [False] * len(nums)

    def dfs():

        if len(path) == len(nums):
            ans.append(path[:])
            return

        for i in range(len(nums)):

            if used[i]:
                continue

            used[i] = True
            path.append(nums[i])

            dfs()

            path.pop()
            used[i] = False

    dfs()
    return ans
```

Complexity

```
Time : O(n × n!)

Space : O(n)
```

---

# 5. Variations

| Pattern             | Change                                |
| ------------------- | ------------------------------------- |
| Subsets             | Include / Exclude                     |
| Subsets II          | Skip duplicates after sorting         |
| Combination Sum     | Reuse current index                   |
| Combination Sum II  | Move to i+1                           |
| Combination of K    | Stop when path length == K            |
| Letter Combinations | Iterate characters instead of numbers |
| Permutations        | visited[]                             |
| Permutations II     | Skip duplicate branches               |
| N Queens            | Add validity checking                 |
| Sudoku              | Try digits 1-9                        |

---

# 6. Common Pitfalls

## 1. Forgetting Backtracking

Wrong

```python
path.append(x)

dfs()

# forgot pop
```

Always

```python
append

dfs

pop
```

---

## 2. Not copying answer

Wrong

```python
ans.append(path)
```

Correct

```python
ans.append(path[:])
```

---

## 3. Wrong recursion index

Subset

```
dfs(i+1)
```

Not

```
dfs(start+1)
```

---

## 4. Forgetting visited[] reset

Permutation

```
used[i]=True

dfs()

used[i]=False
```

Must undo.

---

## 5. Duplicate answers

If duplicates exist

```
sort first

skip duplicates
```

---

# 7. Interview Checklist

## SUBSET

✓ Need every subset

✓ Order doesn't matter

✓ Include/Exclude decisions

✓ Index always moves forward

→ Use Subset Backtracking

---

## PERMUTATION

✓ Need every arrangement

✓ Order matters

✓ Reuse impossible

✓ Need visited array

→ Use Permutation Backtracking

---

# 8. Must-Do Problems

## Easy

⭐ **Top 3**

* **LC 78 – Subsets**
* **LC 46 – Permutations**
* LC 77 – Combinations

---

## Medium

⭐ **Top 3**

* **LC 90 – Subsets II**
* **LC 39 – Combination Sum**
* **LC 40 – Combination Sum II**

Other important ones

* LC 47 – Permutations II
* LC 17 – Letter Combinations of a Phone Number
* LC 131 – Palindrome Partitioning
* LC 22 – Generate Parentheses

---

## Hard (Only Important)

* LC 51 – N Queens
* LC 37 – Sudoku Solver

---

# 9. 30-Second Cheat Sheet

| Pattern                | Recognition                           | Template                         | Complexity  |
| ---------------------- | ------------------------------------- | -------------------------------- | ----------- |
| **Subset / Power Set** | Include/Exclude, order doesn't matter | `dfs(index)` → include → exclude | **O(n·2ⁿ)** |
| **Permutation**        | Order matters, arrange everything     | `visited[] + path`               | **O(n·n!)** |

### Core Ideas

* **Subset:** Every element has **2 choices** → take or skip.
* **Permutation:** Every position chooses **one unused element**.

### Reusable Templates

* **Subset:** `append → dfs(i+1) → pop`
* **Permutation:** `used[i]=True → append → dfs() → pop → used[i]=False`

### Common Variations

* **Subsets II:** Sort + skip duplicates.
* **Combination Sum:** Reuse current index.
* **Combination Sum II:** Move to next index.
* **Permutations II:** Sort + skip duplicate branches.

### Pitfalls

* ❌ Forgetting `path.pop()`
* ❌ `ans.append(path)` instead of `path[:]`
* ❌ Wrong recursion index (`i+1` vs `start+1`)
* ❌ Not resetting `used[i]`
* ❌ Not handling duplicates after sorting

### Memory Trick

* **Subset = Binary Decision Tree** (Take / Skip)
* **Permutation = Fill Positions** (Choose an unused element at each level)
