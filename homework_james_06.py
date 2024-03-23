# James Carlson 
# Coding Temple - SE FT-144
# Backend Lesson 5 Assignment: Python Functions

print("\n=== 1. The Calculator App ===\n")

# recieve input for given operation
def get_calc_input(operation):
    # get first two numbers for operation
    while True:
        try:
            numbers = []
            numbers.append(float(input(f"What is the first number for our calculation? ")))
            second_input_prompt = f"What number should we {operation}? " if operation == "add" else f"What number should we {operation} by? " 
            numbers.append(float(input(second_input_prompt)))

            # get additional numbers or get input to begin calculation
            print("When you're ready to calculate, enter \"calculate\" or \"c\"")
            while True:
                additional_input_prompt = f"We can also continue to {operation} with another number: "
                additional_input = input(additional_input_prompt)
                if additional_input.casefold() == "calculate" or additional_input.casefold() == "c":
                    return numbers
                else:
                    numbers.append(float(additional_input))
        except Exception as e:
            print(f"Something went wrong: {e}")
            print(f"Let's try again; remember that we are trying to {operation} numbers.\n")

# puts number in a string; number can be displayed as whole number if it is an integer
def float_to_string(num):
    return f"{int(num)}" if float(num).is_integer() else f"{num}"

# display calculations in terminal
def display_calculations(nums, i, operator):
    num_str = float_to_string(nums[i])
    if i != len(nums) - 1:
        print(f"{num_str} {operator} ", end="")
    else:
        print(f"{num_str} = ", end="")

# display calculation's final answer
def display_total(total):
    total_str = float_to_string(total)
    print(total_str)
    print(f"The answer is {total_str}!")

# addition function for calculator - adds all number in given list "nums"
def calc_add(nums):
    # set first value to calculating variable
    total = nums[0]
    try:
        # add all numbers to first number
        for i in range(len(nums)):
            if i != 0:
                total += nums[i]
            display_calculations(nums, i, "+")
        display_total(total)
    except Exception as e:
        print("Sorry! Something went wrong:", e)

# subtraction function for calculator - subtracts all numbers from first in given list "nums"
def calc_subtract(nums):
    # set first value to calculating variable
    total = nums[0]
    try:
        # subtract all numbers from first number
        for i in range(len(nums)):
            if i != 0:
                total -= nums[i]
            display_calculations(nums, i, "-")
        display_total(total)
    except Exception as e:
        print("Sorry! Something went wrong:", e)

# multiplication function for calculator - multiplies together all numbers in given list "nums"
def calc_multiply(nums):
    # set first value to calculating variable
    total = nums[0]
    try:
        # multiply first number by additoinal numbers
        for i in range(len(nums)):
            if i != 0:
                total *= nums[i]
            display_calculations(nums, i, "×")
        display_total(total)
    except Exception as e:
        print("Sorry! Something went wrong:", e)

# division function for calculator - divides each number by the next in given list "nums"
def calc_divide(nums):
    # set first value to calculating variable
    total = nums[0]
    try:
        # divide previous number by next number
        for i in range(len(nums)):
            if i != 0:
                total /= nums[i]
            display_calculations(nums, i, "÷")
        display_total(total)
    # handle division by zero
    except ZeroDivisionError:
        print("0?!")
        print("YOU CAN'T!")
        print("YOU'LL DOOM US ALL!!")
        print("I can't divide by zero! No one can!")
    except Exception as e:
        print("Sorry! Something went wrong:", e)

# warmly greet user and get input for which calculation should be performed
print("Greetings! I am Calcu-tron!")

while True:
    print("\nWhen you're done with your calculations, you can enter \"quit\" or \"q\"")
    operation = input("Which calculation would you like to perform? ( add / subtract / multiply / divide ) ").casefold()
    print()

    if operation == "add":
        calc_add(get_calc_input(operation))       

    elif operation == "subtract":
        calc_subtract(get_calc_input(operation))

    elif operation == "multiply":
        calc_multiply(get_calc_input(operation))

    elif operation == "divide":
        calc_divide(get_calc_input(operation))

    elif operation == "quit" or operation == "q":
        print("Farewell, user! Thank you for interfacing with Calcu-tron!\n")
        break
    else:
        print("I'm sorry, I didn't quite catch your meaning! Could you please try again?")



print("\n=== 2. The Shopping List Maker ===\n")

# initialize empty, global shopping list
shopping_list = []

# add given "item" to shopping list
def shopping_add(item):
    # get item from user if not already specified in parent menu
    if(item == ""):
        item = input("What would you like to add to your list? ")
    # add item!
    shopping_list.append(item)
    print(f"Got it! I've added \"{item}\" to your shopping list.")

