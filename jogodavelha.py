import random

def draw_board(board):
    print("     |     |")
    print("  {}  |  {}  |  {}".format(board[0], board[1], board[2]))
    print("     |     |")
    print("-----------------")
    print("     |     |")
    print("  {}  |  {}  |  {}".format(board[3], board[4], board[5]))
    print("     |     |")
    print("-----------------")
    print("     |     |")
    print("  {}  |  {}  |  {}".format(board[6], board[7], board[8]))
    print("     |     |\n\n")

def check_winner(board, player):
    # LINHA
    for i in range(0, 9, 3):
        if board[i] == board[i + 1] == board[i + 2] == player:
            return True

    # COLUNA
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] == player:
            return True

    # DIAGONAL
    if board[0] == board[4] == board[8] == player:
        return True
    if board[2] == board[4] == board[6] == player:
        return True

    return False

def player_move(board):
    while True:
        move = input("Digite sua jogada (1-9): ")
        if move.isdigit() and 1 <= int(move) <= 9 and board[int(move) - 1] == " ":
            return int(move)

        print("Jogada inválida. Por favor, tente novamente.\n")

def computer_move(board):
    empty_cells = [i for i, cell in enumerate(board) if cell == " "]
    return random.choice(empty_cells)

def play_game():
    board = [" "] * 9
    player = "O"
    computer = "X"

    print("\nBem-vindo ao Jogo da Velha!\n")
    print("Para fazer uma jogada, digite o número correspondente à posição no tabuleiro:\n")
    draw_board([str(i + 1) for i in range(9)])  # mostra números de 1 a 9 nas posiçoes

    while True:
        draw_board(board)

        if player == "O":
            move = player_move(board)
            board[move - 1] = player
        else:
            move = computer_move(board)
            board[move] = computer

        if check_winner(board, player):
            draw_board(board)
            if player == "O":
                print("Parabéns! Você venceu! :D\n")
            else:
                print("Haha! Computador venceu! >:D\n")
            break

        if " " not in board:
            draw_board(board)
            print("Empate! (°□°)\n")
            break

        player = "X" if player == "O" else "O"

    play_again = input("Deseja jogar novamente? (s/n): ")
    return play_again.lower() == "s"

while True:
    if not play_game():
        break
