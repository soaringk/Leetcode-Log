#
# @lc app=leetcode id=470 lang=python3
#
# [470] Implement Rand10() Using Rand7()
#

# @lc code=start
# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        while True:
            num = rand7() + (rand7() - 1) * 7
            # 如果在40以内，那就直接返回
            if num <= 40:
                return 1 + num % 10
            # 说明刚才生成的在41-49之间，利用随机数再操作一遍
            num = rand7() + (num - 40 - 1) * 7
            if num <= 60:
                return 1 + num % 10
            # 说明刚才生成的在61-63之间，利用随机数再操作一遍
            num = rand7() + (num - 60 - 1) * 7
            if num <= 20:
                return 1 + num % 10



# @lc code=end
