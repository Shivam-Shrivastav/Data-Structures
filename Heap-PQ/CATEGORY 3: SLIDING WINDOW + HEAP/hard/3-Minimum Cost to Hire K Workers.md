## 💼 Minimum Cost to Hire K Workers (Greedy + Heap)

---

## 1. Problem Statement with Example

You are given:

* `quality[i]` → quality of worker `i`
* `wage[i]` → minimum wage expectation of worker `i`

### Rules:

* You must hire **exactly K workers**

* All workers must be paid using the **same ratio**:

  ```text
  wage / quality = same for all selected workers
  ```

* Each worker must receive **at least their minimum wage**

👉 Return the **minimum total cost** to hire `K` workers

---

### Example

```text
Input:
quality = [10,20,5]
wage    = [70,50,30]
k = 2

Output: 105.0
```

---

## 2. Diagram (Core Idea)

![Image](https://thismatter.com/economics/images/wage-determination-graph.svg)

![Image](https://cdn.hashnode.com/res/hashnode/image/upload/v1724753728063/0cf7eb94-56b0-4dad-895d-24dcb4de7059.png)

![Image](https://dotnettrickscloud.blob.core.windows.net/article/data%20structures/4620231205135529.png)

![Image](https://dotnettrickscloud.blob.core.windows.net/article/data%20structures/4620231205180208.png)

👉 Think:

* Each worker defines a **ratio = wage/quality**
* If we fix a ratio → all workers must be paid using that ratio

---

## 3. Example I/O

### Example 1 (Typical)

```text
Input:
quality = [10,20,5]
wage    = [70,50,30]
k = 2

Output: 105.0

Explanation:
Pick workers (0,2)
ratio = 70/10 = 7
cost = (10+5)*7 = 105
```

---

### Example 2 (Edge Case)

```text
Input:
quality = [3,1,10,10,1]
wage    = [4,8,2,2,7]
k = 3

Output: 30.66667
```

---

## 4. Intuition & Pattern Recognition

### 🔑 Key Signals:

* “Same ratio constraint” → normalize workers by **ratio**
* “Pick K workers minimizing sum” → **Heap**
* “Minimize total cost = ratio × total quality”

---

### 🧠 Interview Thought:

> “Fix ratio → minimize total quality → use max heap to keep smallest K qualities”

---

## 5. Simpler Version

### Step 1:

👉 Ignore ratio → pick K smallest qualities

### Step 2:

👉 Add ratio constraint:

* Must use **max ratio among selected workers**

---

### Build-up Thinking:

```text
Cost = sum(quality) * max_ratio

So:
Fix max_ratio → minimize sum(quality)
```

---

### Related Simpler Problems:

* **Kth Largest Element**
* **Top K Frequent Elements**
* **Find K Pairs with Smallest Sums**

---

## 6. Brute Force

### Idea:

* Try all subsets of size K
* Check valid ratio
* compute cost

```python
from itertools import combinations

def mincostToHireWorkers(quality, wage, k):
    n = len(quality)
    res = float('inf')

    for comb in combinations(range(n), k):
        max_ratio = max(wage[i]/quality[i] for i in comb)
        cost = sum(quality[i] * max_ratio for i in comb)
        res = min(res, cost)

    return res
```

### Complexity

* Time: **O(n choose k)** ❌
* Space: **O(k)**

---

## 7. Optimal Solution (Greedy + Max Heap)

### 🔥 Key Insight:

* Sort workers by **ratio (wage/quality)**
* For each worker as “max ratio”:

  * pick **K smallest qualities so far**

---

### Code

```python
import heapq

def mincostToHireWorkers(quality, wage, k):
    workers = []
    
    # (ratio, quality)
    for q, w in zip(quality, wage):
        workers.append((w / q, q))
    
    workers.sort()  # sort by ratio

    max_heap = []
    total_quality = 0
    res = float('inf')

    for ratio, q in workers:
        heapq.heappush(max_heap, -q)
        total_quality += q

        # keep only k workers
        if len(max_heap) > k:
            total_quality += heapq.heappop(max_heap)

        if len(max_heap) == k:
            cost = total_quality * ratio
            res = min(res, cost)

    return res
```

---

### Complexity

* Time: **O(n log n)**
* Space: **O(k)**

---

## 8. Step-by-Step Trace

### Input:

```text
quality = [10,20,5]
wage    = [70,50,30]
k = 2
```

---

### Step 1: Compute ratios

```text
(7,10), (2.5,20), (6,5)
```

### Step 2: Sort

```text
(2.5,20), (6,5), (7,10)
```

---

### Iteration:

| Step | Worker   | Heap   | Total Q | Cost       |
| ---- | -------- | ------ | ------- | ---------- |
| 1    | (2.5,20) | [20]   | 20      | -          |
| 2    | (6,5)    | [20,5] | 25      | 25*6=150   |
| 3    | (7,10)   | [10,5] | 15      | 15*7=105 ✅ |

---

## 9. Related Problems

1. **Kth Largest Element in Array**
   → Heap for selecting top K

2. **Top K Frequent Elements**
   → Heap with frequency

3. **Find K Pairs with Smallest Sums**
   → Heap + greedy

4. **IPO Problem**
   → Greedy + heap selection

5. **Course Schedule III**
   → Similar: keep best subset with heap

---

## ⚠️ Final Interview Notes

### 🔥 Core Pattern:

👉 **Sort by constraint + Heap to optimize subset**

---

### Key Formula:

```text
Total Cost = sum(quality) * max_ratio
```

---

### Key Strategy:

```text
1. Fix max_ratio (iterate sorted workers)
2. Maintain K smallest qualities (max heap)
3. Compute cost
```

---

### Common Mistakes:

* Not sorting by ratio ❌
* Using min heap instead of max heap ❌
* Forgetting to remove largest quality ❌

---

## 🧠 One-Line Memory Trick

> “Fix ratio → minimize quality sum using max heap”

---

If you want, I can next:

* 🔥 Show **why greedy works (proof intuition)**
* OR give **comparison: this vs Course Schedule III (same trick!)**
