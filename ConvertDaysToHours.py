#My first program in Python
#Program to know following concepts
#Variable (no need to mention types), while loop, try-except block, function definition, for loop, user input, split function, type conversion
calculation_of_units = 24
display_unit = "hours"

def calculate_data(num_of_days):
    return f"{num_of_days} days consists of {24 * num_of_days} {display_unit}"


def validate_and_execute():
    try:
        number_to_calculate = int(user_input_element)
        if number_to_calculate > 0:
            number_to_convert = calculate_data(number_to_calculate)
            print(number_to_convert)
        elif number_to_calculate == 0:
            print("Hey, You have given a Zero!!")
        else:
            print("Hey, You have given a negative number!!")
    except ValueError:
        print("Hey, The input is invalid, Don't ruin my program")


#My first program in Python
#Program to know following concepts
#Variable (no need to mention types), while loop, try-except block, function definition, for loop, user input, split function, type conversion
user_input = ""
while user_input != "exit":
    user_input = input("Hey, Please enter a number of days as a list, I will convert it to hours!\n")
    for user_input_element in user_input.split(","):
        validate_and_execute()
