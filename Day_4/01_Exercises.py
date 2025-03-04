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
print (company[10])

#18-  Create an acronym or an abbreviation for the name 'Python For Everyone'.
phrase = 'Python  For   Everyone'
acr = phrase[0:19:2]
print (acr)
#19-  Create an acronym or an abbreviation for the name 'Coding For All'.
