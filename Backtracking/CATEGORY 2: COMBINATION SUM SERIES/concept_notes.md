# Combination & Combination Sum — Backtracking

The key distinction:

> **Combination = choose elements without caring about order.**
> **Combination Sum = choose elements to satisfy a target, often with repetition.**

---

## 1. Pattern in One Minute

### Combination

Use when the problem asks:

> “Choose **k elements** from `n` elements, and `[1,2]` is the same as `[2,1]`.”

Core technique:

```text
At each position:
    choose current element
    recurse
    undo choice
    move forward
```

Example: `n=4, k=2`

```text
[1,2], [1,3], [1,4], [2,3], [2,4], [3,4]
```

Notice: **no `[2,1]`**.

### Combination Sum

Use when:

> “Find combinations whose sum equals target.”

The major question is:

**Can I reuse the same element?**

That determines the recursive next index.

```text
Can reuse:
    dfs(i, remaining)

Cannot reuse:
    dfs(i + 1, remaining)
```

---

# 2. Recognition Signals

### Strong signals

Think **Combination / Backtracking** when you see:

* "choose `k` elements"
* "select `k` numbers"
* "all possible combinations"
* "combinations that sum to target"
* "find all subsets of size `k`"
* Order doesn't matter
* Need to enumerate **all valid selections**
* Small/moderate `n`
* Output itself can be exponential

### Combination vs Permutation

| Problem says                      | Pattern                  |
| --------------------------------- | ------------------------ |
| `[1,2]` and `[2,1]` are same      | **Combination**          |
| `[1,2]` and `[2,1]` are different | **Permutation**          |
| Choose exactly `k`                | Combination              |
| Sum must equal target             | Combination Sum          |
| Can reuse numbers                 | Combination Sum I-style  |
| Each number used once             | Combination Sum II-style |

### Don't use it when

* You only need the **count**, and DP/memoization can avoid enumeration.
* `n` is huge and generating all combinations is impossible.
* Order matters → likely **Permutation**.
* The problem has overlapping subproblems → consider **DP**.

---

# 3. Mental Model

The most important mental model:

```text
                 []
          /       |       \
        [1]      [2]      [3]
       /   \       \
    [1,2] [1,3]   [2,3]
```

### Rules to remember

1. **Start index controls ordering.**
2. `for i in range(start, n)` explores choices.
3. Choosing `nums[i]` means:

   ```python
   path.append(nums[i])
   ```
4. Then recursively explore the remaining choices.
5. Undo:

   ```python
   path.pop()
   ```
6. To prevent permutations, **never go backwards** in the array.
7. `start = i + 1` → cannot reuse current element.
8. `start = i` → can reuse current element.
9. For target problems, `remaining` is usually easier than maintaining `total`.
10. When `remaining == 0`, you found a valid combination.

### The golden distinction

```text
Combination:
    start → i + 1

Combination Sum with reuse:
    start → i

Combination Sum without reuse:
    start → i + 1
```

---

# 4. Boilerplate Templates

## A. Combination — choose k from n

Classic: **LeetCode 77 — Combinations**

```python
def combine(n, k):
    ans = []

    def dfs(start, path):
        if len(path) == k:
            ans.append(path[:])
            return

        for i in range(start, n + 1):
            path.append(i)
            dfs(i + 1, path)   # cannot reuse
            path.pop()

    dfs(1, [])
    return ans
```

### Complexity

Number of combinations:

[
O\left(\binom{n}{k}\right)
]

Ignoring output-copy cost.

---

## B. Combination Sum — reuse allowed

Classic: **LeetCode 39**

```python
def combinationSum(candidates, target):
    ans = []

    def dfs(start, remaining, path):
        if remaining == 0:
            ans.append(path[:])
            return

        if remaining < 0:
            return

        for i in range(start, len(candidates)):
            path.append(candidates[i])

            dfs(i, remaining - candidates[i], path)
            #   ^
            # same i → can reuse

            path.pop()

    dfs(0, target, [])
    return ans
```

The **one line to remember**:

```python
dfs(i, ...)
```

means **reuse allowed**.

---

## C. Combination Sum — each element once

Classic: **LeetCode 40 — Combination Sum II**

```python
def combinationSum2(candidates, target):
    candidates.sort()
    ans = []

    def dfs(start, remaining, path):
        if remaining == 0:
            ans.append(path[:])
            return

        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]:
                continue

            if candidates[i] > remaining:
                break

            path.append(candidates[i])
            dfs(i + 1, remaining - candidates[i], path)
            path.pop()

    dfs(0, target, [])
    return ans
```

There are **two important tricks**:

```python
candidates.sort()
```

and

```python
if i > start and candidates[i] == candidates[i - 1]:
    continue
```

This removes duplicate combinations.

---

# 5. Variations

### 1. Combination — fixed size

```text
choose k from n
```

Use:

