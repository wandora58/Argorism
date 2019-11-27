
from collections import deque
import math

MAZE = [
'$$$$$$$$',
'$S $G  $',
'$ $$$  $',
'$      $',
'$$$$$$$$',
]
START = 'S'
WALL = '$'
GOAL = 'G'

def solve(maze, sx, sy, gx, gy):

    # d = deque()でdequeオブジェクトを生成

    # d.append() 末尾(右側)に要素追加
    # d.pop 末尾(右側)から要素を削除してその値を返す

    # d.appendleft() 先頭(左側)に要素追加
    # d.popleft 先頭(左側)から要素を削除してその値を返す

    que = deque([[sx,sy]])

    # 訪れていないところを inf にする
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] != "$":
                maze[i][j] = math.inf

    # スタート位置の距離を 0 にする
    maze[sx][sy] = 0

    # まずキューから初期座標を pop
    # 上下左右の座標に対して
    #   壁じゃないなら
    #      上下左右の座標 + 1
    #      キューに上下左右の座標を append
    # 先に追加されたキューから値を pop して繰り返し

    #   $$$$
    #   $S $
    #   $ $$  ならキューの流れは
    #
    #   [[1,1]]         >> [1,1] pop
    #   [[2,1], [1,2]]  >> [2,1] pop
    #   [[1,2], [3,1]]  >> [1,2] pop

    # FIFO キュー構造より幅優先探索
    # 後に入ったものが先に出てくる

    while que:
        x, y = que.popleft()
        for i,j in [[1,0],[0,1],[-1,0],[0,-1]]:
            new_x, new_y = x+i, y+j
            dist = maze[new_x][new_y]
            if dist != '$':
                if dist > maze[x][y]+1:
                    maze[new_x][new_y] = maze[x][y]+1
                    que.append([new_x,new_y])

    return maze


if __name__ == "__main__":

    maze = [list(i) for i in MAZE]

    # STARTの位置を見つける
    for i,col in enumerate(maze):
        if START in col:
            sx = i
            sy = col.index('S')

    # GOALの位置を見つける
    for i,col in enumerate(maze):
        if GOAL in col:
            gx = i
            gy = col.index('G')

    print(solve(maze, sx, sy, gx, gy))
