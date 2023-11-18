import turtle
import pandas
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

def state_onto_map(x,y,state_write):
    new_turtle_state = turtle.Turtle()
    new_turtle_state.penup()
    new_turtle_state.hideturtle()
    new_turtle_state.goto(x, y)
    new_turtle_state.write(state_write, align="center")


game_on = 0
list_of_num = []
while game_on < 50:

    answer_state = screen.textinput(title=f"{game_on}/50 Guess the State",
                                    prompt="What's another states name?").title()

    data = pandas.read_csv("50_states.csv")
    guess = data[data.state == answer_state]
    if guess.empty:
        print("Empty")
    else:
        if guess.index[0] not in list_of_num:
            list_of_num.append(guess.index[0])
            game_on += 1
            x = int(guess.x)
            y = int(guess.y)
            name_of_state = guess.get("state")[guess.index[0]]
            state_onto_map(x=x, y=y, state_write=name_of_state)
