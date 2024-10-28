# https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_9_B
def swap(arr: list, i, j: int) -> list:
    arr[i], arr[j] = arr[j], arr[i]
    return arr


def print_tree(arr: list):
    ln, b = 1, 0
    for i, v in enumerate(arr):
        print(v, end=" ")
        if (i - b) % ln == 0:
            print()
            b = i
            ln *= 2
    print("\n")


to_left_index = lambda index: 2 * index + 1
to_right_index = lambda index: 2 * index + 2


def heapify(arr: list, index: int, heap_size: int):
    target = index
    left_index, right_index = \
        to_left_index(index), to_right_index(index)

    if left_index < heap_size and arr[left_index] > arr[target]:
        target = left_index
    if right_index < heap_size and arr[right_index] > arr[target]:
        target = right_index

    if target != index:
        swap(arr, target, index)
        heapify(arr, target, heap_size)


def build_heap(arr: list):
    for i in range(len(arr) // 2 - 1, -1, -1):
        heapify(arr, i, len(arr))


def heap_sort(arr: list):
    build_heap(arr)
    for i in range(len(arr) - 1, 0, -1):
        swap(arr, i, 0)
        heapify(arr, 0, i)
    return arr


if __name__ == "__main__":
    input()
    Nodes = list(map(int, input().split()))
    build_heap(Nodes)
    print(' ' + ' '.join([str(v) for v in Nodes]))
