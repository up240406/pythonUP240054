#1-   Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
string_1 = 'Thirty ' + 'Days ' +'Of ' + 'Python' 
print (string_1)

#2-   Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
string_2 = 'Coding ' + 'For ' + 'All' 
print (string_2)

#3-   Declare a variable named company and assign it to an initial value "Coding For All".
company = 'coding for all'   #3
print (company)   #4
print (len(company))   #5
print (company.upper ())   #6
print (company.lower ())   #7

#8-   Use capitalize(), title(), swapcase() methods to format the value of the string _Coding For All_.
print (company.capitalize ())
print (company.title ())
print (company. swapcase ())

#9-   Cut(slice) out the first word of _Coding For All_ string.
print (company [7:])

#10-  Check if Coding For All string contains a word Coding using the method index, find or other methods.
print ('coding' in company)

#11-  Replace the word coding in the string 'Coding For All' to Python.
print (company.replace ('coding', 'Python'))

#12-  Change Python for Everyone to Python for All using the replace method or other methods.
print ('python for everyone'.replace ('everyone','all'))

#13-  Split the string 'Coding For All' using space as the separator (split()) .
print (company.split ())

#14-  "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
apps = 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
print (apps.split (','))

#15-  What is the character at index 0 in the string Coding For All.
print (company [0])

#16-  What is the last index of the string Coding For All.
print (len (company)-1)
print (company [13])

#17-  What character is at index 10 in "Coding For All" string.
print (company [10])

#18-  Create an acronym or an abbreviation for the name 'Python For Everyone'.
phrase_1 = 'Python  For   Everyone'
acr_1 = phrase_1 [0:19:2]
print (acr_1)

#19-  Create an acronym or an abbreviation for the name 'Coding For All'.
phrase_2 = 'Coding  for   All'
acr_2 = phrase_2 [0:17:2]
print (acr_2)

#20-  Use index to determine the position of the first occurrence of C in Coding For All.
print (company.index ('c'))

#21-  Use index to determine the position of the first occurrence of F in Coding For All.
print (company.index ('f'))

#22-  Use rfind to determine the position of the last occurrence of l in Coding For All People.
print ("Coding For All People".rfind ('l'))

#23-  Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence_1 = 'You cannot end a sentence with because because because is a conjunction'
print (sentence_1.find ('because'))

#24-  Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence_2 = 'You cannot end a sentence with because because because is a conjunction'
print (sentence_2.rindex ('because'))

#25-  Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
start = sentence_1.find ('because')
end = sentence_1.rindex ('because') + len('because')
print (sentence_1 [start:end])

#26-  Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print (sentence_1.find ('because'))

#27-  Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
start = sentence_2.find ('because')
end = sentence_2.rindex ('because') + len('because')
print (sentence_2 [start:end])

#28-  Does ''Coding For All' start with a substring Coding?
print (company.startswith ('coding'))

#29-  Does 'Coding For All' end with a substring coding?
print(company.endswith ('coding'))

#30-  'Coding For All', remove the left and right trailing spaces in the given string.
removed = '   Coding For All      '.strip ()
print (removed)

#31-  Which one of the following variables return True when we use the method isidentifier():   ---30DaysOfPython   ---thirty_days_of_python
print ('30DaysOfPython'.isidentifier ())
print ('tirty_days_of_python'.isidentifier ())

#32-  The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
python_libraries = ('Django ', 'Flask ', 'Bottle ', 'Pyramid ', 'Falcon ')
print ('#'.join (python_libraries))

#33-  Use the new line escape sequence to separate the following sentences.
print ('I am enjoying this challenge.\nI just wonder what is next')

#34-  Use a tab escape sequence to write the following lines.
print ('Name \t\tAge\t\tCountry\t\tCity\t\tAsebeneh\t\t250\t\tFindland\t\tHelsinki')

#35-  Use the string formatting method to display the following:
radius = 10 
area = 3.14 * radius ** 2
print (f'The area of a circle with radius {radius} is {int(area)} meters square.')

#36-  Make the following using string formatting methods:
a, b = 8, 6 
print (f'{a} + {b} = {a + b}')
print (f'{a} - {b} = {a - b}')
print (f'{a} * {b} = {a * b}')
print (f'{a} / {b} = {a / b}')
print (f'{a} % {b} = {a % b}')
print (f'{a} // {b} = {a // b}')
print (f'{a} ** {b} = {a ** b}')