/*
Source: LeetCode 997. Find the Town Judge
*/

package main

import "fmt"

func findJudge(N int, trust [][]int) int {
	degree := make([]int, N)
	for _, edge := range trust {
		degree[edge[0]-1]--
		degree[edge[1]-1]++
	}

	for i := 1; i <= N; i++ {
		if degree[i-1] == N-1 {
			return i
		}
	}

	return -1
}

type testCase struct {
	N        int
	trust    [][]int
	expected int
}

func main() {
	var actual int

	var tests = []struct {
		N        int
		trust    [][]int
		expected int
	}{
		{1, [][]int{{}}, 1},
		{3, [][]int{{1, 3}, {2, 3}}, 3},
		{2, [][]int{{1, 3}, {2, 3}, {3, 1}}, -1},
	}

	for _, tt := range tests {
		actual = findJudge(tt.N, tt.trust)
		fmt.Println(actual, tt.expected)
	}
}
