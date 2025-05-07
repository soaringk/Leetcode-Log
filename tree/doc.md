# 模版

```python
def traverse(root: TreeNode):
    for child in root.children:
        # 前序位置需要的操作
        traverse(child)
        # 后序位置需要的操作
```