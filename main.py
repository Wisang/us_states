import turtle
import pandas

screen = turtle.Screen()

screen.title("US State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")

state_names = data["state"].to_list()


def write_state_at(position):
    state_text = turtle.Turtle()
    state_text.hideturtle()
    state_text.penup()
    state_text.goto(position)
    state_text.write(answer_state)


score = 0

states_guessed = []

while score < len(state_names):
    answer_state = screen.textinput(f"Score: {score}/50, Guess State name",
                                    "Tell me the name of any state: ").title()
    if answer_state == "Exit":
        break

    if answer_state in state_names:
        states_guessed.append(answer_state)
        state = data[data.state == answer_state]
        location = (int(state.x), int(state.y))
        write_state_at(location)
        score += 1

to_learn = list(set(state_names) - set(states_guessed))
to_learn_csv = pandas.DataFrame(to_learn).to_csv("to_learn.csv")
