#1.-      Create an empty dictionary called dog
dog = {}

#2.-      Add details to the dog dictionary
dog['name'] = 'Lucas'
dog['color'] = 'Brown'
dog['breed'] = 'Golden Retriever'
dog['legs'] = 4
dog['age'] = 3

#3.-      Create a student dictionary
student = {
    'first_name': 'Gael',
    'last_name': 'Trujillo',
    'gender': 'Male',
    'age': 18,
    'marital_status': 'Single',
    'skills': ['Sports', 'Play Guitar'],
    'country': 'Mexico',
    'city': 'Aguascalientes',
    'address': '123 Juan de la barrera, Aguascalientes'
}

#4.-      Get the length of the student dictionary
student_length = len(student)
print("The length of student dictionary is", student_length )

#5.-      Get the value of skills and check its data type
skills_value = student['skills']
print("Skills:", skills_value)
print("Data type of skills:", type(skills_value))

#6.-      Modify the skills values by adding one or two skills
student['skills'].append('Play Piano')
student['skills'].append('Sing')
print("Updated skills:", student['skills'])

#7.-      Get the dictionary keys as a list
student_keys = list(student.keys())
print("Keys in student dictionary:", student_keys)

#8.-      Get the dictionary values as a list
student_values = list(student.values())
print("Values in student dictionary:", student_values)

#9.-     Change the dictionary to a list of tuples using items() method
student_items = list(student.items())
print("Student dictionary as list of tuples:", student_items)

#10.-      Delete one of the items in the dictionary
del student['marital_status']

# Delete one of the dictionaries
del dog
