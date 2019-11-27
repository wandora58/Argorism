
# k階建てのビルのある階から卵を落とします。
# 卵はある階よりも低ければ割れることはなく、ある階よりも高いと割れてしまう。
# 今、あなたは卵をn個持っています。
# 卵を落とす最小回数はどれくらいか
# この問題は試行回数が最小になる階を見つけると同等

import math

def egg_drop(n,k):

    if k == 0 or k == 1:
        return k

    if  n == 1:
        return k

    min = math.inf
    for x in range(1,k+1):

        res = max(egg_drop(n-1,x-1),egg_drop(n,k-x))
        print(res)
        if min > res:
            min = res

    return min + 1



if __name__ == "__main__":

    n = 2
    k = 10

    print(egg_drop(n,k))
