## 🪟 Sliding Window Median (Heap Pattern)

---

## 1. Problem Statement with Example

Given an array `nums` and a window size `k`, return the **median of every sliding window of size k**.

* Window slides from left → right
* Median:

  * If `k` odd → middle element
  * If `k` even → average of two middle elements

### Example

```text
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3  
Output: [1,-1,-1,3,5,6]
```

---

## 2. Diagram

```text
nums = [1, 3, -1, -3, 5, 3, 6, 7]

window1: [1, 3, -1] → sorted [-1,1,3] → median = 1  
window2: [3, -1, -3] → sorted [-3,-1,3] → median = -1  
window3: [-1, -3, 5] → sorted [-3,-1,5] → median = -1  
window4: [-3, 5, 3] → sorted [-3,3,5] → median = 3  
...
```

---

## 3. Example I/O

### Example 1 (Typical)

```text
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3  
Output: [1,-1,-1,3,5,6]
```

### Example 2 (Even Window)

```text
Input: nums = [1,2,3,4], k = 2  
Output: [1.5, 2.5, 3.5]
```

---

## 4. Intuition & Pattern Recognition

### 🔑 Key Signals:

* “Median” → need **ordered structure**
* “Sliding window” → elements added + removed
* Need fast:

  * insert
  * delete
  * get median

👉 Best structure:

* **Two Heaps**

  * Max heap → left half
  * Min heap → right half

### 🧠 Interview Thought:

> “Median = middle → maintain two halves balanced.”

---

## 5. Simpler Version

### Simpler Problem:

👉 “Find median of a stream”

→ LeetCode: **Find Median from Data Stream**

### Build-up Thinking:

```text
Static median → sort  
Dynamic median → two heaps  
Sliding window → also need deletion → lazy removal
```

### Key Jump:

* Normal heaps ❌ can’t delete arbitrary elements
* → Use **lazy deletion (hash map)**

---

## 6. Brute Force

```python
def medianSlidingWindow(nums, k):
    res = []
    for i in range(len(nums) - k + 1):
        window = sorted(nums[i:i+k])
        if k % 2:
            res.append(window[k//2])
        else:
            res.append((window[k//2] + window[k//2 - 1]) / 2)
    return res
```

### Complexity

* Time: **O(n * k log k)**
* Space: **O(k)**

---

## 7. Optimal Solution (Two Heaps + Lazy Deletion)

### Idea:

* `small` (max heap) → smaller half

* `large` (min heap) → larger half

* Maintain:

  * size difference ≤ 1
  * all elements in `small` ≤ `large`

* Use **delayed deletion map**

---

### Code

```python
import heapq
from collections import defaultdict

class Solution:
    def medianSlidingWindow(self, nums, k):
        small, large = [], []  # max heap, min heap
        delayed = defaultdict(int)
        res = []

        def prune(heap):
            while heap:
                num = heap[0]
                if heap is small:
                    num = -num
                if delayed[num]:
                    delayed[num] -= 1
                    heapq.heappop(heap)
                else:
                    break

        def balance():
            # keep sizes balanced
            if len(small) > len(large) + 1:
                heapq.heappush(large, -heapq.heappop(small))
                prune(small)
            elif len(small) < len(large):
                heapq.heappush(small, -heapq.heappop(large))
                prune(large)

        def getMedian():
            if k % 2:
                return -small[0]
            return (-small[0] + large[0]) / 2

        # initialize
        for i in range(k):
            heapq.heappush(small, -nums[i])
        for _ in range(k // 2):
            heapq.heappush(large, -heapq.heappop(small))

        # sliding window
        for i in range(k, len(nums)):
            res.append(getMedian())

            out_num = nums[i - k]
            in_num = nums[i]
            delayed[out_num] += 1

            # add new element
            if in_num <= -small[0]:
                heapq.heappush(small, -in_num)
            else:
                heapq.heappush(large, in_num)

            # remove outgoing element logically
            if out_num <= -small[0]:
                if out_num == -small[0]:
                    prune(small)
            else:
                if large and out_num == large[0]:
                    prune(large)

            balance()

        res.append(getMedian())
        return res
```

---

### Complexity

* Time: **O(n log k)**
* Space: **O(k)**

---

## 8. Step-by-Step Trace

### Input:

```text
nums = [1,3,-1], k = 3
```

### Heaps:

```text
small (max): [1, -1] → top = 1  
large (min): [3]
```

Median:

```text
k = 3 → odd → median = 1
```

---

Next window:

```text
remove 1, add -3

small → [-1, -3]  
large → [3]
```

Median:

```text
-1
```

---

## 9. Related Problems

1. **Find Median from Data Stream**
   → Same two-heap idea, no sliding window

2. **Sliding Window Maximum**
   → Sliding window + heap/deque

3. **Kth Largest Element in Stream**
   → Heap with dynamic updates

4. **Top K Frequent Elements**
   → Heap prioritization

5. **Minimum Size Subarray Sum**
   → Sliding window (different metric)

---

## ⚠️ Final Interview Notes

### 🔥 Core Insights:

* Median → **two heaps**
* Sliding window → **lazy deletion**
* Balance heaps carefully

### Common Mistakes:

* Forgetting lazy deletion
* Not balancing heaps after removal
* Incorrect median for even k

---

If you want, next I can:

* Give **cleaner interview version (shorter code)**
* OR show **TreeMap / SortedList approach (Python vs Java difference)**
