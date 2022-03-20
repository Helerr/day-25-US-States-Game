import turtle
import pandas
import collections

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "./blank_states_img.gif"
data = pandas.read_csv("50_states.csv")
screen.addshape(image)
turtle.shape(image)
game_in_progress = True

all_states = data["state"].to_list()

answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?")

if answer_state in all_states:
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    state_data = data[data.state == answer_state]
    t.goto(int(state_data.x), int(state_data.y))
    t.write(answer_state)
# writer = turtle.Turtle()
# writer.hideturtle()
# writer.speed("fastest")
# screen.addshape(image)
# answer_state = ""
#
# user_guesses = []
# user_score = 0
# writer.penup()
# while game_in_progress:
#     answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?")
#     for state in data["state"]:
#         if answer_state.capitalize() == state.capitalize():
#             state_x = data[data["state"] == state]["x"].to_list()
#             state_y = data[data["state"] == state]["y"].to_list()
#             writer.goto(state_x[0] - 10, state_y[0] - 10)
#             writer.write(state, move=False, align="left", font=("Arial", 8, ""))
#             user_score += 1
#             user_guesses.append(answer_state.capitalize())
#         else:
#             pass
#     if collections.Counter(user_guesses) == collections.Counter(data["state"].to_list()):
#         writer.goto(0, 0)
#         writer.write("Congratulations! You guessed them all", move=False, align="center", font=("Arial", 30, ""))
#         game_in_progress = False
screen.exitonclick()
