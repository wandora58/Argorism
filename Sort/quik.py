
# クイックソート
# 基準値(ピボット)を決めて、その基準値(ピボット)から見て大小の 2 つの配列に分ける
# この基準値の選び方として、配列の最初や最後、適当な 3 つぐらいの値の中央値などを用いる
# 分けたグループの中で、更に再帰的に同じ処理を行っていく

# 走査する配列長が0か１の場合戻る。
# 走査する範囲の中央の要素をピボットとして選ぶ。
# ピボットと比べ、大きい要素は左へ小さい要素は右へ交換する。
# 左右２つに配列を分割してこの関数を再帰的に繰り返す。

def quiksort(array):

    if len(array) < 2:
        return array # 配列長が 0,1 なら return

    left = []
    right = []
    pivot = array[len(array)//2] # 基準値(ピボット) は中央値
    count = 0

    for i in range(len(array)):
        if array[i] < pivot:
            left.append(array[i])

        elif array[i] > pivot:
            right.append(array[i])

        else:
            count += 1

    return quiksort(left) + [pivot]*count + quiksort(right)

if __name__ == "__main__":

    array = [7,2,5,3,1,6,9,4,8,0,0]

    print(quiksort(array))
