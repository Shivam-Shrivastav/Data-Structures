## House Robber III
**Problem:** Houses form a **binary tree**. Cannot rob two directly linked nodes (parent-child). Maximize total money.

**Example:**
```
Input: root = [3,2,3,null,3,null,1]
      3
     / \
    2   3
     \   \
      3   1
Output: 7
Explanation: Rob nodes 3 (root), 3 (left-right), 1 (right-right)
Total = 3 + 3 + 1 = 7
```

```
Input: root = [3,4,5,1,3,null,1]
      3
     / \
    4   5
   / \   \
  1   3   1
Output: 9
Explanation: Rob nodes 4, 5, 3 = 4 + 5 + 3 = 9
```

---

### DP Intuition
- **Tree DP:** Each node returns **two values**:
  1. `rob_this`: Max if we rob this node
  2. `skip_this`: Max if we skip this node
- **Transition:**
  - If rob node: `node.val + left.skip + right.skip`
  - If skip node: `max(left.rob, left.skip) + max(right.rob, right.skip)`
- **Post-order traversal:** Process children first

---

### 1. Recursive Solution (No Memo)
```python
def rob(root):
    def dfs(node):
        if not node:
            return (0, 0)  # (rob_this, skip_this)
        
        left = dfs(node.left)
        right = dfs(node.right)
        
        # Rob this node
        rob_this = node.val + left[1] + right[1]
        # Skip this node
        skip_this = max(left) + max(right)
        
        return (rob_this, skip_this)
    
    return max(dfs(root))
```
**TC:** O(n) | **SC:** O(h) recursion stack

---

### 2. With Memoization
```python
def rob(root):
    memo = {}
    
    def dfs(node):
        if not node:
            return (0, 0)
        if node in memo:
            return memo[node]
        
        left = dfs(node.left)
        right = dfs(node.right)
        
        rob_this = node.val + left[1] + right[1]
        skip_this = max(left) + max(right)
        
        memo[node] = (rob_this, skip_this)
        return memo[node]
    
    return max(dfs(root))
```
**TC:** O(n) | **SC:** O(n)

---

**Key Formula:**
For each node:
```
rob_this = node.val + left.skip + right.skip
skip_this = max(left.rob, left.skip) + max(right.rob, right.skip)
Answer = max(rob_this, skip_this)
```

**Example Walkthrough:**
```
Tree:
      3
     / \
    2   3
     \   \
      3   1

Node (val=1):
rob=1, skip=0 → (1,0)

Node (val=3, left=null, right=null):
rob=3, skip=0 → (3,0)

Node (val=2, left=null, right=(3,0)):
rob=2+0=2, skip=max(0,0)+max(3,0)=3 → (2,3)

Node (val=3, left=null, right=(1,0)):
rob=3+0=3, skip=max(0,0)+max(1,0)=1 → (3,1)

Root (val=3, left=(2,3), right=(3,1)):
rob=3+3+1=7, skip=max(2,3)+max(3,1)=3+3=6 → (7,6)
Answer = max(7,6)=7
```

**Why Two States Work:**
- Decision at each node affects children
- `skip_this` doesn't mean children must be robbed
- Children can be robbed or skipped independently

**Alternative Approaches:**
1. **Return single value with parameter:**
```python
def dfs(node, parent_robbed):
    if not node:
        return 0
    if parent_robbed:
        # Cannot rob this node
        return dfs(node.left, False) + dfs(node.right, False)
    else:
        # Can rob or skip
        rob = node.val + dfs(node.left, True) + dfs(node.right, True)
        skip = dfs(node.left, False) + dfs(node.right, False)
        return max(rob, skip)
```

2. **Naive recursive (exponential):**
```python
def rob(root):
    if not root:
        return 0
    # Rob root
    val1 = root.val
    if root.left:
        val1 += rob(root.left.left) + rob(root.left.right)
    if root.right:
        val1 += rob(root.right.left) + rob(root.right.right)
    # Skip root
    val2 = rob(root.left) + rob(root.right)
    return max(val1, val2)
```
**TC:** O(2ⁿ) | **SC:** O(n)

**Optimization:**
- Two-state DP is optimal: O(n) time, O(h) space
- Memoization helps in unbalanced trees

**Edge Cases:**
- Empty tree → 0
- Single node → node.val
- Skewed tree → works same