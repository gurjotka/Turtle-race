from turtle import Turtle, Screen
import random

# #Etch- Sketch drawing

# def forward():
#     return tim.forward(100)

# def backward():
#     return tim.backward(100)

# def clear_drawing():
#     tim.home()
#     tim.clear()

# def anti_clockwise():
#     return tim.left(45)

# def clockwise():
#     return tim.right(45)

# screen.listen()
# screen.onkey(forward, "w")
# screen.onkey(backward, "s")
# screen.onkey(clockwise, "a")
# screen.onkey(anti_clockwise, "d")
# screen.onkey(clear_drawing, "c")

#Turtle race
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt = "Which turtle will win the race? Enter a color: ")
colors = ["red", "blue", "green", "purple", "brown", "orange"]
y_positions = [-120, -80, -40, 0, 40, 80]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape = "turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor()> 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won!! The {winning_color} turtle won.")
            else:
                print(f"You've lost!! The {winning_color} turtle won.")
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)








screen.exitonclick()