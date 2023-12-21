
def check_winner(board):
    # Check rows
    for row in board:
        for i in range(len(row) - 2):
            if row[i] == row[i + 1] == row[i + 2] and row[i] != 'v':
                return f"Player {row[i]} wins!"

    # Check columns
    for col in range(len(board[0])):
        for i in range(len(board) - 2):
            if board[i][col] == board[i + 1][col] == board[i + 2][col] and board[i][col] != 'v':
                return f"Player {board[i][col]} wins!"

    # Check diagonals
    for i in range(len(board) - 2):
        for j in range(len(board[0]) - 2):
            if board[i][j] == board[i + 1][j + 1] == board[i + 2][j + 2] and board[i][j] != 'v':
                return f"Player {board[i][j]} wins!"
      
    for i in range(len(board) - 2):
        for j in range(2, len(board[0])):
            if board[i][j] == board[i + 1][j - 1] == board[i + 2][j - 2] and board[i][j] != 'v':
                return f"Player {board[i][j]} wins!"

    return "No winner yet."


def is_board_full(board):
    for row in board:
        for cell in row:
            if cell == 'v':
                return False
    return True


def is_equal_number_of_x_and_o(board):
    count_x = sum(row.count('x') for row in board)
    count_o = sum(row.count('o') for row in board)

    return count_x == count_o
#'x' �� 'o'�� ������ ������ True �ٸ��� False �� ��ȯ�ϴ� �Լ�

def generate_new_states_x(board):
    new_states = []

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'v':
                new_board = [row.copy() for row in board]
                new_board[i][j] = 'x'
                new_states.append(new_board)

    return new_states
#���� ä���� ���� ���� ��� ��ĭ�� ������ŭ�� x�� �׸� ���¸� ����Ʈ�� ��ȯ


def generate_new_states_o(board):
    new_states = []

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'v':
                new_board = [row.copy() for row in board]
                new_board[i][j] = 'o'
                new_states.append(new_board)

    return new_states



def sum_weights_matching_o(weight_board, symbol_board):
    total_weight = 0

    for i in range(3):
        for j in range(3):
            if symbol_board[i][j] == 'o':
                total_weight += weight_board[i][j]

    return total_weight



def sum_weights_matching_x(weight_board, symbol_board):
    total_weight = 0

    for i in range(3):
        for j in range(3):
            if symbol_board[i][j] == 'x':
                total_weight += weight_board[i][j]

    return total_weight

def total_weight(weight_board):
    total = sum(sum(row) for row in weight_board)
    return total


def value(board , a, b,weight_board ):

    # board�� ���� ä�����ִ� ���
    if is_board_full(board)==True  :
        if check_winner(board) == "Player o wins!" :
            v=sum_weights_matching_x(weight_board,board)
            return -v

        if check_winner(board) == "Player x wins!" :
            v=sum_weights_matching_o(weight_board,board)
            return v

        if check_winner(board) == "No winner yet." :
            t=total_weight(weight_board)
            x=sum_weights_matching_x(weight_board,board)
            v = (t/2) - x
            return v

    #board�� ���� ä���� ���� ���� ��� - ����
    if is_board_full(board)==False :
        if check_winner(board) == "Player o wins!" :
            v=sum_weights_matching_x(weight_board,board)
            return -v

        if check_winner(board) == "Player x wins!" :
            v=sum_weights_matching_o(weight_board,board)
            return v


    #board�� ���� ä���� ���� ���� ��� - ��� ����
    if is_board_full(board)==False :
        #���� ä���� ���� �����鼭 �ºε� ���� �ʾҰ� 'x'�� 'o'�� ������ ������ ��� : 'x'����
        if check_winner(board) == "No winner yet." and is_equal_number_of_x_and_o(board)==True  :
            v = float('-inf')
            next_states=generate_new_states_x(board)
            for next_state in next_states :
                v=max(v,value(next_state,a,b,weight_board))
                if v >= b :
                    return v
                a = max(a,v)

        #���� ä���� ���� �����鼭 �ºε� ���� �ʾҰ� 'x'�� 'o'�� ������ ������ ��� : 'o'����
        if check_winner(board) == "No winner yet." and is_equal_number_of_x_and_o(board)==False  :
            v = float('inf')
            next_states=generate_new_states_o(board)
            for next_state in next_states :
                v=min(v,value(next_state,a,b,weight_board))
                if v <= a :
                    return v
                b = min(b,v)
        return v


board = [
    ['v', 'v', 'v'],
    ['v', 'v', 'v'],
    ['v', 'v', 'v']
]

weight_board = [
    [95,59,36],
    [76,85,43],
    [48,34,72]
]


a=float('-inf')
b=float('inf')
value(board , a, b,weight_board)