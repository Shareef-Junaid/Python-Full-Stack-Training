from solution import *


class GetSolution:

    def get_solution(self):
        a = [0, 1, 2, 2, 3, 5]
        b = [500000, 500000, 0, 0, 0, 20000]
        print(a)
        print(b)
        s = Solution()
        pair_count = s.solution(a, b)
        print(pair_count)


g = GetSolution()
g.get_solution()
