# Task 1: Converting a basic for loop into a list comprehension

cars = ['honda', 'toyota', 'chevrolet', 'jeep', 'ford']

# basic for loop
for car in cars:
    print(car)

# list comprehension
[print(car) for car in cars]

# Task 2: Converting lower case car names into uppercase

new_cars = []

# using for loop
for car in cars:
    car = car.upper()
    new_cars.append(car)    # append method is time consuming 

cars = new_cars
print(cars)

# list comprehension
cars = [car.upper() for car in cars]    # no need to use append, saves time!
print(cars)


# Task 3: Working with Boolean values

bits = [True, False, False, True, True, True, False]
new_bits = []

# for loop and conditional
for bit in bits:
    if bit == True:
        new_bits.append(1)
    else:
        new_bits.append(0)

# list comprehension
super_bits = [1 if bit == True else 0 for bit in bits]

print(bits)
print(new_bits)
print(super_bits)

# Task 4: Sring Manipulation: Customize a messy string to make it readable

my_string = "ProgrammingIsFunAndExciting"
new_string = ""

# loop and conditionals
for char in my_string:
    if char.isupper():
        new_string += " "+ char
    else:
        new_string += char

print(new_string[1:])

# list comprehension
customized_string = "".join([char if char.islower() else " " + char  for char in my_string])[1:]

print(customized_string)

# Task 5: Use Nested For-Loops to Handle Nested Iterables

genius = ['Albert', 'Newton', 'Faraday', 'Steve', 'Max']
letters = []

for name in genius:
    for char in name:
        letters.append(char)

print(letters)

# list comprehension
letters = [char for name in genius for char in name]
print(letters)

# we can add the optional if conditions after any for-loops
letters = [char for name in genius for char in name if len(name) < 5]
print(letters)


# Task 6: Avoid higher-order function for readability

# non list comprehension
list1 = filter(lambda a: len(a) < 5, genius)
print(list(list1))

# list comprehension way
list2 = [name for name in genius if len(name) < 5]
print(list2)