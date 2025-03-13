#LEVEL 3

#1- Convert the ages to a set and compare the length of the list and the set, which one is bigger?
ages = ['16', '20', '15', '19', '21', '18', '22', '27', '28', '23',]
ages_set = set (ages)
print ('The lenght of the list is:', len (ages))
print ('The lenght of the set is:', len (ages_set))
print ('The list is bigger than the set' if len (ages) > len (ages_set) else 'The set is bigger than the list' if len (ages) < len (ages_set) else 'The list and the set have the same lenght')

#2- Explain the difference between the following data types: string, list, tuple and set
     # The STRING is inmutable and have an order
     # The STRING is mutable and have an order 
     # The TUPLE is inmutable and have an order 
     # The SET is mutable and have no order 

#3- I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
sentence = 'I am a teacher and I love to inspire and teach people'
words = sentence.split () 
unique_words = set (words)
print ('The unique words are:', unique_words)
print ('the number of unique words is:', len (unique_words))