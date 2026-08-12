## 🪟 Sliding Window Maximum (Heap Pattern)

---

## 1. Problem Statement with Example

Given an array `nums` and an integer `k`, return an array of the **maximum value in every sliding window of size k**.

* Window slides from left → right
* At each step, return the max in the current window

### Example

```text
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3  
Output: [3,3,5,5,6,7]
```

---

## 2. Diagram

```
nums = [1, 3, -1, -3, 5, 3, 6, 7]
         --------
window1: [1, 3, -1] → max = 3

            --------
window2:    [3, -1, -3] → max = 3

               --------
window3:       [-1, -3, 5] → max = 5

                  --------
window4:          [-3, 5, 3] → max = 5

                     --------
window5:             [5, 3, 6] → max = 6

                        --------
window6:                [3, 6, 7] → max = 7
```

---

## 3. Example I/O

### Example 1 (Typical)

```
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3  
Output: [3,3,5,5,6,7]
```

### Example 2 (Edge Case)

```
Input: nums = [1], k = 1  
Output: [1]
```

---

## 4. Intuition & Pattern Recognition

### 🔑 Key Signals:

* “Window of size k” → **Sliding Window**
* “Get max in each window” → need **efficient max retrieval**
* Window moves → elements go **outdated**

👉 Combine:

* Sliding Window + **Max Heap**

### 🧠 Interview Thought:

> “I need max in a moving window → heap can give max, but I must remove outdated indices.”

---

## 5. Simpler Version

### Simpler Problem:

👉 “Find max in every window” (brute force)

* For each window → scan k elements → O(nk)

### Related Simpler Problems:

* **Maximum of all subarrays of size k (GFG)**
* **Kth Largest Element** → heap usage

### Build-up Thinking:

```
Brute: scan each window → slow  
Need faster max → heap  
But heap can't delete arbitrary elements → lazy removal needed
```

---

## 6. Brute Force

```python
def maxSlidingWindow(nums, k):
    res = []
    for i in range(len(nums) - k + 1):
        res.append(max(nums[i:i+k]))
    return res
```

### Complexity

* Time: **O(n * k)**
* Space: **O(1)**

---

## 7. Optimal Solution (Heap + Lazy Removal)

### Idea:

* Store `(value, index)` in max heap
* Use negative values for max heap
* Remove elements that are **out of window**

---

### Code

```python
import heapq

def maxSlidingWindow(nums, k):
    maxHeap = []  # (negative value, index)
    res = []

    for i in range(len(nums)):
        # Push current element
        heapq.heappush(maxHeap, (-nums[i], i))

        # Remove elements outside window
        while maxHeap[0][1] <= i - k:
            heapq.heappop(maxHeap)

        # Window is valid
        if i >= k - 1:
            res.append(-maxHeap[0][0])  # top is max

    return res
```

---

### Complexity

* Time: **O(n log n)**
* Space: **O(n)**

---

## 8. Step-by-Step Trace

### Input:

```
nums = [1,3,-1,-3,5], k = 3
```

### Steps:

| i | Element | Heap (top) | Remove Outdated? | Output |
| - | ------- | ---------- | ---------------- | ------ |
| 0 | 1       | 1          | ❌                | -      |
| 1 | 3       | 3          | ❌                | -      |
| 2 | -1      | 3          | ❌                | 3      |
| 3 | -3      | 3          | ❌                | 3      |
| 4 | 5       | 5          | ❌                | 5      |

Final:

```
[3,3,5]
```

---

## 9. Related Problems

1. **Sliding Window Maximum (Deque Optimal)**
   → Same problem, but O(n) using monotonic deque

2. **Kth Largest Element in Stream**
   → Heap + dynamic updates

3. **Find Median from Data Stream**
   → Two heaps + balancing

4. **Top K Frequent Elements**
   → Heap prioritization

5. **Longest Subarray with Limit**
   → Sliding window + monotonic structure

---

## ⚠️ Final Interview Note

### Heap vs Deque

| Approach | Time       | Key Idea                      |
| -------- | ---------- | ----------------------------- |
| Heap     | O(n log n) | Easy, lazy removal            |
| Deque    | O(n)       | Optimal, monotonic decreasing |

👉 If interviewer pushes:

> Start with heap → optimize to deque

---

If you want, I can next give:

* **Monotonic Deque version (VERY important for interviews)**
* OR a **comparison intuition cheat sheet (heap vs deque vs multiset)**
