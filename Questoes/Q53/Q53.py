class MaxSomaSub:
    
    max_soma_atual : int
    max_soma : int
    nums : list[int]

    def __init__(self, nums : list[int]):
        self.nums = nums
        self.max_soma_atual = self.nums[0]
        self.max_soma = self.nums[0]

    def calcMaxSun(self) -> int:

        for i in range(1, len(self.nums)):
            self.max_soma_atual = max(self.nums[i], self.max_soma_atual + self.nums[i])
            self.max_soma = max(self.max_soma, self.max_soma_atual)

        return self.max_soma 

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        s = MaxSomaSub(nums)
        return s.calcMaxSun()

#nums = [-2,1,-3,4,-1,2,1,-5,4]
#s = Solution()
#print(s.maxSubArray(nums))

#nums = [1]
#print(s.maxSubArray(nums))

#nums = [5,4,-1,7,8]
#print(s.maxSubArray(nums))
