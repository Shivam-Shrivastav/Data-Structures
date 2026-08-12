## 🪨 Last Stone Weight (Heap Pattern)

---

## 1. Problem Statement with Example

Given an array `stones` where each element represents the weight of a stone:

* Each turn:

  * Pick the **two heaviest stones** `x` and `y`
  * Smash them:

    * If `x == y` → both destroyed
    * Else → new stone of weight `|x - y|`
* Repeat until ≤1 stone remains

Return the **weight of the last remaining stone** (or `0` if none).

### Example

```
Input:  stones = [2,7,4,1,8,1]
Output: 1
```

---

## 2. Diagram

```
Initial:        [2,7,4,1,8,1]

Step 1: pick 8,7 → new stone = 1
Remaining:      [2,4,1,1,1]

Step 2: pick 4,2 → new stone = 2
Remaining:      [2,1,1,1]

Step 3: pick 2,1 → new stone = 1
Remaining:      [1,1,1]

Step 4: pick 1,1 → destroyed
Remaining:      [1]

Final Answer:   1
```

---

## 3. Example I/O

### Example 1 (Typical)

```
Input:  [2,7,4,1,8,1]
Output: 1
Explanation:
Repeated smashing leads to final stone of weight 1.
```

### Example 2 (Edge Case)

```
Input:  [5,5]
Output: 0
Explanation:
Both stones cancel out.
```

---

## 4. Intuition & Pattern Recognition

### 🔑 Key Signals:

* "Pick largest elements repeatedly" → **Max Heap**
* Dynamic removal + insertion → heap is ideal

### ❌ Why NOT Sliding Window?

* Sliding window works on **contiguous subarrays**
* Here:

  * We pick **global max elements**, not neighbors
  * Structure changes dynamically

👉 So this is **pure Heap**, not sliding window.

### 🧠 Interview Thought:

> “I need to repeatedly extract the top 2 largest values → use max heap.”

---

## 5. Simpler Version

### Simpler Problem:

👉 “Find the largest element repeatedly and remove it”

→ Just use a max heap

### Closely Related LeetCode:

* **Kth Largest Element in Array**
* **Top K Frequent Elements**

### Build-up Thinking:

```
1 element → trivial  
2 elements → compare  
Many elements → need efficient max retrieval → heap
```

👉 This problem = **continuous heap simulation**

---

## 6. Brute Force

### Idea:

* Sort array every time
* Pick last 2 elements

### Code

```python
def lastStoneWeight(stones):
    while len(stones) > 1:
        stones.sort()
        y = stones.pop()
        x = stones.pop()
        if y != x:
            stones.append(y - x)
    return stones[0] if stones else 0
```

### Complexity

* Time: **O(n² log n)** (sorting every iteration)
* Space: **O(1)**

---

## 7. Optimal Solution (Max Heap)

### Idea:

* Use **max heap**
* Python has min heap → store negatives

### Code

```python
import heapq

def lastStoneWeight(stones):
    # Convert to max heap using negative values
    maxHeap = [-s for s in stones]
    heapq.heapify(maxHeap)

    while len(maxHeap) > 1:
        y = -heapq.heappop(maxHeap)  # largest
        x = -heapq.heappop(maxHeap)  # second largest

        if y != x:
            heapq.heappush(maxHeap, -(y - x))  # push difference

    return -maxHeap[0] if maxHeap else 0
```

### Complexity

* Time: **O(n log n)**
* Space: **O(n)**

---

## 8. Step-by-Step Trace

### Input:

```
stones = [2,7,4,1,8,1]
```

### Heap (as negatives):

```
[-8, -7, -4, -1, -2, -1]
```

| Step | Pop y | Pop x | New Stone | Heap After       |
| ---- | ----- | ----- | --------- | ---------------- |
| 1    | 8     | 7     | 1         | [-4,-2,-1,-1,-1] |
| 2    | 4     | 2     | 2         | [-2,-1,-1,-1]    |
| 3    | 2     | 1     | 1         | [-1,-1,-1]       |
| 4    | 1     | 1     | 0         | [-1]             |

Final:

```
Answer = 1
```

---

## 9. Related Problems

1. **Kth Largest Element in an Array**
   → Same idea: repeatedly extract max elements

2. **Top K Frequent Elements**
   → Heap used for frequency prioritization

3. **Last Stone Weight II**
   → Extension: turns into **subset sum / DP**

4. **Find K Pairs with Smallest Sums**
   → Heap + pair generation

5. **Merge K Sorted Lists**
   → Heap for continuous extraction

---

## ⚠️ Final Interview Note

* ❌ Not Sliding Window
* ✅ Pure **Max Heap Simulation**

👉 If interviewer says “sliding window” here → they are **testing your pattern recognition**

---

If you want, I can also show:

* How this connects to **Last Stone Weight II (DP)**
* OR how to implement a **custom max heap without negation**
