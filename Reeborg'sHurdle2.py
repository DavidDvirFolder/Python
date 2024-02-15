class Robot:
    '''
    Reeborg has entered a hurdle race,
    but he does not know in advance how long the race is. Make him run the course, following a path similar to the one shown,
    but stopping at the only flag that will be shown after the
    race has started.
    '''

    def movement(self):
        self.start_movement()
        self.turn_right()
        move()
        self.turn_right()
        move()
        turn_left()

    def start_movement(self):
        move()
        turn_left()
        move()

    def turn_right(self):
        for i in range(3):
            turn_left()

    def repeat_movement(self):
        while not at_goal():
            # while at_goal() != True:
            # while not at_goal():
            # while at_goal() == False:
            for i in range(6):
                self.movement()
                if at_goal():
                    break


my_instance = Robot()
my_instance.repeat_movement()

while front_is_clear():
    move()
    if wall_in_front():
        while not front_is_clear():
            turn_left()
            move()
        for i in range(2):
            for j in range(3):
                turn_left()
            move()
        turn_left()



