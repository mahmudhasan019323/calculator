logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""


def add(num1,num2):
    return (num1+num2)
def subtract(num1,num2):
    return (num1-num2)
def multiply(num1,num2):
    return (num1*num2)
def divide(num1,num2):
    return (num1/num2)

operations = {"+": add, "-": subtract, "*":multiply, "/": divide}

def calculator(result=False):
    if result == False:
        print('\033c')
        print(logo)
        first_num = float(input("enter the first number: "))
        print('+\n-\n*\n/')
        operation = input("Pick an operation: ")
        second_num = float(input("enter the next number: "))
        final_result = operations[operation](first_num, second_num)
        print(f"{first_num} {operation} {second_num} = {final_result}")
        continue_calc = input(f"type 'y' to continue calculating with {final_result}, or type 'n' to start new calculation: ").lower()
        if continue_calc == 'y':
            calculator(final_result)
        else:
            calculator(False)
    else:
        operation = input("pick an operation: ")
        next_num = int(input('enter the next number: '))
        final_result = operations[operation](result,next_num)
        print(f"{result} {operation} {next_num} = {final_result}")
        continue_calc = input(f"type 'y' to continue calculating with {final_result}, or type 'n' to start new calculation: ").lower()
        if continue_calc == 'y':
            calculator(final_result)
        else:
            calculator(False)

calculator()