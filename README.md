# projectFinal Parcheesi

  This is the game of parcheesi where the objective is to reach the center of the board with all your pieces before the other players. the starts by asking the user which player are going to play by clicking on the colors then a box is pronted saying whos turn is it and to roll the dice. the game uses three classes in order to work which are game_master, player, and piece. the game_master creates the player depending on the input of the user and then the player creates four pieces, each one representing the four pieces in the traditional game.

# Game_master
  the class when initialised creates the board that is going to be used and the creates the players and the pieces on the board.

-run_game(self): the most inportant function of the class, it creates the diferent input boxes and makes the game run, it ends when a player win.

-eliminate(self,color,player): function used inside run_game() in order to follow the rule of eliminating oponent pieces in unsafe spots.

-


# Branch B (game_functions)

The updated versions uses functions in order to reduce the size of the main and make it more functional and easy to debug.

The menu_dif(win,dificulty) is used to draw and later undraw a menu to choose the dificulty of the game being easy
(the computer pick random places), normal(the computer try to block the player victory), and hard(the original dificulty of the game where the computer will block and try to win the game).

match_screen(win,grid) will create the screen with the grid for the player and the cumputer to play.

reset_screen(win,grid) will erase and reset the game screen and the inportant variables in order to play again.

player_turn(win,grid, i) is the function that lets the player play is turn, it will stop the player from making incorrect moves, at the end the function would check if the player won the game.

computer_turn(win,grid, i,dificulty) is the functions that plays for the computer, it varies depending on the dificulty that the player chose. it is the longest function because it evaluates all the possible situations. it will evaluate if the computer won at the end of it's move.

rematch(win,contin_playing) is a menu that ask the user if it wants to play again, if the answer is "Yes" then the program would start from the begining runing the function reset_screen(win,grid) in order to clean the screen from last match.

win_check() is used to see if there are the same symbols in a row and declare the winner of the game or the draw if needed.

# Branch C (game_classes)

another updated version of the game this time is organized in classes/objects.

the prinsipal class is the game_master(), the game_master() or gm uses the same functions that were used in the Branch B(gmae_functions) but adapted to be used in an object.

the gm has to more objects inside being the class player and the class computer, this two classes has their own function of turn that are similar to the function player_turn() and computer_turn(); however, the win_check() is a function of the class game_master() and it require the principal variables of the player and computer in order to verify

the lenght of the main in this code was reduced to just two lines having most of the process in the object gm.
