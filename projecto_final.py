  
from graphics import *
from random import *


class game_master:
    def __init__(self):
    
        self.win = GraphWin('Graphics Window',800,800)
        self.win.setCoords(0, 0, 11, 11)
        self.colors = ["Green","Red","Blue","Yellow"]
        self.type_player = ["none","none","none","none"] 
        self.contin = "yes"
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

        self.player_box = Rectangle(Point(7,7),Point(11,11))
        self.player_box.setFill("Red")
        self.player_box.draw(self.win)

        self.player_box = Rectangle(Point(0,0),Point(4,4))
        self.player_box.setFill("Blue")
        self.player_box.draw(self.win)

        self.player_box = Rectangle(Point(7,4),Point(11,0))
        self.player_box.setFill("Orange")
        self.player_box.draw(self.win)
        
        self.board.draw(self.win)
        self.match_screen()
        
        
    def run_game(self):
        
        pass
        
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
            
            
        pass
                
    def reset_screen(self):
    
        pass

    def menu_dif(self):
        pass
        
    def rematch(self):
    
        pass

    def win_check( self):
        pass

    
class player:
    def __init__(self):
        pass
        

    def player_turn(self,win,grid,i):
        pass



def main():
    gm = game_master()
    
    

main()
