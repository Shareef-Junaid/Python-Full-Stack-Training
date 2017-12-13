class Solution:
    c = []
    count = 0;

    def solution(self, a):
        # write your code in Python 2.7
        i, j, minSum = 0, len(a) - 1, 10 ** 10
        a.sort()
        while i <= j:
            sumS = a[i] + a[j]
            minSum = min(minSum, abs(sumS))
            if sumS < 0:
                i += 1
            elif sumS > 0:
                j -= 1
            else:
                return 0
        return minSum

