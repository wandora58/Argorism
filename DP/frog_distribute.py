

# 配るDP　…　ノードiからのの遷移方法を考える

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
    for i in range(0,N-1):
        if i == N-2:
            dp[i+1] = changemin(dp[i+1], dp[i] + abs(h[i] - h[i+1]))
        else:
            dp[i+1] = changemin(dp[i+1], dp[i] + abs(h[i] - h[i+1]))
            dp[i+2] = changemin(dp[i+2], dp[i] + abs(h[i] - h[i+2]))

    # 出力
    print(dp[N-1])
