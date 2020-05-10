'''
Source: LeetCode 997. Find the Town Judge
'''

from typing import List


class Solution:
    # Accepted solution, but a naive attempt
    def findJudgeBruteForce(self, N: int, trust: List[List[int]]) -> int:
        s = N * (N + 1) / 2

        if N == 1:
            return 1

        for i in range(1, N + 1):
            required_sum = s - i
            current_sum = 0
            for [truster, trusted] in trust:
                if i == truster:
                    break
                if i == trusted:
                    current_sum += truster

            if current_sum == required_sum and i != truster:
                return i

        return -1

    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        degree = [0] * N

        for [v1, v2] in trust:
            degree[v2 - 1] += 1
            degree[v1 - 1] -= 1

        for i in range(N):
            if degree[i] == N - 1:
                return i + 1

        return -1


if __name__ == '__main__':
    soln = Solution()
    test_cases = [
        ({'N': 1, 'trust': []}, 1),
        ({'N': 2, 'trust': [[1, 2]]}, 2),
        ({'N': 3, 'trust': [[1, 3], [2, 3]]}, 3),
        ({'N': 3, 'trust': [[1, 3], [2, 3], [3, 1]]}, -1),
        ({'N': 3, 'trust': [[1, 2], [2, 3]]}, -1),
        ({'N': 4, 'trust': [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]] }, 3)
    ]

    for (ip, expected) in test_cases:
        actual = soln.findJudge(ip['N'], ip['trust'])
        assert actual == expected
