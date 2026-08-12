## 973. K Closest Points to Origin
**Category:** **HEAP / KTH ELEMENT / SORTING**

**Problem:** Given an array of `points` where `points[i] = [xi, yi]` and an integer `k`, return the **k closest points** to the origin `(0, 0)`. Distance is Euclidean distance `√(x² + y²)`. Return in **any order**.

**Example:**
```
Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
Explanation: Distance: (1,3)=√10≈3.16, (-2,2)=√8≈2.83 → closest is (-2,2)
```

```
Input: points = [[3,3],[5,-1],[-2,4]], k = 2
Output: [[3,3],[-2,4]]
Explanation: Distances: (3,3)=√18≈4.24, (-2,4)=√20≈4.47, (5,-1)=√26≈5.10
```

---

### **Relation to Kth Element Problems**
**Similar to:** **215. Kth Largest** but with **distance metric** and **return all k closest**
**How it's different:**
1. **Kth Largest:** Return single value (kth largest)
2. **K Closest Points:** Return **all k closest** points (array)
3. **Key Insight:** Need to find the k points with smallest distances

**Key Insight:** 
- Use **max-heap of size k** to keep track of k closest points
- Max-heap stores the **largest distance among k closest** at the root
- When new point has smaller distance, replace the farthest in heap

---

### 1. Max-Heap (Optimal)
```python
import heapq

def kClosest(points, k):
    # Max-heap storing (-distance, point)
    # Using negative to simulate max-heap
    heap = []
    
    for x, y in points:
        dist = -(x*x + y*y)  # Negative for max-heap behavior
        
        if len(heap) < k:
            heapq.heappush(heap, (dist, [x, y]))
        elif dist > heap[0][0]:  # Current point closer than farthest in heap
            heapq.heapreplace(heap, (dist, [x, y]))
    
    return [point for _, point in heap]
```
**TC:** O(n log k) | **SC:** O(k)

---

### 2. Min-Heap (Store all, then extract k smallest)
```python
import heapq

def kClosest(points, k):
    # Min-heap storing (distance, point)
    heap = [(x*x + y*y, [x, y]) for x, y in points]
    heapq.heapify(heap)
    
    # Extract k smallest
    return [heapq.heappop(heap)[1] for _ in range(k)]
```
**TC:** O(n + k log n) | **SC:** O(n)

---

### 3. QuickSelect (Hoare's Selection Algorithm)
```python
import random

def kClosest(points, k):
    # Precompute distances squared (no need for sqrt)
    distances = [(x*x + y*y, [x, y]) for x, y in points]
    
    def quick_select(left, right, k):
        if left == right:
            return
        
        # Random pivot
        pivot_idx = random.randint(left, right)
        pivot_dist = distances[pivot_idx][0]
        
        # Move pivot to end
        distances[pivot_idx], distances[right] = distances[right], distances[pivot_idx]
        
        # Partition: [< pivot] [pivot] [>= pivot]
        store_idx = left
        for i in range(left, right):
            if distances[i][0] < pivot_dist:
                distances[store_idx], distances[i] = distances[i], distances[store_idx]
                store_idx += 1
        
        # Move pivot to final position
        distances[store_idx], distances[right] = distances[right], distances[store_idx]
        
        # pivot is now at store_idx
        if k < store_idx:
            quick_select(left, store_idx - 1, k)
        elif k > store_idx:
            quick_select(store_idx + 1, right, k)
    
    quick_select(0, len(distances) - 1, k)
    
    return [point for _, point in distances[:k]]
```
**TC:** O(n) average, O(n²) worst | **SC:** O(n)

---

### 4. Sorting (Simplest)
```python
def kClosest(points, k):
    # Sort by distance squared
    points.sort(key=lambda p: p[0]*p[0] + p[1]*p[1])
    return points[:k]
```
**TC:** O(n log n) | **SC:** O(1) (if in-place sort)

---

### 5. Heap with Distances Precomputed
```python
import heapq

def kClosest(points, k):
    heap = []
    
    for x, y in points:
        dist = x*x + y*y
        
        if len(heap) < k:
            # Max-heap using negative distance
            heapq.heappush(heap, (-dist, x, y))
        elif -heap[0][0] > dist:  # Compare positive distances
            heapq.heapreplace(heap, (-dist, x, y))
    
    return [[x, y] for _, x, y in heap]
```
**TC:** O(n log k) | **SC:** O(k)

---

**Key Insight (Max-Heap):**
- We want the **k smallest** distances
- Maintain a max-heap of size k containing the **k smallest** distances seen so far
- Heap root = **largest distance among k smallest** = kth closest distance
- When new point has smaller distance, replace the farthest one

**Example Walkthrough (Max-Heap):**
```
points = [[3,3],[5,-1],[-2,4]], k=2

Compute distances squared:
(3,3) → 18
(5,-1) → 26
(-2,4) → 20

k=2, heap size = 2

Process (3,3):
  heap=[(-18, [3,3])]

Process (5,-1):
  heap=[(-26, [5,-1]), (-18, [3,3])]  (heap[0] is -26, largest negative = smallest distance)

Process (-2,4):
  dist=20, heap[0]=-26 → -(-26)=26 > 20? Yes, so replace
  heapreplace: pop (-26, [5,-1]), push (-20, [-2,4])
  heap=[(-20, [-2,4]), (-18, [3,3])]

Result: [[-2,4], [3,3]]
```

**Comparison Table:**

| Approach | Time | Space | Pros | Cons |
|----------|------|-------|------|------|
**Max-Heap** | O(n log k) | O(k) | Best for large n, streaming | Need max-heap simulation |
**Min-Heap + Extract** | O(n + k log n) | O(n) | Simple | Stores all points |
**QuickSelect** | O(n) avg | O(n) | Optimal average | O(n²) worst |
**Sorting** | O(n log n) | O(1) | Simplest | Not optimal for large n |

**K Closest Family:**

| Problem | Key Difference |
|---------|---------------|
**973. K Closest Points to Origin** | Return k closest (Euclidean distance) |
**215. Kth Largest** | Return single value (kth largest) |
**347. Top K Frequent Elements** | Frequency based |
**378. Kth Smallest in Sorted Matrix** | 2D matrix, binary search |
**692. Top K Frequent Words** | Frequency + lexicographic order |

**Edge Cases:**
- k = 0 → empty list
- k = len(points) → all points
- Points with same distance → any order acceptable
- Negative coordinates → distance squared works fine
- Points at origin (0,0) → distance 0

**Why Max-Heap for Smallest Distances:**
```
To find k smallest:
- Use max-heap to store k smallest candidates
- Root = largest among k smallest (kth smallest)
- New element smaller than root → replace
- This ensures heap always contains k smallest seen so far
```

**Distance Calculation:**
- No need to compute √(x² + y²) - compare squared distances
- Avoids floating point precision issues
- Faster computation

**Space-Time Tradeoff:**
- **Sorting:** Simple but O(n log n)
- **Heap (size k):** Best for large n, only O(k) space
- **QuickSelect:** Optimal average time but modifies input
- **Heap (all points):** Simple but uses O(n) space

**Common Pitfalls:**
- Forgetting to use squared distance (no sqrt)
- Using min-heap incorrectly for max-heap requirement
- Not handling k > len(points) (though constraints prevent this)
- Using negative distances incorrectly for max-heap simulation