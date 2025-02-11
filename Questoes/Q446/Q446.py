from collections import defaultdict

class CompSequencia:
    
    nums : list[int]
    mem : list[dict]
    num_ss : int

    def __init__(self, nums : list[int]):
        self.nums = nums
        self.num_ss = 0
        self.mem  = [defaultdict(int) for _ in range(len(self.nums))]

    def calcSubSeq(self):
        for i in range(len(self.nums)):
            for j in range(i):
                dif = self.nums[i] - self.nums[j]
                seq_count = self.mem[j][dif]
                
                self.mem[i][dif] += seq_count + 1
                
                self.num_ss += seq_count

    def getNumSubSeq(self) -> int:
        return self.num_ss

    def execute(self) -> int:
        self.calcSubSeq()
        return self.getNumSubSeq()

class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        s = CompSequencia(nums)
        return s.execute()


nums = [2,4,6,8,10]
s = Solution()
print(s.numberOfArithmeticSlices(nums))

nums = [7,7,7,7,7]
print(s.numberOfArithmeticSlices(nums))

