from turtle import Turtle, Screen
import random

while True:
    is_race_on = False
    screen = Screen()
    screen.setup(width=500, height=400)
    screen.title("Welcome to the Turtle race!")
    user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    y_positions = [-120, -70, -20, 30, 80, 130]
    all_turtles = []

    for turtle_index in range(0, 6):
        new_turtle = Turtle(shape="turtle")
        new_turtle.color(colors[turtle_index])
        new_turtle.shapesize(1.5)
        new_turtle.penup()
        new_turtle.goto(x=-230, y=y_positions[turtle_index])
        all_turtles.append(new_turtle)

    if user_bet:
        is_race_on = True

    while is_race_on:
        for turtle in all_turtles:
            if turtle.xcor() > 230:
                is_race_on = False
                winning_color = turtle.pencolor()
                if winning_color == user_bet:
                    print(f"You've won! The {winning_color} turtle is the winner!")
                    end_game = screen.textinput(title=f"You've won! The {winning_color} turtle is the winner!",
                                                prompt="Would you like to bet on it? Enter reset or end: ")
                else:
                    print(f"You've lost! The {winning_color} turtle is the winner!")
                    end_game = screen.textinput(title=f"You've lost! The {winning_color} turtle is the winner!",
                                                prompt="Would you like to bet on it? Enter reset or end: ")

            random_distance = random.randint(0, 10)
            turtle.forward(random_distance)
    if end_game == 'end':
        screen.bye()
        break
    else:
        screen.clear()
    screen.exitonclick()
