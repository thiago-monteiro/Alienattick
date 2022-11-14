world_speed = 2

optionList = []

class Option:
    def __init__(self):
        self.name = "OPTION"

        self.world_speed = 3
        self.star_speed = 1

        optionList.append(self)

    def increase_speed(self):

        self.world_speed += 3
        self.star_speed += 1

        print(self.world_speed)
        print(self.star_speed)

    def decrease_speed(self):

        if self.world_speed > 0:
            self.world_speed -= 3
            self.star_speed -= 1

        else:
            self.world_speed = 0
            self.star_speed = 0


        print(self.world_speed)
        print(self.star_speed)

option1 = Option()