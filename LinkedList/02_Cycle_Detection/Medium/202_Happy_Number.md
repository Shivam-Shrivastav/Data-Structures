# 202. Happy Number

## 1. Problem Statement with Example

Given an integer `n`, repeatedly replace the number with:

```text
sum of squares of its digits
```

If the process eventually reaches `1`, the number is called a **happy number**.

Return `True` if `n` is happy, otherwise return `False`.

---

## Example

```text
n = 19

1² + 9² = 82
8² + 2² = 68
6² + 8² = 100
1² + 0² + 0² = 1
```

So:

```text
Output = True
```

---

## Constraints

```text
1 <= n <= 2^31 - 1
```

Important observation:

* Numbers eventually either:

  * become `1`
  * or enter a cycle

This is the key pattern.

---

# 2. Diagram

```text
19
↓
82
↓
68
↓
100
↓
1  ✅
```

Unhappy number example:

```text
2
↓
4
↓
16
↓
37
↓
58
↓
89
↓
145
↓
42
↓
20
↓
4   ← cycle repeats
```

Cycle detected → not happy.

---

# 3. Example I/O

## Example 1 (Happy Number)

### Input

```text
n = 19
```

### Output

```text
True
```

### Why?

Sequence eventually reaches `1`.

---

## Example 2 (Not Happy)

### Input

```text
n = 2
```

### Output

```text
False
```

### Why?

Sequence enters repeating cycle.

---

## Example 3 (Edge Case)

### Input

```text
n = 1
```

### Output

```text
True
```

Already happy.

---

# 4. Intuition & Pattern Recognition

## Biggest Clue

Whenever problem says:

* repeatedly transform
* process repeats
* infinite loop possible
* detect repetition

→ Think:

# Cycle Detection

---

## Two Ways to Detect Cycle

### 1. HashSet

Store previously seen numbers.

If number repeats:

* cycle exists

---

### 2. Floyd’s Cycle Detection (Optimal Pattern)

Exactly same as:

* Linked List Cycle

Because:

```text
number → transformed number
```

acts like a linked list transition.

---

## Interview Recognition Trick

If:

```text
next_state(current)
```

exists repeatedly,

then think:

```text
current → next → next → next
```

That is essentially a hidden linked list.

---

# 5. Simpler Version

## Simplest Problem

### “Keep transforming until 1 or repetition.”

Use a set:

```python
seen = set()
```

Very intuitive.

---

## Simpler Related Problems

### 1. Linked List Cycle

Direct same pattern:

* revisit means loop

---

### 2. Find Duplicate Number

Uses Floyd cycle trick on array mapping.

---

### 3. Detect Cycle in Directed Graph

Repeated state detection.

---

## Thinking Progression

```text
Repeated transformation
        ↓
Need repetition detection
        ↓
Use HashSet
        ↓
Can optimize space?
        ↓
Floyd Cycle Detection
```

---

# 6. Brute Force

## Idea

Store all previously seen numbers.

If:

* reaches `1` → happy
* repeats → cycle

---

## Helper Function

```python
def get_next(n):

    total = 0

    while n:
        digit = n % 10
        total += digit * digit
        n //= 10

    return total
```

---

## Code

```python
class Solution:

    def isHappy(self, n: int) -> bool:

        seen = set()

        while n != 1:

            if n in seen:
                return False

            seen.add(n)

            n = self.get_next(n)

        return True

    def get_next(self, n):

        total = 0

        while n:

            digit = n % 10
            total += digit * digit
            n //= 10

        return total
```

---

## Complexity

### Time

Approximately:
O(\log n)
per transformation.

Overall bounded because numbers shrink quickly.

---

### Space

O(k)

Where `k` = unique states visited.

---

# 7. Optimal Solution

# Floyd Cycle Detection

---

## Core Idea

Use:

* slow pointer = 1 step
* fast pointer = 2 steps

If cycle exists:

* they meet

If reaches `1`:

* happy number

---

## Code

```python
class Solution:

    def isHappy(self, n: int) -> bool:

        slow = n
        fast = self.get_next(n)

        while fast != 1 and slow != fast:

            slow = self.get_next(slow)

            # move two steps
            fast = self.get_next(self.get_next(fast))

        return fast == 1

    def get_next(self, n):

        total = 0

        while n:

            digit = n % 10
            total += digit * digit
            n //= 10

        return total
```

---

## Why It Works

This transformation creates:

```text
n → next(n)
```

which behaves exactly like:

```text
node → next node
```

So Floyd cycle detection applies perfectly.

---

## Complexity

### Time

O(\log n)
(amortized small because values rapidly shrink)

### Space

O(1)

---

# 8. Step-by-Step Trace

## Example

```text
n = 19
```

---

## Initial

```text
slow = 19
fast = 82
```

---

| Step | slow | fast |
| ---- | ---- | ---- |
| 1    | 82   | 100  |
| 2    | 68   | 1    |

Since `fast == 1`:

```text
Return True
```

---

## Unhappy Example

```text
n = 2
```

Sequence:

```text
2 → 4 → 16 → 37 → 58 → 89 → 145 → 42 → 20 → 4
```

Eventually:

```text
slow == fast
```

inside cycle.

Return `False`.

---

# 9. Related Problems

## 1. Linked List Cycle

Exact same Floyd cycle detection pattern.

---

## 2. Find the Duplicate Number

Transforms array into cycle graph.

---

## 3. Circular Array Loop

Cycle detection with movement rules.

---

## 4. Linked List Cycle II

Find cycle entry point.

---

## 5. Sum of Digits Problems

Builds digit extraction intuition.

---

# Interview One-Liner

> “This problem is hidden cycle detection because every number deterministically maps to another number.”
