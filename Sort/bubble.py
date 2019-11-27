
# バブルソート
# 配列の中から「大きさが逆転している部分があったら swap する」を繰り返す

# 後ろから順に隣り合う要素を比較する
# 左が右の要素に比べ大きい場合交換
# 走査範囲を前からひとつ狭める

def bubble(array):

    for i in range(len(array)):
        for j in reversed(range(i+1,len(array))):
            if array[j-1] > array[j]:
                array[j-1],array[j] = array[j],array[j-1]

    return array



if __name__ == "__main__":

    array = [2,5,7,4,2,7,5,2,1]

    print(bubble(array))

# 計算量は O(n^2)
