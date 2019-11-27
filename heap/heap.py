# coding=utf-8

import heapq


# ノードの交換を行うメソッド
def min_heapfy(array, i):

    left = 2*i + 1
    right = 2*i + 2
    small = i

    if left <= len(array)-1 and array[left] < array[i]:
        small = left

    if right <= len(array)-1 and array[right] < array[small]:
        small = right

    if small != i:
        array[i], array[small] = array[small], array[i]
        min_heapfy(array, small)  # ノードの交換があったならば交換されたノードに対して min_heapfy()


def insert(array, x):

    i = len(array)  # 追加するノード番号
    array.append(x)  # 追加

    while i > 0:

        p = (i-1) // 2  # 親ノード
        if array[p] <= array[i]:
            break
        array[i] = array[p]  # 親ノードの値を自分のノードに
        i = p

    array[i] = x  # 最後に追加する要素を代入

    return array


# ヒープを構築するメソッド
def build_min_heap(array):

    for i in reversed(range(len(array) // 2)):  # array の 半分のところから逆順に min_heapfy()
        min_heapfy(array, i)


# ヒープソート
def heap_sort(array):

    array = array.copy()
    build_min_heap(array)
    sorted_array = []

    for _ in range(len(array)):
        array[0], array[-1] = array[-1], array[0]  # 先頭要素と末尾要素交換
        sorted_array.append(array.pop())  # pop() で末尾要素削除して取得
        min_heapfy(array, 0)  # 先頭要素に対して min_heapfy

    return sorted_array


# python の組み込み heapq を用いると
# heapq.heappush(heap_array, item) : item を heap_array に push(ヒープ条件を保って)
# heapq.heappop(heap_array) : pop を行い heap から最小の要素を返す
#                             要素の入れ替え、末尾要素の削除、min_heapfy() の3つに相当
# heapq.heapify(array) : build_min_heapに相当


# ヒープソート
def _heap_sort(array):
    h = array.copy()
    heapq.heapify(h)
    return [heapq.heappop(h) for _ in range(len(array))]


def main():
    array = [1, 4, 2, 7, 2, 3, 8, 4, 5, 3, 2]

    print(heap_sort(array))
    # print(_heap_sort(array))

    array.sort()
    print(array)


if __name__ == "__main__":
    main()
