
import math
INF = math.inf

route = [
    [INF,5,4,2,INF,INF],
    [INF,INF,2,INF,INF,6],
    [INF,INF,INF,INF,2,INF],
    [INF,INF,3,INF,6,INF],
    [INF,INF,INF,INF,INF,4],
    [INF,INF,INF,INF,INF,INF]
]


def dijkstra(nodes):

    visited = [0 for _ in range(nodes)] # 訪れたかどうか
    before = [None for _ in range(nodes)] # 1個前のノード
    distance = [INF for _ in range(nodes)] # 距離
    distance[0] = 0

    while True:

        # 探索候補(visited == 0)のなかで暫定最短距離が最も小さいノードを確定ノードとする
        min_dis = INF
        for node in range(nodes):
            if visited[node] == 0 and distance[node] < min_dis:
                fix_node = node # 確定ノード
                min_dis = distance[fix_node] # 確定ノードまでの距離

        if min_dis == INF:
            break

        # 確定ノードを訪問済みにする
        visited[fix_node] = 1

        # 確定ノードから伸びる辺を用いて暫定最短距離を更新できるノードがあるなら更新
        for node in range(nodes):
            if distance[node] > distance[fix_node] + route[fix_node][node]:
                distance[node] = distance[fix_node] + route[fix_node][node]
                before[node] = fix_node

    i = nodes - 1
    path = []
    while True:
        if i == None:
            break

        path.append(str(i))
        i = before[i]

    path = ' <- '.join(path)

    return distance[nodes-1], path

if __name__== "__main__":
    nodes = 6
    distance, path = dijkstra(nodes)
    print(distance)
    print(path)
