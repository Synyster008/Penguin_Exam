def list_all_courses():
    # Printing the courses available with indexes
    file = open('../repo/class.txt', 'r')
    for i in file.readlines():
        print(i.strip('\n'))
    file.close()
