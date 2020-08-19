# Data Structures
# 1. Lists
# 1.1 List indexing

month = 8
days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]

# use list indexing to determine the number of days in month

num_days=days_in_month[month + 1]
print(num_days)

# Slicing lists

eclipse_dates = ['June 21, 2001', 'December 4, 2002', 'November 23, 2003',
                 'March 29, 2006', 'August 1, 2008', 'July 22, 2009',
                 'July 11, 2010', 'November 13, 2012', 'March 20, 2015',
                 'March 9, 2016']
                 
                 
# TODO: Modify this line so it prints the last three elements of the list
print(eclipse_dates[-3:])

# Functions for lists
# len, max, min and Lists

a = [1, 5, 8]
b = [2, 6, 9, 10]
c = [100, 200]

print(max([len(a), len(b), len(c)]))
print(min([len(a), len(b), len(c)]))

# sorted, join and Lists

names = ["Carol", "Albert", "Ben", "Donna"]
print(" & ".join(sorted(names)))

# append and Lists

names = ["Carol", "Albert", "Ben", "Donna"]
names.append("Eugenia")
print(sorted(names))

print(" & ".join(sorted(names)))

# Quiz

arr = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(arr[0])

# Print ['c', 'd', 'e', 'f']

print(arr[2:6])

# Print ['a', 'b', 'c']

print(arr[:3])

# Print ['e', 'f', 'g']

print(arr[4:])

# Dictionaries 

# Define a Dictionary, population,
# that provides information
# on the world's largest cities.
# The key is the name of a city
# (a string), and the associated
# value is its population in
# millions of people.

#   Key     |   Value
# Shanghai  |   17.8
# Istanbul  |   13.3
# Karachi   |   13.0
# Mumbai    |   12.5


population={'Shanghai':17.8, 'Istanbul':13.3, 'Karachi':13.0, 'Mumbai':12.5}








