from turtle import Turtle

ALIGMENT = "center"
FONT = ("Arial", 20, "normal")  

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.write(f"Score: {self.score}", align=ALIGMENT, font=FONT)
    
    def update_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", align= ALIGMENT , font= FONT)        
        
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGMENT, font=FONT)
         