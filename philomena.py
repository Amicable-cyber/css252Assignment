# Declare and initialize an array of fruits
fruits = ["Apple", "Banana", "Cherry", "Mango"]


# Declare and initialize a two-dimensional array of numbers
numbers = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


# Traverse the fruits array using a for loop
for fruit in fruits:
    print(fruit)


# Traverse the numbers array using nested for loops
for row in numbers:
    for num in row:
        print(num)


# Concatenate the strings of the fruits array
concatenated_fruits = " ".join(fruits)
print(concatenated_fruits)


# Concatenate the numbers array
concatenated_numbers = " ".join(str(num) for row in numbers for num in row)
print(concatenated_numbers)
