
# マージソート
# 再帰を利用したソートアルゴリズム
# 配列を分割してからマージする

# 分割
# まずは配列の長さ n を求める　
# 次に mid = (0+(n-1))/2 で真ん中の値を求め left = 0~mid までと right = mid+1~n-1 までの配列二つに分割
# それらを繰り返し分割していき配列の長さが 1 になれば分割を終了
# 分割では各々の配列が二つの配列に分かれる為、二分木構造のように 1 つの長い配列が親となり、2つの同じ長さの短い配列を子として持つ
# この結果、深さが log2(n) の木構造が作成される

#               12 9 15 3 8 17 6 1
#
#          12 9 15 3          8 17 6 1        ↓　分割
#
#        12 9     15 3      8 17    6 1       ↓　分割
#
#       12   9   15   3    8   17  6   1      ↓　分割  深さ log2(8) = 4



# マージ
# マージをする際には 2つの子配列の先頭の要素を比較して親のリストの先頭に入れる
# 要素が余ったらリストの要素を順に格納
# これを木構造の末端ノードからルートノードまで順に繰り返していくと、最後のルートノードで並べ替えられた配列が出来上がっている


#               1 3 6 8 9 12 15 17
#
#          3 9 12 15          1 6 8 17        ↑　マージ
#
#        9 12     3 15      8 17    1 6       ↑　マージ
#
#       12   9   15   3    8   17  6   1      ↑　マージ



#　　　　　　　        マージの部分
#
#      array           3
#                         ↑　　　　　　先頭要素を比較して 3 を親リストに格納
#    left  right    9 12      15
#
#                      3 9
#                         ↑　　　　　　先頭要素を比較して 9 を親リストに格納
#                     12      15
#
#                      3 9 12
#                         ↑　　　　　　先頭要素を比較して 12 を親リストに格納
#                            15
#
#                      3 9 2 15
#                         ↑　　　　　　残りを順に格納
#

def marge(array):

    mid = len(array)

    if mid > 1:
        left = marge(array[:mid//2])
        right = marge(array[mid//2:])

        array = []
        while True:

            if left[0] < right[0]:
                array.append(left.pop(0))

                if len(left) == 0:
                    array.extend(right)
                    break

            elif left[0] > right[0]:
                array.append(right.pop(0))

                if len(right) == 0:
                    array.extend(left)
                    break

    return array


if __name__ == "__main__":

    array = [12,9,15,3,8,17,6,1]

    print(marge(array))

# 最悪計算量は 木の深さが O(logn) で 一回のマージが O(n) より O(nlog(n))
