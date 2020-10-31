  
from graphics import *
from random import *
from dice import *


class game_master:
    def __init__(self):
    
        self.win = GraphWin('Graphics Window',800,800)
        self.win.setCoords(0, 0, 11, 11)
        self.colors = ["Green","Blue","Yellow","Red"]
        self.type_player = ["None","None","None","None"]
        self.center_player = []
        self.dice_roll = 0
        self.dice_set = Dice()
        self.piece_id = 0
        
        self.board = Rectangle(Point(0,0),Point(11,11))
        #creating the box for the colors and home
        self.player_box = Rectangle(Point(4,7),Point(7,4))
        self.player_box.setFill("Purple")
        self.player_box.draw(self.win)
        self.divider = Line(Point(4,7),Point(7,4))
        self.divider.draw(self.win)
        self.divider = Line(Point(4,4),Point(7,7))
        self.divider.draw(self.win)
        
        self.player_box = Rectangle(Point(0,11),Point(4,7))
        self.player_box.setFill("Green")
        self.player_box.draw(self.win)
        self.circle_box = Circle(self.player_box.getCenter(),1.5)
        self.center_player.append(self.player_box.getCenter())
        self.circle_box.setFill("White")
        self.circle_box.draw(self.win)

        self.player_box = Rectangle(Point(0,0),Point(4,4))
        self.player_box.setFill("Blue")
        self.player_box.draw(self.win)
        self.circle_box = Circle(self.player_box.getCenter(),1.5)
        self.center_player.append(self.player_box.getCenter())
        self.circle_box.setFill("White")
        self.circle_box.draw(self.win)

        

        self.player_box = Rectangle(Point(7,4),Point(11,0))
        self.player_box.setFill("Orange")
        self.player_box.draw(self.win)
        self.circle_box = Circle(self.player_box.getCenter(),1.5)
        self.center_player.append(self.player_box.getCenter())
        self.circle_box.setFill("White")
        self.circle_box.draw(self.win)
        
        
        self.player_box = Rectangle(Point(7,7),Point(11,11))
        self.player_box.setFill("Red")
        self.player_box.draw(self.win)
        self.circle_box = Circle(self.player_box.getCenter(),1.5)
        self.center_player.append(self.player_box.getCenter())
        self.circle_box.setFill("White")
        self.circle_box.draw(self.win)

        
        self.board.draw(self.win)
        
        self.match_screen()
        self.menu_dif()

        self.current_players = []
        
        for i in range(4):
            if self.type_player[i]=="Player":
                self.current_players.append(player(self.colors[i],self.center_player[i],self.win))
            elif i == 4:
                return 1
            
        
        
    def run_game(self):
        while True:
            for i in range(len(self.current_players)):
                self.roll_dice(self.current_players[i].return_color())
                self.input_validation(self.current_players[i])
                for j in range(2):
                    self.current_players[i].player_turn(self.piece_id,self.dice_roll,j)
                    self.eliminate(self.current_players[i].return_color(),self.current_players[i])
                if self.win_check(self.current_players[i])==True:
                    self.menu_box = Rectangle(Point(3,3),Point(8,8))
                    self.menu_box.setFill("Grey")
                    self.menu_box.draw(self.win)

                    self.color_turn = Circle(Point(5.5,6),0.75)
                    self.color_turn.setFill(self.current_players[i].return_color())
                    self.color_turn.draw(self.win)

                    self.color_turn_info = Text(Point(5.5,6),"WON")
                    self.color_turn_info.draw(self.win)

                    p = win.getMouse()
                    self.win.close()
     
    def eliminate(self,color,player):
        for i in range(len(self.current_players)):
            if self.current_players[i].return_color() != color:
                for j in range(4):
                    if self.current_players[i].return_center(j) == player.return_center(self.piece_id) and self.current_players[i].return_status(j)!="Safe":
                        self.current_players[i].removed(j)
                        
                        
                    
        
        
    def match_screen(self):
        #left side
        for i in range(8):
            self.grid = Rectangle(Point(0 + (i*0.5),(5.5-0.5)), Point(0.5 + (i*0.5),(5.5+0.5)))
            if i == 0:
                self.grid.setFill("cyan")
                self.circle = Circle(Point(0.25,5.5),0.25)
                
            else:
                self.grid.setFill("DodgerBlue")
            self.grid.setOutline("Black")
            self.grid.draw(self.win)
            if i == 0:
                self.circle.draw(self.win)
        for i in range(8):
            self.grid = Rectangle(Point(0 + (i*0.5),(6.5-0.5)), Point(0.5 + (i*0.5),(6.5+0.5)))
            if i == 4:
                self.grid.setFill("cyan")
                self.circle = Circle(self.grid.getCenter(),0.25)
            self.grid.setOutline("Black")
            self.grid.draw(self.win)
            if i == 4:
                self.circle.draw(self.win)
        for i in range(8):
            self.grid = Rectangle(Point(0 + (i*0.5),(4.5-0.5)), Point(0.5 + (i*0.5),(4.5+0.5)))
            if i == 4:
                self.grid.setFill("DodgerBlue")
                self.circle = Circle(self.grid.getCenter(),0.25)

            self.grid.setOutline("Black")
            self.grid.draw(self.win)
            if i == 4:
                self.circle.draw(self.win)
            if i == 5:
                self.arrow= Line(Point(0 + (i*0.5),(4.5)), Point(0.5 + (i*0.5),(4.5)))
                self.arrow.setArrow("last")
                self.arrow.draw(self.win)
        #Right side
        for i in range(8):
            self.grid = Rectangle(Point(11 - (i*0.5),(5.5-0.5)), Point(10.5 - (i*0.5),(5.5+0.5)))
            if i == 0:
                self.grid.setFill("cyan")
                self.circle = Circle(Point(10.75,5.5),0.25)
                
            else:
                self.grid.setFill("Crimson")
            self.grid.setOutline("Black")
            self.grid.draw(self.win)
            if i == 0:
                self.circle.draw(self.win)
        for i in range(8):
            self.grid = Rectangle(Point(11 - (i*0.5),(6.5-0.5)), Point(10.5 - (i*0.5),(6.5+0.5)))
            if i == 4:
                self.grid.setFill("Crimson")
                self.circle = Circle(self.grid.getCenter(),0.25)
            self.grid.setOutline("Black")
            self.grid.draw(self.win)
            if i == 4:
                self.circle.draw(self.win)
            if i == 5:
                self.arrow= Line(Point(11 - (i*0.5),(6.5)), Point(10.5 - (i*0.5),(6.5)))
                self.arrow.setArrow("last")
                self.arrow.draw(self.win)
        for i in range(8):
            self.grid = Rectangle(Point(11 - (i*0.5),(4.5-0.5)), Point(10.5 - (i*0.5),(4.5+0.5)))
            if i == 4:
                self.grid.setFill("cyan")
                self.circle = Circle(self.grid.getCenter(),0.25)

            self.grid.setOutline("Black")
            self.grid.draw(self.win)
            if i == 4:
                self.circle.draw(self.win)
            
        #top side
        for i in range(8):
            self.grid = Rectangle(Point((5+ 1),(11 - (i*0.5))), Point(5,10.50 - (i*0.5)))
            if i == 0:
                self.grid.setFill("cyan")
                self.circle = Circle(Point(5.5,10.75),0.25)
                
            else:
                self.grid.setFill("ForestGreen")
            self.grid.setOutline("Black")
            self.grid.draw(self.win)
            if i == 0:
                self.circle.draw(self.win)
        for i in range(8):
            self.grid = Rectangle(Point((6+ 1),(11 - (i*0.5))), Point(6,10.50 - (i*0.5)))
            if i == 4:
                self.grid.setFill("cyan")
                self.circle = Circle(self.grid.getCenter(),0.25)

            self.grid.setOutline("Black")
            self.grid.draw(self.win)
            if i == 4:
                self.circle.draw(self.win)
        for i in range(8):
            self.grid = Rectangle(Point((4+ 1),(11 - (i*0.5))), Point(4,10.50 - (i*0.5)))
            if i == 4:
                self.grid.setFill("ForestGreen")
                self.circle = Circle(self.grid.getCenter(),0.25)

            self.grid.setOutline("Black")
            self.grid.draw(self.win)
            if i == 4:
                self.circle.draw(self.win)
            if i == 5:
                self.arrow= Line(Point((4+ 0.5),(11 - (i*0.5))), Point(4+ 0.5,10.50 - (i*0.5)))
                self.arrow.setArrow("last")
                self.arrow.draw(self.win)
        #bottom side
        for i in range(8):
            self.grid = Rectangle(Point((5+ 1),(0 + (i*0.5))), Point(5,0.5 + (i*0.5)))
            if i == 0:
                self.grid.setFill("cyan")
                self.circle = Circle(Point(5.5,0.25),0.25)
                
            else:
                self.grid.setFill("Yellow")
            self.grid.setOutline("Black")
            self.grid.draw(self.win)
            if i == 0:
                self.circle.draw(self.win)
        for i in range(8):
            self.grid = Rectangle(Point((6+ 1),(0 + (i*0.5))), Point(6,0.5 + (i*0.5)))
            if i == 4:
                self.grid.setFill("Yellow")
                self.circle = Circle(self.grid.getCenter(),0.25)

            self.grid.setOutline("Black")
            self.grid.draw(self.win)
            if i == 4:
                self.circle.draw(self.win)
            if i == 5:
                self.arrow= Line(Point((6+ 0.5),(0 + (i*0.5))), Point(6+0.5,0.5 + (i*0.5)))
                self.arrow.setArrow("last")
                self.arrow.draw(self.win)
        for i in range(8):
            self.grid = Rectangle(Point((4+ 1),(0 + (i*0.5))), Point(4,0.5 + (i*0.5)))
            if i == 4:
                self.grid.setFill("cyan")
                self.circle = Circle(self.grid.getCenter(),0.25)

            self.grid.setOutline("Black")
            self.grid.draw(self.win)
            if i == 4:
                self.circle.draw(self.win)
                
    def roll_dice(self,color):
        self.menu_box = Rectangle(Point(3,3),Point(8,8))
        self.menu_box.setFill("Grey")
        self.menu_box.draw(self.win)
        self.play_box = Rectangle(Point(4.5,3.5),Point(6.5,4))
        self.play_box.setFill("White")
        self.play_box.draw(self.win)
        self.play_tex = Text(self.play_box.getCenter(),"Roll")
        self.play_tex.draw(self.win)
        self.color_turn = Circle(Point(5.5,6),0.75)
        self.color_turn.setFill(color)
        self.color_turn.draw(self.win)
        self.color_turn_info = Text(Point(5.5,6),"Turn of player:")
        self.color_turn_info.draw(self.win)
        self.rolling = Text(Point(5.5,5),"press to roll")
        self.rolling.draw(self.win)

        while True:
            click = self.win.getMouse()
            x = click.getX()
            y = click.getY()
            
            if x > 4.5 and x < 6.5 and y > 3.5  and y < 4 and self.play_tex.getText()=="Roll":
                self.dice_set.rollAll()
                self.dice_roll = self.dice_set.values()
                self.rolling.setText(str(self.dice_roll[:2]))
                self.play_tex.setText("Continue")
                
            elif x > 4.5 and x < 6.5 and y > 3.5  and y < 4 and self.play_tex.getText()=="Continue":
                break
        
        self.menu_box.undraw()
        self.play_box.undraw()
        self.play_tex.undraw()
        self.color_turn.undraw()
        self.color_turn_info.undraw()
        self.rolling.undraw()
        

            

    def menu_dif(self):

        self.menu_box = Rectangle(Point(3,3),Point(8,8))
        self.menu_box.setFill("Grey")
        self.menu_box.draw(self.win)
        

        self.green = Circle(Point(4.5,7),0.75)
        self.green.setFill("Green")
        self.green.draw(self.win)
        self.green_tex = Text(Point(4.5,7),"None")
        self.green_tex.draw(self.win)

        self.red = Circle(Point(6.5,7),0.75)
        self.red.setFill("Red")
        self.red.draw(self.win)
        self.red_tex = Text(Point(6.5,7),"None")
        self.red_tex.draw(self.win)

        self.blue = Circle(Point(4.5,5),0.75)
        self.blue.setFill("Blue")
        self.blue.draw(self.win)
        self.blue_tex = Text(Point(4.5,5),"None")
        self.blue_tex.draw(self.win)

        self.yellow = Circle(Point(6.5,5),0.75)
        self.yellow.setFill("Orange")
        self.yellow.draw(self.win)
        self.yellow_tex = Text(Point(6.5,5),"None")
        self.yellow_tex.draw(self.win)

        self.play_box = Rectangle(Point(4.5,3.5),Point(6.5,4))
        self.play_box.setFill("White")
        self.play_box.draw(self.win)
        self.play_tex = Text(self.play_box.getCenter(),"Play")
        self.play_tex.draw(self.win)

        self.hint = Text(Point(5.5,3.25),"Click the circle to select players")
        self.hint.draw(self.win)

        self.option()
        
        self.menu_box.undraw()
        self.green.undraw()
        self.green_tex.undraw()
        self.red.undraw()
        self.red_tex.undraw()
        self.blue.undraw()
        self.blue_tex.undraw()
        self.yellow.undraw()
        self.yellow_tex.undraw()
        self.play_box.undraw()
        self.play_tex.undraw()
        self.hint.undraw()
        
        
        
    def option(self):
        while True:
            click = self.win.getMouse()
            x = click.getX()
            y = click.getY()
            
            if x > 3.75 and x < 5.25 and y > 6.25  and y < 7.75 and self.green_tex.getText()== "None" :
                self.green_tex.setText("Player")
                self.type_player[0]="Player"
            elif x > 5.75 and x < 7.25 and y > 6.25  and y < 7.75 and self.red_tex.getText()=="None":
                self.red_tex.setText("Player")
                self.type_player[3]="Player"
            elif x > 3.75 and x < 5.25 and y > 4.25  and y < 5.75 and self.blue_tex.getText()=="None":
                self.blue_tex.setText("Player")
                self.type_player[1]="Player"
            elif x > 5.75 and x < 7.25 and y > 4.25  and y < 5.75 and self.yellow_tex.getText()=="None":
                self.yellow_tex.setText("Player")
                self.type_player[2]="Player"
            elif x > 3.75 and x < 5.25 and y > 6.25  and y < 7.75 and self.green_tex.getText()=="Player":
                self.green_tex.setText("None")
                self.type_player[0]="None"
            elif x > 5.75 and x < 7.25 and y > 6.25  and y < 7.75 and self.red_tex.getText()=="Player":
                self.red_tex.setText("None")
                self.type_player[3]="None"
            elif x > 3.75 and x < 5.25 and y > 4.25  and y < 5.75 and self.blue_tex.getText()=="Player":
                self.blue_tex.setText("None")
                self.type_player[1]="None"
            elif x > 5.75 and x < 7.25 and y > 4.25  and y < 5.75 and self.yellow_tex.getText()=="Player":
                self.yellow_tex.setText("None")
                self.type_player[2]="None"
            elif x > 4.5 and x < 6.5 and y > 3.5  and y < 4:
                break

    
        

    def win_check( self,current_p):
        pc = current_p
        for i in range(4):
            if pc.player_pieces[i].return_steps()!= 71:
                return False
        return True

    def input_validation(self,player):
        while True:
            click = self.win.getMouse()
            x = click.getX()
            y = click.getY()
           
            for i in player.player_pieces:
                px = i.return_x()
                py = i.return_y()
               
                if x > (px-0.25)and x < (px + 0.25)and y > (py-0.25)and y < (py+0.25):
                   
                    self.piece_id = player.player_pieces.index(i)
                    return self.piece_id 
    
            
    
