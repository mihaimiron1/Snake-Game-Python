from turtle import Turtle

ALIGMENT = "center"
FONT = ("Arial", 20, "normal")  

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0
        with open("data.txt", "r") as file:
            self.high_score = int(file.read())
        
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.write(f"Score: {self.score}", align=ALIGMENT, font=FONT)
    
    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High score: {self.high_score}", align= ALIGMENT , font= FONT)        
        
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGMENT, font=FONT)

    def increase_high_score(self):
        self.score += 1
        self.update_score()
    
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score 
            with open("data.txt", "w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_score()
