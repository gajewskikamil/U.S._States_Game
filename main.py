import turtle
import pandas
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.speed(0.1)
turtle.shape(image)

game_on = 0
list_of_num = []
dict_of_guess = []
def state_onto_map(x,y,state_write):
    new_turtle_state = turtle.Turtle()
    new_turtle_state.speed(0.1)
    new_turtle_state.penup()
    new_turtle_state.hideturtle()
    new_turtle_state.goto(x, y)
    new_turtle_state.write(state_write, align="center")


data = pandas.read_csv("50_states.csv")
while game_on < 50:

    answer_state = screen.textinput(title=f"{game_on}/50 Guess the State",
                                    prompt="What's another states name?").title()
    if answer_state == "Exit":
        break
    if answer_state == "Load":
        if list_of_num == []:
            data_load = pandas.read_csv("save.csv")
            data_load = data_load.to_dict()
            screen.tracer(0)
            for i in range(len(data_load.get("x"))):
                game_on += 1
                list_of_num.append(data_load.get("num")[i])
                dict_of_guess.append({"num": data_load.get("num")[i], "state": data_load.get("state")[i], "x": data_load.get("x")[i], "y": data_load.get("y")[i]})
                state_onto_map(data_load.get("x")[i], data_load.get("y")[i], data_load.get("state")[i])
        else:
            print("You can load game before start typing states")
        screen.update()
        screen.tracer(1)

    if answer_state == "Save":
        save = pandas.DataFrame(dict_of_guess)
        save.to_csv("save.csv")
        print("game saved")


    guess = data[data.state == answer_state]
    if guess.empty == False:
        if guess.index[0] not in list_of_num:
            list_of_num.append(guess.index[0])
            dict_of_guess.append({"num": guess.index[0], "state": answer_state, "x": guess.x.item(), "y": guess.y.item()})
            game_on += 1
            x = int(guess.x.item())
            y = int(guess.y.item())
            name_of_state = guess.state.item()
            state_onto_map(x=x, y=y, state_write=answer_state)
if game_on == 50:
    print("Nice, that's all")
    screen.exitonclick()