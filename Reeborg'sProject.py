class Robot:

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
        for i in range(6):
            self.movement()

#remark
my_instance = Robot()
my_instance.repeat_movement()
