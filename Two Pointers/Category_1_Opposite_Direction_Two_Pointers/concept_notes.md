# Opposite Direction Two Pointers

## 1. Pattern in One Minute

**Core idea:** Put one pointer at each end of an array/string and move them **toward each other**, using the current pair to decide which pointer should move.

```text
L → [ ... ... ... ... ] ← R
```

Think of this pattern when:

* The input is **sorted**, and you need a pair satisfying some condition.
* You compare **symmetric elements** from both ends.
* You need to optimize something using a pair `(left, right)`.
* Moving one side can **monotonically improve** the current condition.

The key question is:

> **Given the current pair, can I prove which endpoint cannot be part of a better/valid answer?**

If yes, you can discard that endpoint → two pointers.

---

## 2. Recognition Signals

### Strong signals

**Sorted array + pair condition**

```text
Find two numbers whose sum = target
Find closest pair
Find pair with sum < / > target
```

Because:

```text
sum too small → increase left
sum too large → decrease right
```

**Symmetry**

```text
palindrome
reverse array/string
compare outer characters
```

**Pair optimization from two ends**

Classic example: **Container With Most Water**.

```text
area = (right - left) * min(height[left], height[right])
```

The shorter wall is the bottleneck, so move it.

### Common disguises

The problem may never say "two pointers."

Instead:

> Find pair in sorted array
> Check palindrome ignoring characters
> Maximize area between two positions
> Find closest sum to target

### When NOT to use it

Don't force opposite pointers when:

* The array is unsorted and sorting destroys required information.
* Pointer movement has no monotonic justification.
* You're dealing with a **contiguous window** → sliding window may fit better.
* Both pointers naturally move forward → same-direction two pointers.

---

# 3. Mental Model

Remember:

> **Start wide → inspect → discard one side → repeat.**

```text
[ 1, 2, 4, 7, 9, 12 ]
  L                 R

        evaluate(L, R)

too large?
  L             R ←

too small?
      L →         R
```

The important intuition:

1. `left = 0`, `right = n - 1`.
2. Consider the pair `(left, right)`.
3. Use ordering/structure to understand what the pair tells you.
4. If condition is satisfied → process/return it.
5. Otherwise determine which endpoint is no longer useful.
6. Move **only the pointer you can logically eliminate**.
7. Search space shrinks every iteration.
8. Each pointer moves at most `n` positions.
9. Therefore traversal is usually **O(n)**.

### Mnemonic

**Evaluate → Eliminate → Move**

The pointer movement is not arbitrary. You're eliminating candidates.

---

# 4. Boilerplate Template

### Generic

```python
def two_pointers(arr):
    left, right = 0, len(arr) - 1

    while left < right:
        # Evaluate arr[left] and arr[right]

        if condition_met(arr[left], arr[right]):
            # process answer
            pass

        if should_move_left(arr[left], arr[right]):
            left += 1
        else:
            right -= 1
```

### Most important version: sorted Two Sum

```python
def two_sum(nums, target):
    left, right = 0, len(nums) - 1

    while left < right:
        total = nums[left] + nums[right]

        if total == target:
            return [left, right]

        if total < target:
            left += 1      # need larger sum
        else:
            right -= 1     # need smaller sum

    return [-1, -1]
```

Why this works:

```text
nums[L] + nums[R] < target

Since sorted:

moving R left → sum gets even smaller ❌
moving L right → sum can increase      ✓
```

That's the essence of the pattern.

---

# 5. Variations

| Variation                     | Pointer rule                                         |
| ----------------------------- | ---------------------------------------------------- |
| **Two Sum sorted**            | Sum small → `L++`; sum large → `R--`                 |
| **Palindrome**                | Match → both inward; mismatch → fail                 |
| **Valid Palindrome II**       | On mismatch, try skipping `L` or `R`                 |
| **Container With Most Water** | Move the **shorter height**                          |
| **3Sum**                      | Fix one index + opposite pointers on remaining range |
| **Closest Sum**               | Move based on whether sum is below/above target      |
| **Pair inequality**           | Move pointer according to monotonic condition        |

