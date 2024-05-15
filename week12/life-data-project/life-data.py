with open("life-expectancy.csv") as cd:

    target_year = 0
    incorrect_input = True
    while incorrect_input:
        target_year = input("\nEnter the year of interest: ")
        try: 
            target_year = int(target_year)
        except:
            print("Please enter an integer value")
        else:
            target_year = int(target_year)
            if target_year < 1543 or target_year > 2019:
                print("Please enter a value between 1543 and 2019")
            else:
                incorrect_input = False
    
    target_year_values = 0
    target_year_sum = 0
    target_min_life = 999
    target_max_life = 0
    min_life = 999
    max_life = 0
    life_expectancy_total = 0
    life_expectancy_values = 0

    next(cd)

    for line in cd:
        line = line.strip()
        data = line.split(",")
        
        entity, code, year, life_expectancy = data[0], data[1], int(data[2]), float(data[3])
        if life_expectancy < min_life:
            min_life = life_expectancy
            min_life_country = entity
            min_life_year = year
        if life_expectancy > max_life:
            max_life = life_expectancy
            max_life_country = entity
            max_life_year = year
        
        if year == target_year:
            target_year_sum += life_expectancy
            target_year_values += 1
            if target_max_life < life_expectancy:
                target_max_life = life_expectancy
                target_max_country = entity
            if target_min_life > life_expectancy:
                target_min_life = life_expectancy
                target_min_country = entity
        life_expectancy_total += life_expectancy
        life_expectancy_values += 1


print(f"""
The overall max life expectancy is: {max_life:.2f} from {max_life_country} in {max_life_year}
The overall min life expectancy is: {min_life:.2f} from {min_life_country} in {min_life_year}
The average life expectancy calculated from data taken over the past 500 years is {life_expectancy_total / life_expectancy_values:.2f}""")
try:
    target_year_sum / target_year_values
except:
    print("\nSorry, there is no data for the year of interest.")
else:
    print(f"""
For the year {target_year}:
The average life expectancy across all countries was {target_year_sum / target_year_values:.2f}
The max life expectancy was in {target_max_country} with {target_max_life:.2f}
The min life expectancy was in {target_min_country} with {target_min_life:.2f}
""")
