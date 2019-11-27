
node = 5 # ノード数
path = 5 # 辺数
node_path = [
    [0,1],
    [0,2],
    [1,2],
    [2,4],
    [4,3]
] # 各辺を表す親ノード、小ノードのペア

from collections import deque, defaultdict

def topological_sort(node,path,node_path):

    outs = defaultdict(list) # 各ノードから出ていく先のノードのリストの辞書
    ins = defaultdict(int) # 各ノードの入次数の辞書

    for v1, v2 in node_path:
        outs[v1].append(v2)
        ins[v2] += 1

    q = deque(i for i in range(node) if ins[i] == 0) # 入次数が0のノードを deque 型で取得
    res = []

    while q:
        v1 = q.popleft() # 先頭から取り出して削除
        res.append(v1)

        for v2 in outs[v1]: # v1ノードから出て行く先のノードに対して
            ins[v2] -= 1 # ノードに入ってくる数を1減らす
            if ins[v2] == 0: # 入次数が0なら次の探索候補に加える
                q.append(v2)

    return res

if __name__=="__main__":
    print(topological_sort(node,path,node_path))
