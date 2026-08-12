## 🧠 LeetCode: **Construct Target Array With Multiple Sums** (Heap / Greedy Reverse Simulation)

---

## 1. **Problem Statement**

You are given an array `target`.

You start with an array `arr` of same length, initially:

```text
arr = [1, 1, 1, ..., 1]
```

Operation:

* Pick an index `i`
* Set:

```text
arr[i] = sum(arr)
```

👉 Return **true** if you can construct `target` from `[1,1,...,1]`, else `false`.

---

### Constraints

* `1 <= target.length <= 5 * 10^4`
* `1 <= target[i] <= 10^9`

---

## 2. **Diagram (Reverse Thinking)**

```text
Forward:
[1,1,1] → pick i → [1,1,3] → pick i → [1,4,3] → ...

Reverse:
[1,4,3]
→ largest = 4
→ previous value = 4 - (sum of rest = 4)
→ new = 0 ❌ invalid
```

---

### Core Trick:

👉 Instead of building forward → **simulate backward**

---

## 3. **Example I/O**

### ✅ Example 1

```text
Input: target = [9,3,5]
Output: true
```

✔ Reverse steps:

```text
[9,3,5] → [1,3,5] → [1,3,1] → [1,1,1]
```

---

### ❌ Example 2

```text
Input: [1,1,1,2]
Output: false
```

✔ Cannot reach base array

---

### ⚠️ Edge Case

```text
Input: [1]
Output: true
```

✔ Already base case

---

## 4. **Intuition & Pattern Recognition**

### 🔑 Signals:

* Operation replaces element with **sum of array**
* Values grow very large
* Direct simulation impossible

---

### 💡 Key Insight:

👉 The largest element must be the **last updated**

So:

```text
previous_value = largest - (sum of rest)
```

---

### 🧠 Interview Thought:

> "Always reverse the operation → focus on largest element → use max heap"

---

## 5. **Simpler Version**

### 🔹 Simpler Problem:

👉 “Keep subtracting sum of rest from largest”

---

### 🔹 Even Simpler:

👉 Only 2 elements → `[x, y]`

Then:

```text
x = x % y
```

---

### 🔥 Transition Thinking:

```text
Naive reverse:
→ largest -= rest

Optimized:
→ largest %= rest  (jump multiple steps)
```

---

### 🔑 Core Leap:

* Replace repeated subtraction with **modulo**

---

## 6. **Brute Force**

### Idea:

* Repeatedly subtract sum of rest from largest

### Complexity:

* Very slow ❌ (TLE due to large values)

---

## 7. **Optimal Solution (Max Heap + Math)**

---

### ✅ Code (Python)

```python
import heapq

def isPossible(target):
    if len(target) == 1:
        return target[0] == 1
    
    total = sum(target)
    
    # max heap (use negative values)
    max_heap = [-x for x in target]
    heapq.heapify(max_heap)
    
    while True:
        largest = -heapq.heappop(max_heap)
        rest = total - largest
        
        # base cases
        if largest == 1 or rest == 1:
            return True
        
        if rest == 0 or largest < rest:
            return False
        
        # reverse operation
        new_val = largest % rest
        
        # edge case
        if new_val == 0:
            return False
        
        # update
        total = rest + new_val
        heapq.heappush(max_heap, -new_val)
```

---

### ⏱ Complexity:

* Time: **O(n log n)**
* Space: **O(n)**

---

## 8. **Step-by-Step Trace**

### Input:

```text
target = [9,3,5]
```

---

| Step | Largest | Rest | New Value | New Array |
| ---- | ------- | ---- | --------- | --------- |
| 1    | 9       | 8    | 1         | [1,3,5]   |
| 2    | 5       | 4    | 1         | [1,3,1]   |
| 3    | 3       | 2    | 1         | [1,1,1]   |

✔ Success

---

## 9. **Related Problems**

1. **Last Stone Weight**

   * Use max heap, repeatedly reduce largest elements

2. **Split Array Into Consecutive Subsequences**

   * Greedy decisions with structure

3. **Minimum Operations to Reduce X to Zero**

   * Reverse thinking

4. **Reduce Array Size to The Half**

   * Heap + greedy removal

5. **Kth Largest Element in an Array**

   * Max heap fundamentals

---

## 🧠 Final Interview Insight

👉 Core idea:

> "Work backward: largest element must have been created last"

---

### 🔥 Key Observations

```text
1. Always pick largest element
2. Replace repeated subtraction with modulo
3. Use max heap for efficiency
```

---

### 🚨 Critical Edge Cases

* `rest == 0` → invalid
* `largest < rest` → impossible
* `new_val == 0` → invalid
* `rest == 1` → always possible

---

## ⚡ One-Line Memory Trick

> "Largest came from sum → reverse with modulo"

---

If you want, I can:

* 🔥 Give a **deep intuition proof (why modulo works)**
* OR compare this with **Euclidean algorithm (they are closely related)**
