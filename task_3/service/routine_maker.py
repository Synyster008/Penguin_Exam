class RoutineMaker:
    def __init__(self):
        # Defining the data
        self.classes = [
            ('English Grammar', 'John Smith'),
            ('Mathematics', 'Lara Gilbert'),
            ('Physics', 'Johanna Kabir'),
            ('Chemistry', 'Danniel Robertson'),
            ('Biology', 'Larry Cooper')
        ]
        self.routine = []

    def create_routine(self):
        # Creating routine in accordance with the sample inputs
        days = int(input("How many days do you want to make the routine for?(1-5): "))
        for i in range(len(self.classes)):
            print(f"{i + 1}. {self.classes[i][0]}")

        print("Please enter in the format of dayIndex(0 - 4) hourIndex(0 - 3) courseIndex(1-5)")
        # Loop for entering values in different lines
        with open('../repo/routine.txt', 'w') as file:
            for i in range(days*4):
                file.write(input()+'\n')


    def show_routine(self):
        with open('../repo/routine.txt', 'r') as file:
            for i in file.readlines():
                print(i[0] + ' ' + i[2] + ' ' + self.classes[int(i[4]) - 1][0])