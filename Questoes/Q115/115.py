class EditStr:

    def __init__(self, s: str, t: str):
        self.s_base = s
        self.s_test = t
        self.lin = len(s)
        self.col = len(t)

        self.mem = [[0] * (self.col + 1) for _ in range(self.lin + 1)]

    def preencheMemoization(self):
        for i in range(self.lin + 1):
            self.mem[i][0] = 1

    def calcSubsequencia(self):
        for i in range(1, self.lin + 1):
            for j in range(1, self.col + 1):
                if self.s_base[i - 1] == self.s_test[j - 1]:
                    self.mem[i][j] = self.mem[i - 1][j - 1] + self.mem[i - 1][j]
                else:
                    self.mem[i][j] = self.mem[i - 1][j]

    def getNumSubseq(self) -> int:
        return self.mem[self.lin][self.col]

    def executa(self):
        self.preencheMemoization()
        self.calcSubsequencia()
        return self.getNumSubseq()

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        e = EditStr(s,t)
        return e.executa()        

#s = "rabbbit" 
#t = "rabbit"
#sol = Solution()
#print(sol.numDistinct(s,t))

#s = "babgbag" 
#t = "bag"
#print(sol.numDistinct(s,t))

