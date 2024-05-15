with open("hr_system.txt") as people:
    for line in people:
        person_data = line.split()
        print(person_data[0])