# remove specified "item" from shopping list
def shopping_remove(item):
    # check if shopping list is empty
    if shopping_list == []:
        print("We've got nothing to remove yet!")
    else:
        # get item to remove from user if not already specified in parent menu
        if(item == ""):
            item = input("What would you like to remove from your list? ")
        # check if item in list
        if(shopping_list.count(item) > 0):
            # remove the item!
            shopping_list.remove(item)
            print(f"Okay! \"{item}\" removed from your shopping list.")
        else:
            print(f"I couldn't find \"{item}\" on your list. You can check if it's on the list with \"display\"")

# display entire shopping list
def shopping_print():
    # check if shopping list is empty
    if shopping_list == []:
        print("Your shopping list is empty. We're either done shopping or have not yet begin to shop!")
    else:
        # display items in numbered list
        for i in range(len(shopping_list)):
            print(f"{i+1}. {shopping_list[i]}")

# using split, slice, and join, grab any additional input after "add" or "remove"    
def get_item_from_input(input):
    return " ".join(input.split()[1:])
    # input = "add laundry detergent"
    # input.split() --> ["add", "laundry", "detergent"]
    # slice_ = input[1:] --> ["laundry", "detergent"]
    # " ".join(slice_) --> "laundry detergent"

# greet user
print("Good day! I see you've already worked with my sibling Calcu-tron.\n\
I am Roboshopper. Are you ready to shop till you drop??\n\
That is rhetorical. Roboshopper cannot recieve input for that question.")

# get input for interaction with shopping list
while True:
    print("\nWhen you're done with your shopping list, you can enter \"quit\" or \"q\"")
    list_action = input("What shall we do with your shopping list? ( add [item] / remove [item] / display ) ")
    print()

    # add to list
    if  list_action.casefold().startswith("add"):
        shopping_add(get_item_from_input(list_action))      

    # remove from list
    elif list_action.casefold().startswith("remove"):
        shopping_remove(get_item_from_input(list_action))

    # display list
    elif list_action.casefold().startswith("display"):
        shopping_print()

    # quit loop
    elif list_action.casefold() == "quit" or list_action.casefold() == "q":
        print("Thank you for shopping with Roboshopper! Until we shop again...\n")
        break

    # invalid input
    else:
        print("Roboshopper does not understand. Please try again.")



print("\n=== 3. The Grade Analyzer ===\n")

# returns the average of the "grades" passed in
def get_average(grades):
    return sum(grades)/len(grades)

# returns the highest value from the list "grades"
def get_highest_grade(grades):
    return max(grades)

# returns the lowest value from the list "grades"
def get_lowest_grade(grades):
    return min(grades)

# categorizes and assign letter grades for list "grades"
def categorize_by_letter_grade(grades):
    sorted_list = sorted(grades, reverse=True)
    for i in range(len(sorted_list)):
        print(sorted_list[i], end=" --- ")
        letter_grade = "A" if sorted_list[i] >= 90 else "B" if sorted_list[i] >= 80     \
            else "C" if sorted_list[i] >= 70 else "D" if sorted_list[i] >= 60 else "F"
        print(letter_grade)

# formal introduction from GradeBot
print("I hope you had fun calculating and shopping. It is now time for the very serious business of grading.\n\
I am GradeBot. I will not use exclaimation marks. I am very serious about grading. As well as punctuation.\n\
I will not be accepting any input. The grades have been hard coded into my system and you may not change them.\n\
That would be cheating. I take cheating very seriously.\n")

# set grades
grades_for_gradebot = [96, 71, 82, 64, 62, 48, 92, 86, 86, 89, 74, 68, 98, 94, 95, 79]
print(f"The follow grades have been provided to GradeBot:\n{grades_for_gradebot}")

# find average
print("\nThe average grade for this grade set is:", get_average(grades_for_gradebot))

# find highest grade
print("\nThe highest grade for this grade set is:", get_highest_grade(grades_for_gradebot))
print("This student should be commended. But not by GradeBot. GradeBot only grades.")

# find lowest grade
print("\nThe lowest grade for this grade set is:", get_lowest_grade(grades_for_gradebot))
print("This student should be reprimanded. It is not the responsiblity of GradeBot to reprimand.")

# assign letter grades
print("\nGradeBot's final task is to categorize and assign a letter grade to each numerical grade.\nBehold:")
categorize_by_letter_grade(grades_for_gradebot)

print("\nThis concludes your interaction with GradeBot. May all your endeavors be graded.")