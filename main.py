from turtle import Turtle, Screen
import pandas
from update_map import UpdateMap

# Define Objects from Classes
screen = Screen()
turtle = Turtle()
map_update = UpdateMap()

# Window Setup
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
screen.setup(width=725, height=491)
turtle.shape(image)
screen.tracer(0)

# Read the CSV File
states_data = pandas.read_csv("50_states.csv")  # Read the CSV file
state_list = states_data.state.to_list()


def get_selected_state_details(selected_state):
    details = states_data[states_data.state == selected_state]  # Get the corresponding state data for user input
    return details


def get_selected_state_name(details):
    name = details.state.item()
    return name


def get_selected_state_map_pos(details):
    map_pos = (int(details.x), int(details.y))  # Get the above selected states x and y columns
    return map_pos


guessed_states = []
is_game_on = True

while len(guessed_states) < 50:

    score = f"{len(guessed_states)}/50"
    user_input = screen.textinput(title=score, prompt="Name another state?")
    user_input = user_input.title()

    if user_input == "Exit":
        break

    if user_input in state_list:
        guessed_states.append(user_input)

        state_details = get_selected_state_details(user_input)
        state_name = get_selected_state_name(state_details)
        state_map_pos = get_selected_state_map_pos(state_details)

        map_update.write_state_name(state=state_name, pos=state_map_pos)

    screen.update()

for element in state_list:
    if element not in guessed_states:
        state_details = get_selected_state_details(element)
        state_name = get_selected_state_name(state_details)
        state_map_pos = get_selected_state_map_pos(state_details)

        map_update.write_state_name(state=state_name, pos=state_map_pos)
        guessed_states.append(element)

screen.exitonclick()
