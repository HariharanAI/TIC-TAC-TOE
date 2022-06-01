#TIC TAC TOI GAME:

board = ["-" for i in range(9)]
def check_condition(player):
    condition = [
        [0,1,2],[3,4,5],[6,7,8],[0,4,8],[2,4,6],[0,3,6],[1,4,7],[2,5,8]
        
        
    ]
    for check in condition:
        if board[check[0]]==player and board[check[1]]==player and board[check[2]]==player:
            return 1
    else:
        return 0
        
def display_board():
    print("|",board[0],"|",board[1],"|",board[2],"|")
    print( "|",board[3],"|",board[4],"|",board[5],"|")
    print("|",board[6],"|",board[7],"|",board[8],"|")



player1 = "x"
player2 = "0"


def game():
    display_board()                
    while True:
        while True:           
            player1_position = int(input(f"{player1},Enter the Positon : "))
            if (player1_position<10):               
                if board[player1_position -1 ] == "-" :
                    board[player1_position -1] = player1
                    display_board()
                    if check_condition(player1):
                        return f"{player1} is Winner"                   
                    break
                    
                else:
                    print("This Place Is Not Empty")
            else:
                print("Choose 1 to 9 ")
                
        while True:
            player2_position = int(input(f"{player2},Enter the Position : "))
            if(player2_position < 10):
                if board[player2_position - 1] == "-" :
                    board[player2_position -1] = player2
                    display_board()
                    if check_condition(player2):
                        return f"{player2} is Winner"    
                    break
                else:
                    print("The Place is Not Empty ")
            else:
                print("Choose 1 to 9")
print(game())
while True:
    print("Want to Play....Press Y to continue or N to exit")
    oncemore = input()
    if oncemore in "yY":
       board = ["-" for i in range(9)]
       print(game())
    else:
        print("Thak You")
        break
