
total_min_life = 9999
selected_min_life = 9999
total_max_life = 0
selected_max_life = 0

chosen_year = int(input("pick a year: "))
chosen_year_sum = 0
chosen_year_num = 0
file_lines = []
with open("life-expectancy.csv") as cd:
    firstline = next(cd)
    for line in cd:
        line = line.strip()
        line = line.split(',')
        line[3] = int(line[3])
        line[4] = float(line[4])
        file_lines.append(line)

for country, code, year, life_expectancy in file_lines:
    if total_max_life < life_expectancy:
        total_max_life = life_expectancy
        overall_top_country = country
        max_expectancy_year = year
    if total_min_life > life_expectancy:
        total_min_life = life_expectancy
        overall_min_country = country
        min_expectancy_year = year

    if year == chosen_year:
        # Calculate chosen year life average here also 
        if selected_max_life < life_expectancy:
            selected_max_life = life_expectancy
            selected_max_country = country
            max_selected_expectancy_year = year
        if selected_min_life < life_expectancy:
            selected_min_life = life_expectancy
            selected_min_country = country
            min_selected_expectancy_year = year
