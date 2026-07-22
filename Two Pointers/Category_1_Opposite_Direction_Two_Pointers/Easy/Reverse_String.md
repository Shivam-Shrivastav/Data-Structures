# Reverse String (LeetCode 344)

**Pattern:** Two Pointers

---

# 1. Problem Statement

You are given a character array `s`.

Reverse the array **in-place** without allocating another array.

The function should modify the input array directly.

### Constraints

* `1 <= s.length <= 10^5`
* `s[i]` is a printable ASCII character.
* **Must use O(1) extra space.**

---

# 2. Diagram

Example:

```text
s = ['h','e','l','l','o']

Initial

L                 R
↓                 ↓
h   e   l   l   o

Swap

o   e   l   l   h
    L       R

Swap

o   l   l   e   h
        ↑
      Stop

Answer

o l l e h
```

The pointers move toward each other after every swap.

---

# 3. Example I/O

### Example 1

```text
Input:
["h","e","l","l","o"]

Output:
["o","l","l","e","h"]
```

Explanation

```text
Reverse the array in-place.
```

---

### Example 2

```text
Input:
["H","a","n","n","a","h"]

Output:
["h","a","n","n","a","H"]
```

---

### Example 3 (Edge Case)

```text
Input:
["a"]

Output:
["a"]
```

A single character remains unchanged.

---

# 4. Intuition & Pattern Recognition

### Signals

Whenever you see:

* Reverse an array/string
* In-place modification
* O(1) extra space
* Start and end elements are related

Think:

> **Two Pointers**

---

### Interview Thinking

Tell yourself:

```text
The first element should go to the last position,
and the last element should come to the first.

Instead of creating another array,
swap both ends and move inward.
```

---

# 5. Simpler Version

## Simpler Question 1

### Swap Two Numbers

```text
a, b = b, a
```

Learn the basic swap operation.

---

## Simpler Question 2

### Reverse an Array (using extra array)

```text
result = arr[::-1]
```

Easy but uses O(N) extra space.

---

## Current Question

Need to reverse **without extra memory**.

```text
Left ↔ Right

Swap

Move inward

Repeat
```

---

### Thinking Progression

```text
Swap two elements

↓

Reverse using extra array

↓

Observe first ↔ last relationship

↓

Use two pointers

↓

Reverse in-place
```

---

# 6. Brute Force

Create another array.

Copy elements from the end to the beginning.

```python
result = []

for i in range(len(s)-1, -1, -1):
    result.append(s[i])

Copy result back into s
```

### Complexity

```text
Time  : O(N)

Space : O(N)
```

---

# 7. Optimal Solution (Two Pointers)

### Idea

Maintain two pointers:

```text
left = 0
right = n-1
```

While `left < right`:

* Swap both characters.
* Move both pointers inward.

---

### Python

```python
class Solution:
    def reverseString(self, s: List[str]) -> None:

        left = 0
        right = len(s) - 1

        while left < right:

            # Swap characters
            s[left], s[right] = s[right], s[left]

            # Move pointers inward
            left += 1
            right -= 1
```

---

### Complexity

```text
Time  : O(N)

Space : O(1)
```

Each character is swapped at most once.

---

# 8. Step-by-Step Trace

Example

```text
s = ['h','e','l','l','o']
```

| Left | Right | Swap  | Array     |
| ---- | ----- | ----- | --------- |
| 0    | 4     | h ↔ o | o e l l h |
| 1    | 3     | e ↔ l | o l l e h |
| 2    | 2     | Stop  | o l l e h |

Final Answer

```text
["o","l","l","e","h"]
```

---

# 9. Related Problems

| Problem                                     | Connection                                                         |
| ------------------------------------------- | ------------------------------------------------------------------ |
| **125. Valid Palindrome**                   | Uses two pointers moving inward while skipping invalid characters. |
| **680. Valid Palindrome II**                | Similar inward traversal, with one allowed deletion.               |
| **977. Squares of a Sorted Array**          | Uses two pointers from both ends to build the answer.              |
| **167. Two Sum II - Input Array Is Sorted** | Two pointers move based on the current sum.                        |
| **344. Reverse String II (LeetCode 541)**   | Extension where only every `k` characters are reversed.            |

---

# Key Interview Takeaways

* **Pattern:** Two Pointers.
* **Pointers:** `left` starts at the beginning, `right` at the end.
* **Invariant:** Everything outside `[left, right]` is already in its final position.
* **Rule:** Swap the two ends and move inward until the pointers meet.
* **Complexity:** **O(N)** time and **O(1)** extra space.

---

**Pattern Summary**

```text
Need to reverse?

↓

Can use extra space?
    Yes → Create new array

↓

Need O(1) space?

↓

Use Two Pointers

↓

Swap ends

↓

Move inward

↓

Done
```

Reference style matches your sliding-window revision sheet format. 
