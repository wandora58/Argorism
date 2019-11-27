
# N 個の品物があって、i 番目の品物の重さは w、価値は vi で与えられている。
# この N 個の品物から「重さの総和が W を超えないように」いくつか選びます。
# このとき選んだ品物の価値の総和の最大値を求めよ。

N = 6
W = 15
item = [[2,3],[1,2],[3,6],[2,1],[1,3],[5,85]]

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

    dp = [[0 for _ in range(W+1)] for _ in range(N+1)]

    for i in range(N):
        for sum_w in range(W+1):

            if sum_w - item[i][0] >= 0:
                dp[i+1][sum_w] = changemax(dp[i+1][sum_w], dp[i][sum_w - item[i][0]] + item[i][1])

            dp[i+1][sum_w] = changemax(dp[i+1][sum_w], dp[i][sum_w])

    print(dp[N][W])
