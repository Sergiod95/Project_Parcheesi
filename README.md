# ProjectFinal Parcheesi

  This is the game of parcheesi where the objective is to reach the center of the board with all your pieces before the other players. the starts by asking the user which player are going to play by clicking on the colors then a box is pronted saying whos turn is it and to roll the dice. the game uses three classes in order to work which are game_master, player, and piece. the game_master creates the player depending on the input of the user and then the player creates four pieces, each one representing the four pieces in the traditional game.

# Class Game_master
  the class when initialised creates the board that is going to be used and the creates the players and the pieces on the board.

- run_game(self): the most inportant function of the class, it creates the diferent input boxes and makes the game run, it ends when a player win.

- eliminate(self,color,player): function used inside run_game() in order to follow the rule of eliminating oponent pieces in unsafe spots.

- match_screen(self): runs when the class is initialised, it is used to create the grid for the game.

- roll_dice(self,color): the function runs on the function run_game(); it creates the box that tells the player who is playing and creates the numbers from the dice.

- menu_dif(self): runs when the class is initialised; is the first box that ask the player who is playing by picking a color.

- option(self):runs in menu_dif(); mostly checks the input to make menu_dif() work.

- win_check( self,current_p):  Runs on the function run_game(); it verefies if the player won the game.

- input_validation(self,player): used to pick the piece that the user wants to move.

# Class Player
  this is the class that orginise the information of each player and helps the pieces navegate the grid; important variables to consider are the color of the player and the four pieces from the class piece.
  
- return_color(self): returns the color of the player
       
- return_center(self, ind): return the center(Point) of the piece with the id.

- return_status(self,ind): return the status("Safe" or "NotSafe") of the piece with the id; used on the function eliminate() to determine if the piece is eliminated or not.

- removed(self,ind): function that helps the function eliminate().

- player_turn(self,ind,dice_rol,i): the most important function of the class; used to controll the pieces on the board.

# Class Piece
  holds all the information about the pieces including position, status, and how many steps from the nest.

  - update_location(self,new_center):change the location of the piece.

  - update_nest(self,status):change if the piece is inside the nest or not.
  
  - eliminated(self): resets the piece to the nest if it is eliminated.

  - return_x(self): return the x value.

  - return_y(self): return the y value.

  - return_stat(self): return the status of the piece.

  - return_position(self): return the position(Point) of the piece.

  - set_steps(self,step): change how many steps the piece has walked.

  - set_status(self,stat): change status of the piece.

  - return_steps(self): return the number of steps.

