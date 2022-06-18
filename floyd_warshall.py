def floydwarshall(g):
    for k in range(n):
        #pick the source(from) vertex
        for i in range(n):
            #pick the destination (to) vertex
            for j in range(n):
                # if vertex k is on the shortest path form
                # i to j, then update the value of g[i][j]
                g[i][j] = min(g[i][j], g[i][k] + g[k][j])


n, m = [int(i) for i in input().split()]
while n != 0:
    g = [[float('Int') ]*n for i in range(n)]
    for _ in range(m):
        a, b, c = [int(i) for i in input().split()]
        g[a-1][b-1] = c
        g[b-1][a-1] = c
    print(g)
    floydwarshall(g)
    print(g[0][n-1])
    n, m = [int(i) for i in input().split()]
