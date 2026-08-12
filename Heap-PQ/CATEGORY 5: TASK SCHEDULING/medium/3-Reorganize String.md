## 🧠 LeetCode: Reorganize String (Heap Pattern)

---

## 1. **Problem Statement with Example**

Given a string `s`, rearrange it so that **no two adjacent characters are the same**.

👉 Return any valid rearrangement. If not possible, return `""`.

### Example:

```text
s = "aab"
Output: "aba"
```

---

### Constraints:

* 1 ≤ s.length ≤ 500
* s consists of lowercase English letters

---

## 2. **Diagram (Max Heap Greedy)**

```text
s = "aaabbc"

Frequencies:
a → 3
b → 2
c → 1

Max Heap:
[3(a), 2(b), 1(c)]

Process:
Step 1: pick a
Step 2: pick b
Step 3: pick a
Step 4: pick b
Step 5: pick a
Step 6: pick c

Result:
a b a b a c
```

👉 Always pick **top 2 most frequent characters**

---

## 3. **Example I/O**

### ✅ Typical Case

```text
Input: s = "aaabbc"
Output: "ababac"
```

---

### ❌ Impossible Case

```text
Input: s = "aaab"
Output: ""
```

✔ Because `a` appears too many times

---

### ⚠️ Edge Case

```text
Input: s = "a"
Output: "a"
```

---

## 4. **Intuition & Pattern Recognition**

### 🔍 Signals:

* “no two adjacent same” → **local adjacency constraint**
* “rearrange string” → **greedy**
* “frequency matters” → **max heap**

---

### 💡 Core Idea:

👉 Always pick **top 2 most frequent characters**

Why?

* Prevents same char repeating
* Keeps high-frequency chars distributed

---

### 🧠 Interview Thought:

> “If I always take the two most frequent, I avoid adjacency conflicts.”

---

## 5. **Simpler Version**

### 🔹 Simplest:

👉 Check feasibility only:

Condition:

```text
max_freq ≤ (n + 1) // 2
```

If false → impossible

---

### 🔹 Related Problems:

* ****
  → Adds cooldown

* ****
  → Generalized distance k

---

### 🔥 Transition Thinking:

| Problem        | Constraint       |
| -------------- | ---------------- |
| This           | no adjacent same |
| k-distance     | gap ≥ k          |
| Task Scheduler | gap via time     |

---

## 6. **Brute Force**

### Idea:

* Generate all permutations
* Check valid

### Complexity:

* Time: **O(N!)** ❌
* Space: **O(N)**

---

## 7. **Optimal Solution (Max Heap)**

### 🚀 Approach:

1. Count frequencies
2. Build max heap
3. Repeatedly:

   * Pop top 2 chars
   * Append both
   * Push back if still remaining

---

### ✅ Code (Python)

```python
import heapq
from collections import Counter

def reorganizeString(s):
    freq = Counter(s)
    
    max_heap = [(-cnt, ch) for ch, cnt in freq.items()]
    heapq.heapify(max_heap)
    
    result = []
    
    while len(max_heap) >= 2:
        count1, ch1 = heapq.heappop(max_heap)
        count2, ch2 = heapq.heappop(max_heap)
        
        result.append(ch1)
        result.append(ch2)
        
        if count1 + 1 < 0:
            heapq.heappush(max_heap, (count1 + 1, ch1))
        if count2 + 1 < 0:
            heapq.heappush(max_heap, (count2 + 1, ch2))
    
    if max_heap:
        count, ch = heapq.heappop(max_heap)
        if count < -1:
            return ""
        result.append(ch)
    
    return "".join(result)
```

---

### ⏱ Complexity:

* Time: **O(N log 26) ≈ O(N)**
* Space: **O(26)**

---

## 8. **Step-by-Step Trace**

### Input:

```text
s = "aaabbc"
```

---

### Initial Heap:

```text
[(-3,a), (-2,b), (-1,c)]
```

---

### Steps:

| Step | Heap  | Pick | Result  |
| ---- | ----- | ---- | ------- |
| 1    | a,b,c | a,b  | ab      |
| 2    | a,b,c | a,b  | abab    |
| 3    | a,c   | a,c  | abababc |

✔ Done

---

## 9. **Related Problems**

1. ****
   → Adds cooldown window

2. ****
   → Generalized spacing

3. ****
   → Same greedy + heap

4. ****
   → Avoid 3 consecutive

---

## 🔥 Interview Takeaway

👉 If you see:

* “no adjacent same”
* “rearrange string”

Think:

> **Pick top 2 from max heap every time**

---

## ⚡ Bonus Insight (IMPORTANT)

You can also solve this using **greedy filling (no heap)**:

* Place most frequent char at even indices
* Then fill others

👉 But heap solution is more **generalizable** (works for k-distance too)

---

If you want, I can give you a **unified template for all 3 problems (Reorganize + k-distance + Task Scheduler)** — that's a killer interview trick.
