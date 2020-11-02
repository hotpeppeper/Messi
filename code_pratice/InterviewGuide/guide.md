### 二叉树

#### 先序，中序，后序遍历二叉树

```python
# 递归实现
# 树节点
class Node:
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None
# 前序遍历
def pre_order_recur(head):
    if head is None:
        return

    print(head.value)
    pre_order_recur(head.left)
    pre_order_recur(head.right)
    
# 中序遍历
def in_order_recur(head):
    if head is None:
        return
        
    in_order_recur(head.left)
    print(head.value)
    in_order_recur(head.right)
    
# 后序遍历
def post_order_recur(head):
    if head is None:
        return
    
    post_order_recur(head.left)
    post_order_recur(head.right)
    print(head.value)
```





