import itertools as it

def win(current_game):
    
    def all_same(l):
        if l.count(l[0])==len(l) and l[0]!=0:
            return True
        else:
            return False
    #horizontal    
    for row in game:
        print(row)
        if all_same(row):
            print(f"Player {row[0]} is the winner horizontally!")
            return True
    
    #diagnol
    diags=[]
    for col, row in enumerate(reversed(range(len(game)))):
        diags.append(game[row][col])
        if all_same(diags):
            print(f"Player {diags[0]} is the winner diagnolly (/)!")
            return True
    diags=[]
    for ix in range(len(game)):
        diags.append(game[ix][ix])
        if all_same(diags):
            print(f"Player {diags[0]} is the winner diagnolly (\\)!")
            return True
    
    #vertically
    for col in range(len(game)):
        check=[]
        for row in game:
            check.append(row[col])
        if all_same(check):
            print(f"Player {check[0]} is the winner vertically!")
            return True
    return False


def game_board(game_map,player=0, row=0, column=0, just_display=False):    
    try:
        if game_map[row][column]!=0:
            print("This positionis occupado! choose another!")
            return game_map,False
        print("   0  1  2")
        if not just_display:
            game_map[row][column]=player
        for count, row in enumerate(game_map):
            print (count, row)
        return game_map,True
    except:
        print("Something went wrong. Calling the team of monkeys!")
        return game_map, False

play=True
players = [1,2]
while play:    
    game = [[0,0,0],
            [0,0,0],
            [0,0,0]]    
    game_won = False
    game, _ = game_board(game, just_display=True)
    player_choice = it.cycle([1,2])
    while not game_won:
        current_player = next(player_choice)
        print(f"Curernt player: {current_player}")
        played=False
        
        while not played:
            column_choice = int(input("what column do you want to play? 0,1,2: "))
            row_choice = int(input("what row do you want to play? 0,1,2: "))
            game, played = game_board(game, current_player,row_choice,column_choice)
        
        if win(game):
                game_won = True
                again = input("Game over. Do you want to play again? y/n")
                if again.lower()=="y":
                    print("restarting")
                elif again.lower()=="n":
                    print("byeeee")
                    play = False
                else:
                    print("Not a valid answer, byeee")
                    play= False
                    

#game = game_board(game,just_display=True)
#game = game_board(game,1, 2, 2)


