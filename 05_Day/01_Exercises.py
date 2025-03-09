# LEVEL 1

# 1. Declare an empty list
empty_list = []

# 2. Declare a list with more than 5 items
list = [1, 2, 3, 4, 5, 6]

# 3. Find the length of your list
print(len(list))

# 4. Get the first item, the middle item, and the last item of the list
first_item = list[0]
middle_item = list[len(list)//2]
last_item = list[-1]
print(first_item, middle_item, last_item)

# 5. Declare a list with mixed data types
mixed_data = ["John Doe", 25, 5.9, "Single", "123 Main St"]

# 6. Declare a list variable named it_companies
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

# 7. Print the list
print(it_companies)

# 8. Print the number of companies in the list
print(len(it_companies))

# 9. Print the first, middle, and last company
print(it_companies[0], it_companies[len(it_companies)//2], it_companies[-1])

# 10. Modify one of the companies
it_companies[1] = "Instagram"
print(it_companies)

# 11. Add an IT company
it_companies.append("Tesla")
print(it_companies)

# 12. Insert an IT company in the middle
it_companies.insert(len(it_companies)//2, "TikTok")
print(it_companies)

# 13. Change one IT company name to uppercase (excluding IBM)
it_companies[2] = it_companies[2].upper()
print(it_companies)

# 14. Join the companies with '#; '
print("#; ".join(it_companies))

# 15. Check if a certain company exists
print("Google" in it_companies)

# 16. Sort the list
it_companies.sort()
print(it_companies)

# 17. Reverse the list in descending order
it_companies.reverse()
print(it_companies)

# 18. Slice out the first 3 companies
print(it_companies[:3])

# 19. Slice out the last 3 companies
print(it_companies[-3:])

# 20. Slice out the middle IT company/companies
mid = len(it_companies) // 2
print(it_companies[:mid] + it_companies[mid+1:])

# 21. Remove the first IT company
it_companies.pop(0)
print(it_companies)

# 22. Remove the middle IT company
mid = len(it_companies) // 2
del it_companies[mid]
print(it_companies)

# 23. Remove the last IT company
it_companies.pop()
print(it_companies)

# 24. Remove all IT companies
it_companies.clear()
print(it_companies)

# 25. Destroy the IT companies list
del it_companies

# 26. Join the following lists
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
full_stack = front_end + back_end
print(full_stack)

# 27. Copy full_stack and insert Python and SQL after Redux
full_stack.insert(full_stack.index("Redux") + 1, "Python")
full_stack.insert(full_stack.index("Python") + 1, "SQL")
print(full_stack)


# LEVEL 2

# 1. List of students' ages
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# 2. Sort the list and find min and max age
ages.sort()
min_age = min(ages)
max_age = max(ages)
print("Sorted ages:", ages)
print("Min age:", min_age, "Max age:", max_age)

# 3. Add min and max age again to the list
ages.append(min_age)
ages.append(max_age)
print("Updated ages:", ages)

# 4. Find the median age
age = len(ages)
if age % 2 == 0:
    median_age = (ages[age//2 - 1] + ages[age//2]) / 2
else:
    median_age = ages[age//2]
print("Median age:", median_age)

# 5. Find the average age
average_age = sum(ages) / len(ages)
print("Average age:", average_age)

# 6. Find the range of the ages
age_range = max_age - min_age
print("Age range:", age_range)

# 7. Compare (min - average) and (max - average)
min_diff = abs(min_age - average_age)
max_diff = abs(max_age - average_age)
print("Min - Average:", min_diff, "Max - Average:", max_diff)

# 8. Find the middle country(ies) in the list
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
countries.sort()
country = len(countries)
if country % 2 == 0:
    middle_countries = countries[country//2-1:country//2+1]
else:
    middle_countries = [countries[country//2]]
print("Middle country(ies):", middle_countries)

# 9. Divide the countries list into two equal lists
first_half = countries[:(country+1)//2]
second_half = countries[(country+1)//2:]
print("First half:", first_half)
print("Second half:", second_half)

# 10. Unpack first three countries and the rest as scandic countries
first, second, third, *all_countries = countries
print("First three countries:", first, second, third)
print("Scandic countries:", all_countries)
