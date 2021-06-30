board = []
cnt = 0
for i in range(8):
    board.append(list(input()))

for j in range(8):
    if j%2 == 0:
        for k in range(0,8,2):
            if board[j][k] == 'F':
                cnt += 1
    else:
        for l in range(1,8,2):
            if board[j][l] == 'F':
                cnt += 1
print(cnt)