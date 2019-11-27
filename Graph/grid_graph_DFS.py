
HEIGHT = 5
WIDTH = 5
START = 'S'
GOAL = 'G'
WALL = '$'

MAZE = [
    "S....",
    "$$$$.",
    "$....",
    "$..$.",
    "$$G$.",
    ]
k = 0

def dfs(maze, seen, sx, sy):

    seen[sx][sy] = True

    # 四方向を探索
    for i,j in [[1,0],[0,1],[-1,0],[0,-1]]:
        next_x, next_y = sx+i, sy+j

        # 場外アウトしたらスルー
        if next_x < 0 or next_x >= WIDTH:
            continue

        if next_y < 0 or next_y >= HEIGHT:
            continue

        # 壁ならスルー
        if maze[next_x][next_y] == '$':
            continue

        # 再帰探索
        dfs(maze, seen, next_x, next_y)


if __name__ == '__main__':

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

    # seen[h][w]:マス(h,w)が検知済みかどうかを表す配列 最初は False で初期化
    seen = [[False for i in range(WIDTH)] for j in range(HEIGHT)]

    dfs(maze, seen, sx, sy)

    if seen[gx][gy]:
        print('YES')
    else:
        print("NO")
