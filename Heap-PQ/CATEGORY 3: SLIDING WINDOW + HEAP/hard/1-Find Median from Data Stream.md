## 📊 Find Median from Data Stream (Two Heaps Pattern)

---

## 1. Problem Statement with Example

Design a data structure that supports:

* `addNum(num)` → add number to stream
* `findMedian()` → return median of all elements so far

### Median Definition:

* Odd count → middle element
* Even count → average of two middle elements

---

### Example

```text
Input:
addNum(1)
addNum(2)
findMedian() → 1.5
addNum(3)
findMedian() → 2
```

---

## 2. Diagram

```text
Stream: 1, 2, 3

Step 1:
[1]
median = 1

Step 2:
[1,2] → split:
left(max heap): [1]
right(min heap): [2]
median = (1+2)/2

Step 3:
[1,2,3] → split:
left: [2,1]
right: [3]
median = 2
```

---

## 3. Example I/O

### Example 1 (Typical)

```text
Operations:
addNum(1)
addNum(2)
findMedian() → 1.5
addNum(3)
findMedian() → 2
```

### Example 2 (Edge Case)

```text
Operations:
addNum(5)
findMedian() → 5
```

---

## 4. Intuition & Pattern Recognition

### 🔑 Key Signals:

* “Median” → need **middle element**
* Dynamic insertion → **cannot sort every time**
* Need:

  * fast insert
  * fast median

👉 Solution:

* **Two Heaps**

  * Max heap → left half (smaller values)
  * Min heap → right half (larger values)

---

### 🧠 Interview Thought:

> “Median splits data into two halves → maintain them using two heaps”

---

## 5. Simpler Version

### Simpler Problem:

👉 “Find median of a static array”

→ Sort → pick middle

---

### Build-up Thinking:

```text
Static → sort → O(n log n)  
Dynamic → need faster insert → heap  
Median → split into two halves → two heaps
```

---

### Related Simpler Problems:

* **Kth Largest Element**
* **Sliding Window Maximum**
* **Last Stone Weight**

---

## 6. Brute Force

```python
class MedianFinder:
    def __init__(self):
        self.arr = []

    def addNum(self, num):
        self.arr.append(num)

    def findMedian(self):
        self.arr.sort()
        n = len(self.arr)
        if n % 2:
            return self.arr[n//2]
        return (self.arr[n//2] + self.arr[n//2 - 1]) / 2
```

### Complexity

* addNum: **O(1)**
* findMedian: **O(n log n)**

---

## 7. Optimal Solution (Two Heaps)

### Idea:

* `small` → max heap (store negatives)
* `large` → min heap

### Maintain:

1. size difference ≤ 1
2. all elements in `small` ≤ elements in `large`

---

### Code

```python
import heapq

class MedianFinder:

    def __init__(self):
        self.small = []  # max heap (negatives)
        self.large = []  # min heap

    def addNum(self, num):
        # step 1: push to max heap
        heapq.heappush(self.small, -num)

        # step 2: ensure order property
        if self.small and self.large and (-self.small[0] > self.large[0]):
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # step 3: balance sizes
        if len(self.small) > len(self.large) + 1:
            heapq.heappush(self.large, -heapq.heappop(self.small))
        elif len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self):
        if len(self.small) > len(self.large):
            return -self.small[0]
        return (-self.small[0] + self.large[0]) / 2
```

---

### Complexity

* addNum: **O(log n)**
* findMedian: **O(1)**
* Space: **O(n)**

---

## 8. Step-by-Step Trace

### Operations:

```text
addNum(1)
addNum(2)
addNum(3)
```

---

| Step | small (max heap) | large (min heap) | Median |
| ---- | ---------------- | ---------------- | ------ |
| 1    | [1]              | []               | 1      |
| 2    | [1]              | [2]              | 1.5    |
| 3    | [2,1]            | [3]              | 2      |

---

## 9. Related Problems

1. **Sliding Window Median**
   → Same idea + deletion

2. **Kth Largest Element in Stream**
   → Heap with dynamic updates

3. **Top K Frequent Elements**
   → Heap prioritization

4. **Merge K Sorted Lists**
   → Always pick smallest

5. **Single-Threaded CPU**
   → Heap-based scheduling

---

## ⚠️ Final Interview Notes

### 🔥 Core Pattern:

👉 **Two Heaps (Max + Min)**

---

### Golden Rules:

```text
1. small holds smaller half (max heap)
2. large holds larger half (min heap)
3. size difference ≤ 1
4. median comes from heap tops
```

---

### Common Mistakes:

* Not balancing heaps ❌
* Wrong median for even count ❌
* Forgetting max heap via negatives ❌

---

## 🧠 One-Line Memory Trick

> “Median = split array into two balanced heaps”

---

If you want, I can next:

* 🔥 Show **Sliding Window Median vs Data Stream (key difference)**
* OR give a **1-page heap pattern cheat sheet (covers all problems you asked)**
