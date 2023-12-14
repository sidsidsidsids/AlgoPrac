N = int(input())
video = [list(map(int,input())) for _ in range(N)]
ans = ''
def quadtree(I,J,size):
    global ans
    zero_cnt = 0
    for i in range(I, I+size):
        for j in range(J, J+size):
            if video[i][j] == 0:
                zero_cnt += 1

    if zero_cnt == size**2:
        ans += '0'
    elif zero_cnt == 0:
        ans += '1'
    else:
        ans += '('
        quadtree(I, J, size//2)
        quadtree(I, J+(size//2), size//2)
        quadtree(I+(size//2), J, size//2)
        quadtree(I+(size//2), J+(size//2), size//2)
        ans += ')'

quadtree(0,0,N)
print(ans)