def compute_area_circle(radius):
    return 3.1415 * radius * radius

def compute_area_rectangle(length, width):
    return length * width

def compute_area_square(length):
    return compute_area_rectangle(length, length)

def compute_area(shape, length, width = 1):
    if shape == "square":
        area = compute_area_square(length)
    elif shape == "circle":
        area = compute_area_circle(length)
    elif shape == "rectangle":
        area = compute_area_rectangle(length, width)
    return area

print()
userinput = ""
while userinput != "quit":
    while userinput not in ["square", "rectangle", "circle", "quit"]:
        userinput = input("What shape would you like to calculate the area for? ").lower()
    if userinput == "square":
        sqr_length = float(input("What is the length of the square? "))
        print(f"The area of the square is: {compute_area('square', sqr_length):.2f}")
    elif userinput == "rectangle":
        rect_length = float(input("What is the length of the rectangle? "))
        rect_width = float(input("What is the width of the rectangle? "))
        print(f"The area of the square is: {compute_area('rectangle', rect_length, rect_width):.2f}")
    elif userinput == "circle":
        cir_radius = float(input("What is the radius of the circle? "))
        print(f"The area of the square is: {compute_area('circle', cir_radius):.2f}")
    else:
        print("\nThanks for using the area calculator\n")
    userinput = "" if userinput != "quit" else "quit"