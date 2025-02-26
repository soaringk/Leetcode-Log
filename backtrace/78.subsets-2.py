#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # 子集型回溯，当前操作为选或不选。"当前操作"是唯一与 17 题不同的地方
        # 这是站在输入 path 的角度思考（另外一个角度是站在答案的视角，每次必须选一个，考虑选哪个）
        ans = []
        def dfs(i, path=[]):
            if i == len(nums): # 子问题
                ans.append(path[:])
                return
            # 当前操作
            path.append(nums[i])
            dfs(i + 1, path) # 下一个子问题
            path.pop()
            dfs(i + 1, path)
        dfs(0)
        return ans
# @lc code=end
