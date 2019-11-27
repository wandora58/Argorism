
# N個の足場があって、i番目の足場の高さは hiです
# 最初、足場 1 にカエルがいて、ぴょんぴょん跳ねながら足場 Nへと向かいます
# カエルは足場 i にいるときに足場 i から足場 i+1 へと移動する (そのコストは |hi−hi+1|)
# 足場 i から足場 i+2 へと移動する (そのコストは |hi−hi+2|)のいずれかの行動を選べます
# カエルが足場 1 から足場 N へと移動するのに必要な最小コストを求めよ。

N = 7
h = [2,9,4,5,1,6,10]

import math

def changemin(a,b):
    if a > b:
        a = b
    return a

def changemax(a,b):
    if a < b:
        a = b
    return a

if __name__ == "__main__":

    # dpテーブル作成(最小化問題より INF に初期化)
    dp = [math.inf for i in range(10000)]

    # 初期条件
    dp[0] = 0

    # ループ
    for i in range(1,N):
        dp[i] = changemin(dp[i], dp[i-1] + abs(h[i] - h[i-1]))
        if i > 1:
            dp[i] = changemin(dp[i], dp[i-2] + abs(h[i] - h[i-2]))

    # 出力
    print(dp[N-1])
