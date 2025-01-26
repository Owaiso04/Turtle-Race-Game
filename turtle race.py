from turtle import Turtle, Screen
import turtle
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(
    title="Make your bet", prompt="Which turtle will to win the race? Enter a color: "
)
colors = ["red", "blue", "yellow", "green", "orange", "purple"]
random.shuffle(colors)

all_turtles = []
i = 0
for color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(x=-230, y=-100 + i)
    i += 50
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for t in all_turtles:
        if t.xcor() > 230:
            is_race_on = False
            winning_color = t.pencolor()
            if winning_color == user_bet:
                t.write(
                    f"You've won! The {winning_color} turtle is the winner!",
                    align="right",
                    font=("Arial", 12, "bold"),
                )
            else:
                t.write(
                    f"Sorry, you've lost. The {winning_color} turtle is the winner!",
                    align="right",
                    font=("Arial", 12, "bold"),
                )
            break

        rand_distance = random.randint(0, 10)
        t.forward(rand_distance)


screen.exitonclick()
