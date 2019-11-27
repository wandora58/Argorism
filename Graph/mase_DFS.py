
MAZE = [
'$$$$$$$$',
'$ S$  G$',
'$$   $$$',
'$  $   $',
'$$$$$$$$',
]
START = 'S'
WALL = '$'
GOAL = 'G'

def solve(maze, x, y):

    # 再帰の終了条件
    if maze[x][y] == GOAL:
        return [(x, y)]

    # 今自分がいる場所 = 調べた場所を壁にしていく
    maze[x][y] = WALL

    # 今自分がいる場所から上下左右に移動を繰り返す
    # まずは右方向へ移動し 分岐ができなくなる or GOAL を見つけるまで再帰を繰り返す
    # 分岐の終了条件は「調べた場所が壁の場合(自分のいる場所は壁にしているので戻りはしない)」
    # 右方向の分岐が全て駄目だった場合、次は上方向、下方向、左方向の順で分岐を試していく = 深さ優先対策

    for next_x, next_y in [[x+1, y], [x, y+1], [x, y-1], [x-1, y]]:
        if maze[next_x][next_y] == WALL:
            continue
        route = solve(maze, next_x, next_y)
        if route:
            return [(x, y)] + route


if __name__ == "__main__":

    maze = [list(i) for i in MAZE]

    # STARTの位置を見つける
    for i,col in enumerate(maze):
        if START in col:
            x = i
            y = col.index('S')

    print(solve(maze, x, y))