```python
dfs(i + 1)
```

→ LeetCode **77**

---

### 2. Combination Sum — unlimited reuse

```text
target + reuse allowed
```

Use:

```python
dfs(i, ...)
```

→ LeetCode **39**

---

### 3. Combination Sum II — each element once

Use:

```python
dfs(i + 1, ...)
```

plus duplicate skipping.

→ LeetCode **40**

---

### 4. Combination Sum III

Choose exactly `k` numbers from `1..9` whose sum is `n`.

State becomes:

```python
dfs(start, remaining, path)
```

with termination:

```python
if len(path) == k:
    if remaining == 0:
        ans.append(path[:])
    return
```

→ LeetCode **216**

---

### 5. Combination Sum IV

⚠️ **Important distinction.**

Here **order matters**.

```text
[1,2] != [2,1]
```

So this is **not ordinary combination backtracking**.

It is primarily a **DP** problem.

→ LeetCode **377**

---

# 6. Common Pitfalls

### ❌ Pitfall 1: Using `dfs(i + 1)` when reuse is allowed

For Combination Sum:

```python
dfs(i, remaining - nums[i])
```

not:

```python
dfs(i + 1, ...)
```

---

### ❌ Pitfall 2: Generating permutations accidentally

Bad:

```python
for i in range(len(nums)):
```

with no `start`.

You'll generate:

```text
[1,2]
[2,1]
```

For combinations, always maintain:

```python
start
```

---

### ❌ Pitfall 3: Forgetting duplicate handling

For Combination Sum II:

```python
if i > start and nums[i] == nums[i-1]:
    continue
```

Notice:

```text
i > start
```

NOT simply:

```python
if nums[i] == nums[i-1]
```

Because duplicates may still be legitimately used at different recursion depths.

---

### ❌ Pitfall 4: Forgetting `path.pop()`

Every:

```python
path.append(x)
```

must eventually have:

```python
path.pop()
```

Think:

> **Choose → Explore → Undo**

---

### ❌ Pitfall 5: Confusing duplicate values with duplicate usage

Example:

```text
[1,1,2]
```

The two `1`s are separate elements.

Combination Sum II allows each element once, but shouldn't produce duplicate **result combinations**.

That's why sorting + same-level skipping is used.

---

# 7. Interview Checklist

When you see:

✓ **"Choose k elements"**
→ Combination

✓ **"Find all combinations"**
→ Backtracking

✓ **"Sum equals target"**
→ Combination Sum

✓ **"Can reuse elements"**
→ `dfs(i, ...)`

✓ **"Use each element at most once"**
→ `dfs(i + 1, ...)`

✓ **"Duplicates in input"**
→ Sort + skip duplicates at the **same recursion level**

✓ **Order matters**
→ Don't use combination pattern; consider **Permutation / DP**

---

# 8. Must-Do Problems

### 🟢 Easy

**1. LeetCode 216 — Combination Sum III** ⭐ **Top 3**

Good for combining:

```text
fixed k + target + backtracking
```

---

### 🟡 Medium

**2. LeetCode 77 — Combinations** ⭐ **Top 3**

The purest combination template.

**3. LeetCode 39 — Combination Sum** ⭐ **Top 3**

The most important one for understanding:

```text
dfs(i) vs dfs(i+1)
```

**4. LeetCode 40 — Combination Sum II**

Critical for:

```text
duplicates + each element once
```

**5. LeetCode 377 — Combination Sum IV**

Important because it tests whether you recognize that **order matters → DP**.

---

### 🔴 Hard

No hard problem is essential for learning this pattern itself. The medium problems above give much higher ROI.

---

# 9. 30-Second Cheat Sheet

```text
COMBINATION
────────────────────────────────

Recognition:
"choose", "select", "k elements",
"all combinations", order doesn't matter

Core:
Choose → Explore → Undo

Template:
for i in range(start, n):
    path.append(nums[i])
    dfs(i + 1, ...)
    path.pop()


COMBINATION SUM
────────────────────────────────

Target + reuse:
dfs(i, remaining - nums[i])

Target + no reuse:
dfs(i + 1, remaining - nums[i])

Duplicates:
sort()
if i > start and nums[i] == nums[i-1]:
    continue


KEY MEMORY TRICK
────────────────────────────────

i       → REUSE
i + 1   → DON'T REUSE

start   → prevents permutations
sort    → enables duplicate handling
pop     → undo choice
```

### The one pattern to burn into memory

```python
def dfs(start, remaining, path):

    if remaining == 0:
        ans.append(path[:])
        return

    for i in range(start, n):

        # choose
        path.append(nums[i])

        # explore
        dfs(
            i if REUSE_ALLOWED else i + 1,
            remaining - nums[i],
            path
        )

        # undo
        path.pop()
```

**Mnemonic:** **`start` = combination, `i` = reuse, `i+1` = no reuse.**
