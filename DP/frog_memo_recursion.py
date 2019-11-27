
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

def memo_recursion(i, dp):

    if dp[i] < math.inf:
        return dp[i]

    if i == 0:
        return 0

    res = math.inf

    res = changemin(res, memo_recursion(i-1, dp) + abs(h[i] - h[i-1]))
    if i > 1:
        res = changemin(res, memo_recursion(i-2, dp) + abs(h[i] - h[i-2]))

    dp[i] = res

    return dp[i]

if __name__ == "__main__":

    # メモ用の dpテーブル作成(最小化問題より INF に初期化)
    dp = [math.inf for i in range(10000)]

    # 出力
    print(memo_recursion(N-1, dp))
