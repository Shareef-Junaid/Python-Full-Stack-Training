from solution import *


class GetSolution:

    def get_solution(self):
        a = [2, -4, 6, -3, 9]

        print(a)

        s = Solution()
        slice_count = s.solution(a)
        print(slice_count)


g = GetSolution()
g.get_solution()
