class Solution:
    c = []
    count = 0;

    def solution(self, a):
        temp = 0

        for p in range(len(a)) :
            for q in range(len(a)):
                    temp = temp + a[q]
                    print(p, q, temp)
                # temp = temp + a[q];

            # print(p, temp)

        # print(self.c)

        return 0