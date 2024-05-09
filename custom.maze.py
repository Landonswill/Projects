import turtle as trtl

# ----- maze and turtle config variables
screen_h = 400
screen_w = 420
startx = -100
starty = -100
turtle_scale = 1.5
cell_size = 50  # Size of each maze cell

# Maze definition (0: open path, 1: obstacle, 2: final destination)
maze = [
    [0, 1, 1, 1, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [1, 0, 0, 0, 2],
    [0, 0, 1, 0, 0]
]

# Target position (top right square)
target_row, target_col = 2, 5

# ----- robot commands

def move_up():
    robot.setheading(90)
    robot.forward(cell_size)

def move_down():
    robot.setheading(270)
    robot.forward(cell_size)

def move_left():
    robot.setheading(180)
    robot.forward(cell_size)

def move_right():
    robot.setheading(0)
    robot.forward(cell_size)

# if the robot has reached the final destination
def reached_destination(row, col):
    return row == target_row and col == target_col and maze[row][col] == 2

# if the robot can move to a specific spot in the maze
def can_move_to(row, col):
    return 0 <= row < len(maze) and 0 <= col < len(maze[0])


# ----- init screen
wn = trtl.Screen()
wn.setup(width=screen_w, height=screen_h)
robot_image = "robot2.gif"
wn.addshape(robot_image)

# ----- init robot
robot = trtl.Turtle(shape=robot_image)
robot.color("darkorchid")
robot.penup()
robot.turtlesize(turtle_scale, turtle_scale)
robot.goto(startx, starty)
robot.showturtle()  # Show the turtle after positioning
robot.speed(2)

# ---- set maze background
wn.bgpic("mazecustom.png")

# available commands
print("Available commands: 'up', 'down', 'left', 'right'")

# User input loop
while True:
    user_input = input("Enter a command: ").lower()

    current_row, current_col = robot.position()
    [startx, starty]= 0,0

    #current_row = int((-current_row + starty) / cell_size)
    #current_col = int((current_col - startx) / cell_size)
    print([current_row, current_col])

    if (
        user_input == "up" and
        can_move_to(current_row + 1, current_col) !=1
    ):
        move_up()
    elif (
        user_input == "down" and
        can_move_to(current_row - 1, current_col) !=1
    ):
        move_down()
    elif (
        user_input == "left" and
        can_move_to(current_row, current_col - 1) !=1
    ):
        move_left()
    elif (
        user_input == "right" and
        can_move_to(current_row, current_col + 1) !=1
    ):
        move_right()
    else:
        print("Invalid move. Try again.")

    if reached_destination(current_row, current_col):
        print("Congratulations! You reached the final destination.")
        break