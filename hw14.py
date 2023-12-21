
def h(s):
    global rows, cols, blank
    v = 0
    for i in range(rows):
        for j in range(cols):
            if s[i][j] != blank:
                v += abs(i - ((s[i][j]-1) // cols))
                v += abs(j - (s[i][j]-1) % cols)
    return v

def int_encoded_state(state):
    global rows, cols
    c = 0
    for i in range(rows):
        for j in range(cols):
            c = c*(rows*cols+1) + state[i][j]
    return c

def is_goal(state):
    for i in range(rows):
        for j in range(cols):
            if state[i][j] !=cols*i+j+1:
                return False
    return True

def state_after_move(state, bi, bj, di, dj):
    global rows, cols, blank
    state_next = [[state[i][j] for j in range(cols)] for i in range(rows)]
    state_next[bi+di][bj+dj] = blank
    state_next[bi][bj] = state[bi+di][bj+dj]
    return state_next

rows, cols = map(int, input().split())

blank = rows*cols
s_init = list()
for i in range(rows):
    s_init.append(list(map(int, input().split())))
    
num_steps = -1
X = set()
Q = list()
h_root = h(s_init)
f_root = h_root
Q.append((f_root, 0, h_root, s_init))

while len(Q) > 0:
    min_idx = 0
    min_f = Q[0][0]
    for i in range(1, len(Q)):
        if Q[i][0] < min_f:
            min_idx = i
            min_f = Q[i][0]
    _, g_n, h_n, s = Q.pop(min_idx)
    
    if is_goal(s):
        num_steps = g_n
        break
    
    if int_encoded_state(s) not in X:
        bi, bj = -1, -1
        for i in range(rows):
            for j in range(cols):
                if s[i][j] == blank:
                    bi, bj = i, j
                    break
        X.add(int_encoded_state(s))
        g_nprime = g_n + 1
        for (di, dj) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if (bi + di >= 0) and (bi + di < rows) and (bj + dj >= 0) and (bj + dj < cols):
                s_nprime = state_after_move(s, bi, bj, di, dj)
                h_nprime = h(s_nprime)
                f_nprime = g_nprime + h_nprime
                Q.append((f_nprime, g_nprime, h_nprime, s_nprime))
                
print(num_steps)