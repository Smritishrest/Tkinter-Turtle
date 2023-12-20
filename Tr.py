import tkinter as tk
import random
import turtle
from tkinter import simpledialog
import time


window = tk.Tk()
window.title("Turtle Race Game")
player1 = turtle.Turtle()
player2 = turtle.Turtle()
target_turtle = turtle.Turtle()
colors = ('red', 'blue', 'pink', 'purple', 'black', 'green')
target_x, target_y = 0, 0
time_limit = 180
winner_declared = False
start_time_player1 = 0
start_time_player2 = 0


def set_target():
    global target_x, target_y
    tt = turtle.Turtle()
    tt.shape("turtle")
    tt.width(10)
    tt.pensize(8)
    tt.color('yellow')
    tt.write('destination')
    target_x = simpledialog.askinteger("Input", "Enter target x-coordinate:")
    target_y = simpledialog.askinteger("Input", "Enter target y-coordinate:")

    target_turtle.hideturtle()
    target_turtle.penup()
    target_turtle.goto((target_x, target_y))
    target_turtle.shape('square')
    target_turtle.shapesize(1)
    target_turtle.color('red')
    target_turtle.stamp()

    return (target_x, target_y)


def display_winner(winner):
    print(f"{winner} is the winner!")
    turtle.bye()


def check_distance():
    global winner_declared
    distance_player1 = player1.distance(target_x, target_y)
    distance_player2 = player2.distance(target_x, target_y)

    if distance_player1 < 10 and distance_player2 < 10:
        print("Both players reached the destination. Determining winner based on distance.")
        if distance_player1 < distance_player2:
            display_winner("Player 1")
        else:
            display_winner("Player 2")
        winner_declared = True
    elif distance_player1 < 10:
        display_winner("Player 1")
        winner_declared = True
    elif distance_player2 < 10:
        display_winner("Player 2")
        winner_declared = True
    else:
        elapsed_time_player1 = time.time() - start_time_player1
        elapsed_time_player2 = time.time() - start_time_player2

        if elapsed_time_player1 > time_limit and elapsed_time_player2 > time_limit:
            print("Time limit exceeded. Determining winner based on distance.")
            if distance_player1 < distance_player2:
                display_winner("Player 1")
            else:
                display_winner("Player 2")
            winner_declared = True
        else:
            window.after(100, check_distance)


def check_time_elapsed(start_time):
    current_time = time.time()
    elapsed_time = current_time - start_time
    if elapsed_time > time_limit and not winner_declared:
        print("Time limit exceeded. Determining winner based on distance.")
        check_distance()
    else:
        window.after(100, lambda: check_time_elapsed(start_time))


def pl1():
    global player1, start_time_player1
    player1.shape('turtle')
    player1.pensize(4)
    player1.write('start from here')

    player1.speed(0)
    color1 = simpledialog.askstring("Input", "what color do you want your turtle?:")
    player1.color(color1)

    start_time_player1 = time.time()

    def up():
        player1.setheading(90)
        player1.forward(10)

    def down():
        player1.setheading(270)
        player1.forward(10)

    def left():
        player1.setheading(180)
        player1.forward(10)

    def right():
        player1.setheading(0)
        player1.forward(10)

    def reached_destination():
        check_distance()

    turtle.listen()
    turtle.onkey(up, 'Up')
    turtle.onkey(down, 'Down')
    turtle.onkey(left, 'Left')
    turtle.onkey(right, 'Right')
    turtle.onkey(reached_destination, 'Return')  # Pressing 'Enter' sets the event

    check_time_elapsed(start_time_player1)


def pl2():
    global player2, start_time_player2
    player2.shape('turtle')
    player2.pensize(4)
    player2.color(random.choice(colors))
    player2.write("player 2 start from here ")

    start_time_player2 = time.time()
    while player2.distance(target_x, target_y) > 10 and not winner_declared:
        player2.setheading(random.uniform(0, 360))
        player2.forward(10)
        turtle.Screen().update()
        time.sleep(0.1)
    end_time_player2 = time.time()
    elapsed_time_player2 = end_time_player2 - start_time_player2
    print(f"Player 2 reached the destination in {elapsed_time_player2:.2f} seconds.")
    check_distance()


def start_race():
    set_target()
    pl1()
    pl2()
    print("Race finished!")


def exit_race():
    turtle.bye()


button1 = tk.Button(window, text="Player 1 (Keyboard)", font=("Arial", 18, 'normal'), command=pl1, width=20, fg='grey')
button1.pack(pady=10)

button2 = tk.Button(window, text="Player 2 (Random)", font=("Arial", 18, 'normal'), command=pl2, width=20, fg='grey')
button2.pack(pady=10)

start_race_button = tk.Button(window, text="Start Race", font=("Arial", 18, 'normal'), command=start_race, width=15, fg='grey')
start_race_button.pack(pady=10)

exit_race_button = tk.Button(window, text="Exit Game", font=("Arial", 18, 'normal'), command=exit_race, width=15, fg='grey')
exit_race_button.pack(pady=10)

window.mainloop()