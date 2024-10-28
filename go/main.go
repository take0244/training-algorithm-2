// https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_5_B
package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
)

type Scanner struct {
	reader  *bufio.Reader
	writer  *bufio.Writer
	line    []string
	lineIdx int
}

func NewScanner() *Scanner {
	return &Scanner{reader: bufio.NewReader(os.Stdin)}
}

func (s *Scanner) NextLine() string {
	var result string
	for {
		line, isPrefix, err := s.reader.ReadLine()
		if err != nil {
			panic(err)
		}

		if result += string(line); !isPrefix {
			break
		}
	}

	s.line = strings.Split(result, " ")
	s.lineIdx = 0

	return result
}

func (s *Scanner) Next() (result string) {
	if s.lineIdx >= len(s.line) {
		s.NextLine()
	}
	result = s.line[s.lineIdx]
	s.lineIdx++
	return
}

func (s *Scanner) NextInt() (result int) {
	result, err := strconv.Atoi(s.Next())
	if err != nil {
		panic(err)
	}

	return
}

// 問題用のカウンター
var cnt = 0

func MergeSort(list []int, left, right int) {
	if left+1 < right {
		mid := (left + right) / 2
		MergeSort(list, left, mid)
		MergeSort(list, mid, right)
		Merge(list, left, right)
	}
}

func Merge(list []int, left, right int) {
	mid := (left + right) / 2
	leftIndex, rightIndex := 0, 0

	L, R :=
		make([]int, len(list[left:mid]), len(list[left:mid])+1),
		make([]int, len(list[mid:right]), len(list[mid:right])+1)
	copy(L, list[left:mid])
	copy(R, list[mid:right])
	L = append(L, math.MaxInt64)
	R = append(R, math.MaxInt64)
	for i := left; i < right; i++ {
		cnt++
		if L[leftIndex] < R[rightIndex] {
			list[i] = L[leftIndex]
			leftIndex++
		} else {
			list[i] = R[rightIndex]
			rightIndex++
		}
	}
}

func main() {
	cnt = 0
	sc := NewScanner()

	n := sc.NextInt()
	S := make([]int, 0, n)
	for i := 0; i < n; i++ {
		s := sc.NextInt()
		S = append(S, s)
	}

	MergeSort(S, 0, len(S))

	results := make([]string, 0, len(S))
	for _, v := range S {
		results = append(results, strconv.Itoa(v))
	}

	fmt.Println(strings.Join(results, " "))
	fmt.Println(cnt)
}
