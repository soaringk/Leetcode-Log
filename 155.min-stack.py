#
# @lc app=leetcode id=155 lang=python3
#
# [155] Min Stack
#

# @lc code=start
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []


    def push(self, x: int) -> None:
        self.stack1.append(x)
        if not self.stack2 or x <= self.stack2[-1]:
            self.stack2.append(x)


    def pop(self) -> None:
        if self.stack1[-1] == self.stack2[-1]:
            self.stack2.pop()
        self.stack1.pop()


    def top(self) -> int:
        return self.stack1[-1]


    def getMin(self) -> int:
        return self.stack2[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end
