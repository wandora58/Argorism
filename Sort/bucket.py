
# バケットソート
# あらかじめデータがとりうる値すべての容器(バケット)を順番どおりに並べて用意しておき、
# 値を対応する容器に移し、上から順に並べることでソートを行う

def bucketsort(array):

    largest = max(array)
    bucket = [0 for _ in range(largest+1)]

    for i in array:
        bucket[i] += 1

    sorted = []
    for i in range(len(bucket)):
        if bucket[i] > 0:
            for j in range(bucket[i]):
                sorted.append(i)

    return sorted

if __name__ == "__main__":

    array = [2,6,4,6,2,1,5,6,8]

    print(bucketsort(array))

# 計算量は O(n+A)
# ただし適用場面はキー値が 1 から A までの整数値であり、しかも A が A=O(n) 程度の小ささである場合に限られる
