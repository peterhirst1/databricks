# Databricks notebook source
print("hello world")
first_name = "peter"
second_name = "hirst"

bool1 =True
bool2 = False

int1 = 15
int2 = 25
int3 = -30

float1 = 1.5
float2 = 2.5

list1 = [1,2,3,4,5]
list_product = ["One", "Two" ," Three" ,"Four"]

print(list_product)

print("sum: ", number1 + number2)
print("subtraction: ", number1 - number2)
print("mult: ", number1 * number2)
print("div: ", number1 + number2)

print("Integer Division: ", number1 // number2)
print("Modulo: ", number1 % number2)

      

# COMMAND ----------

number1 = input("please enter a number")
number2 = input("enter a second")

print(int(number1) + int(number2))

# COMMAND ----------

varName = "variable"
var2Name = 12

var2Name = var2Name - 2

print(var2Name)

# COMMAND ----------

num1 = 12
num2 = 23

print(num1 == num2)
print(num1 < num2)
print(num1 > num2)
print(num1 != num2)
print(num1 <= num2)
print(num1 >= num2)



# COMMAND ----------

num1 = 12
num2 = 23

print( num1 == num2 or 10 > 11)

# COMMAND ----------

num1 = 14
num2 = 13

if num1 > num2: 
    print("first number is greater")
elif num1 == num2:
    print("the number is equal")
else: 
    print("the second number is greater")

# COMMAND ----------

num1 = input("please enter a number")
num2 = input("enter a second")

      
if num1 > num2: 
    print("number 1 is larger")
else:
    print("number 2 is larger")
      

# COMMAND ----------

num1 = input("please enter a year")
num2 = 1996, 2000, 2004, 2008, 2012, 2016, 2020, 2024, 2028, 

if num1 == num2 print("you are born on a leap year")



# COMMAND ----------

inputyear = input("what year are u born in")

if(int(inputyear) % 4 == 0):
   print("born on a leap year")
else:
   print("not born on a leap year")

# COMMAND ----------

products = [1,2,3,4,5,6,7,8]


for counter in range(len(products)):
    print(counter, products[counter])
    

# COMMAND ----------

products = [1,2,3,4,5,6,7,8]

print(products[1])

# COMMAND ----------

count = 1 
while count < 10:
    print(count)
    count += 1

# COMMAND ----------

#while creates loops
password = "opensesame1"

entry = False

while entry != password:
    entry = input("enter password")
    
print("wlecome in")

# COMMAND ----------

guess = False
while guess != "peter"
    guess = imput("guess my name")
print("correct")

# COMMAND ----------

while True:
    guess = input("guess my name")
    if guess == "peter":
        print("correct")
        break
        print("wrong")

# COMMAND ----------

while True:
    guess = input("guess my name")
    if guess != "peter":
        print("wrong")
        continue
        print("continue")
        break

# COMMAND ----------

total = 0
while True:
    guess = input("next number?...")
    if(int(guess) == 0):
        break
    else:
        total += int(guess)
        print("Current total: ", total)
print(total)


# COMMAND ----------

import random

num = 3.1473

print(round("num 3")
print(eval("num + 1"))
      
print(random.randit(1, 5))
 # generates random number 

# COMMAND ----------

def printmessage(message):
    print(message)

    
printmessage(hello)
printmessage(goodbye)

# COMMAND ----------

def square(number):
    squaredNumber = number ** 2
    return squareNumber
    
def output(num):
    print(num)

numToSquare = 5

answer = square(numToSquare)

print("the square of " + str(numToSquare) + " is: ", answer)

# COMMAND ----------

weight= int(input("what is your weight"))
unit = input("in (Kg) or (lb)?")
if unit.lower() == "Kg":
    conversion = weight * 2.205
    print(f"your weight in pounds is {conversion}lb")
else:
    conversion = weight // 2.205
    print(f"your weight in kilograms is {converison}Kg")
except ValueError:
    print("sorry you made an invalid input")

# COMMAND ----------

temp= int(input("what is the temperature"))
unit = input("in (fahrenheit) or (celcius)?")
if unit() == "celcius":
    conversion = temp * 1.8
    print("the temp in fahrenheit is{conversion}fahrenheit")


# COMMAND ----------

number_to_conv = 10

#function will accept boolean:
# True: convert c -> f
# False: convert f -> c
def temp_converter(num, bool ):
    if(bool == False):
        return ((num - 32) * 5/9)
    #convert to celcius
    
    else:
        return((num * 1.8) + 32)
        
temp_converter(10,True)

# COMMAND ----------


list1 = [1,2,3,4,5, "stings", True, False]

list.append("hello world")

list1[2]

# COMMAND ----------

list1 = [[1,2,3], [4,5,6], [7,8,9]]
#create multiple lists
print(list1[1])
#print list 


# COMMAND ----------

import random

my_list = ["i", "d", "l", "e"]

# del my_list[2:4]
#my_list[1] = "n"
# new_list = ["s"] + my_list
# newlist.append("g")

# new_list.insert(1, "t")

final_list = []
for i in my_list:
    print(i, my_list.index(i))
    final_list.append(my_list.index(i))
    
print(final_list)

print(sum(final_list))
print(len(final-list))




# COMMAND ----------

list = [g1, g2, g3, g4, g5, g6, g7, g8, g9, g10]

g1 = input("input number")

print(list[1,11])
 


# COMMAND ----------

user_input = []

for i in range(10):
    input_number = int(input("input a number " + str(10-i) + " left"))
    user_input.append(input_number)

print("input list is: ", + user_input)
print("sum of the list is " + str(input_sum))
print("average of the list is " + str(input_sum))

# COMMAND ----------

dice = [1,2,3,4,5,6]

input_sum = sum(user_input)
input_average = 

# COMMAND ----------



# COMMAND ----------

list = [1, 2, 3, 4, 5, 6]
 
print("dice rolled" )
 
# using random.choice() to get a random number
random_num = random.choice(list)
# printing random number
print("you rolled a... : " + str(random_num))

word = input(" would you like to roll again ")

while word == "yes": 
    random_num = random.choice(list)
    
    print("you rolled a: " + str(random_num))
    word = input(" would you like to roll again ")
if word == "no":
    print("game over")


# COMMAND ----------

list = [1,2,3,4,5,6,7,8,9,10]

random_num = random.choice(list)

num = input("guess number between 1-10")
    
while True:
    num == random_num
    print("welldone you guessed correct")
    break
if int(num) > int(random_num): 
    print("your number is too high")
    
elif int(num) < int(random_num): 
    print("your number is too low")
    num = input("guess number between 1-10")
while  num == random_num:
    print("welldone you guessed correct")
    
if int(num) > int(random_num): 
    print("your number is too high")
    
elif int(num) < int(random_num):
    print("your number is too low")

# COMMAND ----------

import random

random_num = random.randrange(1,100)
num = input("guess number between 1-100")
while num != random_num:
    if(int(num) < random_num):
        print("you guessed low")
        num = input("guess again")
    if(int(num) > random_num):
        print("you guessed high")
        num = input("guess again")
    if(int(num) == random_num):
        print("you guessed correctly")
        break 

# COMMAND ----------

while True:
	print("Welcome, ALL! We are going to write our own Mad Libs!")
	print("Let's begin!")

	adj1 = input("First adjective: ")
	adj2 = input("Second adjective: ")
	typeofbird = input("Type of Bird: ")
	RiaH = input("Room in a house: ")
	verPT = input("Verb (Past Tense): ")
	ver2 = input("Another Verb: ")
	relatives_name = input("A Relatives Name: ")
	noun = input("A Noun: ")
	liquid = input("A type of liquid: ")
	verbing = input("A verb ending in 'ing': ")
	body_part = input("A body part (plural): ")
	noun2 = input("Another noun (plural): ")
	verbing2 = input("A verb ending in 'ing': ")
	noun3 = input("And lastly, another noun: ")


	print("It was a {}, cold November day.".format(adj1))
	print("I woke up to the {} smell of {} roasting in the {} downstairs.".format(adj2, typeofbird, RiaH))
	print("I {} down the stairs to see if I could help {} the dinner.".format(verPT, ver2))
	print("My Mom said, 'See if {} needs a fresh {}.'".format(relatives_name, noun))
	print("So I carried a tray of glasses full of {} into the {} room.".format(liquid,verbing))
	print("When I got there, I couldn't believe my {}!".format(body_part))
	print("There were {} {} on the {}!".format(noun2, verbing2, noun3))

	replay = input("Do you want to play again? y/n :")

	if replay.lower() == 'y':
		print("Let's do it!")
		continue
	else:
		print("I don't like you either..")
		break

# COMMAND ----------



def introScene():
        directions = ["left","right","forward"]
        print("You are at a crossroads, and you can choose to go down any of the four hallways. Where would you like to go?")
        userInput = ""
        while userInput not in directions:
            
 print("Options: left/right/backward/forward")
        userInput = input()
    if userInput == "left":
    showShadowFigure()
elif userInput == "right":
    showSkeletons()
elif userInput == "forward":
    hauntedRoom()
elif userInput == "backward":
    print("You find that this door opens into a wall.")
else: 
    print("Please enter a valid option.")
def showShadowFigure():
        directions = ["right","backward"]
        print("You see a dark shadowy figure appear in the distance. You are creeped out. Where would you like to go?")
        userInput = ""
while userInput not in directions:
        print("Options: right/left/backward")
        userInput = input()
if userInput == "right":
          cameraScene()
elif userInput == "left":
          print("You find that this door opens into a wall.")
elif userInput == "backward":
          introScene()
else:
          print("Please enter a valid option.")

# COMMAND ----------


