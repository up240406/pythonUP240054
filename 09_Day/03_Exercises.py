person = {
    'Gael': 'Asabeneh',
    'last_name': 'Trujillo',
    'age': 18,
    'country': 'Mexico',
    'is_marred': False,
    'skills': ['Sing', 'Swim', 'Play guitar', 'JavaScript', 'Python'],
    'address': {
        'street': 'Juan de la barrera',
        'zipcode': '12345'
    }
}

# Check if the person dictionary has skills key
if 'skills' in person:
    skills = person['skills']
    
    # Print the middle skill
    middle_index = len(skills) // 2
    print("Middle skill:", skills[middle_index])

    # Check if the person has 'Python' skill
    has_python = 'Python' in skills
    print("Has Python skill:", has_python)

    # Check developer type
    if set(skills) == {'JavaScript', 'React'}:
        print('He is a front end developer')
    elif set(skills) >= {'Node', 'Python', 'MongoDB'}:
        print('He is a backend developer')
    elif set(skills) >= {'React', 'Node', 'MongoDB'}:
        print('He is a fullstack developer')
    else:
        print('Unknown title')

# Check if the person is married and lives in Finland
if person.get('is_marred') and person.get('country') == 'Finland':
    print(f"{person['Gael']} {person['last_name']} lives in Finland. He is married.")