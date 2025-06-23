# 原则

## 双指针

1. 利用单调性这个信息。令指针遍历到一个非法条件时可以批量接受/拒绝一个 for 循环的结果

# 模版

#167 有序的两数之和
```python
def twoSum(self, numbers: List[int], target: int) -> List[int]:
    left = 0
    right = len(numbers) - 1
    while True:
        s = numbers[left] + numbers[right]
        if s == target:
            return [left + 1, right + 1]  # 题目要求下标从 1 开始
        if s > target:
            right -= 1
        else:
            left += 1
```
