
# 試し割り法
# 与えられた整数 n に対して、nより小さい数で割り切れるかどうかを順番に確かめることで素数判定を行う
# 既に確かめた数の倍数について確かめる必要はないため、素因数候補として確かめる数を素数のみとすることで、労力を削減できる
# 素因数候補として確かめるべきは sqrt(n) までで十分

import math

def trial_division(n):

    # 素因数を格納するリスト
    factor = []

    # 2から sqrt(n) までで割っていく
    tmp = int(math.sqrt(n))+1
    for num in range(2,tmp):
        while n % num == 0:
            n //= num
            factor.append(num)

    # リストが空ならそれは素数
    if not factor:
        return "prime number"

    else:
        factor.append(n)
        # factor = set(factor) # 素数の集合
        return factor

    return 0

if __name__ == "__main__":

    n = int(input())
    print(trial_division(n))
