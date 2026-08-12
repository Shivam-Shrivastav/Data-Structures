# Contains Duplicate — Frequency Counting

This is one of the simplest **frequency counting / hash-based lookup** patterns. The important revision takeaway is bigger than Contains Duplicate itself: **when you need to know whether you've seen a value before, think hash set immediately.**
 
## 1. Pattern in One Minute

**Core idea:** Scan the array while maintaining a `set` of values already seen.

For each `x`:

```text
Have I seen x before?
        ↓
     Yes → duplicate found
     No  → remember x
```

Why this pattern exists: without hashing, you might compare every element against every other element → **O(n²)**. A hash set gives average **O(1)** membership checks, reducing the whole problem to **O(n)**.

### Immediate recognition

> **"Does any value appear more than once?" → Hash Set**

The key distinction:

* Need only **existence of duplicate** → `set`
* Need **how many times** each value occurs → `dict` / `Counter`

---

## 2. Recognition Signals

Think **frequency counting / hashing** when you see:

* "contains duplicate"
* "appears more than once"
* "all elements distinct?"
* "unique elements"
* "have we seen this before?"
* "frequency/count of each element"
* Pair/matching problems where you need fast lookup

Especially when `n` is large enough that **O(n²)** comparison is undesirable.

### Don't use this exact approach when

You need duplicates only within a **specific window/distance** → combine hashing with sliding window.

You need duplicate counts → use a frequency map.

You have strict **O(1) extra-space** requirements → sorting or problem-specific tricks may be needed.

---

## 3. Mental Model

Remember:

> **Set = "Have I seen this?"**
> **Map = "How many times have I seen this?"**

For:

```python
nums = [4, 7, 2, 7]
```

Walk through:

```text
4 → seen? No  → {4}
7 → seen? No  → {4, 7}
2 → seen? No  → {4, 7, 2}
7 → seen? YES → return True
```

The second `7` is enough. We don't care about its exact frequency.

That's why a `set` is more natural than a frequency dictionary for **Contains Duplicate**.

---

## 4. Boilerplate Template

### Best interview template

```python
def containsDuplicate(nums):
    seen = set()

    for num in nums:
        if num in seen:
            return True

        seen.add(num)

    return False
```

**Time:** O(n) average
**Space:** O(n)

### Python shortcut

```python
def containsDuplicate(nums):
    return len(nums) != len(set(nums))
```

Good Python, but in an interview I'd usually write the first version because it demonstrates the pattern and can terminate early.

### Generic frequency-counting template

When you actually need counts:

```python
freq = {}

for x in nums:
    freq[x] = freq.get(x, 0) + 1
```

Or:

```python
from collections import Counter

freq = Counter(nums)
```

---

## 5. Variations

The pattern branches depending on **what information about repetition matters**:

| Problem asks                            | Structure / Pattern              |
| --------------------------------------- | -------------------------------- |
| Does any duplicate exist?               | `set`                            |
| Count occurrences                       | `dict` / `Counter`               |
| Find values occurring exactly `k` times | Frequency map                    |
| Duplicate within distance `k`           | Set + Sliding Window             |
| Duplicate + index information           | Hash map: `value → index`        |
| Find first repeated element             | Set while scanning               |
| Group items by some property            | Map: `property → frequency/list` |

The interview question to ask yourself:

> **Do I need existence, count, or position?**

That usually determines the data structure.

---

## 6. Common Pitfalls

### Using a dictionary unnecessarily

```python
freq[num] = freq.get(num, 0) + 1
```

This works, but if you only need to detect a duplicate, you're storing information you don't need.

Use:

```python
if num in seen:
```

### Sorting immediately

```python
nums.sort()

for i in range(1, len(nums)):
    if nums[i] == nums[i - 1]:
        return True
```

This is **O(n log n)** and mutates `nums`.

Sorting can make sense when extra space is constrained, but hashing is the natural solution otherwise.

### Comparing every pair

```python
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        ...
```

**O(n²)** → usually the solution you're expected to improve.

### Confusing set and map

```text
Need membership? → set
Need frequency?  → map
Need index?      → map
```

---

## 7. Interview Checklist

✓ Do I need to detect repeated values?

✓ Am I repeatedly asking **"Have I seen X?"**

✓ Do I only care whether X exists, not its count?

→ **Hash Set**

If instead:

✓ I need occurrence counts

→ **Frequency Map / Counter**

If:

✓ I need the previous index/location of X

→ **Hash Map: value → index**

Mnemonic:

> **Seen → Set, Count → Counter, Position → Map**

---

## 8. Must-Do Problems

For this sub-pattern, prioritize:

**Easy**

⭐ **Top 3:**

1. **217. Contains Duplicate** — pure `seen` set
2. **242. Valid Anagram** — pure frequency counting
3. **1. Two Sum** — hash lookup with stored information

Also useful: **383. Ransom Note** and **387. First Unique Character in a String**.

**Medium**

**49. Group Anagrams** — frequency/signature as hash-map key.

**347. Top K Frequent Elements** — frequency counting followed by Top-K processing.

**128. Longest Consecutive Sequence** — excellent example of using a set for more than simple duplicate detection.

No hard problem is necessary just to revise this pattern.

---

# 9. 30-Second Cheat Sheet

```text
FREQUENCY COUNTING / HASHING

Recognition:
"duplicate", "unique", "frequency",
"seen before?", "count occurrences"

Core decision:

Existence?
    → set

Count?
    → dict / Counter

Position/index?
    → dict

Contains Duplicate:

seen = set()

for x in nums:
    if x in seen:
        return True
    seen.add(x)

return False

Time:  O(n) average
Space: O(n)

Mnemonic:
Seen → Set
Count → Counter
Position → Map
```

The broader pattern to retain is **not "Contains Duplicate" specifically**. It is:

**When brute force repeatedly searches previously processed elements, ask whether a hash set/map can turn that search into O(1) average lookup.**
