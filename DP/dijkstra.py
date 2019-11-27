
# スタート:ノード0
# ゴール:ノード6

path = [
    [-1,4,3,-1,-1,-1],
    [4,-1,6,8,1,-1],
    [3,6,-1,6,4,-1],
    [-1,8,6,-1,6,1],
    [-1,1,4,6,-1,6],
    [-1,-1,-1,1,6,-1],
]

node = len(path)

if __name__ == "__main__":

    # dpテーブル 50は最大距離　checked 距離を確定したか表す
    dp = [[0 for _ in range(node)] for _ in range(50)]
    checked = [0 for _ in range(node)]

    # 初期化
    dp[0][0] = 1
    checked[0] = 1

    for i in range(50):
        for j in range(node):

            if checked[j] == 0 and dp[i][j] > 1:
                checked[j] = 1

            if checked[-1] == 1:
                smallest = dp[i][j]
                break

            if dp[i][j] > 0:
                for k in range(node):
                    if path[j][k] > 0:
                        dp[i+path[j][k]][k] = i+path[j][k]

        if checked[-1] == 1:
            break

    print(smallest)
