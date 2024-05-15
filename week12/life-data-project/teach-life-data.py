max_life = 0
min_life = 99999
life_exp_sum = 0
life_sum_count = 0

chosen_max_life = 0
chosen_min_life = 99999

chosen_year = int(input("Pick a year: "))

with open("life-expectancy.csv") as cd:
    first_line = next(cd)

    for line in cd:
        country, code, year, life_expectancy = line.strip().split(',')
        life_expectancy = float(life_expectancy)
        year = int(year)

        # Overall Min Max
        if life_expectancy > max_life:
            max_country = country
            max_year = year
            max_life = life_expectancy
        if life_expectancy < min_life:
            min_country = country
            min_year = year
            min_life = life_expectancy

        # Processed data for chosen year
        if year == chosen_year:
            # Calc ave running totals
            life_exp_sum += life_expectancy
            life_sum_count += 1

            # Chosen Min/Max
            if life_expectancy > chosen_max_life:
                chosen_max_country = country
                chosen_max_year = year
                chosen_max_life = life_expectancy
            if life_expectancy < chosen_min_life:
                chosen_min_country = country
                chosen_min_year = year
                chosen_min_life = life_expectancy

ave_life_exp = life_exp_sum / life_sum_count


print(f"""
Overall:
Max: {max_life}, {max_country}, {max_year}
Min: {min_life}, {min_country}, {min_year}
The min overall life_expectancy was {min_life} in {min_country} from the year {min_year}
    
For the year {chosen_year}:
Average: {ave_life_exp:.2f}
Max: {chosen_max_life}, {chosen_max_country}
Min: {chosen_min_life}, {chosen_min_country}
""")