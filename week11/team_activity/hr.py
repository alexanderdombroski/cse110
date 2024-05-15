print()
with open("hr_system.txt") as employee_data:
    for employee in employee_data:
        data = employee.strip().split()
        # print(f"Name: {data[0]}, Title: {data[2]}")
        if data[2] == "Engineer":
            data[3] = int(data[3]) + 24000
        print(f"{data[0]} (ID: {data[1]}), {data[2]} - ${float(int(data[3]) / 24):.2f}")
print()