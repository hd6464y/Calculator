def output(text, combination):
    text_str = str(text)
    combination_str = str(combination)
    print(text_str + combination_str)

def input_first_int():
    number1_str = input("First number: ")
    number1 = int(number1_str)
    return number1
def input_second_int():
    number2_str = input("Second number: ")
    number2 = int(number2_str)
    return number2

number1 = input_first_int()
number2 = input_second_int()

operation = input("Operation [+, -, *, /]: ")

if operation == "+":
    combination = number1 + number2
elif operation == "-":
    combination = number1 - number2
elif operation == "*":
    combination = number1 * number2
elif operation == "/":
    if number2_str == "0":
        combination = "you can't divide by zero."
    else:
        combination = number1 / number2
else:
    combination = "ERROR ... '" + operation + "' unrecognised"

output("Answer: ", combination)

print()
input("Press return to continue ...")
