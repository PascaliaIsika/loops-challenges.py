
# ask the user to enter their name and display their name three times
person = input("enter your name: ")
for name in range(3):
    print(person)

#ask user enter their name and a number and display the name that number of times
person = input("enter your name: ")
number = int(input("enter a number: "))
for name in range(number):
    print(person)


#ask user enter name, number display their name one letter at a time on each line repeat this for number of times they've entered
person = input("enter your name: ")
number = int(input("enter a number: "))
for letter in person:
    print(letter)
for letter in range(number):
     print(person)


#ak user enter their name and display each letter in their name on a separate line
person = input("enter a name: ")
for index, letter in enumerate(person,1) :
    print(index, letter)



#ask the user to enter a number between 1 and 12 and display the times table for that number
num = int(input("enter a number between 1 and 12: "))
print("times table of",num)
for i in range(1,12):
    print(num,"X",i, "=", num*i)


#ask the user to enter their name and a number. If the number is less than 10,
#then display their name that number of times; otherwise display the message "Too high" three times.
name = input("Enter your name:")
num = int(input("enter a number: "))
if num < 10:
    for num in range(num):
        print(name)
else:
    for num in range(3):
        print("Too high")


#ask for a number below 50 and then count down from 50 to that number,
#making sure you show the number they entered in the output.
num = int(input("enter a number less than 50: "))
for num in range (50):
    print(num)


#ask how many people the user wants to invite to a party.
#if they enter a number below 10, ask for their names and after each name
#display "[name] has been invited.if they enter a number which is
#10 or higher ,display the message"Too many people"
people =int( input("enter number of people you want to invite for the party:"))
if people<10:
    for i in range(0,people):
        name = input("enter their names: ")

        print("[name] has been invited")

if people>=10:
    print("Too many people")

#ask which direction the user wants to count(up or down).If the select up,
#then ask them for the top number and then count from 1 to that number.if they select down,
#ask them to enter a number below 20 and then count down from 20 to that number
#If they entered something other than up or down ,display the message "i don't understand"
direction = input("enter the direction you want to count up or down: ")
if direction == "up":
    num = int(input("What is the top number?: "))
    for i in range (1,num+1):
        print(i)
elif direction == "down":
    num = int(input("Enter a number below 20: "))
    for i in range(20, num-1,-1):
        print(i)
else:
    print("i don't understand")



















