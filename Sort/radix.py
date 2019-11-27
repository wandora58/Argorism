
# 基数ソート
# バケットソートの発展版　
# バケットソートは配列中の数値が巨大になると厳しい
# そこで基数ソートの出番で、例えば配列中の数値が 7 桁以内であることがわかっていたら
#
# まず 1 の位について計数ソートする
# 次に 10 の位について計数ソートする
# 次に 100 の位について計数ソートする
# 　…
# 最後に 1,000,000 の位について計数ソートする

# 例えば、{ 151, 129 } を1桁目をキーにソートすると { 151, 129 }
# 続けて2桁目でソートすると { 129, 151 } となります


def radixsort(array,m):

    bucket = list()
    for i in range(10):
        bucket.append(list())

    # m桁分バケットソート
    for d in range(1,m+1):
        r = 10 **(d-1)

        for val in array:
            key = int(val/r) % 10
            # d 桁目の値を取り出す
            # ex) d = 1
            #     r = 10**(0) = 1
            #   key = (55 / 1) % 10 = 5 (1 桁目が取り出せる)
            bucket[key].append(val)
            # d 桁目の値によってバケットを作る

        # バケットの値を順に配列に戻す
        i = 0
        for values in bucket:
            for val in values:
                array[i] = val
                i += 1

        # バケットの中身を初期化
        for j in range(len(bucket)):
            bucket[j] = list()

    return array


if __name__ == "__main__":

    array = [1000,55,343,441,5454]
    m = 4 # 最大の桁数

    print(radixsort(array,m))
