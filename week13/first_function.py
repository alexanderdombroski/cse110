print()

def data_calculations(number_list):
    try: 
        sum(number_list)
    except: 
        print("error\n")
    else: 
        print(sorted(number_list))
        print(f"Total: {sum(number_list)}")
        print(f"Mean: {sum(number_list) / len(number_list):.2f}")
        print(f"Min: {min(number_list)}, Max: {sum(number_list)}")
        print(f"Reverse Order: {sorted(number_list, reverse = True)}\n")

data_calculations([1,3,6,34,76,14,320])
data_calculations([1,2,3,4,7,8,9])
data_calculations("Hi I don't like numbers")