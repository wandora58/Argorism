
# N 日間の夏休みです。i 日目には、
#
# A: 海で泳ぐ。幸福度 ai を加算
# B: 山で虫取りする。幸福度 bi を加算
# C: 家で宿題をする。幸福度 ci を加算
#
# の三択の中から好きなものを選ぶことができます。
# ただし、2 日連続で A, B, C のうちの同一種類の活動を選択をすることはできません
# この制約下で最終的に得られる幸福度の総和を最大にせよ。

N = 3
a = [3,6,1]
b = [4,5,2]
c = [5,2,1]

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

    dp = [[-math.inf for _ in range(10)] for _ in range(3)]

    dp[0][0] = 0
    dp[1][0] = 0
    dp[2][0] = 0

    for i in range(0,N):
        dp[0][i+1] = changemax(dp[0][i+1], dp[1][i] + b[i])
        dp[0][i+1] = changemax(dp[0][i+1], dp[2][i] + c[i])

        dp[1][i+1] = changemax(dp[1][i+1], dp[0][i] + a[i])
        dp[1][i+1] = changemax(dp[1][i+1], dp[2][i] + c[i])

        dp[2][i+1] = changemax(dp[2][i+1], dp[0][i] + a[i])
        dp[2][i+1] = changemax(dp[2][i+1], dp[1][i] + b[i])

    print(max(dp[0][N], dp[1][N], dp[2][N]))
