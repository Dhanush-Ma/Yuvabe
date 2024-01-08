import copy
import math
import random
from functions import formatedMessage


# multiple assignment
name, height, age = "jane doe", 170, 32
isPremium = True
like = True
dislike = False

# string methods
# name = name.split()
print(f"{name[1:5:2]}, his age is {age}")

# math operators
a = 4.56
print(math.ceil(a))
print(math.floor(a))

i = 0
while i <= 10:
    i += 1
    print(random.randint(1, 10))

isWon = True
num = random.randint(1, 10)
while not isWon:
    # while True:
    guess = int(input("Enter a number: "))
    if guess == num:
        isWon = True
        break
    elif guess > num:
        print("Too high\n")
    else:
        print("Too low\n")
print("You won!")

name = "Jane"
if name == "Jan" or "":
    print("True")

print("" == True)

# Lists
scores = [90, 20, 30]
new_scores = [40, 50]
scores.extend(new_scores)
print(len(scores))
scores.sort(reverse=True)
print(scores)

# for loop

for c in scores:
    print(c)

for i in range(len(scores)):
    print(scores[i], end=" ")

# Memory Refernce
print("\n\n")
list1 = [10, 20, 30]
# list2 = list1 # Memory Reference
list2 = list1.copy()  # Generates a copy
list1[0] = 90
print(list1)
print(list2)

# copy.deepcopy() # for 2d arrays

# tuple
tuple1 = (4, 9, 0)
tuple1 = (9, 4)  # possible
# tuple1[0] = 6 #not possible

# dict
user = {
    "name": "Jane Doe",
    "email": "janedoe@gmail.com",
    "password": "XXXXXXX",
    "postsId": [1, 2, 3],
}

user.update({"name": "Jane"})

for key in user.keys():
    print(user[key])
print(user["name"])

# Set
uniqueNums = {1, 2, 4, 4, 4}
print(uniqueNums)

for i in list(uniqueNums):
    print(i)
