# Same-Direction Two Pointers

## 1. Pattern in One Minute

**Core idea:** Maintain two pointers that move **forward through the data**, but give them different jobs.

Usually:

* `read` / `right` → scans every element.
* `write` / `left` → marks where the next valid element belongs.

```text
Input: [1, 1, 2, 2, 3]

        w
        r →

read  = explore
write = build valid prefix
```

Unlike opposite-direction pointers (`left → ← right`), both pointers progress in the **same direction**.

### Why does this pattern exist?

It lets you **filter, compact, partition, or modify an array in-place** without creating another array.

A common transformation is:

```text
original
[1, 1, 2, 2, 3]
 ↓ filter duplicates
[1, 2, 3, ?, ?]
          ↑
       valid prefix
```

**Mnemonic: "One reads, one writes."**

---

# 2. Recognition Signals

Immediately consider same-direction two pointers when you see:

* "Remove ___ **in-place**"
* "Move all ___ to the end"
* "Keep only elements satisfying..."
* "Return the length after removing..."
* "Modify array with **O(1) extra space**"
* "Preserve relative order"
* "Compact/filter this array"
* Sorted array + remove duplicates

The strongest signal is:

> **Scan everything, but only some elements survive.**

### Common disguise

The problem may look like simple array manipulation:

```text
[0, 1, 0, 3, 12]
```

"Move zeroes to the end while maintaining relative order."

Think:

```text
read  → finds non-zero values
write → says where they belong
```

### Don't use it when

You need to compare elements from **both ends**, such as Two Sum II or Container With Most Water. That's opposite-direction two pointers.

If you're maintaining a contiguous range satisfying some condition and the left pointer moves to shrink that range, that's usually **sliding window**, even though both pointers move forward.

---

# 3. Mental Model

Think **read pointer + write pointer**.

1. `read` scans every element.
2. `write` represents the next valid position.
3. Ask: **Should `nums[read]` survive?**
4. If yes, copy/swap it to `nums[write]`.
5. Advance `write`.
6. If no, only advance `read`.
7. Therefore `nums[:write]` always contains the processed valid elements.
8. Neither pointer moves backward → **O(n)**.
9. Usually modification happens **in-place → O(1)** extra space.

Example: remove `2`s.

```text
nums = [3, 2, 2, 3]

write = 0

read=0: 3 survives
[3, 2, 2, 3]
    ↑ write=1

read=1: 2 reject

read=2: 2 reject

read=3: 3 survives
[3, 3, 2, 3]
       ↑ write=2

Valid answer = nums[:2] = [3, 3]
```

The key invariant:

> **Everything before `write` is already correct.**

---

# 4. Boilerplate Template

The most reusable interview template:

```python
def compact(nums):
    write = 0

    for read in range(len(nums)):
        if should_keep(nums[read]):
            nums[write] = nums[read]
            write += 1

    return write
```

Interpretation:

```text
read  = inspect
write = destination
```

For swap-based problems:

```python
def partition(nums):
    write = 0

    for read in range(len(nums)):
        if condition(nums[read]):
            nums[write], nums[read] = nums[read], nums[write]
            write += 1
```

### Complexity

Usually:

**Time:** `O(n)`
**Space:** `O(1)`

---

# 5. Variations

### A. Remove/filter elements

```python
if nums[read] != val:
    nums[write] = nums[read]
    write += 1
```

Used by **Remove Element**.

### B. Deduplicate sorted array

Instead of checking a generic condition, compare against the last accepted element:

```python
if nums[read] != nums[write - 1]:
    nums[write] = nums[read]
    write += 1
```

Used by **Remove Duplicates from Sorted Array**.

### C. Move certain elements

Compact desired elements first, then handle the remainder.

For Move Zeroes:

```python
write = 0

for read in range(len(nums)):
    if nums[read] != 0:
        nums[write] = nums[read]
        write += 1

while write < len(nums):
    nums[write] = 0
    write += 1
```

### D. Allow at most `k` duplicates

Compare against the element `k` accepted positions back:

```python
if write < k or nums[read] != nums[write - k]:
    nums[write] = nums[read]
    write += 1
```

This generalizes Remove Duplicates I/II.

---

# 6. Common Pitfalls

**Moving `write` every iteration.**

Wrong:

```python
write += 1
```

`write` should normally move **only when an element is accepted**.

**Confusing `write` with the last valid index.**

In the standard template:

```python
write
```

means **next available position**, so it also equals the **number of accepted elements**.

**Overwriting data you still need.**

The pattern works because:

```text
write <= read
```

You're writing into positions you've already processed.

**Confusing it with sliding window.**

Use this distinction:

```text
Same-direction  → read + write
Sliding window  → left + right boundaries
```

Sliding window cares about the **current contiguous range** `[left, right]`. Same-direction compaction cares about the **processed valid prefix** `[0, write)`.

---

# 7. Interview Checklist

✓ Need **O(n)** instead of repeated deletion?

✓ Need **O(1)** extra space?

✓ Need to modify/filter an array **in-place**?

✓ Need to preserve the order of surviving elements?

✓ Can one pointer **scan** while another tracks where accepted elements should go?

Then think:

> **Same-direction two pointers: Read → Decide → Write → Advance**

---

# 8. Must-Do Problems

### Easy

⭐ **Top 3 — 26. Remove Duplicates from Sorted Array**
Canonical `read/write` problem.

⭐ **Top 3 — 27. Remove Element**
Best problem for understanding the generic filtering template.

⭐ **Top 3 — 283. Move Zeroes**
Adds stable compaction + filling/swapping.

Also useful: **88. Merge Sorted Array** — pointers move in the same direction when viewed from right to left; excellent in-place pointer practice.

### Medium

**80. Remove Duplicates from Sorted Array II** — extremely useful variation: allow each value at most `k` times.

**75. Sort Colors** is worth knowing, but its canonical solution is **Dutch National Flag / three pointers**, not the basic read-write pattern.

No hard problem is necessary specifically for revising this sub-pattern.

---

# 9. 30-Second Cheat Sheet

```text
SAME-DIRECTION TWO POINTERS

Recognition:
    in-place + filter/remove/move/deduplicate
    O(1) space
    preserve order

Mental Model:
    read  → scans
    write → next valid destination

Core Template:

    write = 0

    for read in range(len(nums)):
        if valid(nums[read]):
            nums[write] = nums[read]
            write += 1

    return write

Invariant:
    nums[:write] = correct processed result

Complexity:
    Time  O(n)
    Space O(1)

Variations:
    Filter             → accept/reject condition
    Deduplicate        → compare with last accepted
    Allow k duplicates → compare with nums[write-k]
    Move elements      → compact desired values
    Partition          → swap instead of overwrite

Pitfalls:
    ❌ advancing write on rejected elements
    ❌ confusing write with last valid index
    ❌ confusing read/write with sliding window

Mnemonic:
    READ → DECIDE → WRITE → ADVANCE

Top 3:
    26  Remove Duplicates
    27  Remove Element
    283 Move Zeroes
```

The pattern to burn into memory is **"read explores; write owns the valid prefix."**
