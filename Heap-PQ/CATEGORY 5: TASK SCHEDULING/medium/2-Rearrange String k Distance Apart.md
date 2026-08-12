## 🧠 LeetCode: Rearrange String k Distance Apart (Heap Pattern)

---

## 1. **Problem Statement with Example**

Given a string `s` and an integer `k`, rearrange the string so that **the same characters are at least `k` distance apart**.

👉 Return the rearranged string. If not possible, return `""`.

### Example:

```text
s = "aabbcc", k = 3
Output: "abcabc"
```

✔ Same characters are at least 3 distance apart

---

### Constraints:

* 1 ≤ s.length ≤ 3 * 10⁵
* s consists of lowercase English letters
* 0 ≤ k ≤ s.length

---

## 2. **Diagram (Heap + Cooling Queue)**

```text
s = "aaabc", k = 3

Frequencies:
a → 3
b → 1
c → 1

Max Heap:
[3(a), 1(b), 1(c)]

Queue (cooldown): holds used chars until k distance passes

Timeline:
Step 1: pick a → queue → [a]
Step 2: pick b → queue → [a,b]
Step 3: pick c → queue → [a,b,c] → now 'a' becomes available again
Step 4: pick a
...
```

---

## 3. **Example I/O**

### ✅ Typical Case

```text
Input: s = "aabbcc", k = 3
Output: "abcabc"
```

---

### ❌ Impossible Case

```text
Input: s = "aaabc", k = 3
Output: ""
```

✔ Not enough distinct chars to maintain spacing

---

### ⚠️ Edge Case

```text
Input: s = "aa", k = 0
Output: "aa"
```

✔ No constraint → return original

---

## 4. **Intuition & Pattern Recognition**

### 🔍 Signals:

* “distance apart” → **cooldown constraint**
* “rearrange string” → **greedy placement**
* “most frequent matters” → **max heap**

---

### 💡 Core Idea:

* Always place the **most frequent available character**
* After using it → it becomes unavailable for next `k` steps
* Use:

  * **Max Heap** → pick best candidate
  * **Queue** → track cooldown

---

### 🧠 Interview Thought:

> “This is Task Scheduler but instead of counting time, we build the actual string.”

---

## 5. **Simpler Version**

### 🔹 Step 1:

👉 No constraint → return string

---

### 🔹 Step 2:

👉 k = 2 → no adjacent same
Related:

* ****

---

### 🔹 Step 3:

👉 General k distance
Related:

* ****

---

### 🔥 Key Transition:

* Task Scheduler → count time
* This → **construct actual arrangement**

---

## 6. **Brute Force**

### Idea:

* Try all permutations
* Check if valid (distance ≥ k)

### Complexity:

* Time: **O(N!)** ❌
* Space: **O(N)**

---

## 7. **Optimal Solution (Max Heap + Queue)**

### 🚀 Approach:

1. Count frequencies
2. Push into max heap
3. Use queue → `(char, remaining_count, ready_time)`
4. At each step:

   * Pop from heap → append to result
   * Push into queue with cooldown
   * If queue front is ready → push back to heap
5. If heap empty but still chars left → impossible

---

### ✅ Code (Python)

```python
import heapq
from collections import Counter, deque

def rearrangeString(s, k):
    if k == 0:
        return s
    
    freq = Counter(s)
    
    max_heap = [(-cnt, ch) for ch, cnt in freq.items()]
    heapq.heapify(max_heap)
    
    queue = deque()  # (count, char, ready_time)
    result = []
    time = 0
    
    while max_heap or queue:
        time += 1
        
        if max_heap:
            count, ch = heapq.heappop(max_heap)
            result.append(ch)
            
            if count + 1 < 0:
                queue.append((count + 1, ch, time + k - 1))
        else:
            return ""  # idle not allowed → invalid
        
        # check if any char becomes available
        if queue and queue[0][2] == time:
            heapq.heappush(max_heap, (queue[0][0], queue[0][1]))
            queue.popleft()
    
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
s = "aabbcc", k = 3
```

---

### Initial:

```text
Heap: [(-2,a), (-2,b), (-2,c)]
Queue: []
Result: ""
```

---

### Step-by-step:

| Time | Heap        | Pick | Queue            | Result |
| ---- | ----------- | ---- | ---------------- | ------ |
| 1    | a,b,c       | a    | (a,-1,3)         | a      |
| 2    | b,c         | b    | (a),(b,-1,4)     | ab     |
| 3    | c           | c    | (a),(b),(c,-1,5) | abc    |
| 4    | a available | a    | (b),(c),(a,0)    | abca   |
| 5    | b available | b    | (c),(a),(b,0)    | abcab  |
| 6    | c available | c    |                  | abcabc |

✔ Done

---

## 9. **Related Problems**

1. ****
   → Same cooldown idea, but counts time instead of building string

2. ****
   → Special case where k = 2

3. ****
   → Same frequency spacing idea

4. ****
   → Avoid consecutive repetition

5. ****
   → Same problem (this one)

---

## 🔥 Interview Takeaway

👉 If problem says:

* “k distance apart”
* “rearrange string”
* “frequency matters”

Think:

> **Max Heap + Cooling Queue**

---

If you want, I can also give you a **template that works for ALL heap + cooldown problems (Task Scheduler, this, etc.)** — super useful for interviews.
