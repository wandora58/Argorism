
# ちょうど n 円のお釣りを払おうとしています。
# 使用できるコインは何種類かあり、i 番目のコインの額面は value[i] で与えられます。
# どのコインを何枚使っても構いません。支払うコインの枚数の最小値を計算してください。
# (常に払えると仮定して構いません)
#
# Examples
# 0)
#   [1, 2, 4, 8, 16, 32]
#   63
#   Returns: 6
#   全てのコインを 1 枚ずつ使います。
#
# 1)
#   [1, 5, 10, 50, 100, 500]
#   324
#   Returns: 9
#   日本の通貨体系です。
#
# 2)
#   [1, 4, 9]
#   17
#   Returns: 3
#   4 + 4 + 9 = 17 とするのが最適です。


def minchange(value, n):

    dp = [0 for _ in range(1000)]
    dp[0] = 0

    i = 0
    while True:

        if dp[i] == n:
            break

        for j in value:
            if dp[i] + j <= n:
                dp[i+1] = dp[i] + j

        i += 1

    return i

if __name__=="__main__":

    value = [1, 2, 4, 8, 16, 32]
    n = int(input())

    print(minchange(value, n))
