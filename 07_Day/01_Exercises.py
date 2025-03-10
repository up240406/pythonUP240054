# DAY 7 ---------------------------------------------
    #LEVEL 1

#1- Find the length of the set it_companies 
it_companies = {'Amazon', 'Apple', 'Microsoft','Google', 'Facebook'}
print ('The lenght is:', len(it_companies))

#2- Add 'Twitter' to it_companies
it_companies.add ('Twitter')
print (it_companies)

#3- Insert multiple IT companies at once to the set it_companies
it_companies.update (['Nividia', 'Tesla', 'Broadcom',])
print (it_companies)

#4- Remove one of the companies from the set it_companies
it_companies.remove ('Broadcom')
print (it_companies)

#- What is the difference between remove and discard
   #Discard no salta un error si no hay item existente, mientras que remove, si da un error cuando no hay algun item
it_companies.discard ('Instagram')
print (it_companies)