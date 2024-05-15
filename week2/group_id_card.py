print(f'''
Please enter the following information
''')

first_name = input('First name: ')
last_name = input('Last name: ')
email = input('Email address: ')
phone = input('Phone number: ')
job_title = input('Job title: ')
id = input('ID Number: ')
hair = input('Hair color: ')
eyes = input('Eye color: ')
month = input('Birth month: ')
training = input('Are you in training?: ')



print(f'''
The ID Card is:
---------------------------------------------
{last_name.upper()}, {first_name.capitalize()}
{job_title.title()}
ID: {id}

{email.lower()}
{phone}

{'Hair: '+hair:<25} Eyes: {eyes}
{'Month: '+month:<25} Training: {training}
---------------------------------------------
''')