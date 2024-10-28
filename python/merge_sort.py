# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_5_B

# 問題用カウンター
global cnt


def merge_sort(arr: list, left, right, listGetter):
    if left+1 < right:
        mid = int((right + left) / 2)
        # print(arr[left: right], arr[left:mid], arr[mid:right], left, right)
        merge_sort(arr, left, mid, listGetter)
        merge_sort(arr, mid, right, listGetter)
        merge(arr, left, right, listGetter)

    return arr


def merge(arr: list, left: int, right: int, listGetter):
    global cnt

    mid = int((right + left) / 2)
    left_index, right_index = 0, 0
    L, R = arr[left:mid], arr[mid:right]
    for i in range(left, right):
        if left_index == len(L):
            arr[i:right] = R[right_index:]
            cnt += len(R[right_index:])
            break
        elif right_index == len(R):
            arr[i:right] = L[left_index:]
            cnt += len(L[left_index:])
            break

        cnt += 1
        left_value = listGetter(L, left_index)
        right_value = listGetter(R, right_index)
        if left_value > right_value:
            arr[i] = right_value
            right_index += 1
        else:
            arr[i] = left_value
            left_index += 1


if __name__ == '__main__':
    input()
    S = list(map(int, input().split()))
    cnt = 0
    merge_sort(S, 0, len(S), lambda arr, i: arr[i])
    print(' '.join([str(v) for v in S]) + "\n" + str(cnt))
