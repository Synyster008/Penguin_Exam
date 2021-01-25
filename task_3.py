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
        self.show_prompt()

    def show_prompt(self):
        # Creating the prompts and checking the user input
        prompt = input("A. Create Routine\nB. Show Routine\nC. List Courses with Teachers Name\n").upper()
        if prompt == 'A':
            self.create_routine()
        elif prompt == 'B':
            self.show_routine()
        elif prompt == 'C':
            self.list_all_courses()

    def list_all_courses(self):
        # Printing the courses available with indexes
        for i in self.classes:
            print(i[0] + ', ' + i[1])

    def create_routine(self):
        # Creating routine in accordance with the sample inputs
        days = int(input("How many days do you want to make the routine for?(1-5): "))
        for i in range(len(self.classes)):
            print(f"{i + 1}. {self.classes[i][0]}")

        print("Please enter in the format of dayIndex(0 - 4) hourIndex(0 - 3) courseIndex(1-5)")
        # Loop for entering values in different lines
        for i in range(days*4):
            self.routine.append(input().split())

        self.show_prompt()

    def show_routine(self):
        for i in self.routine:
            print(i[0] + ' ' + i[1] + ' ' + self.classes[int(i[2]) - 1][0])


# Defining the instance
routine = RoutineMaker()
