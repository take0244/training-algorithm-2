# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_2_B&lang=jp

global cnt


def swap(arr: list, i, j: int) -> list:
    global cnt
    arr[i], arr[j] = arr[j], arr[i]
    cnt += 1
    return arr


def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        if i != min_idx:
            swap(arr, i, min_idx)


if __name__ == '__main__':
    cnt = 0
    input()
    A = list(map(int, input().split()))
    selection_sort(A)
    print(*A)
    print(cnt)
