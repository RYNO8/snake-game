from snakegame.common import *
from random import choice

def conv(val):
        return (W * val[1]) + val[0]

def find(n):
        global PAR
        if n == PAR[n]:
                return n
        else:
                PAR[n] = find(PAR[n])
                return PAR[n]

cfind = lambda x: find(conv(x))

def join(a, b):
        global PAR, RANK, SIZE
        pa = cfind(a)
        pb = cfind(b)
        if pa == pb:
                return
        if RANK[pa] < RANK[pb]:
                PAR[pa] = pb
                SIZE[pb] += SIZE[pa]
        elif RANK[pb] < RANK[pa]:
                PAR[pb] = pa
                SIZE[pa] += SIZE[pb]
        else:
                PAR[pb] = pa
                RANK[pa] += 1
                SIZE[pa] += SIZE[pb]
        
def axisdis(a, b, tot):
        lo, hi = sorted([a, b])
        return min(hi - lo, tot - hi + lo)

def dis(a, b):
        return axisdis(a[0], b[0], W) + axisdis(a[1], b[1], H)

def unionfind_bot(board, pos):
        #return input(": ")
        (x, y) = pos
        me = board[y][x]
        global H, W, PAR, RANK, SIZE
        H = len(board)
        W = len(board[0])
        apple = False
        enemies = 0
        mylen = 0
        for y in range(H):
                for x in range(W):
                        if board[y][x] not in "*.":
                                if board[y][x].upper() == me:
                                        mylen += 1
                                else:
                                        enemies += 1

        RANK = [0] * (H * W)
        SIZE= [1] * (H * W)
        PAR = []
        for i in range(H * W):
                PAR.append(i)

        seen = []
        for y in range(H):
                seen.append([False] * W)
        seen[y][x] = True

        q = [pos]
        ptr = 0
        while ptr < len(q):
                x, y = q[ptr]
                ptr += 1
                for dir in directions.values():
                        nx = (x + dir[0]) % W
                        ny = (y + dir[1]) % H
                        if board[ny][nx] in ".*" and not seen[ny][nx]:
                                seen[ny][nx] = True
                                q.append((nx, ny))
                                if not apple and board[y][x] == "*":
                                        apple = (x, y)
                                if pos != (x, y):
                                        join((nx, ny), (x, y))
                        elif seen[ny][nx] and pos != (x, y):
                                join((nx, ny), (x, y))

        x, y = pos
        hi = 0
        for dir in directions:
                nx = (x + directions[dir][0]) % W
                ny = (y + directions[dir][1]) % H
                n = cfind((nx, ny))
                hi = max(hi, SIZE[n])

        poss = []
        good = []
        for dir in "DRUL":
                nx = (x + directions[dir][0]) % W
                ny = (y + directions[dir][1]) % H
                if SIZE[cfind((nx, ny))] == hi:
                        poss.append((dir, board[ny][nx]))
        
        for (dir, loc) in poss:
                if mylen < H and not enemies:
                        #if we can't wrap around yet but there aren't enemies about
                        if apple:
                                nx = (x + directions[dir][0]) % W
                                ny = (y + directions[dir][1]) % H
                                if dis((nx, ny), apple) < dis((x, y), apple):
                                        return dir
                elif enemies:
                        if loc == ".":
                                good.append(dir)
                else:
                        if hi == 1 and mylen == H * W - 1:
                                print("matt_bot covered the board :D")
                        if False:#mylen > H:
                                print("matt_bot is going to win, suiciding to make it quicker")
                                return "U"
                        return dir
        if good:
                return choice(good)
        elif enemies and mylen == 1:
                for dir in "DRUL":
                        nx = (x + directions[dir][0]) % W
                        ny = (y + directions[dir][1]) % H
                        if SIZE[cfind((nx, ny))] >= 2:
                                if board[ny][nx] == ".":
                                        return dir

        return choice(poss)[0]


# Test code to run the snake game.
# Leave the if statement as is, otherwise I won't be able to run your bot with
# the other bots.
if __name__ == '__main__':
        from snakegame.engines.pyglet import PygletEngine
        p = PygletEngine(25, 25, 50, wrap=True)
        p.add_bot(unionfind_bot)
        p.run()
