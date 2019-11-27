
N = 8
M = 12
G = [[] for i in range(8)]
G[0] = [3,5,7]
G[1] = [3,4,6]
G[2] = [4,5,7]
G[3] = [0,1,7]
G[4] = [1,2,6]
G[5] = [0,2]
G[6] = [1,4,7]
G[7] = [0,2,3,6]

def dfs(G, seen, v):

    # 頂点 v を訪問済みにする
    seen[v] = True

    # vからいける各頂点 next_v について
    for next_v in G[v]:

        # next_v が探索済みならスルー
        if seen[next_v]:
            continue

        # 再帰的に探索
        dfs(G, seen, next_v)


if __name__ == "__main__":

    # # N:グラフの頂点数  M:辺数
    # N, M = map(int,input().split())
    #
    # # G:その頂点から到達可能な頂点
    # G = [[] for i in range(M)]
    #
    # for i in range(M):
    #     a, b = map(int,input().split())
    #     G[a].append(b)
    #     # 無向グラフなら
    #     G[b].append(a)

    # s:最初の頂点　t:頂点にたどり着けるか
    s, t = map(int, input().split())

    # seen:その頂点を検知済みかどうかを表す配列 最初は False で初期化
    seen = [False for i in range(N)]

    # 頂点 0 をスタートとした探索
    dfs(G, seen, 0)

    # tにたどり着けるか
    if seen[s]:
        print("Yes")
