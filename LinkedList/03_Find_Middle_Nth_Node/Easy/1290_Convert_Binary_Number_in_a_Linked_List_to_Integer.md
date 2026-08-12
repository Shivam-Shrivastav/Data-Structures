# 1290. Convert Binary Number in a Linked List to Integer

## 1. Problem Statement with Example

Given the head of a singly linked list where each node contains either:

```text
0 or 1
```

The linked list represents a binary number.

Return its decimal (base-10) value.

---

## Example

```text
1 → 0 → 1
```

This represents binary:

```text
101₂
```

Which equals:

```text
5
```

So output:

```text
5
```

---

## Constraints

```text
1 <= number of nodes <= 30
Node.val is either 0 or 1
```

Important:

* Nodes are ordered from **most significant bit → least significant bit**
* Need binary-to-decimal conversion

---

# 2. Diagram

```text
Linked List:
1 → 0 → 1 → 1

Binary Formation:
((1 * 2 + 0) * 2 + 1) * 2 + 1

Step-by-step:
1
10
101
1011

Decimal:
11
```

---

# 3. Example I/O

## Example 1

### Input

```text
[1,0,1]
```

### Output

```text
5
```

### Why?

```text
101₂ = 5
```

---

## Example 2

### Input

```text
[0]
```

### Output

```text
0
```

---

## Example 3

### Input

```text
[1,1,1,1]
```

### Output

```text
15
```

### Why?

```text
1111₂ = 15
```

---

# 4. Intuition & Pattern Recognition

## Biggest Clue

Whenever you see:

```text
binary digits arriving left to right
```

Think:

# Multiply current number by 2

because binary shifting works like:

```text
current = current * 2 + new_bit
```

---

## Example

```text
1 → 0 → 1
```

Process:

```text
num = 0

num = 0*2 + 1 = 1
num = 1*2 + 0 = 2
num = 2*2 + 1 = 5
```

Done.

---

## Interview Recognition Trick

If digits come sequentially:

```text
append digit to number
```

then think:

```text
new_num = old_num * base + digit
```

For:

* decimal → multiply by 10
* binary → multiply by 2

---

# 5. Simpler Version

## Simplest Problem

### Convert binary string to decimal

```python
"101"
```

Normally:

```python
int("101", 2)
```

But linked list does not allow direct indexing/string access.

---

## Next Simpler Version

Traverse array:

```python
[1,0,1]
```

Build number progressively.

---

## Final Problem

Same logic applied on linked list traversal.

---

## Related Simpler Problems

### 1. Binary to Decimal Conversion

Core math idea.

---

### 2. Add Binary

Builds binary intuition.

---

### 3. Reverse Linked List

Basic linked list traversal practice.

---

## Thinking Progression

```text
Binary string
      ↓
Binary array
      ↓
Linked list traversal
      ↓
Streaming binary conversion
```

---

# 6. Brute Force

## Idea

Convert linked list into binary string.

Then convert string to integer.

---

## Code

```python
class Solution:

    def getDecimalValue(self, head):

        binary = ""

        curr = head

        while curr:
            binary += str(curr.val)
            curr = curr.next

        return int(binary, 2)
```

---

## Complexity

### Time

O(n)

### Space

O(n)

(extra string)

---

# 7. Optimal Solution

# Streaming Binary Conversion

---

## Core Formula

num = num \times 2 + bit

---

## Why?

Appending a binary digit means:

* left shift existing bits
* add new bit

Equivalent to:

```text
multiply by 2
```

---

## Code

```python
class Solution:

    def getDecimalValue(self, head):

        num = 0

        curr = head

        while curr:

            # shift left and add current bit
            num = num * 2 + curr.val

            curr = curr.next

        return num
```

---

## Bit Manipulation Version

```python
class Solution:

    def getDecimalValue(self, head):

        num = 0

        while head:

            # left shift by 1
            num = (num << 1) | head.val

            head = head.next

        return num
```

---

## Complexity

### Time

O(n)

### Space

O(1)

---

# 8. Step-by-Step Trace

## Example

```text
1 → 0 → 1 → 1
```

---

## Initialization

```text
num = 0
```

---

| Node | Calculation | num |
| ---- | ----------- | --- |
| 1    | 0×2 + 1     | 1   |
| 0    | 1×2 + 0     | 2   |
| 1    | 2×2 + 1     | 5   |
| 1    | 5×2 + 1     | 11  |

---

Return:

```text
11
```

---

# 9. Related Problems

## 1. Add Binary

Binary arithmetic fundamentals.

---

## 2. Number of 1 Bits

Bit manipulation basics.

---

## 3. Reverse Bits

Binary transformation practice.

---

## 4. Binary Tree Paths

String/number building during traversal.

---

## 5. Sum of Digits Problems

Streaming numeric construction pattern.

---

# Interview One-Liner

> “While traversing, multiply current answer by 2 and add the new binary digit.”