A major interview connection:

```text
Opposite Two Pointers
        ↓
      2Sum
        ↓
Fix one element + 2Sum
        ↓
      3Sum
        ↓
Fix two elements + 2Sum
        ↓
      4Sum
```

---

# 6. Common Pitfalls

### 1. Using two pointers without sorted/monotonic structure

For:

```text
nums = [8, 2, 10, 3]
target = 5
```

You cannot use:

```python
if total < target:
    left += 1
```

unless ordering gives that movement meaning.

---

### 2. Wrong loop condition

Pair problems usually:

```python
while left < right:
```

not:

```python
while left <= right:
```

You generally cannot pair an element with itself.

---

### 3. Moving the wrong pointer

Don't memorize:

```text
small → left
large → right
```

Memorize the reasoning:

> Which movement can bring me closer to the condition?

---

### 4. Container Water: moving taller wall

Suppose:

```text
height[L] = 3
height[R] = 10
```

Area is limited by `3`.

Moving `R` reduces width while the `3` bottleneck remains.

So:

```python
left += 1
```

Move the **shorter wall**.

---

### 5. Forgetting duplicate handling

For problems like **3Sum**:

```python
while left < right and nums[left] == nums[left - 1]:
    left += 1
```

Duplicate skipping is often essential.

---

# 7. Interview Checklist

✓ Do I care about **pairs of elements**?

✓ Is the array already **sorted**, or can I sort it?

✓ Does the problem compare elements from **both ends**?

✓ Can I determine from `(L, R)` that one endpoint is useless?

✓ Does moving a pointer monotonically change the relevant value?

✓ Can this replace an **O(n²)** pair search with **O(n)** traversal?

If several are true:

> **Think Opposite Direction Two Pointers.**

---

# 8. Must-Do Problems

### Easy

⭐ **Top 3 — Valid Palindrome (LC 125)**
Pure opposite-pointer mechanics.

⭐ **Top 3 — Two Sum II: Input Array Is Sorted (LC 167)**
The canonical sorted pair problem.

**Reverse String (LC 344)**
Simplest symmetric two-pointer traversal.

### Medium

⭐ **Top 3 — Container With Most Water (LC 11)**
Most important problem for learning **why moving one pointer is safe**.

**3Sum (LC 15)**
Sort + fix one element + opposite pointers.

**Valid Palindrome II (LC 680)**
Two pointers + branching at mismatch.

**Boats to Save People (LC 881)**
Greedy + opposite pointers.

**3Sum Closest (LC 16)**
Target-based pointer movement.

### Hard

**Trapping Rain Water (LC 42)**

Important, but it's a more advanced two-pointer invariant. Revise it separately after the core pattern.

### Revision Top 3

**LC 167 → LC 125 → LC 11**

Together they cover the three major forms:

```text
Sorted Pair       → Two Sum II
Symmetric Compare → Valid Palindrome
Greedy Optimize   → Container With Most Water
```

---

# 9. 30-Second Cheat Sheet

```text
OPPOSITE DIRECTION TWO POINTERS

Recognition:
• Sorted array + pair condition
• Compare opposite ends
• Pair optimization
• Palindrome/symmetry
• One endpoint can be safely discarded

Core:
L = 0
R = n - 1

while L < R:
    evaluate(L, R)

    move L and/or R based on condition

Mental Model:
Evaluate → Eliminate → Move

Sorted sum:
sum < target → L++
sum > target → R--

Palindrome:
equal    → L++, R--
mismatch → fail / handle exception

Container:
move shorter wall

Complexity:
Traversal: O(n)
Space: O(1)

But:
sorting first → O(n log n)

Key invariant:
Never move a pointer unless you can explain
why the discarded endpoint cannot help.

Top 3:
LC 167 Two Sum II
LC 125 Valid Palindrome
LC 11  Container With Most Water
```

**Best recall question during an interview:**

> “From this pair, can I prove that moving one endpoint cannot make me miss the answer?”

If the answer is yes, opposite-direction two pointers should be high on your pattern shortlist.
