print ('Hello, World!')
# Variables and assigment operators
mv_popultion = 74728
mv_popultion += 4000 - 600
print (mv_popultion)

# Quiz
# # The current volume of a water reservoir (in cubic metres)
reservoir_volume = 4.445e8
# The amount of rainfall from a storm (in cubic metres)
rainfall = 5e6

# decrease the rainfall variable by 10% to account for runoff
rainfall *= 0.90
# add the rainfall variable to the reservoir_volume variable
reservoir_volume += rainfall

# increase reservoir_volume by 5% to account for stormwater that flows
# into the reservoir in the days following the storm
reservoir_volume *= 1.05

# decrease reservoir_volume by 5% to account for evaporation
reservoir_volume *= 0.95

# subtract 2.5e5 cubic metres from reservoir_volume to account for water
# that's piped to arid regions.
reservoir_volume -= 2.5e5

# print the new value of the reservoir_volume variable
print(reservoir_volume)

# strings
this_string = 'Simon\'s skateboard is in the garage.'
print(this_string)

first_word = 'hello'
second_word = 'world'
print(first_word + second_word)
print (first_word + '' + second_word)
print(first_word * 5)
print(len(first_word+second_word))
print(first_word[2])

# Quiz

# TODO: Fix this string!

ford_quote = 'Whether you think you can, or you think you can\'t--you\'re right.'

# Quiz
username = "Kinari"
timestamp = "04:50"
url = "http://petshop.com/pets/mammals/cats"

# TODO: print a log message using the variables above.
# The message should have the same format as this one:
# "Yogesh accessed the site http://petshop.com/pets/reptiles/pythons at 16:20."

print(username + " accessed the site " + url + " at " + timestamp + ".")

# Quiz

given_name = "William"
middle_names = "Bradley"
family_name = "Pitt"

name_length = len(given_name+middle_names+family_name) + 2
#todo: calculate how long this name is

# Now we check to make sure that the name fits within the driving license character limit
# Nothing you need to do here
driving_license_character_limit = 28
print(name_length <= driving_license_character_limit)


# Type and Type conversions
# Quix
mon_sales = "121"
tues_sales = "105"
wed_sales = "110"
thurs_sales = "98"
fri_sales = "95"

#TODO: Print a string with this format: This week's total sales: xxx
# You will probably need to write some lines of code before the print statement.

total_sales = int(mon_sales)+int(tues_sales)+int(wed_sales)+int(thurs_sales)+int(fri_sales)
total_sales = str(total_sales)

print("This week\'s total sales: " + total_sales)

# String Methods
print("sonal sood".title())

print("it is a beautiful day".islower())

# Practice format()

kind_str= "Kind {} still {}"
print(kind_str.format("souls", "exist"))

# Practice split()

new_str="love and kindness."
print(new_str.split())
print(new_str.split(' ', 2))
print(new_str.split("."))





