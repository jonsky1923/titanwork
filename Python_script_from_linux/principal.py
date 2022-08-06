calculation_to_hours = 24
name_of_unit = "hours"



def days_to_unit(num_of_days):
    if num_of_days > 0:
        return f"{num_of_days} days are {num_of_days * calculation_to_hours} {name_of_unit}"
    else:
        return "you entered a negative value,we can't converted"

i
user_input = input("Hey user enter a number of days and i will converted it to hours!\n")
user_input_number = int(user_input)

calculated_value = days_to_unit(user_input_number)
print(calculated_value)