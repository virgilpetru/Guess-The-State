import turtle
import pandas
import pyarrow
from scoreboard import Scoreboard

game_on = True
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"  #path to shape
screen.addshape(image)
turtle.shape(image)
correct_answer = []

data = pandas.read_csv("50_states.csv")
states = data["state"].to_list()

while len(correct_answer) < 50:
    answer = screen.textinput(title=f"{len(correct_answer)}/50 States Correct",
                              prompt="What's another state's name?").title()

    if answer == "Exit":
        missing_states = [state for state in states if state not in correct_answer]
        # if you want to have the missing states in a separate file, uncomment the lines below
        #missing_states = []
        #for state in states:
        #    if state not in correct_answer:
        #        missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer in states:
        correct_answer.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data["state"] == answer]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer, align="center", font=("arial", 10, "normal"))

#states_to_learn.csv
