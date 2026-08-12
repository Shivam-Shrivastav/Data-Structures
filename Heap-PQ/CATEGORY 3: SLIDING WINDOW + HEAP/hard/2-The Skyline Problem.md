## 🏙️ The Skyline Problem (Sweep Line + Heap Pattern)

---

## 1. Problem Statement with Example

You are given a list of buildings:

```text
buildings[i] = [left_i, right_i, height_i]
```

Each building is a rectangle on the x-axis.

👉 Return the **skyline** formed by these buildings as a list of key points:

* Each key point = `[x, height]`
* Represents a change in skyline height

---

### Example

```text
Input:
[[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]

Output:
[[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
```

---

## 2. Diagram (Visual Intuition)

![Image](https://assets.leetcode.com/uploads/2020/12/01/merged.jpg)

![Image](https://cdn.tutsplus.com/cdn-cgi/image/width%3D360/vector/uploads/2014/01/4.png)

![Image](https://miro.medium.com/v2/resize%3Afit%3A1200/1%2AESfLlWOGBumB5QVw5Sqytw.jpeg)

![Image](https://www.researchgate.net/profile/Suzan-Girginkaya/publication/257026645/figure/fig8/AS%3A707701881438210%401545740685264/a-Visual-skyline-analysis-in-the-West-East-direction-1999-b-Visual-skyline.jpg)

👉 Think:

* Sweep from left → right
* Track tallest active building at each x

---

## 3. Example I/O

### Example 1 (Typical)

```text
Input:
[[2,9,10],[3,7,15],[5,12,12]]

Output:
[[2,10],[3,15],[7,12],[12,0]]
```

### Example 2 (Edge Case: no overlap)

```text
Input:
[[1,2,1],[3,4,2]]

Output:
[[1,1],[2,0],[3,2],[4,0]]
```

---

## 4. Intuition & Pattern Recognition

### 🔑 Key Signals:

* “Overlapping intervals” → **Sweep Line**
* “Need max height at each point” → **Max Heap**
* “Track active buildings” → dynamic structure

---

### 🧠 Interview Thought:

> “Process all start/end events → maintain current max height using heap”

---

## 5. Simpler Version

### Step 1:

👉 No overlaps → just output edges

### Step 2:

👉 Overlaps → need max height at each point

### Step 3:

👉 Dynamic add/remove → heap required

---

### Related Simpler Problems:

* **Merge Intervals**
* **Meeting Rooms II**
* **Sliding Window Maximum**

---

### Build-up Thinking:

```text
Intervals → overlaps → need active set  
Active set → need max → heap  
Dynamic removal → lazy removal
```

---

## 6. Brute Force

### Idea:

* For every x-coordinate:

  * check all buildings
  * find max height

```python
def getSkyline(buildings):
    xs = set()
    for l, r, _ in buildings:
        xs.add(l)
        xs.add(r)

    xs = sorted(xs)
    res = []

    for x in xs:
        max_h = 0
        for l, r, h in buildings:
            if l <= x < r:
                max_h = max(max_h, h)

        if not res or res[-1][1] != max_h:
            res.append([x, max_h])

    return res
```

### Complexity

* Time: **O(n²)**
* Space: **O(n)**

---

## 7. Optimal Solution (Sweep Line + Max Heap)

### Idea:

1. Convert buildings into events:

   * Start → `(x, -height, right)`
   * End → `(x, 0, 0)`
2. Sort events
3. Use max heap → `(height, right)`
4. Remove expired buildings

---

### Code

```python
import heapq

def getSkyline(buildings):
    events = []
    
    # create events
    for l, r, h in buildings:
        events.append((l, -h, r))  # start
        events.append((r, 0, 0))   # end

    events.sort()

    res = []
    heap = [(0, float('inf'))]  # (height, right)

    prev_max = 0

    for x, neg_h, r in events:
        # remove expired buildings
        while heap and heap[0][1] <= x:
            heapq.heappop(heap)

        # add new building
        if neg_h != 0:
            heapq.heappush(heap, (neg_h, r))

        curr_max = -heap[0][0]

        if curr_max != prev_max:
            res.append([x, curr_max])
            prev_max = curr_max

    return res
```

---

### Complexity

* Time: **O(n log n)**
* Space: **O(n)**

---

## 8. Step-by-Step Trace

### Input:

```text
[[2,9,10],[3,7,15]]
```

---

### Events:

```text
(2,-10,9)
(3,-15,7)
(7,0,0)
(9,0,0)
```

---

| x | Heap    | Max Height | Output |
| - | ------- | ---------- | ------ |
| 2 | [10]    | 10         | [2,10] |
| 3 | [15,10] | 15         | [3,15] |
| 7 | [10]    | 10         | [7,10] |
| 9 | []      | 0          | [9,0]  |

---

## 9. Related Problems

1. **Meeting Rooms II**
   → Track overlapping intervals

2. **Merge Intervals**
   → Basic interval overlap handling

3. **Sliding Window Maximum**
   → Maintain max dynamically

4. **Employee Free Time**
   → Interval merging + gaps

5. **Car Pooling**
   → Sweep line + events

---

## ⚠️ Final Interview Notes

### 🔥 Core Pattern:

👉 **Sweep Line + Max Heap**

---

### Key Insights:

```text
1. Convert intervals → events  
2. Process left → right  
3. Maintain active buildings (heap)  
4. Track max height changes  
```

---

### Common Mistakes:

* Not removing expired buildings ❌
* Wrong event sorting ❌
* Missing duplicate x handling ❌

---

## 🧠 One-Line Memory Trick

> “Skyline = sweep line + track tallest active building”

---

If you want, I can next:

* 🔥 Give **clean mental template for all sweep line problems**
* OR compare **Skyline vs Meeting Rooms vs Car Pooling (pattern clarity)**