class player:
    def __init__(self,color_home,center,win):
        self.color_player = color_home
        self.x = center.getX()
        self.y = center.getY()
        self.player_pieces = [piece(color_home, Point(self.x-0.5,self.y+0.5), win),piece(color_home, Point(self.x+0.5,self.y+0.5), win),piece(color_home, Point(self.x-0.5,self.y-0.5), win),piece(color_home, Point(self.x+0.5,self.y-0.5), win)]

        #creating the track for the pieces
        self.track_green = []
        for i in range(72):
            if i >= 0 and i<4:
                self.track_green.append(Point(4.5,(8.75-(i*0.5))))
            elif i >= 4 and i<12:
                self.track_green.append(Point((3.75-((i-4)*0.5)),6.5))
            elif i==12:
                self.track_green.append(Point(0.25,5.5))
            elif i >12 and i<21:
                self.track_green.append(Point((0.25+((i-13)*0.5)),4.5))
            elif i >= 21 and i<29:
                self.track_green.append(Point(4.5,(3.75-((i-21)*0.5))))
            elif i==29:
                self.track_green.append(Point(5.5,0.25))
            elif i > 29 and i<38:
                self.track_green.append(Point(6.5,(0.25+((i-30)*0.5))))
            elif i >=38 and i<46:
                self.track_green.append(Point((7.25+((i-38)*0.5)),4.5))
            elif i==46:
                self.track_green.append(Point(10.75,5.5))
            elif i >46 and i<55:
                self.track_green.append(Point((10.75-((i-47)*0.5)),6.5))
            elif i >=55 and i<63:
                self.track_green.append(Point(6.5,(7.25+((i-55)*0.5))))
            elif i==63:
                self.track_green.append(Point(5.5,10.75))
            elif i > 63 and i<72:
                self.track_green.append(Point(5.5,(10.25-((i-64)*0.5))))
                
        self.track_red = []
        for i in range(72):
            if i >= 0 and i<4:
                self.track_red.append(Point((8.75-((i)*0.5)),6.5))
            elif i >= 4 and i<12:
                self.track_red.append(Point(6.5,(7.25+((i-4)*0.5))))
            elif i==12:
                self.track_red.append(Point(5.5,10.75))
            elif i >12 and i<21:
                self.track_red.append(Point(4.5,(10.75-((i-13)*0.5))))
            elif i >= 21 and i<29:
                self.track_red.append(Point((3.75-((i-21)*0.5)),6.5))
            elif i==29:
                self.track_red.append(Point(0.25,5.5))
            elif i > 29 and i<38:
                self.track_red.append(Point((0.25+((i-30)*0.5)),4.5))
            elif i >=38 and i<46:
                self.track_red.append(Point(4.5,(3.75-((i-38)*0.5))))
            elif i==46:
                self.track_red.append(Point(5.5,0.25))
            elif i >46 and i<55:
                self.track_red.append(Point(6.5,(0.25+((i-47)*0.5))))
            elif i >=55 and i<63:
                self.track_red.append(Point((7.25+((i-55)*0.5)),4.5))
            elif i==63:
                self.track_red.append(Point(10.75,5.5))
            elif i > 63 and i<72:
                self.track_red.append(Point((10.25-((i-64)*0.5)),5.5))
        self.track_blue = []
        for i in range(72):
            if i >= 0 and i<4:
                self.track_blue.append(Point((2.25+((i)*0.5)),4.5))
            elif i >= 4 and i<12:
                self.track_blue.append(Point(4.5,(3.75-((i-4)*0.5))))
            elif i==12:
                self.track_blue.append(Point(5.5,0.25))
            elif i >12 and i<21:
                self.track_blue.append(Point(6.5,(0.25+((i-13)*0.5))))
            elif i >= 21 and i<29:
                self.track_blue.append(Point((7.25+((i-21)*0.5)),4.5))
            elif i==29:
                self.track_blue.append(Point(10.75,5.5))
            elif i > 29 and i<38:
                self.track_blue.append(Point((10.75-((i-30)*0.5)),6.5))
            elif i >=38 and i<46:
                self.track_blue.append(Point(6.5,(7.25+((i-38)*0.5))))
            elif i==46:
                self.track_blue.append(Point(5.5,10.75))
            elif i >46 and i<55:
                self.track_blue.append(Point(4.5,(10.75-((i-47)*0.5))))
            elif i >=55 and i<63:
                self.track_blue.append(Point((3.75-((i-55)*0.5)),6.5))
            elif i==63:
                self.track_blue.append(Point(0.25,5.5))
            elif i > 63 and i<72:
                self.track_blue.append(Point((0.75+((i-64)*0.5)),5.5))
        self.track_yellow = []
        for i in range(72):
            if i >= 0 and i<4:
                self.track_yellow.append(Point(6.5,(2.25+(i*0.5))))
            elif i >= 4 and i<12:
                self.track_yellow.append(Point((7.25+((i-4)*0.5)),4.5))
            elif i==12:
                self.track_yellow.append(Point(10.75,5.5))
            elif i >12 and i<21:
                self.track_yellow.append(Point((10.75-((i-13)*0.5)),6.5))
            elif i >= 21 and i<29:
                self.track_yellow.append(Point(6.5,(7.25+((i-21)*0.5))))
            elif i==29:
                self.track_yellow.append(Point(5.5,10.75))
            elif i > 29 and i<38:
                self.track_yellow.append(Point(4.5,(10.75-((i-30)*0.5))))
            elif i >=38 and i<46:
                self.track_yellow.append(Point((3.75-((i-38)*0.5)),6.5))
            elif i==46:
                self.track_yellow.append(Point(0.25,5.5))
            elif i >46 and i<55:
                self.track_yellow.append(Point((0.25+((i-47)*0.5)),4.5))
            elif i >=55 and i<63:
                self.track_yellow.append(Point(4.5,(3.75-((i-55)*0.5))))
            elif i==63:
                self.track_yellow.append(Point(5.5,0.25))
            elif i > 63 and i<72:
                self.track_yellow.append(Point(5.5,(0.75+((i-64)*0.5))))
            
            
        
    def return_color(self):
        return self.color_player
    def return_center(self, ind):
        return self.player_pieces[ind].return_position()
    def return_status(self,ind):
        return self.player_pieces[ind].return_stat()
    def removed(self,ind):
        self.player_pieces[ind].eliminated()
        

    def player_turn(self,ind,dice_rol,i):

        total = self.player_pieces[ind].return_steps()
        total = total + dice_rol[i]
        if total > 71:
            total = 71

        
        if self.color_player=="Green":
           
            if self.player_pieces[ind].nest == True:
                if (dice_rol[0]+dice_rol[1])< 5:
                    return 1
                self.player_pieces[ind].update_location(Point(4.5,8.75))
                self.player_pieces[ind].update_nest(False)
                self.player_pieces[ind].update_location(self.track_green[total])
                self.player_pieces[ind].set_steps(total)
                if total == 0 or total == 7 or total == 12 or total == 24 or total == 29 or total == 41 or total == 46 or total == 58 or total == 63 :
                    self.player_pieces[ind].set_status("Safe")
                else:
                    self.player_pieces[ind].set_status("NotSafe")
            else:
                self.player_pieces[ind].update_location(self.track_green[total])
                self.player_pieces[ind].set_steps(total)
                if total == 0 or total == 7 or total == 12 or total == 24 or total == 29 or total == 41 or total == 46 or total == 58 or total == 63 :
                    self.player_pieces[ind].set_status("Safe")
                else:
                    self.player_pieces[ind].set_status("NotSafe")
        elif self.color_player=="Red":
            if self.player_pieces[ind].nest == True:
                self.player_pieces[ind].update_location(Point(4.5,8.75))
                self.player_pieces[ind].update_nest(False)
                self.player_pieces[ind].update_location(self.track_red[total])
                self.player_pieces[ind].set_steps(total)
                if total == 0 or total == 7 or total == 12 or total == 24 or total == 29 or total == 41 or total == 46 or total == 58 or total == 63 :
                    self.player_pieces[ind].set_status("Safe")
                else:
                    self.player_pieces[ind].set_status("NotSafe")
            else:
                self.player_pieces[ind].update_location(self.track_red[total])
                self.player_pieces[ind].set_steps(total)
                if total == 0 or total == 7 or total == 12 or total == 24 or total == 29 or total == 41 or total == 46 or total == 58 or total == 63 :
                    self.player_pieces[ind].set_status("Safe")
                else:
                    self.player_pieces[ind].set_status("NotSafe")
        elif self.color_player=="Blue":
            if self.player_pieces[ind].nest == True:
                self.player_pieces[ind].update_location(Point(4.5,8.75))
                self.player_pieces[ind].update_nest(False)
                self.player_pieces[ind].update_location(self.track_blue[total])
                self.player_pieces[ind].set_steps(total)
                if total == 0 or total == 7 or total == 12 or total == 24 or total == 29 or total == 41 or total == 46 or total == 58 or total == 63 :
                    self.player_pieces[ind].set_status("Safe")
                else:
                    self.player_pieces[ind].set_status("NotSafe")
            else:
                self.player_pieces[ind].update_location(self.track_blue[total])
                self.player_pieces[ind].set_steps(total)
                if total == 0 or total == 7 or total == 12 or total == 24 or total == 29 or total == 41 or total == 46 or total == 58 or total == 63 :
                    self.player_pieces[ind].set_status("Safe")
                else:
                    self.player_pieces[ind].set_status("NotSafe")
        elif self.color_player=="Yellow":
            if self.player_pieces[ind].nest == True:
                self.player_pieces[ind].update_location(Point(4.5,8.75))
                self.player_pieces[ind].update_nest(False)
                self.player_pieces[ind].update_location(self.track_yellow[total])
                self.player_pieces[ind].set_steps(total)
                if total == 0 or total == 7 or total == 12 or total == 24 or total == 29 or total == 41 or total == 46 or total == 58 or total == 63 :
                    self.player_pieces[ind].set_status("Safe")
                else:
                    self.player_pieces[ind].set_status("NotSafe")
            else:
                self.player_pieces[ind].update_location(self.track_yellow[total])
                self.player_pieces[ind].set_steps(total)
                if total == 0 or total == 7 or total == 12 or total == 24 or total == 29 or total == 41 or total == 46 or total == 58 or total == 63 :
                    self.player_pieces[ind].set_status("Safe")
                else:
                    self.player_pieces[ind].set_status("NotSafe")
        
class piece:
    def __init__(self,color_home, center, win):
        self.board = win
        self.color = color_home
        self.status = "Safe"
        self.nest= True
        self.steps = 0
        self.origen = center
        self.center = center
        self.entity = Circle(center,0.25)
        self.entity.setFill(color_home)
        self.entity.draw(self.board)

    def update_location(self,new_center):
        self.entity.undraw()
        self.entity = Circle(new_center,0.25)
        self.entity.setFill(self.color)
        self.center = new_center
        self.entity.draw(self.board)
    def update_nest(self,status):
        self.nest = status
    def eliminated(self):
        self.entity.undraw(self.board)
        self.entity = Circle(self.origen,0.25)
        self.steps = 0
        self.center = self.origen
        self.status = "Safe"
        self.entity.draw(self.board)
        self.nest = True
    def return_x(self):
        return self.center.getX()
    def return_y(self):
        return self.center.getY()
    def return_stat(self):
        return self.status
    def return_position(self):
        return self.center
    def set_steps(self,step):
        self.steps = step
    def set_status(self,stat):
        self.status = stat
    def return_steps(self):
        return self.steps

def main():
    gm = game_master()
    gm.run_game()
    
    

main()
