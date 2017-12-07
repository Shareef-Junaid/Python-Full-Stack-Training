class Solution:
    c = []
    count = 0

    def solution(self, a, b):

        for i in range(len(a)):
            temp = (a[i]+(b[i]/1000000))
            self.c.insert(i, temp)

        print(self.c)

        for p in range(len(self.c)):
            for q in range(len(self.c)):
                if self.c[p] * self.c[q] >= self.c[p] + self.c[q] and q < p :
                    self.count = self.count + 1

        return self.count







