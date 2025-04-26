# 原则

滑动窗口使用前提：

1. 连续子数组/子串。
2. 有单调性。范围越大，越接近正确答案，范围越小越没有正确答案。

# 模版

```python
def minSubArrayLen(self, target: int, nums: List[int]) -> int:
    n = len(nums)
    ans = n + 1  # 也可以写 inf
    s = left = 0
    for right, x in enumerate(nums):  # 枚举子数组右端点
        s += x
        while s - nums[left] >= target:  # 尽量缩小子数组长度
            s -= nums[left]
            left += 1  # 左端点右移
        if s >= target:
            ans = min(ans, right-left+1)
    return ans if ans <= n else 0
```
