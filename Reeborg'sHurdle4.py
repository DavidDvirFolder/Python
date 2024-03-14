def turn_right():
    for i in range(3):
        turn_left()


def jump():
    for i in range(2):
        for i in range(3):
            turn_left()
        move()


while not at_goal():
    if not wall_on_right():
        jump()
    if wall_in_front():
        turn_left()
    if right_is_clear():
        turn_right()
    if front_is_clear():
        move()
