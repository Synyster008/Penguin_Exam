import sys
sys.path.append("..")

from service import RoutineMaker, show_prompt, list_all_courses

routine = RoutineMaker()
running = True

while running:
    prompt = show_prompt()
    if prompt == 'A':
        routine.create_routine()
    elif prompt == 'B':
        routine.show_routine()
    elif prompt == 'C':
        list_all_courses()

    continue_prompt = input("Continue? Y/N\n").upper()
    if continue_prompt == 'N':
        running = False



