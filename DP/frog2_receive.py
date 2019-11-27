
# N 個の足場があって、i 番目の足場の高さは hi です。
# 最初、足場 1 にカエルがいて、ぴょんぴょん跳ねながら足場 N へと向かいます。カエルは足場 i にいるときに
#
# 足場 i から足場 i+1 へと移動する (そのコストは |hi−hi+1|)
# 足場 i から足場 i+2 へと移動する (そのコストは |hi−hi+2|)
# ...
# 足場 i から足場 i+K へと移動する (そのコストは |hi−hi+K|)
# のいずれかの行動を選べます。カエルが足場 1 から足場 N へと移動するのに必要な最小コストを求めよ。

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

    dp = [math.inf for _ in range(100000)]
    dp[0] = 0

    for i in range(1,N):
        for j in range(i):
            dp[i] = changemin(dp[i],dp[i-j-1] + abs(h[i] - h[i-j-1]))

    print(dp[N-1])
