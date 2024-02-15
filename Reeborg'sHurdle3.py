while True:
    while front_is_clear() and not at_goal():
        move()
    if at_goal():
        break
    while wall_in_front():
        turn_left()
        move()
    for i in range(2):
        for j in range(3):
            turn_left()
        move()
    turn_left()
    if front_is_clear():
        move()
    if at_goal():
        break

        
        # while not at_goal():
        #     if wall_in_front():
        #         jump()
        #     else:
        #         move()
