# Create dictionary for inputs and input prompts for madlib
d = {'adjective1':'', 
'animal1':'', 
'verb1':'', 
'exclamation1':'', 
'verb2':'', 
'verb3':'',
'animal2':'',
'verb4':'',
'name1':'',
'exclamation2':''
}

# retrieve inputs and utilize dictionary tags as input prompts
print('''
Please enter the following:
''')
for key in d:
    d[key] = input(f'{str(key).capitalize()[:-1]}: ')

# create madlib
print(f'''
Your story is:

The other day, I was really in trouble. It all started when I saw a very
{d["adjective1"].lower()} {d["animal1"].lower()} {d["verb1"].lower()} down the hallway. "{d["exclamation1"].capitalize()}!" I yelled. But all
I could think to do was to {d["verb2"].lower()} over and over. Miraculously, that caused 
it to stop, but not before it tried to {d["verb3"].lower()} right in front of my family.

All of the sudden, a {d["animal2"].lower()} pounced and ate the {d["animal1"].lower()}. It decided 
to {d["verb4"].lower()} and then it ran off. {d["name1"].capitalize()}, one of my siblings said, "{d["exclamation2"].capitalize()}. I 
didn't know that a {d["animal2"].lower()} could eat a {d["animal1"].lower()}." 
''')