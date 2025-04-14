import random
import time
import sys


symbol = "|"

player_symbol = "X"
ai_symbol = "O"



grid_structure = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

def grid():
    print()
    for row in grid_structure:
        for x_o in row:
            print(x_o, end=" ")
            print(symbol, end=" ")
        print()
    print("\n")
      




def place_position(answer):
    while answer < 1 or answer > 9:
         print("Invalid Choice Please Try Again!!!\n")
         answer = int(input("Please Enter where to place a piece (1-9): "))
       
    find_col = (answer - 1) % 3
    find_row = (answer - 1) // 3

    
    while grid_structure[find_row][find_col] == player_symbol or grid_structure[find_row][find_col] == ai_symbol:
     answer = int(input("(Already Taken) Please Enter where to place a piece (1-9): "))
     find_col = (answer - 1) % 3
     find_row = (answer - 1) // 3

    grid_structure[find_row][find_col] = player_symbol



def ai_placement():
    print("Ai is Picking their Move")
    time.sleep(1.5)
    while(True):
     ai_piece = random.randint(1, 9)
     find_ai_row = (ai_piece - 1) // 3
     find_ai_col = (ai_piece - 1) % 3
     if grid_structure[find_ai_row][find_ai_col] != player_symbol and grid_structure[find_ai_row][find_ai_col] != ai_symbol:
        grid_structure[find_ai_row][find_ai_col] = ai_symbol
        break
    



def check_win():
   row = grid_structure[0]
   row1 = grid_structure[1]
   row2 = grid_structure[2]



   if row[0] == player_symbol and row[1] == player_symbol and row[2] == player_symbol:
      print("Player Won")
      sys.exit()
   elif row[0] == ai_symbol and row[1] == ai_symbol and row[2] == ai_symbol:
      print("Ai Won")
      sys.exit()
   if row1[0] == player_symbol and row1[1] == player_symbol and row1[2] == player_symbol:
      print("Player Won")
      sys.exit()
   elif row1[0] == ai_symbol and row1[1] == ai_symbol and row1[2] == ai_symbol:
      print("Ai Won")
      sys.exit()
   if row2[0] == player_symbol and row2[1] == player_symbol and row2[2] == player_symbol:
      print("Player Won")
      sys.exit()
   elif row2[0] == ai_symbol and row2[1] == ai_symbol and row2[2] == ai_symbol:
      print("Ai Won")
      sys.exit()

   if grid_structure[0][0] == player_symbol and grid_structure[1][0] == player_symbol and grid_structure[2][0] == player_symbol:
      print("Player Won")
      sys.exit()
   elif grid_structure[0][0] == ai_symbol and grid_structure[1][0] == ai_symbol and grid_structure[2][0] == ai_symbol:
      print("Ai Won")
      sys.exit()
   if grid_structure[0][1] == player_symbol and grid_structure[1][1] == player_symbol and grid_structure[2][1] == player_symbol:
      print("Player Won")
      sys.exit()
   elif grid_structure[0][1] == ai_symbol and grid_structure[1][1] == ai_symbol and grid_structure[2][1] == ai_symbol:
      print("Ai Won")
      sys.exit()
   if grid_structure[0][2] == player_symbol and grid_structure[1][2] == player_symbol and grid_structure[2][2] == player_symbol:
      print("Player Won")
      sys.exit()
   elif grid_structure[0][2] == ai_symbol and grid_structure[1][2] == ai_symbol and grid_structure[2][2] == ai_symbol:
      print("Ai Won")
      sys.exit()
   if grid_structure[0][0] == player_symbol and grid_structure[1][1] == player_symbol and grid_structure[2][2] == player_symbol:
      print("Player Won")
      sys.exit()
   elif grid_structure[0][0] == ai_symbol and grid_structure[1][1] == ai_symbol and grid_structure[2][2] == ai_symbol:
      print("Ai Won")
      sys.exit()
   if grid_structure[2][0] == player_symbol and grid_structure[1][1] == player_symbol and grid_structure[0][2] == player_symbol:
      print("Player Won")
      sys.exit()
   elif grid_structure[2][0] == ai_symbol and grid_structure[1][1] == ai_symbol and grid_structure[0][2] == ai_symbol:
      print("Ai Won")
      sys.exit()


    



def game_play():
    for i in range(5):
        answer = int(input("Please Enter where to place a piece (1-9): "))
        place_position(answer)
        ai_placement()
        grid()
        check_win()
        
        
        
def restart():
   game_play()


grid()
game_play()
    


    












   



       

       



