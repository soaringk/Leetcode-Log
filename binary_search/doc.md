# 原则

1. 利用有序性质（集合传递性）
2. 搞清楚区间限制（闭区间、半开半闭、开区间），再写指针移动的判断条件
3. 思考顺序：1. 是否能利用单调性；2. 检查条件是什么；3. 上下界区间

# 技巧

## 红蓝染色法

以查找 lower_bound 为例

默认全都是白色，即不确定是否满足条件
1. false 区间染色为红色，不变量：l - 1 一定是红色（不满足条件）
2. true 区间染色为蓝色，不变量：r + 1 一定是蓝色（满足条件）
通常 left 为红色，right 为蓝色，判断 mid 应该为红还是蓝。
若要返回第一个 true，即迭代结束后反悔 r + 1 或者 l

### [] 闭区间

```
left, right = 0, len(nums) - 1
while left <= right: # 结束条件是 right 在 left 的左边
    left = mid + 1
    right = mid - 1
return right + 1 # or left
```

### [) 左闭右开区间

```
while left < right:
    left = mid + 1
    right = mid
return left # or right
```

### () 开区间

```
while left + 1 < right:
    left = mid
    right = mid
return right
```

## 四种条件转换

lower_bound 即查找下限，对应第一个 >= target 的元素。

1. >=, 查找 lower_bound: lower_bound(nums, target)
2. >, 转化成 (>=x) + 1, 即 lower_bound 的下一个位置: lower_bound(nums, target + 1)
3. <, 转化成 (>=x) - 1, 即 lower_bound 的前一个位置: lower_bound(nums, target - 1)
4. <=, 转化成 (>x) - 1, 即 lower_bound 的下一个位置的上一个位置: lower_bound(nums, target + 1) - 1

# 模版

```python
# lower_bound 返回最小的满足 nums[i] >= target 的下标 i
# 如果数组为空，或者所有数都 < target，则返回 len(nums)
# 要求 nums 是非递减的，即 nums[i] <= nums[i + 1]
def lower_bound(self, nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1  # 闭区间 [left, right]
    while left <= right:  # 区间不为空
        # 循环不变量：
        # nums[left-1] < target
        # nums[right+1] >= target
        mid = (left + right) // 2
        if nums[mid] >= target:
            right = mid - 1  # 范围缩小到 [left, mid-1]
        else:
            left = mid + 1  # 范围缩小到 [mid+1, right]
    # 循环结束后 left = right+1
    # 此时 nums[left-1] < target 而 nums[left] = nums[right+1] >= target
    # 所以 left 就是第一个 >= target 的元素下标
    return left

def searchRange(self, nums: List[int], target: int) -> List[int]:
    start = self.lower_bound(nums, target)
    if start == len(nums) or nums[start] != target:
        return [-1, -1]  # nums 中没有 target
    # 如果 start 存在，那么 end 必定存在
    end = self.lower_bound(nums, target + 1) - 1
    return [start, end]
```
