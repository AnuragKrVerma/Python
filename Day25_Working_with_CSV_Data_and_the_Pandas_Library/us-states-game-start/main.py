import turtle, pandas


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "Python/Day25_Working_with_CSV_Data_and_the_Pandas_Library/us-states-game-start/blank_states_img.gif"
screen.addshape(image)
screen.setup(height=491,width=725)
turtle.shape(image)

data = pandas.read_csv("Python/Day25_Working_with_CSV_Data_and_the_Pandas_Library/us-states-game-start/50_states.csv")
all_states = data["state"].tolist()
guessed_state = []

while len(guessed_state) < 50+1:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 the State" , prompt= "What's another state Name ?").title()
    print(answer_state)
    
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_state:
                missing_states.append(state)
        
        df = pandas.DataFrame(missing_states)
        df.to_csv("Python/Day25_Working_with_CSV_Data_and_the_Pandas_Library/us-states-game-start/states_to_learn.csv")
        print(missing_states)
        break
    if answer_state in all_states:
        guessed_state.append(answer_state)
        t= turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)


