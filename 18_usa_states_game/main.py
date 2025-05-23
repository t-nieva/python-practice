from turtle import Turtle, Screen
from state import State
import pandas

FONT = ("Courier", 14, "bold")
IMAGE = 'images/blank_states_img.gif'
DATA_FILE = 'data/50_states.csv'
OUTPUT_FILE = 'data/states_to_learn.csv'

screen = Screen()
screen.title('U.S. States Game')
screen.addshape(IMAGE)

turtle = Turtle()
turtle.shape(IMAGE)

# Load state data with Pandas
data = pandas.read_csv("data/50_states.csv") # Data Frame
all_states = data.state.to_list() # Series
guessed_states = []

while len(guessed_states) < 50:
    guess = screen.textinput(
        title=f"{len(guessed_states)}/50 States Correct",
        prompt="What's another state's name?")

    # User pressed Cancel or empty input
    if not guess:
        continue

    guess = guess.title()
    if guess == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        data_to_learn = pandas.DataFrame(missing_states)
        data_to_learn.to_csv(OUTPUT_FILE)
        screen.bye()
        break

    if (guess in all_states and
            not guess in guessed_states):
        guessed_states.append(guess)
        state_data = data[data['state'] == guess]
        x = state_data.x.item()
        y = state_data.y.item()
        state = State()
        state.goto(x, y)
        state.write(f"{guess}", align="center", font=FONT)
    else:
        print(f"'{guess}' is not a valid U.S. state.")

screen.mainloop()
